// Render notes figures (flow, cycle, named diagrams) to PNG for the DOCX builder.
// Usage: node tools/notes/figures.mjs notes/chapters/CV-7.json [more]
// Output: notes/build/fig/<unit>-<n>.png and notes/build/fig/<unit>.json (sizes, in order of appearance)
import fs from 'fs';
import path from 'path';
import { createRequire } from 'module';
import { execSync } from 'child_process';
const require = createRequire(import.meta.url);
const { chromium } = require(execSync('npm root -g').toString().trim() + '/playwright');

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const OUT = path.join(ROOT, 'notes/build/fig');
fs.mkdirSync(OUT, { recursive: true });
const INK = '#0B1530', TERRA = '#8B3A2E', GRAY = '#4A5160', LINE = '#9AA0AC';
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const BASE = `<style>*{box-sizing:border-box;margin:0}body{font-family:'Plus Jakarta Sans',sans-serif;color:${INK};background:#fff}
#fig{display:inline-block;padding:14px;background:#fff}
.box{border:2px solid ${INK};border-radius:10px;background:#fff;padding:9px 12px;font-size:15px;line-height:1.3;text-align:center;font-weight:600}
.n{display:inline-flex;align-items:center;justify-content:center;flex:0 0 24px;width:24px;height:24px;border-radius:12px;background:${INK};color:#fff;font-size:12.5px;margin-right:10px;font-weight:800;text-align:center;vertical-align:middle}
.fl{display:flex;align-items:center;text-align:left}
.ha{width:26px;display:flex;align-items:center;justify-content:center;color:${GRAY};font-size:16px}
.arr{width:2px;height:22px;background:${GRAY};margin:0 auto;position:relative}
.arr:after{content:'';position:absolute;left:-6px;bottom:-2px;border-left:7px solid transparent;border-right:7px solid transparent;border-top:10px solid ${GRAY}}
</style>`;

function flowHTML(b) {
  const parts = b.steps.map((st, i) => `<div class="box fl" style="width:236px;min-height:74px;font-size:14.5px"><span class="n">${i + 1}</span><span>${esc(st)}</span></div>` + (i < b.steps.length - 1 ? `<div class="ha">&#9654;</div>` : ''));
  return `<div id="fig" style="width:820px"><div style="display:flex;flex-wrap:wrap;align-items:stretch;row-gap:12px">${parts.join('')}</div></div>`;
}
function cycleHTML(b) {
  const n = b.steps.length, W = 780, H = n <= 4 ? 500 : 640, cx = W / 2, cy = H / 2, R = n <= 4 ? 175 : 245, bw = 196, bh = 96;
  const pts = b.steps.map((_, i) => { const a = -Math.PI / 2 + i * 2 * Math.PI / n; return [cx + R * Math.cos(a), cy + R * Math.sin(a)]; });
  let svg = `<svg width="${W}" height="${H}" style="position:absolute;left:0;top:0"><defs><marker id="m" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="${GRAY}"/></marker></defs>`;
  for (let i = 0; i < n; i++) {
    const a0 = -Math.PI / 2 + i * 2 * Math.PI / n, a1 = -Math.PI / 2 + (i + 1) * 2 * Math.PI / n, gap = 0.5 * (2 * Math.PI / n) * 0.42;
    const s = [cx + R * Math.cos(a0 + gap), cy + R * Math.sin(a0 + gap)], e = [cx + R * Math.cos(a1 - gap), cy + R * Math.sin(a1 - gap)];
    svg += `<path d="M${s[0]},${s[1]} A${R},${R} 0 0,1 ${e[0]},${e[1]}" fill="none" stroke="${GRAY}" stroke-width="2.5" marker-end="url(#m)"/>`;
  }
  svg += '</svg>';
  const boxes = b.steps.map((s, i) => `<div class="box" style="position:absolute;width:${bw}px;min-height:${bh - 20}px;left:${pts[i][0] - bw / 2}px;top:${pts[i][1] - bh / 2}px;font-size:14px;display:flex;align-items:center;justify-content:center"><span><span class="n">${i + 1}</span>${esc(s)}</span></div>`).join('');
  return `<div id="fig" style="width:${W + 28}px"><div style="position:relative;width:${W}px;height:${H}px">${svg}${boxes}</div></div>`;
}

// Named schematics. Values follow standard physiology teaching figures (Guyton and Hall consensus).
function axisSVG(w, h, body, ylab) {
  return `<div id="fig"><svg width="${w}" height="${h}" font-family="Plus Jakarta Sans" fill="${INK}">${body}${ylab || ''}</svg></div>`;
}
function ecg() {
  // baseline y=200; 1 px = 4 ms horizontally (grid 40 px = 0.16 s), 1 mm style grid
  let g = '';
  for (let x = 40; x <= 860; x += 20) g += `<line x1="${x}" y1="40" x2="${x}" y2="300" stroke="#E3E5EA" stroke-width="${(x - 40) % 100 === 0 ? 1.4 : 0.7}"/>`;
  for (let y = 40; y <= 300; y += 20) g += `<line x1="40" y1="${y}" x2="860" y2="${y}" stroke="#E3E5EA" stroke-width="${(y - 40) % 100 === 0 ? 1.4 : 0.7}"/>`;
  const B = 200;
  const d = `M40,${B} L120,${B} C135,${B} 140,${B - 28} 155,${B - 28} C170,${B - 28} 175,${B} 190,${B} L250,${B} L262,${B + 18} L285,${B - 150} L305,${B + 40} L318,${B} L420,${B} C455,${B} 470,${B - 55} 500,${B - 55} C530,${B - 55} 545,${B} 575,${B} L860,${B}`;
  const lab = (x, y, t, a = 'middle', w = 600) => `<text x="${x}" y="${y}" font-size="15" font-weight="${w}" text-anchor="${a}">${t}</text>`;
  const br = (x1, x2, y, t) => `<line x1="${x1}" y1="${y}" x2="${x2}" y2="${y}" stroke="${TERRA}" stroke-width="2"/><line x1="${x1}" y1="${y - 6}" x2="${x1}" y2="${y + 6}" stroke="${TERRA}" stroke-width="2"/><line x1="${x2}" y1="${y - 6}" x2="${x2}" y2="${y + 6}" stroke="${TERRA}" stroke-width="2"/>${lab((x1 + x2) / 2, y + 22, t)}`;
  return axisSVG(900, 450, g + `<path d="${d}" fill="none" stroke="${INK}" stroke-width="3"/>` +
    lab(155, B - 40, 'P wave') + lab(285, B - 160, 'QRS complex') + lab(500, B - 67, 'T wave') + lab(370, B + 24, 'ST segment', 'middle', 500) + lab(222, B + 64, 'PR segment', 'middle', 500) + `<line x1="222" y1="${B + 48}" x2="222" y2="${B + 6}" stroke="${GRAY}" stroke-width="1"/>` +
    br(120, 250, 330, 'PR interval (0.12 to 0.20 s)') + br(250, 318, 372, 'QRS (under 0.12 s)') + br(250, 575, 404, 'QT interval (rate dependent)') +
    `<text x="860" y="30" font-size="12" text-anchor="end" fill="${GRAY}">Small box 0.04 s, large box 0.20 s at 25 mm/s</text>`);
}
function conduction() {
  const node = (x, y, w, t, sub) => `<rect x="${x}" y="${y}" width="${w}" height="54" rx="10" fill="#fff" stroke="${INK}" stroke-width="2"/><text x="${x + w / 2}" y="${y + 24}" font-size="15" font-weight="700" text-anchor="middle">${t}</text>${sub ? `<text x="${x + w / 2}" y="${y + 43}" font-size="12" text-anchor="middle" fill="${GRAY}">${sub}</text>` : ''}`;
  const ar = (x1, y1, x2, y2) => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${GRAY}" stroke-width="2.5" marker-end="url(#a)"/>`;
  return axisSVG(760, 560, `<defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="${GRAY}"/></marker></defs>` +
    node(250, 10, 260, 'SA node', 'primary pacemaker, about 60 to 100 per min') + ar(380, 64, 380, 92) +
    node(230, 96, 300, 'Atrial myocardium', 'atria depolarize (P wave)') + ar(380, 150, 380, 178) +
    node(230, 182, 300, 'AV node', 'slow conduction, delay about 0.1 s') + ar(380, 236, 380, 264) +
    node(250, 268, 260, 'Bundle of His', 'passes through fibrous skeleton') + ar(330, 322, 190, 360) + ar(430, 322, 570, 360) +
    node(60, 364, 260, 'Right bundle branch', '') + node(440, 364, 260, 'Left bundle branch', 'anterior and posterior fascicles') + ar(190, 418, 330, 456) + ar(570, 418, 430, 456) +
    node(230, 460, 300, 'Purkinje fibers', 'fastest conduction, about 2 to 4 m/s') +
    `<text x="380" y="545" font-size="13" text-anchor="middle" fill="${GRAY}">Ventricles depolarize from endocardium to epicardium, apex to base (QRS complex)</text>`);
}
function apPlot(kind) {
  const W = 780, top = 40, vmax = 40, vmin = kind === 'pacemaker' ? -75 : -100, sc = kind === 'pacemaker' ? 2.6 : 2.1;
  const y = v => top + 20 + (vmax - v) * sc, axisY = y(vmin), H = axisY + 50, x0 = 90;
  let g = `<line x1="${x0}" y1="${top}" x2="${x0}" y2="${axisY}" stroke="${INK}" stroke-width="2"/><line x1="${x0}" y1="${axisY}" x2="${W - 20}" y2="${axisY}" stroke="${INK}" stroke-width="2"/>`;
  for (let v = 20; v > vmin; v -= 20) g += `<line x1="${x0 - 6}" y1="${y(v)}" x2="${x0}" y2="${y(v)}" stroke="${INK}"/><text x="${x0 - 10}" y="${y(v) + 5}" font-size="13" text-anchor="end">${v}</text>`;
  g += `<text x="24" y="${(top + axisY) / 2}" font-size="13" transform="rotate(-90 24 ${(top + axisY) / 2})" text-anchor="middle">Membrane potential (mV)</text><text x="${(x0 + W) / 2}" y="${axisY + 34}" font-size="13" text-anchor="middle">Time</text>`;
  const lab = (x, yy, t, a = 'middle') => `<text x="${x}" y="${yy}" font-size="14" font-weight="700" text-anchor="${a}" fill="${TERRA}">${t}</text>`;
  const note = (x, yy, t, a = 'middle') => `<text x="${x}" y="${yy}" font-size="12.5" text-anchor="${a}" fill="${GRAY}">${t}</text>`;
  if (kind === 'pacemaker') {
    const cyc = o => `C${x0 + o + 60},${y(-56)} ${x0 + o + 120},${y(-48)} ${x0 + o + 170},${y(-40)} C${x0 + o + 185},${y(-30)} ${x0 + o + 200},${y(5)} ${x0 + o + 215},${y(10)} C${x0 + o + 240},${y(8)} ${x0 + o + 280},${y(-40)} ${x0 + o + 310},${y(-60)} `;
    const d = `M${x0},${y(-60)} ` + cyc(0) + cyc(310);
    g += `<line x1="${x0}" y1="${y(-40)}" x2="${W - 20}" y2="${y(-40)}" stroke="${LINE}" stroke-dasharray="6 5"/>` + note(x0 + 322, y(-40) - 8, 'threshold about -40 mV', 'start');
    g += `<path d="${d}" fill="none" stroke="${INK}" stroke-width="3"/>` +
      lab(x0 + 110, y(-12), 'Phase 4') + note(x0 + 110, y(-12) + 18, 'funny current (HCN, Na+ in),') + note(x0 + 110, y(-12) + 34, 'then T-type Ca2+ in') +
      lab(x0 + 196, y(28), 'Phase 0', 'end') + note(x0 + 196, y(28) + 18, 'L-type Ca2+ in', 'end') +
      lab(x0 + 262, y(4), 'Phase 3', 'start') + note(x0 + 262, y(4) + 18, 'K+ out', 'start') +
      note(x0 + 10, y(-60) + 22, 'maximum diastolic potential about -60 mV', 'start');
  } else {
    const d = `M${x0},${y(-90)} L${x0 + 90},${y(-90)} L${x0 + 96},${y(25)} L${x0 + 112},${y(8)} C${x0 + 140},${y(14)} ${x0 + 260},${y(10)} ${x0 + 330},${y(-5)} C${x0 + 380},${y(-20)} ${x0 + 410},${y(-80)} ${x0 + 450},${y(-89)} L${x0 + 650},${y(-90)}`;
    g += `<path d="${d}" fill="none" stroke="${INK}" stroke-width="3"/>` +
      lab(x0 + 84, y(-30), 'Phase 0', 'end') + note(x0 + 84, y(-30) + 18, 'fast Na+ in', 'end') +
      lab(x0 + 120, y(40), 'Phase 1', 'start') + note(x0 + 190, y(40), 'brief K+ out (Ito)', 'start') +
      lab(x0 + 230, y(-12), 'Phase 2 (plateau)') + note(x0 + 230, y(-12) + 18, 'L-type Ca2+ in balances K+ out') +
      lab(x0 + 420, y(-35), 'Phase 3', 'start') + note(x0 + 420, y(-35) + 18, 'K+ out (IKr, IKs)', 'start') +
      lab(x0 + 560, y(-74), 'Phase 4') + note(x0 + 560, y(-74) + 18, 'resting about -90 mV (IK1)');
  }
  return axisSVG(W, H, g);
}
const DIAG = { 'ecg-waveform': ecg, 'conduction-pathway': conduction, 'pacemaker-ap': () => apPlot('pacemaker'), 'ventricular-ap': () => apPlot('ventricular') };

const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 2.5 });
for (const f of process.argv.slice(2)) {
  const d = JSON.parse(fs.readFileSync(f, 'utf8'));
  const out = [];
  let n = 0;
  const blocks = [...d.sections.flatMap(s => s.blocks), ...(d.integration || [])];
  for (const b of blocks) {
    if (!['flow', 'cycle', 'diagram'].includes(b.type)) continue;
    n++;
    const html = b.type === 'flow' ? flowHTML(b) : b.type === 'cycle' ? cycleHTML(b) : DIAG[b.name]();
    await page.setContent(`<!doctype html><html><head><meta charset="utf-8">${BASE}</head><body>${html}</body></html>`);
    await page.evaluate(() => document.fonts.ready);
    const el = await page.$('#fig');
    const box = await el.boundingBox();
    const file = path.join(OUT, `${d.unit}-${n}.png`);
    await el.screenshot({ path: file });
    out.push({ n, file, w: Math.round(box.width), h: Math.round(box.height) });
  }
  fs.writeFileSync(path.join(OUT, `${d.unit}.json`), JSON.stringify(out, null, 1));
  console.log(d.unit, out.length, 'figures');
}
await browser.close();
