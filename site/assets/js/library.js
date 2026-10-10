
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
