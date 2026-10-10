from lib import *
from data import *
import json

LIB_CSS = '''
.libhero{background:var(--slate-deep); color:#fff; position:relative; overflow:hidden}
.libhero .wrap{padding-block:clamp(48px,6vw,84px) clamp(36px,4vw,56px); position:relative; z-index:3}
.libhero .wm-daisy{z-index:2}
.libhero .mk{background:none; color:var(--mint)}
.libhero h1{font-size:clamp(3rem,9vw,8.4rem); font-stretch:125%; font-weight:900; text-transform:uppercase; line-height:.85; letter-spacing:-.03em; margin:0 0 .25em}
.libhero__bg{position:absolute; inset:0; display:grid; grid-template-columns:repeat(8,1fr); gap:6px; opacity:.3; z-index:1}
.libhero__bg img{width:100%; height:100%; object-fit:cover}
.libhero__bg::after{content:""; position:absolute; inset:0; background:linear-gradient(90deg, var(--slate-deep) 26%, rgba(22,53,64,.55) 62%, rgba(22,53,64,.2)), linear-gradient(0deg, var(--slate-deep), transparent 40%)}
.lsearch{display:flex; align-items:center; gap:12px; background:#fff; border-radius:14px; padding:6px 6px 6px 18px; max-width:860px; box-shadow:var(--shadow-soft)}
.lsearch svg{width:24px; height:24px; color:var(--teal); flex:none}
.lsearch input{flex:1; min-width:0; border:0; outline:0; font:inherit; font-size:1.2rem; padding:12px 0; color:var(--slate); background:transparent}
.lsearch .btn{box-shadow:none}
.lcounts{display:flex; flex-wrap:wrap; gap:10px 26px; margin-top:22px; font-family:var(--mono); font-size:.8rem; letter-spacing:.06em; text-transform:uppercase; color:var(--aqua)}
.lcounts b{color:var(--mint); font-size:1.1rem}
.lbar{position:sticky; top:calc(76px + env(safe-area-inset-top,0px)); z-index:20; background:rgba(255,255,255,.96); backdrop-filter:blur(8px); border-bottom:1px solid var(--line)}
.lbar .wrap{display:flex; flex-wrap:wrap; gap:10px 16px; align-items:center; padding-block:12px}
.fmt{display:flex; gap:4px; background:var(--mist); border-radius:10px; padding:4px}
.fmt button{font:inherit; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:.95rem; border:0; background:transparent; padding:8px 14px; border-radius:7px; cursor:pointer; color:var(--slate); white-space:nowrap}
.fmt button[aria-pressed="true"]{background:var(--slate); color:#fff}
.fmt button span{font-family:var(--mono); font-size:.7rem; opacity:.7; margin-left:4px}
.lsel{display:flex; gap:8px; margin-left:auto; flex-wrap:wrap}
.lsel select{font:inherit; font-size:.9rem; font-weight:600; padding:9px 12px; border-radius:8px; border:2px solid var(--line); background:#fff; color:var(--slate)}
.topics{display:flex; gap:6px; overflow-x:auto; padding:2px 0 12px; scrollbar-width:thin; flex-basis:100%}
.topics button{font:inherit; font-size:.82rem; font-weight:700; white-space:nowrap; padding:7px 12px; border-radius:999px; border:1.5px solid var(--line); background:#fff; cursor:pointer; color:var(--slate)}
.topics button:hover{border-color:var(--teal)}
.topics button[aria-pressed="true"]{background:var(--mint); border-color:var(--mint)}
.lstatus{display:flex; justify-content:space-between; align-items:center; gap:12px; margin:26px 0 18px; flex-wrap:wrap}
.lstatus p{margin:0; font-weight:600}
.lstatus button{font:inherit; font-weight:700; color:var(--logo-teal); background:none; border:0; cursor:pointer; text-decoration:underline; text-decoration-color:var(--mint); text-underline-offset:3px}
.lgrid{display:grid; grid-template-columns:repeat(auto-fill,minmax(270px,1fr)); gap:20px}
@media (min-width:900px){ .lgrid--3{grid-template-columns:repeat(3,minmax(0,1fr)); grid-auto-flow:dense} .lgrid--lead > :first-child, .lgrid--lead2 > :nth-child(-n+2){grid-column:span 2; flex-direction:row} .lgrid--lead > :first-child .item__media, .lgrid--lead2 > :nth-child(-n+2) .item__media{flex:0 0 50%; aspect-ratio:auto; min-height:100%} }
@media (min-width:560px) and (max-width:899px){ .lgrid--3{grid-template-columns:repeat(2,minmax(0,1fr))} .lgrid--lead > :first-child{grid-column:span 2} }
.lgrid--wide{grid-template-columns:minmax(0,1fr)}
@media (min-width:700px){ .lgrid--wide .item{flex-direction:row} .lgrid--wide .item__media{flex:0 0 min(42%,420px); aspect-ratio:auto; min-height:240px} .lgrid--wide .item__body{justify-content:center; padding:26px 30px} .lgrid--wide .item__body p{-webkit-line-clamp:5} }
.lshelf{margin-bottom:54px}
.lshelf:last-child{margin-bottom:0}
.lshelf__head{display:flex; justify-content:space-between; align-items:end; gap:16px; margin-bottom:18px; flex-wrap:wrap}
.lshelf__head h2{font-size:clamp(1.6rem,2.8vw,2.4rem); margin:0}
.item{position:relative; display:flex; flex-direction:column; text-align:left; font:inherit; color:var(--slate); background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; cursor:pointer; text-decoration:none; padding:0; transition:transform .2s, box-shadow .2s; height:100%}
.item:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.item__media{position:relative; aspect-ratio:16/9; background:var(--slate); overflow:hidden}
.item__media img{width:100%; height:100%; object-fit:cover; transition:transform .5s}
.item:hover .item__media img{transform:scale(1.05)}
.item__kind{position:absolute; left:10px; top:10px; display:flex; gap:5px}
.item__kind span{font-family:var(--mono); font-size:.64rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; padding:4px 7px; border-radius:4px; background:rgba(13,34,40,.78); color:#fff}
.item__kind span.g{background:var(--mint); color:var(--slate)}
.item__kind span.w{background:var(--coral); color:var(--slate)}
.item__play{position:absolute; right:10px; bottom:10px; width:40px; height:40px; border-radius:50%; background:var(--mint); color:var(--slate); display:grid; place-items:center}
.item__play svg{width:16px; height:16px; margin-left:2px}
.item__body{padding:16px 18px 18px; display:flex; flex-direction:column; gap:6px; flex:1}
.item__body b{font-family:var(--display); font-stretch:106%; font-size:1.12rem; line-height:1.2}
.item__body small{color:var(--ink-soft); font-size:.82rem; font-weight:600}
.item__body p{font-size:.88rem; color:var(--ink-soft); margin:2px 0 0; line-height:1.5; display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden}
.item__topics{display:flex; flex-wrap:wrap; gap:5px; margin-top:auto; padding-top:8px}
.item__topics span{font-size:.7rem; font-weight:700; background:var(--mist); border-radius:4px; padding:3px 7px}
.item--podcast .item__media{aspect-ratio:auto; display:grid; grid-template-columns:96px 1fr; gap:14px; padding:14px; background:var(--slate); color:#fff; align-items:center}
.item--podcast .item__media img{width:96px; height:96px; border-radius:10px}
.item--podcast .item__media .pshow{font-family:var(--mono); font-size:.68rem; letter-spacing:.06em; text-transform:uppercase; color:var(--aqua); line-height:1.4}
.item--podcast .item__media .pdate{display:block; color:var(--mint); margin-top:6px}
.item--guide .item__media{aspect-ratio:16/10; background:var(--aqua); display:flex; align-items:flex-end; justify-content:center; padding-top:16px}
.item--guide .item__media img{width:auto; height:100%; max-width:62%; object-fit:cover; object-position:top; border-radius:6px 6px 0 0; box-shadow:0 -10px 30px -10px rgba(0,0,0,.35)}
.lempty{padding:60px 20px; text-align:center; border:2px dashed var(--line); border-radius:var(--r-xl)}
.lempty h3{margin-bottom:.3em}
/* drawer */
.ldrawer{position:fixed; inset:0; z-index:96; display:none}
.ldrawer.open{display:block}
.ldrawer__panel{position:absolute; right:0; top:0; bottom:0; width:min(620px,100%); background:#fff; overflow:auto; padding:calc(18px + env(safe-area-inset-top,0px)) clamp(18px,3vw,32px) calc(30px + env(safe-area-inset-bottom,0px)); box-shadow:-30px 0 60px rgba(0,0,0,.3)}
.ldrawer__panel h2{font-size:clamp(1.6rem,3vw,2.3rem); margin-top:16px}
.ldrawer .vid{margin:14px 0}
.ldrawer .audio{margin:14px 0}
.ldrawer__links{display:grid; gap:0; margin-top:18px}
/* More from SafeBAE: the two new programs, each in its own look */
.lmore{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:20px 22px; align-items:stretch; margin-top:60px; padding-top:44px; border-top:1px solid var(--line)}
.lmore h2{grid-column:1/-1; font-size:clamp(1.6rem,2.8vw,2.4rem); margin:0 0 -2px}
.lmore__card{display:grid; grid-template-columns:150px minmax(0,1fr) auto; gap:22px; align-items:center; padding:16px 18px 16px 16px; text-decoration:none; transition:transform .25s var(--ease), box-shadow .25s var(--ease); min-width:0}
.lmore__card:hover{transform:translateY(-3px)}
.lmore__txt{min-width:0}
.lmore__txt b{display:block; font-size:1.18rem; line-height:1.15; margin-bottom:4px}
.lmore__txt small{display:block; font-size:.9rem; line-height:1.45}
.lmore__card .go{width:38px; height:38px; border-radius:50%; display:grid; place-items:center; font-weight:800; transition:transform .2s var(--ease)}
.lmore__card:hover .go{transform:translateX(3px)}
.lmore--ai{background-color:var(--aqua); background-image:radial-gradient(rgba(19,132,143,.22) 1.1px, transparent 1.5px); background-size:16px 16px; color:var(--slate); border:2px solid var(--slate); border-radius:16px; box-shadow:6px 6px 0 var(--mint)}
.lmore--ai:hover{box-shadow:8px 9px 0 var(--mint)}
.lmore--ai b{font-family:"Balsamiq Sans","Comic Neue",var(--body); font-weight:700; font-size:1.3rem}
.lmore--ai small{color:var(--ink-soft)}
.lmore--ai .go{background:var(--slate); color:var(--mint)}
.lmore__fig img{width:100%; aspect-ratio:1200/834; object-fit:cover; border-radius:10px; border:2px solid var(--slate); transform:rotate(-2deg)}
.lmore--ch{background-color:var(--slate); background-image:var(--grain); color:#fff; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.lmore--ch b{font-family:var(--display); font-weight:900; font-stretch:112%}
.lmore--ch small{color:rgba(255,255,255,.82)}
.lmore--ch .go{background:var(--mint); color:var(--slate)}
.lb-label{display:block; container-type:inline-size; background:#FFD600; color:#0d0d0d; border-radius:8px; padding:3.5%; transform:rotate(-3deg); box-shadow:0 14px 26px -16px rgba(0,0,0,.8)}
.lb-label > span{display:flex; flex-direction:column; align-items:center; text-align:center; border:2px solid #0d0d0d; border-radius:5px; padding:7cqi 5cqi 6cqi; font-family:var(--display); font-weight:900; text-transform:uppercase; line-height:1; white-space:nowrap}
.lb-label__w{display:flex; align-items:center; gap:3cqi; font-size:15cqi; font-stretch:104%}
.lb-label__w svg{width:.95em; height:.84em; flex:none}
.lb-label__a{font-size:7.3cqi; margin-top:5cqi; font-stretch:100%}
.lb-label__c{font-size:6.4cqi; margin-top:5cqi; text-transform:none; font-weight:800}
@media (max-width:860px){ .lmore{grid-template-columns:minmax(0,1fr)} .lmore__card{grid-template-columns:96px minmax(0,1fr) auto; gap:14px} }
.libfoot{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:16px}
@media (max-width:860px){.libfoot{grid-template-columns:1fr} .lsel{margin-left:0} .lbar{top:calc(76px + env(safe-area-inset-top,0px))} .fmt{overflow-x:auto; max-width:100%}}
'''

def lib_json():
    out = []
    feat_order = {it['id']: it.get('feat', 99) for it in LIB}
    for it in library_items():
        g = it.get('guide')
        th = it.get('thumb')
        imgsrc(th)
        if g and g.get('cover'): imgsrc(g['cover'])
        out.append({k: v for k, v in dict(
            id=it['id'], k=it['kind'], t=it['title'], s=it.get('sub', ''), d=it.get('desc', ''), y=it.get('year'), date=it.get('date'),
            top=it.get('topics', []), aud=it.get('aud', []), kw=it.get('kw', ''), th=f'assets/img/{th}.webp', h=it.get('href'),
            yt=it.get('yt'), sp=it.get('spotify'), url=it.get('url'), g=({'pdf': g['pdf'], 'pages': g.get('pages'), 'cover': f'assets/img/{g["cover"]}.webp', 'label': g.get('label')} if g else None),
            links=it.get('links', []), note=it.get('note'), f=it.get('feat')).items() if v not in (None, [], '')})
    return out

def library():
    data = lib_json()
    with open(f'{SITE}/assets/js/library-data.js', 'w') as fh:
        fh.write('window.SB_LIB=' + json.dumps(data, ensure_ascii=False) + ';window.SB_TOPICS=' + json.dumps(TOPICS) + ';')
    n_vid = sum(1 for d in data if d['k'] in ('film', 'video', 'series'))
    n_pod = sum(1 for d in data if d['k'] == 'podcast')
    n_gui = sum(1 for d in data if d.get('g') and d.get('k') != 'guide')
    bg = ''.join(img(n, '') for n in ['red-flags', 'gameon1', 'knowb4unude', '2l3a1960', 'yt-rixb8vlmajy', 'qts-full-cast-copy-2', 'yt-fsmycfjpws4', 'safebae-14'])
    body = f'''
<section class="libhero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="libhero__bg" aria-hidden="true">{bg}</div>
  <div class="wrap rise">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="resources.html">Resources</a><span>/</span><span>Library</span></nav>
    <h1>The <span class="mk">Library</span></h1>
    <p class="lede" style="color:rgba(255,255,255,.9)">Since 2015, SafeBAE has built a collection of youth-led media to spark honest conversations about consent, relationships and prevention. Every film is envisioned, written, directed and performed by young people, and most come with a ready-to-teach guide. Search everything in one place.</p>
    <form class="lsearch" role="search" id="lform"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg><label class="sr-only" for="lq">Search the library</label><input id="lq" type="search" placeholder="Search by topic, title, speaker or keyword" autocomplete="off"><button class="btn" type="submit">Search</button></form>
    <div class="lcounts"><span><b>{n_vid}</b> films &amp; videos</span><span><b>{n_pod}</b> podcasts</span><span><b>{n_gui}</b> teaching guides</span><span><b>{len(TOPICS)}</b> topics</span></div>
  </div>
</section>
<div class="lbar">
  <div class="wrap">
    <div class="fmt" role="group" aria-label="Format">
      <button aria-pressed="true" data-fmt="all">All<span>{len(data)}</span></button><button aria-pressed="false" data-fmt="films">Films &amp; videos<span>{n_vid}</span></button><button aria-pressed="false" data-fmt="podcasts">Podcasts<span>{n_pod}</span></button><button aria-pressed="false" data-fmt="guides">Teaching guides<span>{n_gui}</span></button>
    </div>
    <div class="lsel">
      <label class="sr-only" for="laud">Audience</label><select id="laud"><option value="">For anyone</option><option>Students</option><option>Educators</option><option>Parents</option></select>
      <label class="sr-only" for="lsort">Sort</label><select id="lsort"><option value="feat">Featured first</option><option value="new">Newest first</option><option value="az">A to Z</option></select>
    </div>
    <div class="topics" role="group" aria-label="Topics" id="ltopics"></div>
  </div>
</div>
<section class="band band--paper" style="padding-top:8px">
  <div class="wrap">
    <div class="lstatus"><p id="lcount" aria-live="polite"></p><button id="lclear" hidden>Clear all filters</button></div>
    <div id="lout"></div>
    <section class="lmore" aria-labelledby="lmore-h">
      <h2 id="lmore-h">More from SafeBAE</h2>
      <a class="lmore__card lmore--ai" href="ai-literacy.html"><span class="lmore__fig">{img('ai-illo-hello', '')}</span><span class="lmore__txt"><b>SafeBAE AI Literacy Training</b><small>Six free, self-paced modules for anyone 13 or older. Launches during U.S. Media Literacy Week, October 26–30, 2026.</small></span><span class="go" aria-hidden="true">&rarr;</span></a>
      <a class="lmore__card lmore--ch" href="choking-hazard.html"><span class="lb-label" aria-hidden="true"><span><span class="lb-label__w"><svg viewBox="0 0 48 42" aria-hidden="true"><path d="M24 4 45 39H3Z" fill="none" stroke="currentColor" stroke-width="5" stroke-linejoin="round"/><rect x="21.6" y="14.5" width="4.8" height="13.5" rx="1.2" fill="currentColor"/><circle cx="24" cy="33" r="2.8" fill="currentColor"/></svg>Warning</span><span class="lb-label__a">Choking is a hazard</span><span class="lb-label__c">chokinghazard.org</span></span></span><span class="lmore__txt"><b>Choking Hazard</b><small>SafeBAE’s campaign on sexual strangulation. There’s no safe way to choke someone.</small></span><span class="go" aria-hidden="true">&rarr;</span></a>
    </section>
  </div>
</section>
<section class="band band--aqua band--tight">
  <div class="wrap libfoot">
    <a class="card" href="posters.html"><div class="card__body"><h3>Prevention posters</h3><p>Free downloadable posters on consent, boundaries and online harassment.</p></div></a>
    <a class="card" href="consent-curriculum.html"><div class="card__body"><h3>The Consent Curriculum</h3><p>15 lessons with slides, facilitator guides and assessments, aligned with NHES.</p></div></a>
    <a class="card" href="contact.html"><div class="card__body"><h3>Suggest a topic</h3><p>Looking for a topic we don’t cover yet? Tell us what would help in your classroom.</p></div></a>
  </div>
</section>
<div class="ldrawer" id="ldrawer" aria-hidden="true"><div class="drawer__scrim" data-lclose></div><div class="ldrawer__panel" role="dialog" aria-label="Library item"><div class="drawer__head"><p class="eyebrow" style="margin:0" id="ldk"></p><button class="close-x" data-lclose aria-label="Close">&times;</button></div><div id="ldbody"></div></div></div>
'''
    page('library.html', 'The Library · SafeBAE', 'Every SafeBAE film, podcast and teaching guide in one searchable library.', body, active='library',
         fonts='family=Balsamiq+Sans:wght@700', head_extra=f'<style>{LIB_CSS}</style>', scripts='<script src="assets/js/library-data.js"></script><script src="assets/js/library.js"></script>')

LIB_JS = r'''
(function(){
  var L = window.SB_LIB || [], T = window.SB_TOPICS || [], d = document;
  var st = { q:'', fmt:'all', topic:'', aud:'', sort:'feat' };
  var PLAY = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 4.5v15l13-7.5z"/></svg>';
  function esc(s){ return String(s||'').replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
  function norm(s){ return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[’']/g,'').replace(/[^a-z0-9#+ ]/g,' '); }
  var hay = {}; L.forEach(function(it){ hay[it.id] = { t: norm(it.t), all: norm([it.t, it.s, it.d, (it.top||[]).join(' '), it.kw, (it.aud||[]).join(' ')].join(' ')) }; });
  function score(it, terms){ var h = hay[it.id], s = 0; for(var i=0;i<terms.length;i++){ var q = terms[i]; if(h.t.indexOf(q)>=0) s += 6; else if(h.all.indexOf(q)>=0) s += 2; else return 0; } return s; }
  function fmtOK(it){ if(st.fmt==='all') return true; if(st.fmt==='films') return it.k==='film'||it.k==='video'||it.k==='series'; if(st.fmt==='podcasts') return it.k==='podcast'; if(st.fmt==='guides') return !!it.g; return true; }
  function dateOf(it){ return it.date || (it.y ? it.y + '-06-01' : '0000'); }
  function kindLabel(it){ return {film:'Film', video:'Video', podcast:'Podcast', series:'Series', guide:'Guide'}[it.k]; }
  function fmtDate(s){ if(!s) return ''; var p = s.split('-'); var m = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][+p[1]-1]; return m + ' ' + (+p[2]) + ', ' + p[0]; }
  function card(it, mode){
    var guideMode = mode==='guides' && it.g;
    var tag = it.h && !/^https?:/.test(it.h) && (it.k==='film'||it.k==='series') ? 'a' : 'button';
    var attrs = tag==='a' ? ' href="' + it.h + '"' : ' type="button" data-open="' + it.id + '"';
    var media;
    if(it.k==='podcast'){
      media = '<span class="item__media"><img src="' + it.th + '" alt="" loading="lazy"><span class="pshow">' + esc(it.s) + (it.date ? '<span class="pdate">' + fmtDate(it.date) + '</span>' : '') + '</span></span>';
    } else if(guideMode){
      media = '<span class="item__media"><img src="' + it.g.cover + '" alt="" loading="lazy"><span class="item__kind"><span class="g">Teaching guide</span></span></span>';
    } else {
      var chips = '<span>' + kindLabel(it) + '</span>' + (it.g && it.k!=='guide' ? '<span class="g">' + (it.k==='series' ? '4 lessons' : 'Guide' + (it.g.pages ? ' · ' + it.g.pages + ' pp' : '')) + '</span>' : '') + (it.note ? '<span class="w">' + esc(it.note) + '</span>' : '');
      media = '<span class="item__media"><img src="' + it.th + '" alt="" loading="lazy"><span class="item__kind">' + chips + '</span>' + (it.yt ? '<span class="item__play">' + PLAY + '</span>' : '') + '</span>';
    }
    var tops = (it.top||[]).slice(0,3).map(function(t){ return '<span>' + esc(t) + '</span>'; }).join('');
    var cls = 'item' + (it.k==='podcast' ? ' item--podcast' : '') + (guideMode || it.k==='guide' ? ' item--guide' : '');
    return '<' + tag + ' class="' + cls + '"' + attrs + '>' + media + '<span class="item__body"><b>' + esc(it.t) + '</b>' + (it.k!=='podcast' ? '<small>' + esc(it.s) + '</small>' : '') + '<p>' + esc(it.d) + '</p><span class="item__topics">' + tops + '</span></span></' + tag + '>';
  }
  function sortList(a){
    if(st.sort==='az') return a.sort(function(x,y){ return x.t.replace(/[^a-z0-9]/ig,'').localeCompare(y.t.replace(/[^a-z0-9]/ig,'')); });
    if(st.sort==='new') return a.sort(function(x,y){ return dateOf(y).localeCompare(dateOf(x)); });
    return a.sort(function(x,y){ return (x.f||99)-(y.f||99) || ({film:0,series:0,video:1,guide:2,podcast:3}[x.k]-{film:0,series:0,video:1,guide:2,podcast:3}[y.k]) || dateOf(y).localeCompare(dateOf(x)); });
  }
  var out = d.getElementById('lout'), count = d.getElementById('lcount'), clear = d.getElementById('lclear');
  function render(){
    var terms = norm(st.q).split(/\s+/).filter(Boolean);
    var list = L.filter(function(it){ return fmtOK(it) && (!st.topic || (it.top||[]).indexOf(st.topic)>=0) && (!st.aud || (it.aud||[]).indexOf(st.aud)>=0); });
    var scored = terms.length ? list.map(function(it){ return [score(it, terms), it]; }).filter(function(x){ return x[0]>0; }) : list.map(function(it){ return [0, it]; });
    var res = terms.length && st.sort==='feat' ? scored.sort(function(a,b){ return b[0]-a[0]; }).map(function(x){ return x[1]; }) : sortList(scored.map(function(x){ return x[1]; }));
    var filtered = terms.length || st.topic || st.aud || st.fmt!=='all';
    clear.hidden = !filtered;
    count.textContent = res.length + (res.length===1 ? ' result' : ' results') + (st.q ? ' for “' + st.q + '”' : '') + (st.topic ? ' in ' + st.topic : '');
    if(!res.length){ out.innerHTML = '<div class="lempty"><h3>Nothing matches yet.</h3><p class="muted">Try a broader word like <b>consent</b>, or clear the filters. You can also <a class="link" href="contact.html">tell us what you were looking for</a>.</p></div>'; return; }
    if(!filtered && st.sort==='feat'){
      var shelves = [
        ['Films with teaching guides', 'Each film is paired with a ready-to-teach guide for short, meaningful discussions.', res.filter(function(i){ return i.k==='film'||i.k==='series'; }), 'lgrid--3 lgrid--lead'],
        ['Podcasts', 'Conversations SafeBAE’s founders, staff and student leaders were invited into. Want to feature SafeBAE on your show or in your reporting? Email <a class="link" href="mailto:info@safebae.org">info@safebae.org</a>.', res.filter(function(i){ return i.k==='podcast'; }), 'lgrid--3 lgrid--lead'],
        ['More videos', 'Explainers, campaigns and moments from the SafeBAE community.', res.filter(function(i){ return i.k==='video'; }), 'lgrid--3 lgrid--lead'],
        ['Guides for adults', '', res.filter(function(i){ return i.k==='guide'; }), 'lgrid--wide']
      ];
      out.innerHTML = shelves.filter(function(s){ return s[2].length; }).map(function(s){ return '<div class="lshelf"><div class="lshelf__head"><div><h2>' + s[0] + '</h2>' + (s[1] ? '<p class="muted" style="margin:.3em 0 0">' + s[1] + '</p>' : '') + '</div></div><div class="lgrid ' + s[3] + '">' + s[2].map(function(i){ return card(i, ''); }).join('') + '</div></div>'; }).join('');
    } else {
      out.innerHTML = '<div class="lgrid">' + res.map(function(i){ return card(i, st.fmt); }).join('') + '</div>';
    }
  }
  /* topics */
  var tw = d.getElementById('ltopics');
  tw.innerHTML = T.map(function(t){ return '<button type="button" aria-pressed="false" data-topic="' + esc(t) + '">' + esc(t) + '</button>'; }).join('');
  tw.addEventListener('click', function(e){ var b = e.target.closest('[data-topic]'); if(!b) return; st.topic = st.topic===b.dataset.topic ? '' : b.dataset.topic; syncTopics(); render(); });
  function syncTopics(){ tw.querySelectorAll('button').forEach(function(b){ b.setAttribute('aria-pressed', String(b.dataset.topic===st.topic)); }); }
  d.querySelectorAll('[data-fmt]').forEach(function(b){ b.addEventListener('click', function(){ st.fmt = b.dataset.fmt; syncFmt(); render(); }); });
  function syncFmt(){ d.querySelectorAll('[data-fmt]').forEach(function(x){ x.setAttribute('aria-pressed', String(x.dataset.fmt===st.fmt)); }); }
  d.getElementById('laud').addEventListener('change', function(){ st.aud = this.value; render(); });
  d.getElementById('lsort').addEventListener('change', function(){ st.sort = this.value; render(); });
  var q = d.getElementById('lq'), t;
  q.addEventListener('input', function(){ clearTimeout(t); t = setTimeout(function(){ st.q = q.value.trim(); render(); }, 120); });
  d.getElementById('lform').addEventListener('submit', function(e){ e.preventDefault(); st.q = q.value.trim(); render(); out.scrollIntoView({behavior:'smooth', block:'start'}); });
  clear.addEventListener('click', function(){ st = { q:'', fmt:'all', topic:'', aud:'', sort:st.sort }; q.value=''; d.getElementById('laud').value=''; syncFmt(); syncTopics(); render(); });
  /* drawer */
  var dr = d.getElementById('ldrawer'), db = d.getElementById('ldbody'), last;
  function openItem(id){
    var it = L.filter(function(x){ return x.id===id; })[0]; if(!it) return; last = d.activeElement;
    d.getElementById('ldk').textContent = kindLabel(it) + (it.date ? ' · ' + fmtDate(it.date) : '');
    var media = '';
    if(it.yt) media = '<a class="vid" href="https://www.youtube.com/watch?v=' + it.yt + '" target="_blank" rel="noopener" data-yt="' + it.yt + '"><img src="' + it.th + '" alt=""><span class="vid__play"><span>' + PLAY + '</span></span><span class="vid__label"><span>' + esc(it.t) + '</span><small>Watch</small></span></a>';
    else if(it.sp) media = '<a class="audio" href="https://open.spotify.com/episode/' + it.sp + '" target="_blank" rel="noopener" data-spotify="episode/' + it.sp + '"><img src="' + it.th + '" alt=""><span><b>' + esc(it.t) + '</b><small>' + esc(it.s) + '</small></span><span class="playdot">' + PLAY + '</span></a>';
    else if(it.url) media = '<a class="audio" href="' + it.url + '" target="_blank" rel="noopener"><img src="' + it.th + '" alt=""><span><b>' + esc(it.t) + '</b><small>' + esc(it.s) + '</small></span><span class="playdot">' + PLAY + '</span></a>';
    var links = (it.links||[]).map(function(l){ var ext = /^https?:/.test(l[1]); return '<a class="row" href="' + l[1] + '"' + (ext ? ' target="_blank" rel="noopener"' : '') + '><span><b>' + esc(l[0]) + '</b></span><span class="go">' + (ext ? '↗' : '→') + '</span></a>'; });
    if(it.h){ var ext = /^https?:/.test(it.h); links.unshift('<a class="row" href="' + it.h + '"' + (ext ? ' target="_blank" rel="noopener"' : '') + '><span><b>' + (it.k==='guide' ? 'Open the guide (PDF)' : 'Go to the related page') + '</b><small>' + (it.g ? 'Teaching guide, discussion questions and activities' : '') + '</small></span><span class="go">' + (ext ? '↗' : '→') + '</span></a>'); }
    db.innerHTML = '<h2>' + esc(it.t) + '</h2><p class="muted" style="font-weight:600">' + esc(it.s) + '</p>' + media + (it.note ? '<p class="note note--coral small"><b>Content note:</b> this video uses real messages survivors received and includes explicit language. A non-explicit version is in the library.</p>' : '') + '<p>' + esc(it.d) + '</p><div class="chips">' + (it.top||[]).map(function(t){ return '<button class="chip" style="border:0;cursor:pointer" data-jump="' + esc(t) + '">' + esc(t) + '</button>'; }).join('') + '</div><div class="ldrawer__links rows">' + links.join('') + '</div>';
    dr.classList.add('open'); dr.setAttribute('aria-hidden','false'); d.body.style.overflow='hidden';

    db.querySelectorAll('[data-jump]').forEach(function(b){ b.addEventListener('click', function(){ st.topic = b.dataset.jump; syncTopics(); render(); closeItem(); out.scrollIntoView({behavior:'smooth'}); }); });
    setTimeout(function(){ dr.querySelector('.close-x').focus(); }, 30);
  }
  function closeItem(){ dr.classList.remove('open'); dr.setAttribute('aria-hidden','true'); d.body.style.overflow=''; if(last && last.focus) last.focus(); }
  out.addEventListener('click', function(e){ var b = e.target.closest('[data-open]'); if(b) openItem(b.dataset.open); });
  dr.querySelectorAll('[data-lclose]').forEach(function(b){ b.addEventListener('click', closeItem); });
  d.addEventListener('keydown', function(e){ if(e.key==='Escape' && dr.classList.contains('open')){ e.stopPropagation(); closeItem(); } }, true);
  /* initial state from hash or session */
  function fromHash(){
    var h = location.hash.slice(1).toLowerCase();
    if(h==='films'||h==='podcasts'||h==='guides'){ st.fmt = h; }
    else if(h.indexOf('q-')===0){ st.q = decodeURIComponent(h.slice(2)); }
    else if(h){ var tp = T.filter(function(x){ return norm(x).replace(/ /g,'-').replace(/-+/g,'-').indexOf(h)===0 || norm(x).indexOf(h)>=0; })[0]; if(tp) st.topic = tp; }
  }
  var sq = null; try{ sq = sessionStorage.getItem('libq'); sessionStorage.removeItem('libq'); }catch(e){}
  fromHash();
  if(sq){ st.q = sq; }
  q.value = st.q; syncFmt(); syncTopics(); render();
  window.addEventListener('hashchange', function(){ fromHash(); q.value = st.q; syncFmt(); syncTopics(); render(); var bar = document.querySelector('.lib-bar, .filters, [data-libbar]'); (bar || q).scrollIntoView({behavior:'smooth', block:'start'}); });
})();
'''

def build():
    with open(f'{SITE}/assets/js/library.js', 'w') as fh:
        fh.write(LIB_JS)
    library()
