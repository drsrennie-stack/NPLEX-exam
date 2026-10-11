"""Build the NPLEX competency viewer (HTML) and PDF from nplex-competencies.js.

Usage: python3 tools/build_competency_pages.py <out_dir>
Writes:
  nplex-competencies.html          full page for the repo / GitHub Pages
  nplex-competencies-artifact.html same page without the document wrapper
  NPLEX-Part-I-Competencies.pdf    print version (competencies + USMLE crosswalk appendix)
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TITLE = "NPLEX Part I Competencies"


def load():
    src = open(os.path.join(ROOT, "nplex-competencies.js"), encoding="utf-8").read()
    def grab(name):
        i = src.index("window." + name + " = ") + len("window." + name + " = ")
        dec = json.JSONDecoder()
        val, _ = dec.raw_decode(src[i:])
        return val
    return grab("NPLEX_BLUEPRINT"), grab("NPLEX_COMPETENCIES"), grab("NPLEX_CROSSWALK"), grab("NPLEX_EXCLUDED")


STYLE = r"""
<style>
/* Layout: one reading column. Header facts, weighting table, filters, then one white card per body system,
   then the USMLE crosswalk. Brand: MedMasters navy, terracotta, gold. Dark: navy page, white cards. */
:root{
  --page:#FFFFFF; --soft:#FAFAF9; --card:#FFFFFF; --ink:#0B1530; --ink2:rgba(11,21,48,.74);
  --accent:#8B3A2E; --accent-hover:#6B2A20; --gold:#C9A14A; --goldlt:#EFD9A4;
  --line:rgba(11,21,48,.14); --line-strong:rgba(11,21,48,.55);
  --head-ink:#0B1530; --head-ink2:rgba(11,21,48,.74); --head-accent:#8B3A2E;
  --shadow:0 1px 3px rgba(0,0,0,.10); --shadow-hover:0 10px 22px rgba(0,0,0,.14);
  --display:"Open Sans","Plus Jakarta Sans",system-ui,sans-serif;
  --body:"Plus Jakarta Sans",system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
  color-scheme:light;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --page:#060A18; --soft:#0A1222; --head-ink:#EEF1F6; --head-ink2:#B6C0D0; --head-accent:#E09A8C;
  --shadow:0 1px 3px rgba(0,0,0,.4); --shadow-hover:0 10px 22px rgba(0,0,0,.5); color-scheme:dark}}
:root[data-theme="dark"]{
  --page:#060A18; --soft:#0A1222; --head-ink:#EEF1F6; --head-ink2:#B6C0D0; --head-accent:#E09A8C;
  --shadow:0 1px 3px rgba(0,0,0,.4); --shadow-hover:0 10px 22px rgba(0,0,0,.5); color-scheme:dark}
*{box-sizing:border-box}
em,i,cite,dfn,var,address{font-style:normal}
body{background:var(--page);color:var(--head-ink);font-family:var(--body);font-size:15px;line-height:1.55;margin:0}
.wrap{max-width:1080px;margin:0 auto;padding-inline:16px;padding-block:28px 56px}
.skip{position:absolute;left:-9999px;top:8px;background:var(--card);color:var(--ink);padding:8px 12px;border-radius:6px;z-index:10}
.skip:focus{left:16px}
:focus-visible{outline:3px solid var(--gold);outline-offset:2px;border-radius:4px}
h1,h2,h3{text-wrap:balance;margin:0}
.eyebrow{font-size:12px;font-weight:700;letter-spacing:.3em;text-transform:uppercase;color:var(--head-accent);margin:0 0 6px}
h1{font-family:var(--display);font-weight:800;letter-spacing:-.03em;font-size:clamp(1.9rem,4.6vw,2.8rem);line-height:1.06;color:var(--head-ink)}
h1 .accent{color:var(--head-accent)}
.lede{max-width:70ch;color:var(--head-ink2);margin:12px 0 0;font-size:1.02rem}
header{display:grid;gap:4px;margin-bottom:22px}
.card{background:var(--card);color:var(--ink);border-radius:14px;box-shadow:var(--shadow);padding:18px 20px}
.card .eyebrow{color:var(--accent)}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin:0 0 20px;padding:0;list-style:none}
.facts li{border-radius:14px;padding:14px 16px;box-shadow:var(--shadow)}
.facts b{display:block;font-size:1.6rem;font-weight:800;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.facts span{font-size:.86rem;font-weight:600}
.t-white{background:#FFFFFF;color:#0B1530}
.t-gold{background:#C9A14A;color:#0B1530}
.t-terra{background:#8B3A2E;color:#FFFFFF}
.t-goldlt{background:#EFD9A4;color:#0B1530}
.section{margin:0 0 22px}
.section h2,.card h2{font-size:1.2rem;font-weight:800;letter-spacing:-.01em}
.tablebox{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums;font-size:14px}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}
thead th{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink2);font-weight:700;background:#F3F4F7}
tbody th{font-weight:700}
td.num,th.num{text-align:right}
.legend{display:flex;flex-wrap:wrap;gap:10px 18px;margin:12px 0 0;padding:0;list-style:none;font-size:14px}
.legend li{display:flex;align-items:center;gap:8px}
.src{display:inline-flex;align-items:center;font-size:11.5px;font-weight:700;border-radius:999px;padding:1px 9px;white-space:nowrap;border:1.5px solid}
.src.s-NPLEX{color:#0B1530;border-color:#0B1530;background:#FFFFFF}
.src.s-Both{color:#0B1530;border-color:#C9A14A;background:#EFD9A4}
.src.s-USMLE{color:#8B3A2E;border-color:#8B3A2E;background:#FFFFFF}
.tag{display:inline-flex;font-size:11.5px;font-weight:600;border:1px solid var(--line);border-radius:999px;padding:1px 9px;color:var(--ink2);white-space:nowrap}
.controls{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end}
.field{display:grid;gap:4px;min-width:0;flex:1 1 200px}
.field label{font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--ink2)}
input[type=search],select{font:inherit;color:var(--ink);background:#FFFFFF;border:1px solid var(--line-strong);border-radius:10px;padding:9px 11px;width:100%}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 0;padding:0;list-style:none}
.chip-btn{font:inherit;font-size:13px;font-weight:700;color:var(--ink);background:#FFFFFF;border:1px solid var(--line-strong);border-radius:999px;padding:5px 12px;cursor:pointer}
.chip-btn[aria-pressed="true"]{background:#0B1530;color:#FFFFFF;border-color:#0B1530}
.status{font-size:13px;color:var(--head-ink2);margin:12px 0 16px}
.sys{margin-bottom:20px;transition:box-shadow 200ms ease}
.sys:hover{box-shadow:var(--shadow-hover)}
.sys-head{display:flex;flex-wrap:wrap;gap:4px 16px;align-items:baseline;justify-content:space-between;margin-bottom:6px}
.sys-head h2{font-size:1.55rem;font-weight:800;letter-spacing:-.02em}
.sys-head .full{font-weight:600;color:var(--ink2);font-size:.95rem;margin-left:8px}
.meta{font-size:13px;color:var(--ink2);font-variant-numeric:tabular-nums}
h3.group{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin:18px 0 4px}
.unit{padding:12px 0;border-top:1px solid var(--line)}
.unit-top{display:grid;grid-template-columns:5.6rem minmax(0,1fr);gap:2px 12px}
.code{font-weight:800;font-size:13px;color:var(--ink);font-variant-numeric:tabular-nums;padding-top:2px}
.uname{font-weight:800;font-size:1.02rem}
.stmt{margin:2px 0 4px;color:var(--ink2);font-size:14px;max-width:78ch}
.conds{display:flex;flex-wrap:wrap;gap:4px 14px;margin:2px 0 4px;padding:0;list-style:none;font-size:13.5px;color:var(--ink2)}
.conds .c{font-weight:700;color:var(--ink);margin-right:4px;font-size:12px}
ol.objs{list-style:none;margin:8px 0 0;padding:0 0 0 5.6rem;display:grid;gap:7px}
.obj{display:grid;grid-template-columns:4.6rem minmax(0,1fr);gap:2px 10px}
.obj .oid{font-size:12.5px;font-weight:700;color:var(--accent);font-variant-numeric:tabular-nums;padding-top:1px}
.obj .ot{font-size:14.5px}
.obj .otags{display:flex;flex-wrap:wrap;gap:5px;margin-top:3px}
.obj .ot+.otags{}
.obj:target{background:#FFF7E3;border-radius:8px}
.empty{padding:24px;text-align:center}
details.cw{border-top:1px solid var(--line);padding:8px 0}
details.cw summary{cursor:pointer;font-weight:800;font-size:1.02rem;padding:6px 0}
details.cw summary .meta{font-weight:600;margin-left:8px}
.cw table a{color:var(--accent);font-weight:700}
.notes p{margin:0 0 8px;max-width:78ch}
.notes p:last-child{margin-bottom:0}
a{color:var(--accent)}
footer{margin-top:28px;font-size:13px;color:var(--head-ink2)}
footer a{color:var(--head-accent)}
@media (max-width:620px){
  .unit-top{grid-template-columns:1fr}
  ol.objs{padding-left:0}
  .obj{grid-template-columns:3.9rem minmax(0,1fr)}
}
@media (prefers-reduced-motion: reduce){*{transition:none!important}}
@page{size:Letter;margin:0.55in 0.6in}
@media print{
  :root{--page:#FFFFFF;--head-ink:#0B1530;--head-ink2:rgba(11,21,48,.74);--head-accent:#8B3A2E}
  body{font-size:10pt}
  .wrap{max-width:none;padding:0}
  .skip,.controls,.chips,.status,#filters{display:none!important}
  .card,.facts li{box-shadow:none}
  .card{padding:0}
  .facts li{border:1px solid rgba(11,21,48,.2)}
  .sys{break-before:page}
  .unit-top,.obj{break-inside:avoid}
  h3.group{break-after:avoid}
  details.cw{break-inside:auto}
  details.cw summary{list-style:none}
  #crosswalk{break-before:page}
  tr{break-inside:avoid}
  .obj:target{background:none}
  body{font-size:9.2pt;line-height:1.36}
  .unit{padding:6px 0}
  .unit-top{grid-template-columns:4.4rem minmax(0,1fr)}
  .uname{font-size:10.5pt}
  .stmt,.conds{font-size:8.8pt;margin:0 0 2px}
  ol.objs{padding-left:0;gap:2px;margin-top:3px}
  .obj{grid-template-columns:4.4rem minmax(0,1fr)}
  .obj .ot{font-size:9.2pt}
  .obj .otags{display:inline;margin:0 0 0 4px}
  .obj .otags .src,.obj .otags .tag{font-size:7pt;padding:0 5px;border-width:1px;margin-right:2px}
  .sys-head h2{font-size:16pt}
  h3.group{margin:8px 0 2px}
  .cw table{font-size:8.6pt}
  .cw th,.cw td{padding:3px 6px}
}
</style>
"""

BODY = r"""
<a class="skip" href="#list">Skip to the competency list</a>
<div class="wrap">
<header>
  <p class="eyebrow">NPLEX Part I · Board Review · MedMasters Collaborative</p>
  <h1>NPLEX Part I <span class="accent">Competencies</span></h1>
  <p class="lede">Built on the NABNE Part I blueprint and written to USMLE Step 1 depth. Each blueprint unit lists what you should be able to do, tagged by where it comes from.</p>
</header>
<main id="main">
<ul class="facts" aria-label="At a glance" id="facts"></ul>

<section class="section card" aria-labelledby="src-h">
  <h2 id="src-h">Where each competency comes from</h2>
  <ul class="legend">
    <li><span class="src s-NPLEX">NPLEX</span> Required by the NPLEX blueprint</li>
    <li><span class="src s-Both">NPLEX + USMLE</span> On both outlines</li>
    <li><span class="src s-USMLE">USMLE extension</span> Step 1 topic added inside the closest NPLEX unit</li>
  </ul>
</section>

<section class="section card" aria-labelledby="wt-h">
  <h2 id="wt-h">Weighting by body system</h2>
  <div class="tablebox" role="region" tabindex="0" aria-label="Weighting by body system (scrolls sideways)">
  <table>
    <thead><tr><th scope="col">System</th><th scope="col" class="num">Exam %</th><th scope="col" class="num">Questions</th><th scope="col" class="num">Cases</th><th scope="col" class="num">Units</th><th scope="col" class="num">Competencies</th><th scope="col" class="num">USMLE extensions</th><th scope="col" class="num">Week</th></tr></thead>
    <tbody id="wt-body"></tbody>
  </table>
  </div>
  <p class="meta" style="margin:10px 0 0">Structure/Function 60% (Anatomy, Physiology, Biochemistry &amp; Genetics). Disease/Dysfunction 40% (Microbiology &amp; Immunology, Pathology). You must pass both.</p>
</section>

<section class="section card" id="filters" aria-labelledby="fl-h">
  <h2 id="fl-h" style="margin-bottom:10px">Find a competency</h2>
  <div class="controls">
    <div class="field"><label for="q">Search</label><input type="search" id="q" placeholder="Try WPW, thiamine, Graves, CV-7.3" autocomplete="off"></div>
    <div class="field"><label for="sea">Exam area</label><select id="sea"><option value="">All exam areas</option></select></div>
    <div class="field"><label for="srcf">Source</label><select id="srcf"><option value="">Everything</option><option value="NPLEX">NPLEX only</option><option value="Both">On both outlines</option><option value="USMLE">USMLE extensions only</option></select></div>
  </div>
  <ul class="chips" id="sys-chips" aria-label="Filter by body system"></ul>
</section>
<p class="status" id="status" aria-live="polite"></p>

<div id="list"></div>

<section class="section card" id="crosswalk" aria-labelledby="cw-h">
  <p class="eyebrow">Appendix</p>
  <h2 id="cw-h">USMLE Step 1 crosswalk</h2>
  <p class="meta" style="margin:6px 0 4px">Every topic the USMLE Step 1 outline names for each system, and where it lives in this course. Topics outside NPLEX Part I are listed as excluded with the reason.</p>
  <div id="cw-list"></div>
</section>

<section class="section card notes" aria-labelledby="notes-h">
  <h2 id="notes-h" style="margin-bottom:8px">About this list</h2>
  <p><strong>NPLEX source.</strong> NABNE, NPLEX Part I Biomedical Sciences Study Guide, revised March 2026, for the August 2026 administrations. <a href="https://www.nabne.org/pdf/NPLEX-Part-I-Biomedical-Sciences-Study-Guide-08-2026.pdf" target="_blank" rel="noopener">Open the study guide</a>.</p>
  <p><strong>USMLE source.</strong> USMLE Step 1 Content Outline and Specifications. <a href="https://www.usmle.org/exam-resources/step-1-materials/step-1-content-outline-and-specifications" target="_blank" rel="noopener">Open the specifications</a>. USMLE removed its General Principles section, so foundational science sits inside each organ system here too.</p>
  <p><strong>Not included.</strong> Pharmacology, behavioral and social sciences, biostatistics and epidemiology, and care of the well patient. NPLEX Part I does not test them. A drug appears only when it causes a listed condition.</p>
  <p><strong>Codes.</strong> Unit codes come from the blueprint (CV-7, CV-18-C). Competency codes add a number (CV-7.3). Condition codes add a digit to the category (CV-18-C3 is myocardial infarction).</p>
  <p><strong>Added by MedMasters, not NABNE.</strong> Unit short names, exam-area tags, depth (DOK) levels, the USMLE extensions, and the crosswalk. Each question still carries its own exam area.</p>
</section>
</main>
<footer>MedMasters Collaborative · Dr. Sharilyn Rennie</footer>
</div>
"""

SCRIPT = r"""
<script>
(function(){
var BP=__BP__, C=__C__, CW=__CW__, EX=__EX__;
var SHORT={CV:'Cardio',GI:'GI',MS:'MSK',NE:'Neuro',RE:'Repro',UR:'Urology',EN:'Endo',IM:'Immuno',PU:'Pulm',HE:'Heme',IN:'Derm'};
var SEA={A:'Anatomy',P:'Physiology',B:'Biochemistry & Genetics',M:'Microbiology & Immunology',X:'Pathology'};
var SRC={NPLEX:'NPLEX',Both:'NPLEX + USMLE',USMLE:'USMLE extension'};
var state={q:'',sea:'',src:'',sys:''};
function $(s){return document.querySelector(s);}
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
var NAME={}; BP.systems.forEach(function(s){NAME[s.name]=s.code;});
function sysCode(n){ return NAME[n]||n; }

var totalObj=0, ext=0; C.forEach(function(c){ (c.objectives||[]).forEach(function(o){ totalObj++; if(o.src==='USMLE') ext++; }); });
$('#facts').innerHTML=[['t-white','200','questions in 50 cases of 4'],['t-gold',String(C.length),'study units on the blueprint'],['t-terra',totalObj.toLocaleString(),'specific competencies'],['t-goldlt',String(ext),'USMLE extensions added']].map(function(f){return '<li class="'+f[0]+'"><b>'+f[1]+'</b><span>'+f[2]+'</span></li>';}).join('');

var tb='', T={q:0,c:0,u:0,o:0,x:0};
BP.systems.forEach(function(s){
  var mine=C.filter(function(c){return c.systemCode===s.code;}), o=0, x=0;
  mine.forEach(function(c){ (c.objectives||[]).forEach(function(z){ o++; if(z.src==='USMLE') x++; }); });
  T.q+=s.items; T.c+=s.cases; T.u+=mine.length; T.o+=o; T.x+=x;
  tb+='<tr><th scope="row">'+esc(SHORT[s.code])+' <span class="meta">'+esc(s.full)+'</span></th><td class="num">'+s.weight+'%</td><td class="num">'+s.items+'</td><td class="num">'+s.cases+'</td><td class="num">'+mine.length+'</td><td class="num">'+o+'</td><td class="num">'+x+'</td><td class="num">'+s.week+'</td></tr>';
});
tb+='<tr><th scope="row">Total</th><td class="num">100%</td><td class="num">'+T.q+'</td><td class="num">'+T.c+'</td><td class="num">'+T.u+'</td><td class="num">'+T.o.toLocaleString()+'</td><td class="num">'+T.x+'</td><td></td></tr>';
$('#wt-body').innerHTML=tb;

Object.keys(SEA).forEach(function(k){ var o=document.createElement('option'); o.value=k; o.textContent=SEA[k]; $('#sea').appendChild(o); });
var chips=[{code:'',lab:'All systems'}].concat(BP.systems.map(function(s){return {code:s.code,lab:SHORT[s.code]};}));
$('#sys-chips').innerHTML=chips.map(function(s){return '<li><button type="button" class="chip-btn" data-sys="'+s.code+'" aria-pressed="'+(s.code===''?'true':'false')+'">'+esc(s.lab)+'</button></li>';}).join('');
$('#sys-chips').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;state.sys=b.dataset.sys;
  document.querySelectorAll('#sys-chips button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false');});render();});
$('#q').addEventListener('input',function(){state.q=this.value.trim().toLowerCase();render();});
$('#sea').addEventListener('change',function(){state.sea=this.value;render();});
$('#srcf').addEventListener('change',function(){state.src=this.value;render();});

function objOk(o){
  if(state.sea && o.sea!==state.sea) return false;
  if(state.src && o.src!==state.src) return false;
  if(state.q && (o.id+' '+o.t+' '+(o.usmle||'')).toLowerCase().indexOf(state.q)<0) return false;
  return true;
}
function unitHead(c){
  var h='<div class="unit-top"><div class="code">'+esc(c.code)+'</div><div><div class="uname">'+esc(c.name)+'</div>';
  if(c.kind==='conditions') h+='<ul class="conds">'+c.conditions.map(function(x){return '<li><span class="c">'+esc(x.code.slice(c.code.length))+'</span>'+esc(x.name)+'</li>';}).join('')+'</ul>';
  else h+='<p class="stmt">'+esc(c.can)+'</p>';
  return h+'</div></div>';
}
function objLi(o){
  return '<li class="obj" id="o-'+esc(o.id)+'"><span class="oid">'+esc(o.id)+'</span><div><span class="ot">'+esc(o.t)+'</span>'+
    '<span class="otags"><span class="src s-'+o.src+'">'+SRC[o.src]+'</span><span class="tag">'+esc(SEA[o.sea])+'</span><span class="tag">DOK '+o.dok+'</span></span></div></li>';
}
function render(){
  var out='', nu=0, no=0, filtered=state.q||state.sea||state.src||state.sys;
  BP.systems.forEach(function(s){
    if(state.sys && state.sys!==s.code) return;
    var units=C.filter(function(c){return c.systemCode===s.code;}), body={comp:'',cond:''}, any=false;
    units.forEach(function(c){
      var objs=(c.objectives||[]).filter(objOk);
      var headHit = state.q && !state.sea && !state.src && (c.code+' '+c.name+' '+c.can+' '+(c.conditions||[]).map(function(x){return x.code+' '+x.name;}).join(' ')).toLowerCase().indexOf(state.q)>=0;
      if(headHit) objs=(c.objectives||[]);
      if(filtered && !objs.length) return;
      any=true; nu++; no+=objs.length;
      body[c.kind==='conditions'?'cond':'comp']+='<div class="unit">'+unitHead(c)+(objs.length?'<ol class="objs" aria-label="Competencies for '+esc(c.code)+'">'+objs.map(objLi).join('')+'</ol>':'')+'</div>';
    });
    if(!any) return;
    out+='<section class="card sys" id="sys-'+s.code+'" aria-labelledby="h-'+s.code+'"><div class="sys-head"><h2 id="h-'+s.code+'">'+esc(SHORT[s.code])+'<span class="full">'+esc(s.full)+'</span></h2>'+
      '<span class="meta">'+s.weight+'% · '+s.items+' questions · Week '+s.week+'</span></div>';
    if(body.comp) out+='<h3 class="group">How the body works</h3>'+body.comp;
    if(body.cond) out+='<h3 class="group">Diseases and conditions</h3>'+body.cond;
    out+='</section>';
  });
  $('#list').innerHTML=out||'<div class="card empty">Nothing matches. Clear the search or pick All systems.</div>';
  $('#status').textContent = filtered ? ('Showing '+no.toLocaleString()+' competencies in '+nu+' units.') : (totalObj.toLocaleString()+' competencies across '+C.length+' units in 11 systems.');
  postH();
}
render();

var cw='';
BP.systems.forEach(function(s){
  var rows=CW.filter(function(x){return x.system===s.code;}), ex=EX.filter(function(x){return x.system===s.code;});
  if(!rows.length && !ex.length) return;
  var t='<div class="tablebox" role="region" tabindex="0" aria-label="'+esc(SHORT[s.code])+' crosswalk (scrolls sideways)"><table><thead><tr><th scope="col">USMLE Step 1 topic</th><th scope="col">Where in this course</th><th scope="col">Note</th></tr></thead><tbody>'+
    rows.map(function(x){ var w=x.where==='excluded'?'Excluded':'<a href="#o-'+esc(x.where)+'">'+esc(x.where)+'</a>'; return '<tr><td>'+esc(x.usmle)+'</td><td>'+w+'</td><td>'+esc(x.note||'')+'</td></tr>'; }).join('')+
    ex.map(function(x){ return '<tr><td>'+esc(x.usmle)+'</td><td>Excluded</td><td>'+esc(x.reason||'')+'</td></tr>'; }).join('')+'</tbody></table></div>';
  cw+='<details class="cw" data-sys="'+s.code+'"><summary>'+esc(SHORT[s.code])+'<span class="meta">'+rows.filter(function(x){return x.where!=='excluded';}).length+' mapped · '+(ex.length+rows.filter(function(x){return x.where==='excluded';}).length)+' excluded</span></summary>'+t+'</details>';
});
$('#cw-list').innerHTML=cw;
document.addEventListener('click',function(e){ var a=e.target.closest('a[href^="#o-"]'); if(!a) return;
  state.q='';state.sea='';state.src='';state.sys=''; $('#q').value=''; $('#sea').value=''; $('#srcf').value='';
  document.querySelectorAll('#sys-chips button').forEach(function(x){x.setAttribute('aria-pressed',x.dataset.sys===''?'true':'false');}); render(); });
window.addEventListener('beforeprint',function(){ document.querySelectorAll('details.cw').forEach(function(d){d.open=true;}); });
function postH(){ try{ parent.postMessage({id:'nplex-competencies',height:document.documentElement.scrollHeight},'*'); }catch(e){} }
window.addEventListener('load',postH); window.addEventListener('resize',postH);
document.addEventListener('toggle',postH,true);
if(window.ResizeObserver){ new ResizeObserver(postH).observe(document.body); }
})();
</script>
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap">'


def main(out):
    bp, comps, cw, ex = load()
    script = (SCRIPT.replace("__BP__", json.dumps(bp, ensure_ascii=False))
                    .replace("__C__", json.dumps(comps, ensure_ascii=False))
                    .replace("__CW__", json.dumps(cw, ensure_ascii=False))
                    .replace("__EX__", json.dumps(ex, ensure_ascii=False)))
    meta = '<meta name="description" content="NPLEX Part I competencies by body system, built on the NABNE blueprint and written to USMLE Step 1 depth, with a USMLE crosswalk.">'
    inner = f"<title>{TITLE}</title>\n{meta}\n{FONTS}\n{STYLE}\n{BODY}\n{script}"
    full = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
            f"<title>{TITLE}</title>\n{meta}\n{FONTS}\n{STYLE}\n</head>\n<body>\n{BODY}\n{script}\n</body>\n</html>\n")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "nplex-competencies.html"), "w", encoding="utf-8").write(full)
    open(os.path.join(out, "nplex-competencies-artifact.html"), "w", encoding="utf-8").write(inner)

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto("file://" + os.path.abspath(os.path.join(out, "nplex-competencies.html")), wait_until="load", timeout=30000)
        pg.emulate_media(media="print", color_scheme="light")
        pg.evaluate("document.querySelectorAll('details.cw').forEach(function(d){d.open=true;})")
        pg.wait_for_timeout(600)
        pg.pdf(path=os.path.join(out, "NPLEX-Part-I-Competencies.pdf"), format="Letter", print_background=True,
               display_header_footer=True, header_template="<div></div>",
               footer_template="<div style='width:100%;font-size:8pt;color:#4F576A;padding:0 0.6in;display:flex;justify-content:space-between;font-family:Plus Jakarta Sans,sans-serif'><span>NPLEX Part I Competencies · NABNE blueprint (Mar 2026) with USMLE Step 1 depth</span><span><span class='pageNumber'></span> / <span class='totalPages'></span></span></div>",
               margin={"top": "0.55in", "bottom": "0.7in", "left": "0.6in", "right": "0.6in"})
        b.close()
    print("ok")


if __name__ == "__main__":
    main(sys.argv[1])
