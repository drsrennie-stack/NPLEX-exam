// Build the printable Comprehensive Notes DOCX for one or more chapters.
// Usage: node tools/notes/build_docx.js notes/chapters/CV-7.json [more]
// Needs figures from tools/notes/figures.mjs. Output: notes/build/<UNIT>.docx
const fs = require('fs');
const path = require('path');
const D = require('docx');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  AlignmentType, ImageRun, Header, Footer, PageNumber, PositionalTab, PositionalTabAlignment, PositionalTabRelativeTo,
  PositionalTabLeader, LevelFormat, PageBreak, TableLayoutType, VerticalAlign, LineRuleType, TabStopType, Tab } = D;

const ROOT = path.resolve(__dirname, '../..');
const REG = JSON.parse(fs.readFileSync(path.join(ROOT, 'notes/registry/identifiers.json'), 'utf8')).entries;
const NAVY = '0B1530', TERRA = '8B3A2E', GRAY = '4A5160', RULE = 'B8BDC7', SOFT = 'F3F4F7', HEAD = 'E7E9EF';
const FONT = process.env.BODY_FONT || 'Helvetica Neue', HFONT = process.env.HEAD_FONT || 'Helvetica Neue', BODY_SIZE = +(process.env.BODY_SIZE || 20), SAMPLE = process.env.SAMPLE_LABEL || '';
const PAGE_W = 12240, PAGE_H = 15840, ML = 1008, MR = 2448, MT = 936, MB = 936; // wide right margin = blank notes column
const TW = PAGE_W - ML - MR; // text width in DXA
const PX_MAX = Math.floor(TW / 15); // DXA to px at 96 dpi (1 px = 15 DXA)

const run = (t, o = {}) => new TextRun({ text: t, font: (o.size >= 24 || o.hd) ? HFONT : FONT, size: BODY_SIZE, ...o });
const para = (children, o = {}) => { if (o.spacing && o.spacing.line) o.spacing = { ...o.spacing, lineRule: LineRuleType.AUTO }; return new Paragraph({ children: Array.isArray(children) ? children : [children], ...o }); };
const P = (t, o = {}) => para(run(t), { spacing: { after: 110, line: 256 }, ...o });
const border = (c = RULE, sz = 4) => ({ style: BorderStyle.SINGLE, size: sz, color: c });
const allB = c => ({ top: border(c), bottom: border(c), left: border(c), right: border(c) });
const noB = { top: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, bottom: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, left: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, right: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' } };

function card(children, fill = SOFT) {
  return new Table({
    width: { size: TW, type: WidthType.DXA }, columnWidths: [TW], layout: TableLayoutType.FIXED,
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({ width: { size: TW, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, fill, color: 'auto' }, borders: allB('D5D8DE'), margins: { top: 140, bottom: 100, left: 200, right: 200 }, children })] })]
  });
}
const spacer = (after = 120) => para(run(''), { spacing: { after } });

function colWidths(cols, rows) {
  const len = cols.map((c, j) => Math.max(8, Math.min(60, (c.length + rows.reduce((a, r) => a + String(r[j] || '').length, 0) / Math.max(1, rows.length)))));
  const tot = len.reduce((a, b) => a + b, 0);
  let w = len.map(l => Math.max(1100, Math.round(TW * l / tot)));
  const s = w.reduce((a, b) => a + b, 0); w = w.map(x => Math.round(x * TW / s));
  w[w.length - 1] += TW - w.reduce((a, b) => a + b, 0);
  return w;
}
function dataTable(cols, rows, opts = {}) {
  const w = opts.widths || colWidths(cols, rows);
  const cell = (t, j, head) => new TableCell({
    width: { size: w[j], type: WidthType.DXA }, borders: allB(RULE), margins: { top: 50, bottom: 50, left: 90, right: 90 },
    shading: head ? { type: ShadingType.CLEAR, fill: HEAD, color: 'auto' } : undefined, verticalAlign: VerticalAlign.TOP,
    children: [para(run(String(t), { size: 17, bold: head, color: NAVY }), { spacing: { after: 0, line: 240 } })]
  });
  return new Table({
    width: { size: TW, type: WidthType.DXA }, columnWidths: w, layout: TableLayoutType.FIXED,
    rows: [new TableRow({ tableHeader: true, cantSplit: true, children: cols.map((c, j) => cell(c, j, true)) }),
      ...rows.map(r => new TableRow({ cantSplit: true, children: r.map((c, j) => cell(c, j, false)) }))]
  });
}
function noteLines(n = 4) {
  const out = [para(run('My notes', { bold: true, size: 17, color: GRAY }), { spacing: { before: 200, after: 60 }, keepNext: true })];
  for (let i = 0; i < n; i++) out.push(para(run(''), { spacing: { after: 0, line: 420 }, border: { bottom: border('C9CDD5', 4) }, keepNext: i < n - 1 }));
  out.push(spacer(200));
  return out;
}
const capLabel = (kind, num, title) => para([run(`${kind} ${num}. `, { bold: true, color: TERRA, size: 19 }), run(title, { bold: true, color: NAVY, size: 19 })], { spacing: { before: 160, after: 80 }, keepNext: true });
const caption = t => para(run(t, { size: 17, color: GRAY }), { spacing: { after: 220, line: 260 } });

function build(file) {
  const d = JSON.parse(fs.readFileSync(file, 'utf8'));
  const figs = JSON.parse(fs.readFileSync(path.join(ROOT, 'notes/build/fig', d.unit + '.json'), 'utf8'));
  const chapNum = d.unit.replace(/^[A-Z]{2}-/, '').replace('-', '');
  let figN = 0, tabN = 0;
  const body = [];

  // Chapter heading block (no separate title page)
  body.push(para(run('NPLEX PART I  |  BIOMEDICAL SCIENCE  |  COMPREHENSIVE NOTES', { size: 15, bold: true, color: TERRA, characterSpacing: 30 }), { spacing: { after: 100 } }));
  body.push(para(run(d.title, { size: 44, color: NAVY }), { heading: HeadingLevel.HEADING_1, spacing: { after: 80, line: 240 } }));
  body.push(para([run(d.chapter_id, { bold: true, size: 17, color: GRAY }), run('   |   ' + d.subject + '   |   Course unit ' + d.unit + '   |   Version ' + d.version + '   |   Dr. Sharilyn Rennie, MedMasters Collaborative', { size: 17, color: GRAY })], { spacing: { after: 240 }, border: { bottom: border('D5D8DE', 6) } }));
  // Overview
  const ov = d.overview || {};
  body.push(para(run('Chapter Overview', { size: 30, color: NAVY }), { heading: HeadingLevel.HEADING_2, spacing: { after: 160 }, keepNext: true }));
  String(ov.intro || '').split(/\n\n+/).forEach(t => t.trim() && body.push(P(t.trim())));
  const lab = (t, rest) => para([run(t + ' ', { bold: true, color: TERRA, size: 18 }), run(rest, { size: 18 })], { spacing: { after: 80, line: 250 } });
  body.push(lab('Before you start:', (ov.prerequisites || []).join('; ') + '.'));
  body.push(lab('Connects to:', (ov.connections || []).map(c => c.to + ' (' + c.how.replace(/\.$/, '') + ')').join('; ') + '.'));
  body.push(para(run('Chapter competencies', { bold: true, size: 22, color: TERRA }), { heading: HeadingLevel.HEADING_3, spacing: { before: 160, after: 60 }, keepNext: true }));
  d.sections.forEach(s => body.push(para([run(s.comp + '  ', { bold: true, size: 17, color: NAVY }), run(REG[s.comp] ? REG[s.comp].text : s.title, { size: 17 })], { spacing: { after: 50, line: 240 } })));
  body.push(para(run('Key terminology', { bold: true, size: 22, color: TERRA }), { heading: HeadingLevel.HEADING_3, spacing: { before: 160, after: 60 }, keepNext: true }));
  const T = ov.terms || [], half = Math.ceil(T.length / 2), tw4 = [1300, Math.round(TW / 2) - 1300, 1300, TW - Math.round(TW / 2) - 1300];
  body.push(dataTable(['Term', 'Definition', 'Term', 'Definition'], Array.from({ length: half }, (_, i) => [T[i].term, T[i].def, T[i + half] ? T[i + half].term : '', T[i + half] ? T[i + half].def : '']), { widths: tw4 }));
  body.push(spacer(160));

  // Sections
  for (const s of d.sections) {
    const reg = REG[s.comp];
    body.push(para([run(s.comp, { bold: true, size: 18, color: TERRA, characterSpacing: 20 }), run('   |   ' + s.obj, { size: 18, color: GRAY })], { spacing: { before: 120, after: 40 }, keepNext: true }));
    body.push(para(run(s.title, { size: 30, color: NAVY }), { heading: HeadingLevel.HEADING_2, spacing: { after: 140, line: 250 }, keepNext: true }));
    if (reg) body.push(card([para([run('Competency: ', { bold: true, color: TERRA, size: 19 }), run(reg.text, { color: NAVY, size: 20 })], { spacing: { after: 40, line: 280 } })]));
    body.push(spacer(120));
    for (const b of s.blocks) {
      if (b.type === 'p') body.push(P(b.text));
      else if (b.type === 'h') body.push(para(run(b.text, { bold: true, size: 22, color: TERRA }), { heading: HeadingLevel.HEADING_3, spacing: { before: 220, after: 100 }, keepNext: true }));
      else if (b.type === 'bullets') { b.items.forEach(t => body.push(para(run(t), { numbering: { reference: 'bul', level: 0 }, spacing: { after: 60, line: 252 } }))); body.push(spacer(80)); }
      else if (b.type === 'table') { tabN++; body.push(capLabel('Table', `${chapNum}.${tabN}`, b.title)); body.push(dataTable(b.cols, b.rows, { boldFirst: true })); body.push(b.caption ? caption(b.caption) : spacer(200)); }
      else if (['flow', 'cycle', 'diagram'].includes(b.type)) {
        const f = figs[figN]; figN++;
        const scale = Math.min(1, (PX_MAX - 10) / f.w, (b.type === 'diagram' ? 290 : 250) / f.h);
        body.push(capLabel('Figure', `${chapNum}.${figN}`, b.title || ({ 'ecg-waveform': 'The normal ECG waveform', 'conduction-pathway': 'The cardiac conduction system', 'pacemaker-ap': 'The SA nodal (pacemaker) action potential', 'ventricular-ap': 'The ventricular myocyte action potential' })[b.name] || 'Figure'));
        body.push(para(new ImageRun({ type: 'png', data: fs.readFileSync(f.file), transformation: { width: Math.round(f.w * scale), height: Math.round(f.h * scale) }, altText: { title: b.title || b.name || 'Figure', description: b.caption || '', name: 'fig' } }), { alignment: AlignmentType.CENTER, keepNext: true, spacing: { after: 60 } }));
        body.push(caption((b.caption || '') + (b.type === 'diagram' ? ' Original schematic, MedMasters Collaborative.' : '')));
      }
      else if (b.type === 'example') {
        const parts = String(b.text).split(/\n\n+/);
        body.push(card([para([run('Worked example: ', { bold: true, color: TERRA }), run(b.title || '', { bold: true, color: NAVY })], { spacing: { after: 100 } }), ...parts.map(t => para(run(t.trim(), { size: 20 }), { spacing: { after: 100, line: 252 } }))]));
        body.push(spacer(200));
      }
      else if (b.type === 'stop') {
        const L = (lab, t) => para([run(lab + ' ', { bold: true, color: TERRA }), run(t, { size: 20 })], { spacing: { after: 80, line: 280 } });
        body.push(card([L('STOP:', 'Cover or close the notes.'), L('PREDICT:', b.predict), L('EXPLAIN:', b.explain), L('CHECK:', b.check)], 'FFFFFF'));
        body.push(spacer(200));
      }
    }
    body.push(spacer(120));
  }

  // Integration, summary, checklist, sources
  const H2 = t => para(run(t, { size: 30, color: NAVY }), { heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 140 }, keepNext: true });
  body.push(H2('Biomedical Integration'));
  for (const b of d.integration || []) b.type === 'h' ? body.push(para(run(b.text, { bold: true, size: 22, color: TERRA }), { spacing: { before: 200, after: 100 }, keepNext: true })) : body.push(P(b.text));
  body.push(H2('Chapter Summary'));
  (d.summary || []).forEach(t => body.push(para(run(t), { numbering: { reference: 'bul', level: 0 }, spacing: { after: 80, line: 252 } })));
  body.push(H2('Competency Checklist'));
  body.push(P('Mark each competency only when you can do it from memory, without your notes. Record the date so you can schedule the next retrieval.'));
  body.push(dataTable(['Competency ID', 'Competency', 'I can do this', 'Date'], d.sections.map(s => [s.comp, REG[s.comp] ? REG[s.comp].text : s.title, '', '']), { widths: [2500, TW - 2500 - 1250 - 1000, 1250, 1000], boldFirst: true }));
  body.push(H2('Sources'));
  (d.sources || []).forEach(r => body.push(para([run(r.book + ': ', { bold: true }), run(r.where)], { numbering: { reference: 'bul', level: 0 }, spacing: { after: 60, line: 252 } })));
  body.push(P('Figures are original schematics by MedMasters Collaborative unless a source is named in the caption.', { spacing: { before: 160 } }));

  const header = new Header({ children: [para([run(SAMPLE || 'NPLEX Part I Comprehensive Notes', { size: 15, color: SAMPLE ? TERRA : GRAY, bold: true }), run('   ' + d.chapter_id + '   ' + d.title, { size: 15, color: GRAY })], { border: { bottom: border('D5D8DE', 4) }, spacing: { after: 0 } })] });
  const footer = new Footer({ children: [para([run('MedMasters Collaborative  |  Dr. Sharilyn Rennie  |  Version ' + d.version, { size: 15, color: GRAY }),
    new TextRun({ children: [new Tab(), 'Page ', PageNumber.CURRENT, ' of ', PageNumber.TOTAL_PAGES], font: FONT, size: 15, color: GRAY })], { style: 'Footer', tabStops: [{ type: TabStopType.RIGHT, position: TW }] })] });

  const doc = new Document({
    creator: 'Dr. Sharilyn Rennie', title: d.title + ' (' + d.chapter_id + ')', description: 'NPLEX Part I Comprehensive Notes',
    styles: {
      default: { document: { run: { font: FONT, size: BODY_SIZE, color: '1A2033' }, paragraph: { spacing: { line: 256, lineRule: LineRuleType.AUTO } } } },
      paragraphStyles: [
        { id: 'Footer', name: 'footer', basedOn: 'Normal', run: { font: FONT, size: 15, color: GRAY } },
        { id: 'Header', name: 'header', basedOn: 'Normal', run: { font: FONT, size: 15, color: GRAY } },
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HFONT, size: 44, bold: false, color: NAVY }, paragraph: { outlineLevel: 0 } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HFONT, size: 30, bold: false, color: NAVY }, paragraph: { outlineLevel: 1, keepNext: true } },
        { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HFONT, size: 22, bold: true, color: TERRA }, paragraph: { outlineLevel: 2, keepNext: true } }]
    },
    numbering: { config: [{ reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } } } }] }] },
    sections: [{ properties: { page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MT, bottom: MB, left: ML, right: MR, header: 540, footer: 540 } }, },
      headers: { default: header }, footers: { default: footer }, children: body }]
  });
  const out = path.join(ROOT, 'notes/build', d.unit + '.docx');
  return Packer.toBuffer(doc).then(buf => { fs.writeFileSync(out, buf); console.log('wrote', out, figN, 'figures', tabN, 'tables'); });
}
(async () => { for (const f of process.argv.slice(2)) await build(f); })();
