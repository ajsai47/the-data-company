import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
FONTS='https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,500;0,600;0,700&family=Inter:wght@300;400;500&family=JetBrains+Mono:wght@400;500&display=swap'
AR='<span class="ar"></span>'
def k(i,t): return f'<div class="k label"><i>{i}</i><span>{t}</span></div>'
def sh(i,label,h,lead=None,cls=''):
    l=f'\n    <p class="lead reveal d3">{lead}</p>' if lead else ''
    solo='' if lead else ' solo'
    return f'''  <div class="sh grid{solo} {cls}">
    <div class="reveal">{k(i,label)}</div>
    <h2 class="d reveal d2">{h}</h2>{l}
  </div>'''
def rows(items,cls=''):
    out=[]
    for n,(i,t,p) in enumerate(items):
        pp=f'<p>{p}</p>' if p else ''
        c=cls+('' if p else ' solo')
        out.append(f'    <div class="row grid {c} reveal"><div class="i label">{i}</div><div class="t2">{t}</div>{pp}</div>')
    return '  <div class="ledger">\n'+'\n'.join(out)+'\n  </div>'
def specs(items,n=3):
    out=[]
    for j,(i,t,body) in enumerate(items):
        out.append(f'    <div class="spec reveal d{min(j+1,4)}"><div class="i label">{i}</div><div class="t2">{t}</div>{body}</div>')
    return f'  <div class="specs n{n}">\n'+'\n'.join(out)+'\n  </div>'
def close(i,h,lead,btn,href='appraisal.html',img='ascent.jpg',small='An appraisal is not a listing: no buyer sees anything unless you decide to go further.',bold=None):
    ba=f' data-bold="{bold}"' if bold else ''
    return f'''<section class="scene end">
  <div class="bg" style="background-image:url(media/{img})"></div>
  <div class="w">
    <div class="reveal">{k(i,'Free appraisal')}</div>
    <h2 class="d reveal d2"{ba}>{h}</h2>
    <p class="lead reveal d3">{lead}</p>
    <div class="ctas reveal d4"><a class="btn" href="{href}">{btn} {AR}</a></div>
    <small class="reveal d4">{small}</small>
  </div>
</section>'''
def phero(img,label,h,sub,ctas,meta,bold=None):
    ba=f' data-bold="{bold}"' if bold else ''
    c=''.join(f'<a class="btn{" line m-hide" if j else ""}" href="{hr}">{tx}{" "+AR if not j else ""}</a>' for j,(tx,hr) in enumerate(ctas))
    return f'''<header class="scene top">
  <div class="bg" style="background-image:url(media/{img})"></div>
  <div class="w">
    {k('00',label)}
    <h1 class="d"{ba}>{h}</h1>
    <p class="sub">{sub}</p>
    <div class="ctas">{c}</div>
  </div>
  <div class="meta label">{meta}</div>
</header>'''
def page(fn,title,desc,body,scripts=''):
    html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link id="fonts" href="{FONTS}" rel="stylesheet">
<script src="themes.js"></script>
<link rel="stylesheet" href="site.css">
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="media/apple-touch-icon.png">
<meta property="og:type" content="website"><meta property="og:site_name" content="The Data Company">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="https://datacompanyusa.com/media/og.jpg"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B0B0C">
</head>
<body>
<nav id="nav">
  <a class="wm" href="index.html">The <b>Data</b> Company</a>
  <div class="links"><a href="investors.html">For investors</a><a href="founders.html">For founders</a><a href="how-it-works.html">How it works</a><a class="cta" href="appraisal.html">Free appraisal →</a></div>
  <a class="btn" href="appraisal.html">Free appraisal</a><button class="menu" aria-label="Menu"><i></i><i></i></button>
</nav>
{body}
<footer>
  <div class="grid">
    <div class="fw"><a class="wm" href="index.html">The <b>Data</b> Company</a><p>Portfolio recovery for early-stage investors. We license company data to AI buyers on the seller's terms, without ever holding the data.</p></div>
    <div class="fc"><div class="label">Site</div><a href="index.html">Home</a><a href="investors.html">For investors</a><a href="founders.html">For founders</a><a href="how-it-works.html">How it works</a><a href="privacy.html">Privacy</a></div>
    <div class="fc"><div class="label">Principles</div><span>Sell-side only</span><span>Several buyers compete</span><span>No data custody</span><span>The seller decides</span></div>
    <div class="fc"><div class="label">Start</div><a href="appraisal.html">Free appraisal</a><a href="appraisal.html?role=investor">For a fund</a><a href="appraisal.html?role=founder">For a company</a></div>
    <div class="base label"><span>© 2026 The Data Company</span><span>datacompanyusa.com</span></div>
  </div>
</footer>
<script src="config.js"></script>
<script src="launch.js"></script>
<script src="site.js"></script>
{scripts}</body>
</html>
'''
    open(fn,'w').write(html)

STEPS=[("01","Assessment call","A short call to understand the company, what it built, and what records remain.","You decide whether to continue"),
("02","Private appraisal","What the data is, what rights appear to exist, and how AI buyers may value it. Nothing is shared with buyers.","You decide whether to take it to market"),
("03","Buyer process","Several buyers review an anonymized summary. Names are shared only under NDA. Offers come back to you.","You decide which offers to pursue"),
("04","Seller's final say","See the terms side by side. Accept, negotiate, or walk away.","You decide. Always")]

def chips(name,opts,kind='radio',req=False):
    return '<div class="chips">'+''.join(f'<label><input type="{kind}" name="{name}" value="{o}"{" required" if req and kind=="radio" else ""}><span>{o}</span></label>' for o in opts)+'</div>'
HOME_JS=r"""<script>
(function(){
  var w=document.getElementById('wall'),cls=[],seed=7;
  function rnd(){seed=(seed*16807)%2147483647;return seed/2147483647}
  for(var i=0;i<100;i++)cls.push(i<4?'g':i<69?'r':'n');
  for(i=99;i>0;i--){var j=Math.floor(rnd()*(i+1)),t=cls[i];cls[i]=cls[j];cls[j]=t}
  w.innerHTML=cls.map(function(c,i){return '<i class="'+c+'" style="transition-delay:'+(i*12)+'ms">'+(c==='g'?'10x':c==='r'?'&lt;1x':'')+'</i>'}).join('');
  new IntersectionObserver(function(e,o){if(e[0].isIntersecting){w.classList.add('lit');o.disconnect()}},{threshold:.35}).observe(w);
  var f=document.getElementById('qa'),bars=[].slice.call(document.querySelectorAll('#meter i')),vd=document.getElementById('verdict'),vn=document.getElementById('vnote');
  function v(n){var x=f.querySelector('[name='+n+']:checked');return x?x.value:null}
  f.addEventListener('change',function(){
    var i=v('qi'),y=v('qy'),s=v('qs'),a=v('qa1'),d=f.querySelectorAll('[name=qd]:checked').length;
    if(!i&&!y&&!s&&!a&&!d)return;
    var sc=(i?(i==='Other'?1:2):0)+({'Under 2':1,'2–5':2,'More than 5':3}[y]||0)+d+({'Still accessible':2,'Archived':1}[s]||0)+(a==='Yes'?1:0);
    var n=Math.round(sc/13*10);bars.forEach(function(b,k){b.classList.toggle('on',k<n)});
    var done=i&&y&&s&&a;
    var q=new URLSearchParams();if(i)q.set('industry',i);var lf=[].map.call(f.querySelectorAll('[name=qd]:checked'),function(x){return x.value});if(lf.length)q.set('left',lf.join('|'));if(done)q.set('signal',sc>=9?'Strong signal':sc>=5?'Promising signal':'Early signal');document.getElementById('qcta').href='appraisal.html?'+q;
    vd.textContent=!done?'Keep going…':sc>=9?'Strong signal':sc>=5?'Promising signal':'Early signal';
    vn.textContent=!done?'Answer all five for a signal.':sc>=9?'Specialized, long-lived, accessible data is what AI buyers tend to look for. An appraisal can tell you what it may be worth.':sc>=5?'There may be something here. An appraisal will show what is licensable and what needs attention first.':'Worth a closer look before ruling it out. The appraisal is free and tells you whether there is anything to pursue.';
  });
})();
</script>
"""

BIO=f"""<section class="sec">
{sh('{n}',"Who's behind TDC",'A sell-side advisor, <em>not a marketplace.</em>')}
  <div class="grid">
    <div class="spec reveal" style="grid-column:1/span 4"><div class="i label">Founder</div><div class="t2">AJ Green</div><p><span class="tbc">Bio: role and background TBC</span></p></div>
    <div class="prose reveal d2" style="grid-column:6/span 7"><p style="font-size:var(--t-lead);line-height:1.55;color:rgba(var(--fg-rgb),.8)">TDC works for the seller, never the buyer. Every request is read by a person, and every appraisal is private.</p></div>
  </div>
</section>
"""
# ---------- HOME ----------
vows=[("01","We work for <em>the seller.</em>","Never the buyer. We assess what a wound-down company has and estimate what it could be worth to AI buyers."),
("02","Several buyers <em>compete.</em>","We run a competitive process when the seller wants to go ahead, not a sale to the first buyer who asks."),
("03","We never <em>hold the data.</em>","It stays with the seller until a deal closes. We don't take custody of it, copy it, or warehouse it."),
("04","Names stay <em>private.</em>","No company name reaches a buyer without consent and an NDA. De-identification is built into the process."),
("05","The seller <em>decides.</em>","Every step, every offer, the final call.")]
def tags(xs): return '<div class="tags">'+''.join(f'<span>{x}</span>' for x in xs)+'</div>'
page('index.html','The Data Company — Portfolio recovery for early-stage investors','TDC helps early-stage VCs recover value from wound-down portfolio companies by licensing their data to AI buyers. We never hold the data, and the seller always decides.',f'''
<header class="hero" data-launch>
  <div class="stage">
    <video data-src="media/launch.mp4" data-src-mobile="media/launch-portrait.mp4" data-poster-mobile="media/launch-portrait-poster.jpg" poster="media/launch-poster.jpg" muted playsinline preload="auto"></video>
    <div class="copy">
      <div class="phase on" data-from="-1" data-to=".3">
        {k('00','Portfolio recovery for early-stage investors')}
        <h1 class="d" data-bold="Your write-offs <em>aren't grounded yet.</em>">Your written-off companies <em>still have value.</em></h1>
        <p class="sub">TDC helps early-stage VCs recover value from wound-down portfolio companies by licensing their data to AI buyers. We never hold the data, and the seller always decides.</p>
        <div class="ctas"><a class="btn" href="appraisal.html" data-bold='Start the launch sequence <span class="ar"></span>'>Get a free appraisal {AR}</a><a class="btn line m-hide" href="how-it-works.html">How it works</a></div>
      </div>
      <div class="phase" data-from=".3" data-to=".66">
        {k('T+1','Ignition')}
        <h2 class="d" data-bold="The cap table hit zero. <em>The data didn't.</em>">A write-off doesn't have to be <em>the last entry.</em></h2>
        <p class="sub m-hide">What a company built often outlives the company: years of operating records, engineering history, and domain data that AI teams can't get anywhere else.</p>
      </div>
      <div class="phase" data-from=".66">
        {k('T+2','Ascent')}
        <h2 class="d" data-bold="Turn your losses into <em>a second launch.</em>">Turn a write-off into <em>a recovery.</em></h2>
        <div class="ctas"><a class="btn" href="appraisal.html" data-bold='Start the launch sequence <span class="ar"></span>'>Get a free appraisal {AR}</a></div>
      </div>
    </div>
    <div class="meta label"><span>Sell-side only · Seller decides</span><span class="bar"></span></div>
    <div class="cue label">Scroll</div>
  </div>
</header>

<section class="sec">
{sh('01','The math of venture','Even the best portfolios <em>carry losses.</em>','Venture returns come from a few outsized winners. Most companies never return the capital invested. Those positions get marked down and forgotten, but what the companies built often has value.')}
  <div class="wall reveal" id="wall" aria-label="100 squares: 4 green, 65 red, 31 gray"></div>
  <div class="legend reveal"><span class="g"><b>4%</b> returned 10x or more</span><span class="r"><b>65%</b> returned less than the capital invested</span><span class="n"><b>31%</b> in between</span></div>
  <p class="src reveal">Share of venture financings by outcome, 21,000+ U.S. financings, 2004–2013. Source: Correlation Ventures, via <a href="https://sethlevine.com/archives/2014/08/venture-outcomes-are-even-more-skewed-than-you-think.html" target="_blank" rel="noopener">Seth Levine</a>.</p>
  <h3 class="t2 reveal" style="font-size:var(--t-2);margin-top:var(--gap);max-width:22ch" data-bold="We help turn <em>the red into recoveries.</em>">TDC works on <em>the red squares.</em></h3>
</section>

<section class="sec">
{sh('02','The problem','Written off is not the same as <em>worth nothing.</em>')}
  <div class="prose grid">
    <p class="reveal">When an early-stage company winds down, the cap table goes to zero, but what the company built often stays behind: years of operating records, engineering history, domain-specific datasets, and workflows that took real people real time to create.</p>
    <p class="reveal d2 m-hide">AI teams need exactly this kind of real-world data, and most of it sits on a drive with no plan. For a fund, that is unrecovered value on a position already marked down.</p>
  </div>
</section>

<section class="scene dense">
  <div class="bg" style="background-image:url(media/ignition.jpg)"></div>
  <div class="w">
{sh('03','What TDC does','A sell-side advisor <em>for company data.</em>','TDC works for the seller, not the buyer. The seller approves every step, sees every offer, and makes the final call.')}
{rows(vows,'brief')}
  </div>
</section>

<section class="sec">
{sh('04','For investors','One relationship, <em>many companies.</em>','Most funds carry a handful of companies that wound down or were written off. Each one might hold licensable data, and no one at the fund has time to find out.')}
{specs([("You","Make the intro.","<p>Name the companies and make one warm intro per founder.</p>"),("TDC","Run the process.","<p>The assessment, appraisal, and buyer process, under NDA.</p>"),("The founder","Make the call.","<p>Approves every step, sees every offer, makes the final call.</p>")])}
  <a class="more reveal" href="investors.html">For investors {AR}</a>
</section>

<section class="sec">
{sh('05','Where data is most valuable','Real work, in <em>specialized fields.</em>','We focus on companies whose data reflects real work in specialized fields.')}
{specs([("I","Manufacturing",tags(["Process and quality records","Sensor and machine data","Inspection imagery","Operating procedures"])),("II","Software development",tags(["Code history","Issue and review records","Test suites","Internal tooling and documentation"])),("III","Healthcare",tags(["Operational and workflow data","De-identified clinical or administrative records, where permitted"]))])}
  <p class="note reveal">Other industries can qualify. The appraisal tells you whether yours does.</p>
</section>

<section class="sec" id="process">
{sh('06','How it works','A careful process. <em>Your decision at every step.</em>')}
{rows([(n,t,f"<span class='m-hide'>{p}</span><b>{d}</b>") for n,t,p,d in STEPS])}
  <a class="more reveal" href="how-it-works.html">See the full process {AR}</a>
</section>
<!-- Proof section: leave out until the first deal closes and testimonials have written consent. -->

<section class="sec" id="assess">
{sh('07','Quick assessment','Is there something <em>on the pad?</em>','Five questions about one wound-down company. A rough signal in under a minute, not a valuation.')}
  <div class="qa">
    <form id="qa">
      <div class="f"><div class="q label">Industry</div>{chips('qi',['Manufacturing','Software development','Healthcare','Other'])}</div>
      <div class="f"><div class="q label">Years operating</div>{chips('qy',['Under 2','2–5','More than 5'])}</div>
      <div class="f"><div class="q label">What's left behind <span class="opt">Select any</span></div>{chips('qd',['Code and engineering history','Operational records','Customer or usage data','Imagery or sensor data','Documents and procedures'],'checkbox')}</div>
      <div class="f"><div class="q label">Where it is now</div>{chips('qs',['Still accessible','Archived','Not sure'])}</div>
      <div class="f"><div class="q label">Can you reach a founder or officer?</div>{chips('qa1',['Yes','Not sure'])}</div>
    </form>
    <div class="out" aria-live="polite">
      <div class="i label" style="color:var(--ac)">Your signal</div>
      <div class="meter" id="meter">{''.join('<i></i>' for _ in range(10))}</div>
      <div class="t2" id="verdict">Answer to see your signal</div>
      <p id="vnote">Your answers stay in your browser.</p>
      <a class="btn" href="appraisal.html" id="qcta">Get the free appraisal {AR}</a>
    </div>
  </div>
</section>

{BIO.replace('{n}','08')}
{close('09',"Find out what's still <em>on the books.</em>","A free portfolio data appraisal is private and carries no obligation.","Get a free portfolio data appraisal",bold="Put your write-offs <em>back on the pad.</em>")}
''',HOME_JS)

# ---------- INVESTORS ----------
page('investors.html','For investors — The Data Company','TDC works with early-stage funds to find and license the data left behind by wound-down portfolio companies. You make the introduction. We run the process. The seller decides.',f'''
{phero('pad.jpg','For investors',"Recover value from the companies <em>you've written off.</em>","TDC works with early-stage funds to find and license the data left behind by wound-down portfolio companies. You make the introduction. We run the process. The seller decides.",[("Get a free portfolio data appraisal","appraisal.html?role=investor"),("How the intro works","#intro")],"<span>You introduce</span><span>TDC runs the process</span><span>The seller decides</span>",bold="Relaunch the value in <em>your write-offs.</em>")}

<section class="sec">
{sh('01','Why it matters to a fund','The mark is zero. <em>The assets may not be.</em>')}
  <div class="prose grid">
    <p class="reveal">A write-off closes the position on paper. It doesn't always account for what the company built. Data from real operations is hard for AI teams to get any other way, and the companies that created it are often the last ones to think of it as an asset.</p>
    <p class="reveal d2">TDC gives you a way to check, company by company, with no cost to find out and no commitment until the seller sees real offers.</p>
  </div>
  <div class="mt">
{specs([("01","Recovery on written-off positions.","<p>Proceeds flow according to the company's own agreements and obligations, which we don't override.</p>"),("02","No work for your team.","<p>One introduction per company. We handle assessment, buyers, and paperwork.</p>"),("03","Founder goodwill.","<p>You bring founders a useful option at a hard moment, not another ask.</p>"),("04","Discretion.","<p>Nothing is shared with buyers, and no company is named, without the seller's consent and a signed NDA.</p>")],4)}
  </div>
</section>

<section class="sec">
{sh('02','Who this is for',"Funds with companies <em>that didn't make it.</em>")}
{rows([("A","Early-stage funds and angels writing initial checks under roughly $1–2M",None),("B","Partners with portfolio companies that have wound down, been written off, or are winding down now",None),("C","Funds with exposure in manufacturing, software development, or healthcare (other sectors considered)",None),("D","GPs who want a responsible, founder-respecting way to recover something from a loss",None)],'q0')}
</section>

<section class="sec" id="intro">
{sh('03','How the intro works','One introduction. <em>We handle the rest.</em>')}
{specs([("Who to introduce","Founders and officers",'<ul><li>Founders or former officers of portfolio companies that have wound down, been written off, or are clearly heading there</li><li>Ideally companies in manufacturing, software development, or healthcare, but send anything you&#39;re unsure about</li><li>Whoever still has authority over the company&#39;s remaining assets: a founder, board member, or the person handling the wind-down</li></ul>'),
("What we ask of you","A list and an email",'<ul><li>A short list of candidate companies. Names and a sentence each is enough to start.</li><li>A warm email introduction to the right founder or officer. The blurb below is ready to forward.</li><li>Nothing else. You don&#39;t need to share data, documents, or fund information.</li></ul>'),
("What the founder gets","A free, private appraisal",'<ul><li>A free, private appraisal of what the company&#39;s data may be worth to AI buyers</li><li>A sell-side advisor who works only for them, with several buyers competing</li><li>Full control: they approve every step, see every offer, and can stop at any time</li><li>No data leaves their hands until a deal they&#39;ve approved closes</li></ul>')])}
  <div class="mt reveal">
    <table class="tbl">
      <thead><tr><th>You do</th><th>TDC does</th><th>The founder decides</th></tr></thead>
      <tbody>
        <tr><td data-h="You do">Name the companies</td><td data-h="TDC does">Assessment call and private appraisal</td><td data-h="The founder decides">Whether to go to market</td></tr>
        <tr><td data-h="You do">Make the intro</td><td data-h="TDC does">Rights review, de-identification plan, buyer outreach under NDA</td><td data-h="The founder decides">Which offers to pursue</td></tr>
        <tr><td data-h="You do">Stay informed (optional)</td><td data-h="TDC does">Negotiation and closing support</td><td data-h="The founder decides">Whether to sign</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section class="sec">
  <div class="sh grid solo"><div class="reveal">{k('04','Forwardable blurb')}</div></div>
  <div class="grid">
    <div class="blurb-side"><h2 class="d reveal" style="font-size:var(--t-1)">Ready to send <em>to a founder.</em></h2><p class="lead reveal d2">Copy and paste. Edit freely.</p></div>
    <div class="letter reveal d2" id="blurb">
      <div class="bar label"><span>Email · Introduction</span><button class="copy-btn" type="button">Copy text</button></div>
      <p>Hi <span class="ph">[Founder name]</span>,</p>
      <p>I wanted to introduce you to AJ Green at The Data Company (TDC). TDC helps wound-down companies license the data they left behind to AI buyers. They work only for the seller, bring several buyers to compete, never hold the data themselves, and you make the final call on everything.</p>
      <p>They offer a free, private appraisal of what <span class="ph">[Company]</span> built. It's not a listing, and no buyer sees anything unless you decide to go further. Given what the team built, I thought it was worth a 20-minute conversation.</p>
      <p>AJ, over to you.</p>
      <p><span class="ph">[Your name]</span></p>
    </div>
  </div>
</section>

<section class="sec">
{sh('05','Investor FAQ','Questions funds <em>ask first.</em>')}
  <div class="faq reveal">
    <details open><summary><span class="i label">Q1</span><span class="t2">Does this cost the fund anything?</span></summary><p>No. The appraisal is free. <span class="tbc" data-cfg="fee">Fee structure: wording to confirm</span></p></details>
    <details><summary><span class="i label">Q2</span><span class="t2">Who receives the proceeds?</span></summary><p>The seller, according to the company's existing agreements, creditor obligations, and wind-down plan. TDC doesn't change who is owed what.</p></details>
    <details><summary><span class="i label">Q3</span><span class="t2">Does TDC guarantee the company has the right to sell its data?</span></summary><p>No. We review what rights appear to exist and flag issues early, but the seller confirms ownership and permissions, and buyers do their own diligence.</p></details>
    <details><summary><span class="i label">Q4</span><span class="t2">Will buyers know which fund or company this is?</span></summary><p>Not without consent. Buyers see an anonymized summary first. Names are shared only after the seller approves and the buyer signs an NDA. <a class="cfg-link" data-cfg-href="ndaUrl" hidden>Read our standard NDA</a></p></details>
    <details><summary><span class="i label">Q5</span><span class="t2">What happens to personal or sensitive data?</span></summary><p>De-identification is part of the process, not an afterthought. Records that can't be handled responsibly stay out of the deal. <span data-cfg="deid" data-cfg-hide></span></p></details>
  </div>
</section>

{BIO.replace('{n}','06')}
{close('07',"Find out what's still <em>on the books.</em>","A free portfolio data appraisal is private and carries no obligation.","Get a free portfolio data appraisal",href="appraisal.html?role=investor",img='rise.jpg',bold="Put your write-offs <em>back on the pad.</em>")}
''','''<script>
document.querySelector('.copy-btn').addEventListener('click',function(e){
  var t=[].map.call(document.querySelectorAll('#blurb p'),function(p){return p.innerText}).join('\\n\\n'),b=e.target;
  function ok(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy text'},1800)}
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(ok,fallback)}else fallback();
  function fallback(){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();try{document.execCommand('copy');ok()}catch(x){}a.remove()}
});
</script>
''')

# ---------- FOUNDERS ----------
concerns=[("I don't want my data out in the world.","We never take custody. Data stays with you until a deal you approve closes."),
("I don't want my company's name shopped around.","Buyers see an anonymized summary. Your name is shared only with your OK and under NDA."),
("Some of this involves customer or patient information.","De-identification is built in. Anything that can't be handled responsibly stays out."),
("I'm not sure the company owns all of it.","We help you review what rights exist before anything goes to market. We won't assume them."),
("I don't have time for this.","One call to start. We handle buyers, paperwork, and negotiation.")]
page('founders.html','For founders — The Data Company',"TDC helps founders of wound-down companies license their company's data to AI buyers. We work only for you, bring several buyers to compete, never hold your data, and you always decide.",f'''
{phero('smoke.jpg','For founders',"The company closed. <em>What you built may still be worth something.</em>","TDC helps founders of wound-down companies license their company's data to AI buyers. We work only for you, bring several buyers to compete, never hold your data, and you always decide.",[("Get a free data appraisal","appraisal.html?role=founder"),("How it works","how-it-works.html")],"<span>Sell-side only</span><span>No data custody</span><span>You decide</span>")}

<section class="sec">
{sh('01','Why founders call us',"Winding down is hard enough. <em>This part doesn't have to be.</em>")}
  <div class="prose grid">
    <p class="reveal">Winding down a company is hard enough. You shouldn't also have to figure out whether the records, code, or datasets your team built have value, or who would pay for them.</p>
    <p class="reveal d2">TDC does that work for you. We start with a private conversation and a free appraisal. If there's something worth pursuing and you want to go ahead, we take a de-identified summary to several AI buyers under NDA and bring every offer back to you. If you don't like the terms, you walk away. Nothing has been shared that you didn't approve.</p>
  </div>
</section>

<section class="scene dense">
  <div class="bg" style="background-image:url(media/plume.jpg)"></div>
  <div class="w">
{sh('02','Your concerns','How we handle <em>what worries you.</em>')}
{rows([(f"0{j+1}",a,b) for j,(a,b) in enumerate(concerns)],'q')}
  </div>
</section>

<section class="sec">
{sh('03','Sent by your investor?',"They've made the intro. <em>The rest is up to you.</em>","Many founders reach us through their investors. If your investor sent you here, they've already done the introduction. You're under no obligation either way.")}
  <div class="ctas reveal"><a class="btn" href="appraisal.html?role=founder">Get a free data appraisal {AR}</a></div>
</section>

{close('04',"The company closed. <em>The data may still be worth something.</em>","Start with one private call and a free appraisal.","Get a free data appraisal",href="appraisal.html?role=founder",img='ascent.jpg')}
''')

# ---------- HOW IT WORKS ----------
LONG=[("01","Assessment call","A short conversation, usually with the founder or whoever is handling the wind-down. We learn what the company did, what records remain, and where they're stored. No data is shared on this call.","You decide whether to continue"),
("02","Private appraisal","We look at what the data is, how it was created, what permissions and agreements appear to apply, and how AI buyers are likely to see it. You get a written appraisal with a view on fit, likely buyer interest, and anything that needs attention first, such as rights questions or de-identification. The appraisal is private. It is not a listing, and no buyer sees it.","You decide whether to take it to market"),
("03","Buyer process","If you go ahead, we prepare an anonymized summary and take it to several qualified AI buyers at once so they compete on price and terms. A buyer learns your company's name only after you approve it and they sign an NDA. Data stays with you; buyers evaluate through approved samples or controlled review, never a handover.","You decide which offers to pursue"),
("04","Seller's final say","We bring every offer back to you, laid out side by side: price, license scope, exclusivity, duration, and data-handling terms. We'll give you our recommendation. You accept, negotiate, or walk away.","You decide. Always")]
ph=''.join(f'''
      <div class="phase" data-from="{.2+i*.2:.2f}"{'' if i==3 else f' data-to="{.4+i*.2:.2f}"'}>
        {k('Step '+n,t)}
        <h2 class="d">{t}. <em>{d}.</em></h2>
      </div>''' for i,(n,t,b,d) in enumerate(LONG))
TBC='<span class="tbc" data-cfg="fee">Fee wording TBC</span>'
trs=[("Cost to you","Free","Free",TBC,TBC),
("Data shared","None","Description and metadata only, with you","Anonymized summary; samples only with approval","Per the agreement you sign"),
("Company name shared","No","No","Only with your OK, under NDA","Yes, with the chosen buyer"),
("Your commitment","None","None","None until you sign","Your call")]
H=["","Assessment call","Private appraisal","Buyer process","Seller's final say"]
tr='\n'.join('        <tr>'+''.join(f'<td data-h="{H[j]}">{c}</td>' if j else f'<td>{c}</td>' for j,c in enumerate(r))+'</tr>' for r in trs)
page('how-it-works.html','How it works — The Data Company','TDC runs a sell-side process built for discretion: one free assessment, a private appraisal, a competitive buyer process, and a final decision that is always yours.',f'''
<header class="hero" data-launch>
  <div class="stage">
    <video data-src="media/launch.mp4" data-src-mobile="media/launch-portrait.mp4" data-poster-mobile="media/launch-portrait-poster.jpg" poster="media/launch-poster.jpg" muted playsinline preload="auto"></video>
    <div class="copy">
      <div class="phase on" data-from="-1" data-to=".2">
        {k('00','How it works')}
        <h1 class="d" data-bold="Countdown to a deal. <em>You hold the launch key.</em>">A careful process. <em>Your decision at every step.</em></h1>
        <p class="sub">TDC runs a sell-side process built for discretion: one free assessment, a private appraisal, a competitive buyer process, and a final decision that is always yours.</p>
      </div>{ph}
    </div>
    <div class="meta label"><span>Four steps · Seller decides</span><span class="bar"></span></div>
    <div class="cue label">Scroll</div>
  </div>
</header>

<section class="sec" id="process">
{sh('01','The four steps','What happens, <em>and who decides.</em>')}
{rows([(n,t,f"{b}<b>{d}</b>") for n,t,b,d in LONG])}
</section>

<section class="sec">
{sh('02','At a glance',"What's shared, <em>and when.</em>")}
  <div class="reveal">
    <table class="tbl">
      <thead><tr>{''.join(f'<th>{h}</th>' for h in H)}</tr></thead>
      <tbody>
{tr}
      </tbody>
    </table>
  </div>
</section>

{close('03',"Start with a free, <em>private appraisal.</em>","An appraisal is private and carries no obligation.","Get a free portfolio data appraisal",img='rise.jpg',bold="Start the <em>launch sequence.</em>")}
''')

# ---------- APPRAISAL: launch sequence ----------
TRACK=[("T-4","Who you are"),("T-3","The portfolio"),("T-2","What was built"),("T-1","Pre-flight check")]
trk=''.join(f'<li data-i="{n}"><span class="label">{a}</span><span class="label">{b}</span></li>' for n,(a,b) in enumerate(TRACK))
page('appraisal.html','Free appraisal — The Data Company',"Get a free portfolio data appraisal. It's private, it's free, and it is not a listing. Nothing goes to a buyer without your consent.",f"""
<main class="ls" id="main">
  <div class="ls-stage" aria-hidden="true"><video data-src="media/launch.mp4" data-src-mobile="media/launch-portrait.mp4" poster="media/launch-poster.jpg" data-poster-mobile="media/launch-portrait-poster.jpg" muted playsinline preload="auto"></video></div>
  <div class="ls-panel">
    <div class="ls-head">
      {k('<b id="tm">T-4</b>','Launch sequence')}
      <h1 class="d" data-bold="Start the <em>launch sequence.</em>">Get a free portfolio <em>data appraisal.</em></h1>
      <p class="lead">Four short steps. Private, free, and not a listing.</p>
    </div>
    <ol class="ls-track">{trk}</ol>
    <form id="f" novalidate>
      <input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px">
      <fieldset class="st on" data-step="0">
        <div class="f"><label class="label" for="n">Your name</label><input type="text" id="n" name="name" required autocomplete="name"></div>
        <div class="f"><label class="label" for="e">Email</label><input type="email" id="e" name="email" required autocomplete="email"></div>
        <div class="f"><div class="q label">I am a…</div>{chips('role',['Investor','Founder or former officer','Other'],req=True)}</div>
      </fieldset>
      <fieldset class="st" data-step="1">
        <div class="f"><label class="label" for="o">Fund or company name <span class="opt">Kept confidential</span></label><input type="text" id="o" name="org" required></div>
        <div class="f" id="count" hidden><div class="q label">Number of companies to review</div>{chips('count',['1','2–5','6–20','More than 20'])}</div>
        <div class="f"><div class="q label">Company status</div>{chips('status',['Wound down','Written off','Winding down','Other'])}</div>
      </fieldset>
      <fieldset class="st" data-step="2">
        <div class="f"><div class="q label">Industry <span class="opt">Select any</span></div>{chips('industry',['Manufacturing','Software development','Healthcare','Other'],'checkbox')}</div>
        <div class="f"><label class="label" for="b">What did the company build or collect? <span class="opt">Optional</span></label><textarea id="b" name="built" placeholder="A sentence is enough."></textarea></div>
      </fieldset>
      <fieldset class="st" data-step="3">
        <div class="f"><label class="label" for="kn">Anything we should know? <span class="opt">Optional</span></label><textarea id="kn" name="notes" placeholder="E.g. customer or patient data, open obligations."></textarea></div>
        <div class="f"><div class="q label">Your request</div><dl class="sum" id="sum"></dl></div>
      </fieldset>
      <div class="ls-nav">
        <button class="btn line" type="button" id="back">Back</button>
        <button class="btn" type="submit" id="next"><span id="nl">Continue</span> {AR}</button>
      </div>
      <p class="fine err" id="err" hidden>We couldn't send this just now. Please try again in a minute.</p>
      <p class="fine">Submitting this form doesn't share anything with buyers or commit you to anything. We'll reply within <span class="tbc" data-cfg="replyTime">response time TBC</span>.</p>
    </form>
    <div class="done" aria-live="polite">
      <h2 class="d">Request received. <em>We'll be in touch.</em></h2>
      <p class="lead">Nothing has been shared with any buyer, and you haven't committed to anything. We'll reply within <span class="tbc" data-cfg="replyTime">response time TBC</span>.</p>
      <div class="ctas"><a class="btn" id="book" data-cfg-href="bookingUrl" hidden target="_blank" rel="noopener">Book the assessment call {AR}</a><a class="btn line" href="how-it-works.html">See what happens next</a></div>
    </div>
  </div>
  <div class="ls-hud label"><span>Sell-side only · Not a listing</span><span class="bar"><i id="bar"></i></span></div>
</main>
""",r"""<script>
(function(){
  var f=document.getElementById('f'),main=document.getElementById('main'),count=document.getElementById('count');
  var steps=[].slice.call(f.querySelectorAll('.st')),track=[].slice.call(document.querySelectorAll('.ls-track li'));
  var back=document.getElementById('back'),nl=document.getElementById('nl'),tm=document.getElementById('tm'),bar=document.getElementById('bar');
  var v=document.querySelector('.ls-stage video'),small=matchMedia('(max-width:720px)').matches,reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  v.muted=true;v.playsInline=true;v.src=small?v.dataset.srcMobile:v.dataset.src;if(small)v.poster=v.dataset.posterMobile;
  var STOPS=[.35,2.6,4.6,6.6,10],target=STOPS[0],cur=0;
  v.addEventListener('loadedmetadata',function(){STOPS[4]=v.duration-.08;v.currentTime=STOPS[0];v.pause()});
  function fly(){
    if(v.readyState>=1){
      if(reduce){if(Math.abs(v.currentTime-target)>.05)v.currentTime=target}
      else if(v.currentTime>target+.08){v.pause();v.currentTime=target}
      else if(v.currentTime<target-.04){if(v.paused)v.play().catch(function(){})}
      else if(!v.paused)v.pause();
    }
    requestAnimationFrame(fly);
  }
  requestAnimationFrame(fly);
  var role=new URLSearchParams(location.search).get('role'),map={investor:'Investor',founder:'Founder or former officer'};
  if(map[role])f.querySelector('input[name=role][value="'+map[role]+'"]').checked=true;
  var qp=new URLSearchParams(location.search);
  (qp.get('industry')||'').split('|').forEach(function(x){var el=f.querySelector('input[name=industry][value="'+x+'"]');if(el)el.checked=true});
  if(qp.get('left'))f.built.value='Left behind: '+qp.get('left').split('|').join(', ')+'.';
  var signal=qp.get('signal')||'';
  var at=0;
  function val(n){var x=f.querySelectorAll('[name='+n+']:checked');if(x.length)return[].map.call(x,function(i){return i.value}).join(', ');var i=f.querySelector('[name='+n+']');return i&&i.type!=='radio'&&i.type!=='checkbox'?i.value.trim():''}
  function sync(){var r=val('role');count.hidden=r!=='Investor'}
  function show(i){
    at=i;steps.forEach(function(s,n){s.classList.toggle('on',n===i)});
    track.forEach(function(t,n){t.classList.toggle('on',n===i);t.classList.toggle('ok',n<i)});
    back.style.visibility=i?'visible':'hidden';nl.textContent=i===3?'Request my appraisal':'Continue';
    tm.textContent='T-'+(4-i);target=STOPS[i];bar.style.transform='scaleX('+(i/4)+')';
    if(i===3){var rows=[['Name',val('name')],['Email',val('email')],['Role',val('role')],['Fund or company',val('org')],['Companies',count.hidden?'':val('count')],['Status',val('status')],['Industry',val('industry')]];
      document.getElementById('sum').innerHTML=rows.filter(function(r){return r[1]}).map(function(r){return '<dt class="label">'+r[0]+'</dt><dd></dd>'}).join('');
      [].forEach.call(document.querySelectorAll('#sum dd'),function(d,n){d.textContent=rows.filter(function(r){return r[1]})[n][1]})}
    var first=steps[i].querySelector('input[type=text],input[type=email],textarea');if(first&&!small)first.focus({preventScroll:true});
    if(small&&i)document.querySelector('.ls-track').scrollIntoView({behavior:'smooth',block:'start'});
  }
  function check(i){var ok=true;steps[i].querySelectorAll('.f').forEach(function(x){x.classList.remove('bad')});
    steps[i].querySelectorAll('[required]').forEach(function(el){var bad=el.type==='radio'?!f.querySelector('input[name='+el.name+']:checked'):!el.checkValidity()||!el.value.trim();if(bad){el.closest('.f').classList.add('bad');ok=false}});return ok}
  f.addEventListener('change',function(e){sync();var x=e.target.closest('.f');if(x)x.classList.remove('bad')});
  f.addEventListener('input',function(e){var x=e.target.closest('.f');if(x)x.classList.remove('bad')});
  back.addEventListener('click',function(){if(at>0)show(at-1)});
  f.addEventListener('submit',function(e){
    e.preventDefault();if(!check(at))return;
    if(at<3){show(at+1);return}
    var btn=document.getElementById('next'),err=document.getElementById('err');btn.disabled=true;err.hidden=true;
    var body={name:val('name'),email:val('email'),role:val('role'),org:val('org'),count:count.hidden?'':val('count'),status:val('status'),
      industry:[].map.call(f.querySelectorAll('[name=industry]:checked'),function(x){return x.value}),built:val('built'),notes:val('notes'),signal:signal,page:location.pathname+location.search,website:f.website.value};
    fetch('/api/appraisal',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)})
      .then(function(r){if(!r.ok)throw r;liftoff()})
      .catch(function(){err.hidden=false;btn.disabled=false});
  });
  function liftoff(){
    main.classList.add('sent');tm.textContent='T-0';document.querySelector('.ls-head .k span').textContent='Liftoff';target=STOPS[4];bar.style.transform='scaleX(1)';
    track.forEach(function(t){t.classList.remove('on');t.classList.add('ok')});
    document.querySelector('.ls-panel').scrollIntoView({behavior:'smooth'});
  }
  sync();show(0);
})();
</script>
""")

# ---------- PRIVACY ----------
def ps(h,body): return f'<div class="row grid reveal"><div class="i label"></div><div class="t2" style="grid-column:2/span 4;font-size:var(--t-3)">{h}</div><div class="pp" style="grid-column:7/span 6">{body}</div></div>'
page('privacy.html','Privacy — The Data Company','How The Data Company handles information you share through this site.',f"""
<section class="sec" style="padding-top:clamp(140px,18vh,200px)">
{sh('00','Privacy','How we handle <em>what you share.</em>','<span class="tbc">Draft for review. Last updated: date TBC</span>')}
  <div class="ledger privacy">
{ps('What we collect','<p>When you request an appraisal we collect what you type into the form: your name, email, role, fund or company name, and anything you choose to tell us about the company. The quick assessment on the home page runs in your browser; its answers are only sent if you carry them into the appraisal form and submit it.</p>')}
{ps('How we use it','<p>Only to reply to you, prepare a private appraisal, and run a process you have approved. We never sell your information and never share it with a buyer without your consent and a signed NDA.</p>')}
{ps('Where it is kept','<p>Requests are stored in our internal workspace (Notion) and may be sent to us by email. The site is hosted on Vercel, which keeps standard server logs. Fonts load from Google Fonts, which receives your IP address when a page loads.</p>')}
{ps('Cookies and tracking','<p>This site sets no advertising or analytics cookies.</p>')}
{ps('Your choices','<p>You can ask us to see, correct, or delete what you sent at any time. Email <span class="tbc" data-cfg="contactEmail">contact email TBC</span>.</p>')}
  </div>
</section>
""")
print('ok')
