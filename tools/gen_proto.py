"""Prototype additions on top of gen_pages.py: run `python3 tools/gen_proto.py`."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_pages as G
from gen_pages import page, sh, rows, specs, k, close, AR, phero, tags
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
TBC = lambda t: f'<span class="tbc">{t}</span>'
FORBES = 'https://www.forbes.com/sites/annatong/2026/04/16/ais-new-training-data-your-old-work-slacks-and-emails/'
def sec(inner): return f'<section class="sec">\n{inner}\n</section>\n'
QUALIFY = sec(sh('+', 'Do you qualify', 'What buyers <em>tend to look for.</em>', 'A quick screen for each company in your portfolio. Missing one doesn\'t rule a company out; the appraisal tells you.') + '\n' + rows([
 ('01', 'A real team', 'Buyer programs publish bars such as 25–30+ employees at peak.'),
 ('02', 'Years of history', 'Years of Slack or Teams, tickets, code and documents, not a few months.'),
 ('03', 'Records still reachable', 'Workspaces, repos and drives that someone can still access or export.'),
 ('04', 'Authority to decide', 'A founder, officer or board member who can approve a deal.'),
 ('05', 'Rights to the data', 'Agreements that let the company license what it created. We review this with you.')]) +
 '\n  <p class="src reveal">Example bar from micro1\'s published defunct-company program (25+ employees at peak, substantial Slack or Teams history, English). Each buyer sets its own.</p>')
COMPARE = sec(sh('+', 'Your options', 'Three ways to sell. <em>One works only for you.</em>') + '''
  <div class="reveal"><table class="tbl cmp">
    <thead><tr><th></th><th>TDC</th><th>Marketplace listing</th><th>Selling to one buyer</th></tr></thead>
    <tbody>
''' + '\n'.join('      <tr><td>' + r[0] + '</td>' + ''.join(f'<td data-h="{h}">{c}</td>' for h, c in zip(['TDC', 'Marketplace listing', 'Selling to one buyer'], r[1:])) + '</tr>' for r in [
 ('Who we work for', 'You, the seller', 'The platform serves buyers and sellers', 'The buyer runs the process'),
 ('Buyers competing', 'Several, at the same time', 'Whoever finds the listing', 'One'),
 ('Where the data sits', 'With you until close', 'Depends on the platform', 'Under the buyer\'s review terms'),
 ('Company name', 'Shared only with consent and an NDA', 'Depends on the listing', 'Known from first contact'),
 ('Who does the work', 'We run assessment, buyers and paperwork', 'You list and negotiate', 'You negotiate alone'),
 ('Final say', 'You', 'You', 'You')]) + '\n    </tbody>\n  </table></div>')
MARKET = sec(sh('+', 'What the market reports', 'AI teams are already <em>buying this data.</em>', 'Public reporting on the market. These are not TDC results or quotes.') + '\n' + specs([
 ('Forbes · Apr 16, 2026', 'AI\'s new training data: your old work Slacks and emails', f'<p>Reports SimpleClosure typically paying $10,000–$100,000 per closed company, and that price depends on size, age and how linked the records are.</p><a class="more" style="margin-top:18px" href="{FORBES}" target="_blank" rel="noopener">Read {AR}</a>'),
 ('Upstarts · Sep 3, 2026', 'What fetches top dollar on the dead-startup data marketplace', '<p>Reports 350+ companies listed on SimpleClosure\'s AssetHub since April, with prospective buyers up 9x.</p><a class="more" style="margin-top:18px" href="https://www.upstartsmedia.com/p/exclusive-simpleclosure-data-what-ai-labs-buy" target="_blank" rel="noopener">Read ' + AR + '</a>'),
 ('New York Post · Nov 10, 2026', 'Data from defunct businesses are goldmines for data brokers', '<p>Coverage of brokers buying records from closed companies.</p><a class="more" style="margin-top:18px" href="https://nypost.com/2026/11/10/business/data-from-defunct-businesses-are-goldmines-for-data-brokers/" target="_blank" rel="noopener">Read ' + AR + '</a>')]))
TIMELINE = sec(sh('+', 'Timeline', 'How long <em>each step takes.</em>', TBC('Target timing, to confirm')) + '\n' + rows([
 ('Day 1', 'Assessment call', 'Booked within one business day of your request.'),
 ('Week 1', 'Private appraisal', 'Written appraisal of what the data is and how buyers may see it.'),
 ('Weeks 2–4', 'Buyer process', 'Anonymized summary to several buyers under NDA; offers come back to you.'),
 ('Your pace', 'Seller\'s final say', 'Nothing closes until you sign.')]))
DEID = sec(sh('+', 'Privacy by design', 'How personal data <em>stays out.</em>', '<span data-cfg="deid" class="tbc">De-identification method: one-line summary TBC</span>') + '\n' + rows([
 ('01', 'Inventory first', 'We map what exists and flag customer, patient, employee and credential data before anything moves.'),
 ('02', 'Remove what identifies people', 'Names, contact details, credentials and other identifiers are removed or masked.'),
 ('03', 'Samples, never a handover', 'Buyers evaluate approved samples or a controlled review, never a full copy.'),
 ('04', 'Leave out what can\'t be cleaned', 'Records that can\'t be handled responsibly stay out of the deal.')]))
DEALS = sec(sh('+', 'Deal structures', 'Ways a deal <em>can be shaped.</em>', 'We lay these out side by side for every offer. You choose.') + '\n' + specs([
 ('One-time', 'Single license fee', '<p>One payment for a defined license. Simple and final.</p>'),
 ('Ongoing', 'Licensing over time', '<p>Payments that continue as the data is used or relicensed, where a buyer offers it.</p>'),
 ('Scope', 'Exclusive or not', '<p>Exclusive terms usually change the price. Non-exclusive keeps you free to license again.</p>')]))
def inject(fn, block, before):
    s = open(fn).read(); i = s.index(before); i = s.rfind('<section', 0, i)
    open(fn, 'w').write(s[:i] + block + '\n' + s[i:])
inject('index.html', QUALIFY + COMPARE + MARKET, "Who's behind TDC")
inject('investors.html', QUALIFY + COMPARE, "Who's behind TDC")
s = open('how-it-works.html').read(); i = s.index('<section class="scene end">')
open('how-it-works.html', 'w').write(s[:i] + TIMELINE + DEID + DEALS + '\n' + s[i:])
# quick assessment: cited market range; form: public signals + operating companies
s = open('index.html').read()
s = s.replace('<p id="vnote">Your answers stay in your browser.</p>', f'<p id="vnote">Your answers stay in your browser.</p>\n      <p class="src">Reported market range: $10,000–$100,000 per closed company (SimpleClosure, via <a href="{FORBES}" target="_blank" rel="noopener">Forbes</a>). Not a TDC quote.</p>')
open('index.html', 'w').write(s)
s = open('appraisal.html').read()
s = s.replace('<span>Winding down</span></label>', '<span>Winding down</span></label><label><input type="radio" name="status" value="Still operating"><span>Still operating</span></label>')
s = s.replace('<div class="f" id="count" hidden>', '<div class="f"><label class="label" for="site">Company website or GitHub org <span class="opt">Optional · we start from public signals</span></label><input type="text" id="site" name="site" placeholder="example.com"></div>\n        <div class="f" id="count" hidden>')
s = s.replace("built:val('built'),", "built:val('built'),site:val('site'),")
open('appraisal.html', 'w').write(s)

# new pages
page('data.html', 'What sells — The Data Company', 'The kinds of company data AI buyers license, what makes it more valuable, and what stays out.', phero('rise.jpg', 'What sells', 'The records a company leaves behind <em>are the product.</em>', 'AI teams license real work: how code was written, how tickets were solved, how decisions moved across tools. Here is what tends to qualify.', [('Get a free appraisal', 'appraisal.html'), ('Do you qualify', 'index.html')], '<span>Code</span><span>Workspace</span><span>Operations</span>') + '\n' + sec(sh('01', 'Asset classes', 'Four kinds of data <em>buyers ask for.</em>') + '\n' + specs([
 ('Code', 'Source code', tags(['Repos and commit history', 'Code review threads', 'Tests and CI', 'Internal tools', 'Technical docs'])),
 ('Workspace', 'How work happened', tags(['Slack or Teams', 'Email', 'Docs, Notion, Drive', 'Jira or Linear tickets', 'Figma and design files'])),
 ('Operations', 'Running the business', tags(['CRM history', 'Support tickets', 'Analytics and logs', 'Procedures and playbooks'])),
 ('Domain', 'Specialized datasets', tags(['Sensor and inspection imagery', 'Process and quality records', 'De-identified clinical or admin records, where permitted']))], 4)) +
 sec(sh('02', 'What raises value', 'Linked records <em>are worth more.</em>', f'A ticket tied to the commit that fixed it tells a buyer more than either alone. Buyers reportedly price on size, age and how connected the records are (<a href="{FORBES}" target="_blank" rel="noopener">Forbes</a>).') + '\n' + rows([
 ('01', 'Connected tools', 'Tickets, code, chat and docs that reference each other.'),
 ('02', 'Depth over time', 'Years of history, not a snapshot.'),
 ('03', 'Real work in a specialized field', 'Manufacturing, software and healthcare records are hard to get any other way.')])) +
 sec(sh('03', 'What stays out', 'Some data <em>never goes in a deal.</em>') + '\n' + rows([
 ('×', 'Personal data that can\'t be de-identified', None), ('×', 'Credentials, keys and secrets', None), ('×', 'Anything the company doesn\'t have the rights to license', None), ('×', 'Regulated records without the permissions they require', None)])) +
 close('04', 'Find out what <em>yours could qualify for.</em>', 'A free, private appraisal. Not a listing.', 'Get a free appraisal', img='plume.jpg'))
page('advisors.html', 'For advisors — The Data Company', 'For shutdown advisors, attorneys and accountants: a free, seller-first way for wind-down clients to recover value from their data.', phero('smoke.jpg', 'For wind-down advisors', 'Winding down a client? <em>Their data may still be worth something.</em>', 'For shutdown advisors, attorneys and accountants. TDC gives your clients a free, private appraisal and a sell-side process where they keep every decision.', [('Refer a client', 'appraisal.html'), ('How it works', 'how-it-works.html')], '<span>Free to your client</span><span>Sell-side only</span><span>Client decides</span>') + '\n' + sec(sh('01', 'How referrals work', 'One introduction. <em>We handle the rest.</em>') + '\n' + rows([
 ('01', 'You introduce', 'An email introduction to the founder or officer handling the wind-down.'),
 ('02', 'We appraise, free', 'A private appraisal of what the company built. No data leaves their hands.'),
 ('03', 'Your client decides', 'Every step, every offer, the final call. Proceeds follow the company\'s own obligations.')])) +
 sec(sh('02', 'Why it fits a wind-down', 'Recovered value, <em>no extra work.</em>') + '\n' + specs([
 ('For the estate', 'Possible recovery', '<p>Proceeds flow under the company\'s existing agreements and wind-down plan, which we don\'t override.</p>'),
 ('For you', 'No added workload', '<p>We run assessment, buyers and paperwork.</p>'),
 ('For the founder', 'Discretion', '<p>No company name reaches a buyer without consent and an NDA.</p>')])) +
 close('03', 'Refer a client <em>in one email.</em>', 'Or start the appraisal with them.', 'Refer a client', img='ascent.jpg'))
# nav + footer links on every page
for fn in [f for f in os.listdir('.') if f.endswith('.html')]:
    s = open(fn).read()
    s = s.replace('<a href="how-it-works.html">How it works</a><a class="cta"', '<a href="how-it-works.html">How it works</a><a href="data.html">What sells</a><a class="cta"')
    s = s.replace('<a href="how-it-works.html">How it works</a><a href="privacy.html">Privacy</a>', '<a href="how-it-works.html">How it works</a><a href="data.html">What sells</a><a href="advisors.html">For advisors</a><a href="privacy.html">Privacy</a>')
    open(fn, 'w').write(s)
