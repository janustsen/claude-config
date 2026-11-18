() => {
  // Measure a live page's design decisions. Paste into DevTools, or run:
  //   chrome-devtools-axi eval "$(cat measure.js)"
  // Returns JSON: display type, type histograms, nav, filled buttons,
  // dominant transitions, easings, reduced-motion / view-transition support, libraries.
  const px = v => Math.round(parseFloat(v) * 10) / 10;
  const em = (ls, fs) => (ls === 'normal' ? 0 : Math.round((parseFloat(ls) / parseFloat(fs)) * 1000) / 1000);
  const visible = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const type = el => { const s = getComputedStyle(el); return {
    text: (el.textContent || '').trim().slice(0, 80), family: s.fontFamily.split(',')[0].replace(/["']/g, ''),
    size: px(s.fontSize), weight: s.fontWeight, lineHeight: s.lineHeight === 'normal' ? 'normal' : Math.round(parseFloat(s.lineHeight) / parseFloat(s.fontSize) * 100) / 100,
    trackingEm: em(s.letterSpacing, s.fontSize), color: s.color, align: s.textAlign }; };

  // Leaf text nodes: size and family histograms, largest text as fallback display.
  const sizes = {}, fams = {}; let largest = null;
  for (const el of document.body.querySelectorAll('*')) {
    if (!visible(el) || ![...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) continue;
    const s = getComputedStyle(el), size = px(s.fontSize), fam = s.fontFamily.split(',')[0].replace(/["']/g, '');
    sizes[size] = (sizes[size] || 0) + 1; fams[fam] = (fams[fam] || 0) + 1;
    if (!largest || size > px(getComputedStyle(largest).fontSize)) largest = el;
  }
  const h1 = [...document.querySelectorAll('h1')].find(visible) || largest;

  const nav = document.querySelector('header, nav, [role="banner"]');
  const navInfo = nav && (() => { const s = getComputedStyle(nav), r = nav.getBoundingClientRect(); return {
    position: s.position, height: Math.round(r.height), background: s.backgroundColor, backdrop: s.backdropFilter || s.webkitBackdropFilter,
    borderBottom: s.borderBottomWidth + ' ' + s.borderBottomColor, links: nav.querySelectorAll('a').length }; })();

  const btns = [...document.querySelectorAll('a, button')].filter(el => {
    if (!visible(el)) return false; const bg = getComputedStyle(el).backgroundColor;
    return bg && bg !== 'transparent' && !/rgba\(.*, 0\)$/.test(bg);
  }).slice(0, 4).map(el => { const s = getComputedStyle(el), r = el.getBoundingClientRect(); return {
    text: el.textContent.trim().slice(0, 40), bg: s.backgroundColor, color: s.color, radius: s.borderRadius,
    height: Math.round(r.height), size: px(s.fontSize), weight: s.fontWeight }; });

  const trans = {};
  [...document.querySelectorAll('*')].slice(0, 4000).forEach(el => {
    const s = getComputedStyle(el); if (s.transitionDuration === '0s') return;
    const k = s.transitionDuration.split(',')[0] + ' ' + s.transitionTimingFunction.split(/,(?![^(]*\))/)[0];
    trans[k] = (trans[k] || 0) + 1;
  });

  const easings = new Set(); let reducedMotion = false, viewTransition = false, unreadable = 0;
  for (const sheet of document.styleSheets) {
    let rules; try { rules = sheet.cssRules; } catch (e) { unreadable++; continue; }
    const walk = list => { for (const r of list) {
      const t = r.cssText || '';
      (t.match(/cubic-bezier\([^)]*\)/g) || []).forEach(e => easings.add(e.replace(/\s/g, '')));
      if (/prefers-reduced-motion/.test(t)) reducedMotion = true;
      if (/view-transition/.test(t)) viewTransition = true;
      if (r.cssRules) walk(r.cssRules);
    } };
    walk(rules);
  }

  const libs = {
    gsap: !!window.gsap, lenis: !!document.querySelector('.lenis, [data-lenis]') || !!window.lenis,
    canvases: document.querySelectorAll('canvas').length, videos: document.querySelectorAll('video').length,
    next: !!window.next || !!document.getElementById('__next'), astro: !!document.querySelector('astro-island'),
  };

  const top = o => Object.entries(o).sort((a, b) => b[1] - a[1]);
  return {
    url: location.href, viewport: innerWidth + 'x' + innerHeight, docHeight: document.documentElement.scrollHeight,
    page: (({ text, ...rest }) => ({ background: getComputedStyle(document.body).backgroundColor, ...rest }))(type(document.body)),
    display: h1 && type(h1), sizes: top(sizes).slice(0, 14), families: top(fams).slice(0, 6),
    nav: navInfo, buttons: btns, topTransitions: top(trans).slice(0, 6), easings: [...easings].slice(0, 20),
    reducedMotion, viewTransition, unreadableSheets: unreadable, libs,
  };
}
