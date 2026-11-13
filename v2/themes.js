/* Design-language variants for the v2 home. Pick one with ?t=<id>. */
window.TDC_THEMES = [
  { id:'dynamism', name:'American Dynamism', note:'a16z kit: night, sapphire, ivory, gold. Didone display.',
    fonts:'Bodoni+Moda:ital,opsz,wght@0,6..96,400;1,6..96,400&family=Newsreader:ital,opsz,wght@0,6..72,300;1,6..72,300&family=Archivo:wdth,wght@62..125,300..600',
    type:['Bodoni Moda','Newsreader','Archivo Expanded'],
    v:{bg:'#01050D',bg2:'#092344',bg3:'#06142A',fg:'#F6F4EE',ac:'#CFA13D',acInk:'#8A6A22',onAc:'#01050D',paper:'#F6F4EE',ink:'#01050D',ink2:'#22262E',hero:'#01050D',heroFg:'#F6F4EE'},
    t:{display:'"Bodoni Moda",serif',body:'"Newsreader",serif',ui:'"Archivo",sans-serif',dWt:400,dLs:'-.02em',dLh:.98,dTt:'none',em:'italic',ds:1}},
  { id:'mission', name:'Mission Control', note:'Graphite and safety orange. Condensed caps, mono labels. Launch-ops feel.',
    fonts:'Barlow+Condensed:ital,wght@0,500;0,600;1,500&family=Inter:wght@300;400;500&family=JetBrains+Mono:wght@400;500',
    type:['Barlow Condensed','Inter','JetBrains Mono'],
    v:{bg:'#0B0B0C',bg2:'#17181A',bg3:'#111214',fg:'#F2F2F0',ac:'#FF5A1F',acInk:'#D9440F',onAc:'#0B0B0C',paper:'#EDEDEA',ink:'#0B0B0C',ink2:'#2A2B2E',hero:'#0B0B0C',heroFg:'#F2F2F0'},
    t:{display:'"Barlow Condensed",sans-serif',body:'"Inter",sans-serif',ui:'"JetBrains Mono",monospace',dWt:600,dLs:'-.005em',dLh:.9,dTt:'uppercase',em:'normal',ds:1.12,bWt:300},
    vf:'saturate(.55) contrast(1.15)'},
  { id:'greenback', name:'Greenback', note:'Treasury green, banknote cream, brass. Old-money credibility.',
    fonts:'Playfair+Display:ital,wght@0,400;0,500;1,400&family=Libre+Caslon+Text:ital,wght@0,400;1,400&family=IBM+Plex+Mono:wght@400;500',
    type:['Playfair Display','Libre Caslon Text','IBM Plex Mono'],
    v:{bg:'#0A1A13',bg2:'#123326',bg3:'#0E241B',fg:'#F2EDDF',ac:'#C2A15A',acInk:'#7E6327',onAc:'#0A1A13',paper:'#F2EDDF',ink:'#0A1A13',ink2:'#2B3530',hero:'#07130E',heroFg:'#F2EDDF'},
    t:{display:'"Playfair Display",serif',body:'"Libre Caslon Text",serif',ui:'"IBM Plex Mono",monospace',dWt:400,dLs:'-.015em',dLh:1,dTt:'none',em:'italic',ds:.96,bWt:400},
    vf:'sepia(.25) saturate(.8)',tint:'#1F6B47',tintO:.28},
  { id:'renaissance', name:'Renaissance', note:'Oxblood, parchment, gilt. Roman capitals, Garamond text.',
    fonts:'Cinzel:wght@400;500;600&family=EB+Garamond:ital,wght@0,400;0,500;1,400',
    type:['Cinzel','EB Garamond','Cinzel'],
    v:{bg:'#1C0709',bg2:'#3A0D12',bg3:'#2A0A0E',fg:'#F1E8D4',ac:'#D1AB55',acInk:'#86621E',onAc:'#1C0709',paper:'#F1E8D4',ink:'#1C0709',ink2:'#3B2A26',hero:'#160506',heroFg:'#F1E8D4'},
    t:{display:'"Cinzel",serif',body:'"EB Garamond",serif',ui:'"Cinzel",serif',dWt:400,dLs:'.01em',dLh:1.04,dTt:'none',em:'normal',ds:.74,bWt:400},
    vf:'sepia(.45) contrast(1.05)'},
  { id:'glacier', name:'Glacier', note:'Deep ink and ice blue. Wide geometric display. Cold, precise, futurist.',
    fonts:'Syne:wght@400;500;600;700&family=Inter:wght@300;400;500&family=Space+Mono:wght@400',
    type:['Syne','Inter','Space Mono'],
    v:{bg:'#06111B',bg2:'#0C2233',bg3:'#091A27',fg:'#EAF3F7',ac:'#8FD3FF',acInk:'#1E6E9E',onAc:'#06111B',paper:'#EAF3F7',ink:'#06111B',ink2:'#26343F',hero:'#050E17',heroFg:'#EAF3F7'},
    t:{display:'"Syne",sans-serif',body:'"Inter",sans-serif',ui:'"Space Mono",monospace',dWt:600,dLs:'-.035em',dLh:.95,dTt:'none',em:'normal',ds:.86,bWt:300},
    vf:'grayscale(.5) contrast(1.1)',tint:'#5FB8FF',tintO:.35},
  { id:'mars', name:'Mars', note:'Rust, sand, ember. Warm frontier editorial.',
    fonts:'Instrument+Serif:ital@0;1&family=Instrument+Sans:wdth,wght@75..100,400..600',
    type:['Instrument Serif','Instrument Sans','Instrument Sans'],
    v:{bg:'#150B07',bg2:'#3A1A0E',bg3:'#24110A',fg:'#F3E6D3',ac:'#E8692C',acInk:'#B04A16',onAc:'#150B07',paper:'#F3E6D3',ink:'#150B07',ink2:'#3D2B22',hero:'#120805',heroFg:'#F3E6D3'},
    t:{display:'"Instrument Serif",serif',body:'"Instrument Sans",sans-serif',ui:'"Instrument Sans",sans-serif',dWt:400,dLs:'-.025em',dLh:.95,dTt:'none',em:'italic',ds:1.08,bWt:400},
    vf:'saturate(1.15) sepia(.2)'},
  { id:'swiss', name:'Swiss Modernist', note:'Black, white, signal red. Tight grotesk, no ornament. Maximum contrast.',
    fonts:'Inter+Tight:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@300;400;500',
    type:['Inter Tight','Inter','Inter'],
    v:{bg:'#000000',bg2:'#111111',bg3:'#0A0A0A',fg:'#FFFFFF',ac:'#E30613',acInk:'#E30613',onAc:'#FFFFFF',paper:'#FFFFFF',ink:'#000000',ink2:'#222222',hero:'#000000',heroFg:'#FFFFFF'},
    t:{display:'"Inter Tight",sans-serif',body:'"Inter",sans-serif',ui:'"Inter",sans-serif',dWt:600,dLs:'-.045em',dLh:.92,dTt:'none',em:'normal',ds:.98,bWt:300},
    vf:'grayscale(1) contrast(1.25)'},
  { id:'blueprint', name:'Blueprint', note:'Cobalt duotone, cyan. Engineering drawing meets space program.',
    fonts:'Unbounded:wght@300;400;500&family=IBM+Plex+Sans:wght@300;400&family=IBM+Plex+Mono:wght@400;500',
    type:['Unbounded','IBM Plex Sans','IBM Plex Mono'],
    v:{bg:'#040B2A',bg2:'#0B2A8A',bg3:'#081C5C',fg:'#EEF3FF',ac:'#6FE3FF',acInk:'#0B5FA8',onAc:'#040B2A',paper:'#EEF3FF',ink:'#040B2A',ink2:'#24304F',hero:'#030822',heroFg:'#EEF3FF'},
    t:{display:'"Unbounded",sans-serif',body:'"IBM Plex Sans",sans-serif',ui:'"IBM Plex Mono",monospace',dWt:300,dLs:'-.03em',dLh:1,dTt:'none',em:'normal',ds:.72,bWt:300},
    vf:'grayscale(1) contrast(1.2)',tint:'#2456FF',tintO:.6},
  { id:'ledger', name:'Ledger Daylight', note:'Brand v2 palette: paper, deep ink, copper. Light sections, dark hero.',
    fonts:'Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,400&family=Inter:wght@300;400;500&family=IBM+Plex+Mono:wght@400;500',
    type:['Newsreader','Inter','IBM Plex Mono'],
    v:{bg:'#F7F4EE',bg2:'#EFEAE0',bg3:'#E8E1D3',fg:'#14213D',ac:'#A8643A',acInk:'#C98A5E',onAc:'#F7F4EE',paper:'#14213D',ink:'#F7F4EE',ink2:'#C9CDD6',hero:'#0E1830',heroFg:'#F7F4EE'},
    t:{display:'"Newsreader",serif',body:'"Inter",sans-serif',ui:'"IBM Plex Mono",monospace',dWt:400,dLs:'-.025em',dLh:1,dTt:'none',em:'italic',ds:1,bWt:300}},
  { id:'chroma', name:'Chroma', note:'Black and chrome with a violet-to-cyan gradient. Technofuturist.',
    fonts:'Space+Grotesk:wght@300;400;500&family=Space+Mono:wght@400',
    type:['Space Grotesk','Space Grotesk','Space Mono'],
    v:{bg:'#07070A',bg2:'#12121A',bg3:'#0C0C12',fg:'#E8E9EE',ac:'#B9A6FF',acInk:'#6A3FD8',onAc:'#07070A',paper:'#E8E9EE',ink:'#07070A',ink2:'#2A2A33',hero:'#050508',heroFg:'#E8E9EE'},
    t:{display:'"Space Grotesk",sans-serif',body:'"Space Grotesk",sans-serif',ui:'"Space Mono",monospace',dWt:300,dLs:'-.045em',dLh:.95,dTt:'none',em:'normal',ds:.95,bWt:300},
    vf:'grayscale(.85) contrast(1.15)',
    css:'.d em{background:linear-gradient(90deg,#A162FF,#56FAF7);-webkit-background-clip:text;background-clip:text;color:transparent!important}.btn:not(.line){background:linear-gradient(90deg,#A162FF,#56FAF7)}'},
  { id:'launchops', name:'Launch Ops', blend:true, note:'Blend: Swiss type with Mission Control colors. Tight grotesk, graphite, safety orange, mono labels.',
    fonts:'Inter+Tight:ital,wght@0,500;0,600;0,700&family=Inter:wght@300;400;500&family=JetBrains+Mono:wght@400;500',
    type:['Inter Tight','Inter','JetBrains Mono'],
    v:{bg:'#0B0B0C',bg2:'#17181A',bg3:'#111214',fg:'#F2F2F0',ac:'#FF5A1F',acInk:'#D9440F',onAc:'#0B0B0C',paper:'#EDEDEA',ink:'#0B0B0C',ink2:'#2A2B2E',hero:'#0B0B0C',heroFg:'#F2F2F0'},
    t:{display:'"Inter Tight",sans-serif',body:'"Inter",sans-serif',ui:'"JetBrains Mono",monospace',dWt:600,dLs:'-.045em',dLh:.92,dTt:'none',em:'normal',ds:.98,bWt:300},
    vf:'saturate(.55) contrast(1.15)'},
  { id:'signal', name:'Signal', blend:true, note:'Blend: Mission Control condensed caps with the Swiss palette. Pure black and white, signal red, black-and-white video.',
    fonts:'Barlow+Condensed:ital,wght@0,500;0,600;1,500&family=Inter:wght@300;400;500',
    type:['Barlow Condensed','Inter','Inter'],
    v:{bg:'#000000',bg2:'#111111',bg3:'#0A0A0A',fg:'#FFFFFF',ac:'#E30613',acInk:'#E30613',onAc:'#FFFFFF',paper:'#FFFFFF',ink:'#000000',ink2:'#222222',hero:'#000000',heroFg:'#FFFFFF'},
    t:{display:'"Barlow Condensed",sans-serif',body:'"Inter",sans-serif',ui:'"Inter",sans-serif',dWt:600,dLs:'-.005em',dLh:.9,dTt:'uppercase',em:'normal',ds:1.12,bWt:300},
    vf:'grayscale(1) contrast(1.25)'},
  { id:'countdown', name:'Countdown', blend:true, note:'Blend: condensed caps for big headlines, Swiss grotesk for smaller titles. Black, white, orange; black-and-white video with orange fire.',
    fonts:'Barlow+Condensed:ital,wght@0,500;0,600;1,500&family=Inter+Tight:wght@500;600&family=Inter:wght@300;400;500&family=JetBrains+Mono:wght@400;500',
    type:['Barlow Condensed + Inter Tight','Inter','JetBrains Mono'],
    v:{bg:'#000000',bg2:'#121212',bg3:'#0A0A0A',fg:'#FFFFFF',ac:'#FF5A1F',acInk:'#E04A10',onAc:'#000000',paper:'#FFFFFF',ink:'#000000',ink2:'#222222',hero:'#000000',heroFg:'#FFFFFF'},
    t:{display:'"Barlow Condensed",sans-serif',display2:'"Inter Tight",sans-serif',d2Tt:'none',d2Ls:'-.035em',body:'"Inter",sans-serif',ui:'"JetBrains Mono",monospace',dWt:600,dLs:'-.005em',dLh:.9,dTt:'uppercase',em:'normal',ds:1.12,bWt:300},
    vf:'grayscale(1) contrast(1.25)',tint:'#FF5A1F',tintO:.32}
];
(function(){
  var q=new URLSearchParams(location.search).get('t'); if(!q) return;
  var th=TDC_THEMES.find(function(x){return x.id===q}); if(!th) return;
  function rgb(h){h=h.replace('#','');return [0,2,4].map(function(i){return parseInt(h.substr(i,2),16)}).join(',')}
  var v=th.v,t=th.t,r=document.documentElement.style;
  var set={'--bg':v.bg,'--bg2':v.bg2,'--bg3':v.bg3,'--bg-rgb':rgb(v.bg),'--fg-rgb':rgb(v.fg),'--ac':v.ac,'--ac-rgb':rgb(v.ac),'--ac-ink':v.acInk,'--on-ac':v.onAc,
    '--paper':v.paper,'--ink':v.ink,'--ink-rgb':rgb(v.ink),'--ink2':v.ink2,'--h-rgb':rgb(v.hero),'--hf-rgb':rgb(v.heroFg),
    '--display':t.display,'--body':t.body,'--ui':t.ui,'--d-wt':t.dWt,'--d-ls':t.dLs,'--d-lh':t.dLh,'--d-tt':t.dTt,'--em':t.em,'--ds':t.ds,'--b-wt':t.bWt||300,
    '--vf':th.vf||'none','--tint':th.tint||'transparent','--tint-o':th.tintO||0};
  if(t.display2){set['--display2']=t.display2;set['--d2-tt']=t.d2Tt;set['--d2-ls']=t.d2Ls}
  for(var k in set) r.setProperty(k,set[k]);
  document.documentElement.dataset.theme=th.id;
  document.addEventListener('DOMContentLoaded',function(){
    var f=document.getElementById('fonts'); if(f) f.href='https://fonts.googleapis.com/css2?family='+th.fonts+'&display=swap';
    if(th.css){var s=document.createElement('style');s.textContent=th.css;document.head.appendChild(s)}
    var g=document.getElementById('tag'); if(g) g.textContent='Variant · '+th.name;
  });
})();
