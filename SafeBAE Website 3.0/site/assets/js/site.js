/* SafeBAE site behaviors */
(function(){
  'use strict';
  var d = document, root = d.documentElement;
  root.classList.add('js');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $(s, c){ return (c||d).querySelector(s); }
  function $$(s, c){ return Array.prototype.slice.call((c||d).querySelectorAll(s)); }
  function store(k, v){ try{ if(v===undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); }catch(e){ return null; } }

  /* Can this page embed third-party players? Only on a real website that is not framed. */
  var framed = false; try { framed = window.self !== window.top; } catch(e){ framed = true; }
  var canEmbed = /^https?:$/.test(location.protocol) && !framed;
  window.SB = { canEmbed: canEmbed };

  /* ---------- in-artifact page switching ----------
     Inside the claude.ai artifact viewer the frame can't navigate to sibling pages,
     so internal links fetch the page and swap the whole document in place. */
  var inArtifact = framed && /claudeusercontent\.com$/.test(location.hostname);
  function softGo(href){
    var u; try { u = new URL(href, location.href); } catch(e){ return; }
    if(u.origin !== location.origin || !/\.html$/.test(u.pathname)){ location.href = href; return; }
    fetch(u.pathname, {credentials: 'include'}).then(function(r){ if(!r.ok) throw new Error(r.status); return r.text(); }).then(function(html){
      var frag = u.hash ? decodeURIComponent(u.hash.slice(1)) : '';
      try { history.replaceState(null, '', location.pathname + location.search + (frag ? '#' + frag : '')); } catch(e){}
      d.open(); d.write(html); d.close();
      window.scrollTo(0, 0);
      if(frag) setTimeout(function(){ var el = document.getElementById(frag); if(el) el.scrollIntoView(); }, 350);
    }).catch(function(){ location.href = href; });
  }
  window.SB.go = inArtifact ? softGo : function(href){ location.href = href; };
  if(inArtifact){
    d.addEventListener('click', function(e){
      if(e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      var a = e.target.closest && e.target.closest('a[href]'); if(!a || a.target === '_blank') return;
      var h = a.getAttribute('href') || '';
      if(!h || h.charAt(0) === '#' || /^[a-z][a-z0-9+.-]*:/i.test(h) || !/\.html(#|$)/.test(h)) return;
      e.preventDefault(); softGo(h);
    });
  }

  /* ---------- overlays ---------- */
  var lastFocus = null;
  function openOverlay(el){ if(!el) return; lastFocus = d.activeElement; el.classList.add('open'); el.setAttribute('aria-hidden','false'); d.body.style.overflow='hidden'; var f = el.querySelector('input,button,a'); if(f) setTimeout(function(){ f.focus(); }, 30); }
  function closeOverlay(el){ if(!el) return; el.classList.remove('open'); el.setAttribute('aria-hidden','true'); if(!$('.drawer.open,.help.open,.palette.open,.lightbox.open')) d.body.style.overflow=''; if(lastFocus && lastFocus.focus) lastFocus.focus(); }
  $$('[data-close]').forEach(function(b){ b.addEventListener('click', function(){ closeOverlay(b.closest('.drawer,.help,.palette,.lightbox')); }); });
  $$('[data-open-menu]').forEach(function(b){ b.addEventListener('click', function(){ openOverlay($('#menu')); }); });
  $$('[data-open-help]').forEach(function(b){ b.addEventListener('click', function(e){ e.preventDefault(); closeOverlay($('#menu')); openOverlay($('#help')); }); });
  $$('[data-open-search]').forEach(function(b){ b.addEventListener('click', function(){ openSearch(); }); });
  $('#palette') && $('#palette').addEventListener('click', function(e){ if(e.target.id==='palette') closeOverlay(this); });

  /* ---------- announcement ribbon ---------- */
  (function(){ var r = $('#sb-ribbon'); if(!r) return; if(store('sb-ribbon') === 'x') r.classList.add('gone'); var x = $('[data-ribbon-x]', r); if(x) x.addEventListener('click', function(){ r.classList.add('gone'); store('sb-ribbon', 'x'); }); var its = $$('.ribbon__items a', r), k = 0; if(its.length){ its[0].classList.add('on'); if(its.length > 1 && !reduce){ var iv = setInterval(function(){ if(!r.isConnected){ clearInterval(iv); return; } if(r.matches(':hover') || r.contains(d.activeElement)) return; its[k].classList.remove('on'); k = (k+1) % its.length; its[k].classList.add('on'); }, 5200); } else if(reduce){ its.forEach(function(a){ a.classList.add('on'); a.style.position='static'; }); } } })();

  /* ---------- quick exit ---------- */
  function quickExit(){ try{ sessionStorage.clear(); }catch(e){} try{ (window.top || window).location.replace('https://www.google.com/search?q=weather'); }catch(e){ location.replace('https://www.google.com/search?q=weather'); } }
  $$('[data-quick-exit]').forEach(function(b){ b.addEventListener('click', quickExit); });
  var lastEsc = 0;
  d.addEventListener('keydown', function(e){
    if(e.key === 'Escape'){
      var open = $('.drawer.open,.help.open,.palette.open,.lightbox.open');
      if(open){ closeOverlay(open); lastEsc = 0; return; }
      var ae = d.activeElement; if(ae && /^(input|textarea)$/i.test(ae.tagName) && ae.value){ lastEsc = 0; return; }
      var now = Date.now(); if(now - lastEsc < 600){ quickExit(); } lastEsc = now;
    }
    if((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k'){ e.preventDefault(); openSearch(); }
    if(e.key === '/' && !/input|textarea|select/i.test((d.activeElement||{}).tagName||'') && !$('.palette.open')){ e.preventDefault(); openSearch(); }
  });

  /* ---------- main nav ---------- */
  var navItems = $$('.nav__item');
  function closeAll(except){ navItems.forEach(function(n){ if(n!==except){ n.classList.remove('open'); var b=n.querySelector('.nav__top'); b && b.setAttribute('aria-expanded','false'); } }); }
  navItems.forEach(function(item){
    var btn = item.querySelector('.nav__top'), t;
    btn.addEventListener('click', function(){ var o = !item.classList.contains('open'); closeAll(item); item.classList.toggle('open', o); btn.setAttribute('aria-expanded', String(o)); });
    item.addEventListener('mouseenter', function(){ if(window.matchMedia('(hover:hover)').matches){ clearTimeout(t); closeAll(item); item.classList.add('open'); btn.setAttribute('aria-expanded','true'); } });
    item.addEventListener('mouseleave', function(){ if(window.matchMedia('(hover:hover)').matches){ t = setTimeout(function(){ item.classList.remove('open'); btn.setAttribute('aria-expanded','false'); }, 160); } });
    item.addEventListener('focusout', function(e){ if(!item.contains(e.relatedTarget)){ item.classList.remove('open'); btn.setAttribute('aria-expanded','false'); } });
  });
  d.addEventListener('click', function(e){ if(!e.target.closest('.nav__item')) closeAll(); });

  /* ---------- video / audio / iframe facades ---------- */
  d.addEventListener('click', function(e){
    var el = e.target.closest('[data-yt]');
    if(el && canEmbed){
      e.preventDefault();
      var id = el.getAttribute('data-yt'), st = el.getAttribute('data-start');
      var f = d.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0' + (st ? '&start=' + st : '');
      f.title = el.getAttribute('aria-label') || 'Video'; f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share'; f.allowFullscreen = true;
      el.innerHTML = ''; el.appendChild(f); el.removeAttribute('href'); el.removeAttribute('data-yt');
      return;
    }
    var sp = e.target.closest('[data-spotify]');
    if(sp && canEmbed){
      e.preventDefault();
      var g = d.createElement('iframe');
      g.src = 'https://open.spotify.com/embed/' + sp.getAttribute('data-spotify') + '?utm_source=safebae';
      g.style.cssText = 'width:100%;height:152px;border:0;border-radius:12px'; g.allow = 'autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture'; g.title = sp.getAttribute('aria-label') || 'Podcast';
      sp.replaceWith(g);
    }
  });
  $$('[data-embed]').forEach(function(el){
    if(!canEmbed) return;
    var f = d.createElement('iframe');
    f.src = el.getAttribute('data-embed'); f.title = el.getAttribute('data-title') || 'Form'; f.loading = 'lazy';
    f.style.cssText = 'width:100%;border:0;border-radius:12px;background:#fff;min-height:' + (el.getAttribute('data-h') || 720) + 'px';
    el.innerHTML = ''; el.appendChild(f);
  });

  /* ---------- tabs ---------- */
  var tabSelectors = [];
  function tabFromHash(h, scroll){ if(!h) return false; var hit = false; tabSelectors.forEach(function(ts){ var t = ts.tabs.filter(function(x){ return x.id === h || x.id === 'tab-'+h; })[0]; if(t){ ts.sel(t); hit = true; if(scroll){ var r = ts.wrap.getBoundingClientRect(); window.scrollTo({top: window.pageYOffset + r.top - 120, behavior: 'smooth'}); } } }); return hit; }
  window.addEventListener('hashchange', function(){ tabFromHash(decodeURIComponent(location.hash.slice(1)), true); });
  d.addEventListener('click', function(e){ var l = e.target.closest('a[href^="#"]'); if(!l || l.closest('[role="tablist"]')) return; var h = decodeURIComponent(l.getAttribute('href').slice(1)); if(h && h === decodeURIComponent(location.hash.slice(1)) && tabFromHash(h, true)) e.preventDefault(); });
  $$('[data-tabs]').forEach(function(wrap){
    var tabs = $$('[role="tab"]', wrap);
    function sel(t, focus){ tabs.forEach(function(x){ var on = x===t; x.setAttribute('aria-selected', String(on)); x.tabIndex = on?0:-1; var p = d.getElementById(x.getAttribute('aria-controls')); if(p) p.hidden = !on; }); if(focus) t.focus(); var k = wrap.getAttribute('data-tabs'); if(k) store('tab:'+k, t.id); }
    tabs.forEach(function(t, i){
      t.addEventListener('click', function(){ sel(t); });
      t.addEventListener('keydown', function(e){ var n = e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0; if(n){ e.preventDefault(); sel(tabs[(i+n+tabs.length)%tabs.length], true); } });
    });
    var k = wrap.getAttribute('data-tabs'), saved = k && store('tab:'+k), h = location.hash.slice(1);
    var pick = tabs.filter(function(t){ return t.id === h || t.id === 'tab-'+h; })[0] || tabs.filter(function(t){ return t.id === saved; })[0];
    if(pick) sel(pick);
    tabSelectors.push({wrap: wrap, tabs: tabs, sel: sel});
  });

  /* ---------- flip cards ---------- */
  $$('[data-flip]').forEach(function(b){ b.addEventListener('click', function(){ b.setAttribute('aria-pressed', b.getAttribute('aria-pressed')==='true'?'false':'true'); }); });

  /* ---------- slide players ---------- */
  $$('[data-player]').forEach(function(p){
    var slides = $$('.player__slide', p), cap = $('.player__cap', p), bar = $('.player__bar i', p), i = 0, iv = +(p.getAttribute('data-interval')||5000), t0 = 0, raf, paused = false;
    if(!slides.length) return;
    function show(n){ slides[i].classList.remove('on'); i = (n+slides.length)%slides.length; slides[i].classList.add('on'); if(cap) cap.textContent = (i+1) + ' / ' + slides.length + ' · ' + (slides[i].getAttribute('data-cap')||''); t0 = performance.now(); }
    var stopped = false; function stop(){ stopped = true; p.classList.add('is-stopped'); }
    function tick(t){ if(!p.isConnected || stopped) return; if(!paused && !reduce){ var k = (t - t0)/iv; if(k>=1){ if(i === slides.length - 1){ show(0); stop(); return; } show(i+1); k=0; } if(bar) bar.style.width = (k*100)+'%'; } raf = requestAnimationFrame(tick); }
    $('[data-prev]', p) && $('[data-prev]', p).addEventListener('click', function(){ stop(); show(i-1); });
    $('[data-next]', p) && $('[data-next]', p).addEventListener('click', function(){ stop(); show(i+1); });
    p.addEventListener('mouseenter', function(){ paused = true; }); p.addEventListener('mouseleave', function(){ paused = false; t0 = performance.now(); });
    p.addEventListener('focusin', function(){ paused = true; });
    show(0); raf = requestAnimationFrame(tick);
    p.addEventListener('click', function(e){ if(e.target.closest('button')) return; var im = slides[i].querySelector('img'); if(im && p.hasAttribute('data-zoom')) openLightbox(slides.map(function(s){ var m=s.querySelector('img'); return {src:m.src, cap:s.getAttribute('data-cap')||''}; }), i); });
  });

  /* ---------- lightbox ---------- */
  var lb = $('#lightbox'), lbSet = [], lbI = 0;
  function lbShow(){ var it = lbSet[lbI]; if(!it) return; $('img', lb).src = it.src; $('img', lb).alt = it.cap || ''; $('.lightbox__cap', lb).textContent = it.cap ? it.cap + ' · ' + (lbI+1) + ' of ' + lbSet.length : (lbI+1) + ' of ' + lbSet.length; }
  function openLightbox(set, i){ lbSet = set; lbI = i||0; lbShow(); openOverlay(lb); }
  window.SB.openLightbox = openLightbox;
  if(lb){
    $('.lightbox__prev', lb).addEventListener('click', function(){ lbI = (lbI-1+lbSet.length)%lbSet.length; lbShow(); });
    $('.lightbox__next', lb).addEventListener('click', function(){ lbI = (lbI+1)%lbSet.length; lbShow(); });
    lb.addEventListener('click', function(e){ if(e.target === lb) closeOverlay(lb); });
    d.addEventListener('keydown', function(e){ if(!lb.classList.contains('open')) return; if(e.key==='ArrowLeft') $('.lightbox__prev', lb).click(); if(e.key==='ArrowRight') $('.lightbox__next', lb).click(); });
  }
  $$('[data-gallery]').forEach(function(g){
    var btns = $$('button[data-src]', g);
    btns.forEach(function(b, i){ b.addEventListener('click', function(){ openLightbox(btns.map(function(x){ return {src:x.getAttribute('data-src'), cap:x.getAttribute('data-cap')}; }), i); }); });
  });

  /* ---------- copy buttons ---------- */
  $$('[data-copy]').forEach(function(b){ b.addEventListener('click', function(){ var t = b.getAttribute('data-copy'); var done = function(){ var o = b.textContent; b.textContent = 'Copied'; setTimeout(function(){ b.textContent = o; }, 1400); }; if(navigator.clipboard){ navigator.clipboard.writeText(t).then(done, function(){ selectText(b.parentNode); }); } else selectText(b.parentNode); }); });
  function selectText(el){ var r = d.createRange(); r.selectNodeContents(el); var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); }

  /* ---------- static forms ---------- */
  $$('form[data-static]').forEach(function(f){ f.addEventListener('submit', function(e){ e.preventDefault(); if(!f.reportValidity()) return; var to = f.getAttribute('data-mailto'); if(to && canEmbed){ var data = new FormData(f), body = []; data.forEach(function(v,k){ body.push(k + ': ' + v); }); location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(f.getAttribute('data-subject')||'Website message') + '&body=' + encodeURIComponent(body.join('\n')); } f.classList.add('sent'); }); });

  /* ---------- reveal ---------- */
  if('IntersectionObserver' in window && !reduce){
    var io = new IntersectionObserver(function(es){ es.forEach(function(en){ if(en.isIntersecting){ en.target.classList.remove('pre'); io.unobserve(en.target); } }); }, {rootMargin:'0px 0px -8% 0px'});
    $$('.reveal').forEach(function(el){ var r = el.getBoundingClientRect(); if(r.top > window.innerHeight){ el.classList.add('pre'); io.observe(el); } });
  }

  /* ---------- search palette ---------- */
  var idx = null, sel = 0, results = [];
  function loadIndex(cb){ if(idx) return cb(); if(window.SB_SEARCH){ idx = window.SB_SEARCH; return cb(); } var s = d.createElement('script'); s.src = 'assets/js/search-index.js'; s.onload = function(){ idx = window.SB_SEARCH || []; cb(); }; s.onerror = function(){ idx = []; cb(); }; d.head.appendChild(s); }
  function norm(s){ return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9#+ ]/g,' '); }
  function score(it, terms){ var t = norm(it.t), b = norm(it.t + ' ' + (it.k||'') + ' ' + (it.d||'')), s = 0; for(var i=0;i<terms.length;i++){ var q = terms[i]; if(!q) continue; if(t.indexOf(q)===0) s+=12; else if(t.indexOf(' '+q)>=0) s+=8; else if(t.indexOf(q)>=0) s+=5; else if(b.indexOf(q)>=0) s+=2; else return 0; } return s + (it.w||0); }
  function render(q){
    var list = $('#palette-list'), terms = norm(q).split(/\s+/).filter(Boolean);
    results = terms.length ? idx.map(function(it){ return [score(it, terms), it]; }).filter(function(x){ return x[0]>0; }).sort(function(a,b){ return b[0]-a[0]; }).slice(0, 30).map(function(x){ return x[1]; }) : idx.filter(function(it){ return it.f; });
    sel = 0;
    if(!results.length){ list.innerHTML = '<p class="palette__empty">No matches for “' + q.replace(/</g,'&lt;') + '”. Try a topic like <b>consent</b>, <b>Title IX</b> or <b>bystander</b>.</p>'; return; }
    list.innerHTML = (terms.length ? '' : '<p class="palette__empty" style="padding:8px 12px">Popular</p>') + results.map(function(it, i){ var ext = /^https?:/.test(it.u); return '<a class="palette__item" role="option" aria-selected="' + (i===0) + '" href="' + it.u + '"' + (ext?' target="_blank" rel="noopener"':'') + '><span class="palette__kind">' + it.c + '</span><span><b>' + it.t + '</b><small>' + (it.d||'') + '</small></span><span aria-hidden="true">' + (ext?'↗':'→') + '</span></a>'; }).join('');
  }
  function move(n){ var items = $$('.palette__item'); if(!items.length) return; sel = (sel+n+items.length)%items.length; items.forEach(function(x,i){ x.setAttribute('aria-selected', String(i===sel)); }); items[sel].scrollIntoView({block:'nearest'}); }
  function openSearch(q){ var p = $('#palette'); if(!p) return; closeOverlay($('#menu')); openOverlay(p); var inp = $('#palette-q'); if(typeof q === 'string') inp.value = q; loadIndex(function(){ render(inp.value); }); }
  window.SB.openSearch = openSearch;
  var pin = $('#palette-q');
  if(pin){
    pin.addEventListener('input', function(){ loadIndex(function(){ render(pin.value); }); });
    pin.addEventListener('keydown', function(e){ if(e.key==='ArrowDown'){ e.preventDefault(); move(1); } else if(e.key==='ArrowUp'){ e.preventDefault(); move(-1); } else if(e.key==='Enter'){ var it = $$('.palette__item')[sel]; if(it){ e.preventDefault(); it.click(); } } });
  }
})();
