"""Vercel Python function: POST /api/appraisal

Writes a free-appraisal request to the Notion "TDC Website Requests" database and,
if configured, emails a notification through Resend.

Env vars (Vercel → Project → Settings → Environment Variables):
  NOTION_TOKEN        Notion internal integration secret (share the database with the integration)
  NOTION_DATABASE_ID  ID of "TDC Website Requests"
  RESEND_API_KEY      optional, for the email notification
  NOTIFY_EMAIL        optional, where notifications go
  NOTIFY_FROM         optional, verified Resend sender (default onboarding@resend.dev)
"""
from http.server import BaseHTTPRequestHandler
import json
import os
import re
import urllib.request

ROLES = {"Investor", "Founder or former officer", "Other"}
COUNTS = {"1", "2–5", "6–20", "More than 20"}
INDUSTRIES = {"Manufacturing", "Software development", "Healthcare", "Other"}
STATUSES = {"Wound down", "Written off", "Winding down", "Still operating", "Other"}
SIGNALS = {"Strong signal", "Promising signal", "Early signal"}
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def clean(v, n=2000):
    return str(v or "").strip()[:n]


def validate(d):
    out = {
        "name": clean(d.get("name"), 200),
        "email": clean(d.get("email"), 200),
        "role": clean(d.get("role"), 60),
        "org": clean(d.get("org"), 200),
        "count": clean(d.get("count"), 20),
        "status": clean(d.get("status"), 40),
        "industry": [i for i in d.get("industry") or [] if i in INDUSTRIES],
        "built": clean(d.get("built")),
        "notes": clean(d.get("notes")),
        "site": clean(d.get("site"), 300),
        "signal": clean(d.get("signal"), 40),
        "page": clean(d.get("page"), 300),
    }
    errors = [k for k in ("name", "org") if not out[k]]
    if not EMAIL_RE.match(out["email"]):
        errors.append("email")
    if out["role"] not in ROLES:
        errors.append("role")
    if out["count"] not in COUNTS or out["role"] != "Investor":
        out["count"] = ""
    if out["status"] not in STATUSES:
        out["status"] = ""
    if out["signal"] not in SIGNALS:
        out["signal"] = ""
    return out, errors


def text(v):
    return {"rich_text": [{"text": {"content": v}}]} if v else {"rich_text": []}


def notion_properties(r):
    p = {
        "Fund or company": {"title": [{"text": {"content": r["org"]}}]},
        "Name": text(r["name"]),
        "Email": {"email": r["email"]},
        "Role": {"select": {"name": r["role"]}},
        "Industry": {"multi_select": [{"name": i} for i in r["industry"]]},
        "What was built": text(r["built"]),
        "Notes": text("\n".join(x for x in (r["notes"], r["site"] and "Website/GitHub: " + r["site"]) if x)),
        "Source page": text(r["page"]),
        "Status": {"status": {"name": "New"}},
    }
    for key, prop in (("count", "Companies to review"), ("status", "Company status"), ("signal", "Assessment signal")):
        if r[key]:
            p[prop] = {"select": {"name": r[key]}}
    return p


def post(url, headers, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.status


def save(r):
    post("https://api.notion.com/v1/pages",
         {"Authorization": "Bearer " + os.environ["NOTION_TOKEN"], "Notion-Version": "2022-06-28", "Content-Type": "application/json"},
         {"parent": {"database_id": os.environ["NOTION_DATABASE_ID"]}, "properties": notion_properties(r)})


def notify(r):
    key, to = os.environ.get("RESEND_API_KEY"), os.environ.get("NOTIFY_EMAIL")
    if not key or not to:
        return
    lines = [f"{k}: {v}" for k, v in (("Name", r["name"]), ("Email", r["email"]), ("Role", r["role"]), ("Fund or company", r["org"]),
             ("Companies", r["count"]), ("Status", r["status"]), ("Industry", ", ".join(r["industry"])), ("Built", r["built"]),
             ("Notes", r["notes"]), ("Assessment", r["signal"])) if v]
    try:
        post("https://api.resend.com/emails", {"Authorization": "Bearer " + key, "Content-Type": "application/json"},
             {"from": os.environ.get("NOTIFY_FROM", "TDC Website <onboarding@resend.dev>"), "to": [to], "reply_to": r["email"],
              "subject": f"New appraisal request: {r['org']}", "text": "\n".join(lines)})
    except Exception:
        pass


class handler(BaseHTTPRequestHandler):
    def reply(self, code, body):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        try:
            n = min(int(self.headers.get("Content-Length") or 0), 20000)
            d = json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            return self.reply(400, {"ok": False, "error": "bad_request"})
        if d.get("website"):  # honeypot field, hidden from people
            return self.reply(200, {"ok": True})
        r, errors = validate(d)
        if errors:
            return self.reply(422, {"ok": False, "error": "invalid", "fields": errors})
        if not os.environ.get("NOTION_TOKEN") or not os.environ.get("NOTION_DATABASE_ID"):
            return self.reply(503, {"ok": False, "error": "not_configured"})
        try:
            save(r)
        except Exception:
            return self.reply(502, {"ok": False, "error": "store_failed"})
        notify(r)
        return self.reply(200, {"ok": True})

    def do_GET(self):
        self.reply(405, {"ok": False, "error": "method_not_allowed"})
