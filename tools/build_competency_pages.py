"""Build the NPLEX competency viewer (HTML) and PDF from blueprint_data.py.

Usage: python3 build_competency_pages.py <out_dir>
Writes:
  nplex-competencies.html          full page for the repo / GitHub Pages
  nplex-competencies-artifact.html same page without the document wrapper (for Artifact publish)
  NPLEX-Part-I-Competencies.pdf    print version
"""
import json, os, sys
from build_competencies import build, blueprint_obj
from blueprint_data import SYSTEMS

TITLE = "NPLEX Part I Competencies"

STYLE = r"""
<style>
/* Layout: one reading column; a system weight table, then one white card per body system.
   Primary teaching palette: white cards on off-white, navy text, terra eyebrow, gold accents. */
:root{
  --bg:#FAFAF9; --card:#FFFFFF; --ink:#1E3D4C; --ink-deep:#142a36; --soft:#4A6170;
  --terra:#A0522D; --gold:#B8924A; --line:#D7DFE3; --tint:#EDF1F3;
  --shadow:0 1px 3px rgba(0,0,0,.08); --shadow-hover:0 8px 16px rgba(0,0,0,.10);
  --display:"Plus Jakarta Sans", "Segoe UI", system-ui, sans-serif;
  --body:"DM Sans", "Segoe UI", system-ui, sans-serif;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#0F1D25; --card:#16303D; --ink:#E6EDF1; --ink-deep:#FFFFFF; --soft:#B4C3CC;
  --terra:#E9A07C; --gold:#D6B57A; --line:#2B4655; --tint:#1D3A49;
  --shadow:0 1px 3px rgba(0,0,0,.4); --shadow-hover:0 8px 16px rgba(0,0,0,.45); color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#0F1D25; --card:#16303D; --ink:#E6EDF1; --ink-deep:#FFFFFF; --soft:#B4C3CC;
  --terra:#E9A07C; --gold:#D6B57A; --line:#2B4655; --tint:#1D3A49;
  --shadow:0 1px 3px rgba(0,0,0,.4); --shadow-hover:0 8px 16px rgba(0,0,0,.45); color-scheme:dark}

*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:15px;line-height:1.55;margin:0}
.wrap{max-width:1040px;margin:0 auto;padding-inline:16px;padding-block:28px 56px}
.skip{position:absolute;left:-9999px;top:8px;background:var(--card);color:var(--ink);padding:8px 12px;border:1px solid var(--ink);border-radius:6px;z-index:10}
.skip:focus{left:16px}
:focus-visible{outline:3px solid var(--gold);outline-offset:2px;border-radius:4px}
h1,h2,h3{font-family:var(--display);text-wrap:balance;margin:0}
.eyebrow{font-family:var(--body);font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--terra);margin:0 0 6px}
h1{font-weight:800;font-size:clamp(1.8rem,4.5vw,2.6rem);line-height:1.1;color:var(--ink)}
.sub{font-family:var(--display);font-weight:600;color:var(--terra);font-size:1.1rem;margin:8px 0 0}
.lede{max-width:68ch;color:var(--soft);margin:14px 0 0}
header{display:grid;gap:4px;margin-bottom:24px}

.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:0 0 24px;padding:0;list-style:none}
.facts li{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px;box-shadow:var(--shadow)}
.facts b{display:block;font-family:var(--display);font-size:1.5rem;font-weight:800;font-variant-numeric:tabular-nums;color:var(--ink)}
.facts span{font-size:13px;color:var(--soft)}

.panel{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;box-shadow:var(--shadow);margin-bottom:24px}
.panel h2{font-size:1.15rem;font-weight:600;color:var(--terra);margin-bottom:10px}
.tablebox{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums;font-size:14px}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);white-space:nowrap}
thead th{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--soft);font-weight:700}
tbody th{font-weight:600;color:var(--ink);white-space:normal;min-width:12rem}
td.num,th.num{text-align:right}
tbody tr:last-child td{border-bottom:0}
.gea{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-top:14px}
.gea p{margin:0;font-size:14px;color:var(--soft)}
.gea strong{color:var(--ink)}

.controls{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end;margin:0 0 10px}
.field{display:grid;gap:4px;min-width:0;flex:1 1 220px}
.field label{font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--soft)}
input[type=search],select{font:inherit;color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:8px;padding:9px 11px;width:100%}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 18px;padding:0;list-style:none}
.chip-btn{font:inherit;font-size:13px;font-weight:600;color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:999px;padding:5px 12px;cursor:pointer;transition:border-color 150ms ease}
.chip-btn:hover{border-color:var(--ink)}
.chip-btn[aria-pressed="true"]{border-color:var(--ink);background:var(--tint)}
.status{font-size:13px;color:var(--soft);margin:0 0 14px}

.sys{background:var(--card);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow);padding:20px;margin-bottom:20px;transition:transform 200ms ease,box-shadow 200ms ease}
.sys:hover{transform:translateY(-2px);box-shadow:var(--shadow-hover)}
.sys-head{display:flex;flex-wrap:wrap;gap:6px 16px;align-items:baseline;justify-content:space-between;margin-bottom:12px}
.sys-head h2{font-size:1.45rem;font-weight:800;color:var(--ink)}
.meta{font-size:13px;color:var(--soft);font-variant-numeric:tabular-nums}
h3.group{font-size:12px;font-family:var(--body);font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--terra);margin:16px 0 6px}
ul.comps{list-style:none;margin:0;padding:0}
.comp{display:grid;grid-template-columns:5.2rem minmax(0,1fr);gap:4px 12px;padding:10px 0;border-top:1px solid var(--line)}
.code{font-family:var(--display);font-weight:700;font-size:13px;color:var(--ink);font-variant-numeric:tabular-nums;padding-top:1px}
.name{font-weight:700;color:var(--ink)}
.stmt{margin:2px 0 6px;color:var(--soft);font-size:14px;max-width:72ch}
.tags{display:flex;flex-wrap:wrap;gap:5px}
.tag{font-size:11.5px;font-weight:600;border:1px solid var(--line);border-radius:999px;padding:1px 9px;color:var(--soft)}
.tag.nd{border-color:var(--gold);color:var(--terra)}
.conds{display:flex;flex-wrap:wrap;gap:4px 14px;margin:2px 0 6px;padding:0;list-style:none;font-size:14px}
.conds li{min-width:0}
.conds .c{font-variant-numeric:tabular-nums;color:var(--soft);font-size:12.5px;margin-right:5px}
.empty{padding:24px;text-align:center;color:var(--soft)}
.notes{font-size:14px;color:var(--soft)}
.notes p{margin:0 0 8px;max-width:72ch}
.notes p:last-child{margin-bottom:0}
footer{margin-top:28px;font-size:13px;color:var(--soft)}
footer a,.notes a{color:var(--ink)}
@media (prefers-reduced-motion: reduce){*{transition:none!important}.sys:hover{transform:none}}
@media (max-width:520px){.comp{grid-template-columns:1fr}.code{padding-top:0}}

@page{size:Letter;margin:0.55in 0.6in}
@media print{
  :root{--bg:#FFFFFF}
  body{font-size:10.5pt}
  .wrap{max-width:none;padding:0}
  .skip,.controls,.chips,.status{display:none!important}
  .sys,.panel,.facts li{box-shadow:none}
  .sys{break-before:page;border:0;padding:0}
  .sys:hover{transform:none}
  .comp{break-inside:avoid}
  h3.group{break-after:avoid}
  .panel{break-inside:auto;padding:12px 0;border:0}
  tr{break-inside:avoid}
  .tablebox{overflow:visible}
  table{font-size:9.5pt}
  th,td{padding:5px 6px}
  thead th{font-size:8pt;white-space:normal}
  .facts{margin-bottom:12px}
  .comp{padding:6px 0}
  .stmt{margin:1px 0 4px}
  .sys-head{margin-bottom:6px}
}
</style>
"""

BODY = r"""
<a class="skip" href="#list">Skip to the competency list</a>
<div class="wrap">
<header>
  <p class="eyebrow">NPLEX Part I &middot; Board Review &middot; MedMasters Collaborative</p>
  <h1>NPLEX Part I Competencies</h1>
  <p class="sub">Biomedical Science Examination blueprint</p>
  <p class="lede">Every competency and condition on the NABNE blueprint, grouped by body system. Each one has a code you can tag questions with and track in spaced recall.</p>
</header>

<main id="main">
<ul class="facts" aria-label="Exam format">
  <li><b>200</b><span>questions, four options each</span></li>
  <li><b>50</b><span>cases with four questions each</span></li>
  <li><b>2 &times; 2.5 h</b><span>two sessions of 100, same day</span></li>
  <li><b>60 / 40</b><span>Structure/Function vs Disease/Dysfunction</span></li>
</ul>

<section class="panel" aria-labelledby="wt-h">
  <h2 id="wt-h">Weighting by body system</h2>
  <div class="tablebox">
  <table>
    <thead><tr><th scope="col">System</th><th scope="col" class="num">Exam %</th><th scope="col" class="num">Questions</th><th scope="col" class="num">Cases</th><th scope="col" class="num">Competencies</th><th scope="col" class="num">Conditions</th><th scope="col" class="num">Course week</th></tr></thead>
    <tbody id="wt-body"></tbody>
  </table>
  </div>
  <div class="gea">
    <p><strong>Structure/Function (60%)</strong>: Anatomy, Physiology, and Biochemistry &amp; Genetics, about 40 questions each.</p>
    <p><strong>Disease/Dysfunction (40%)</strong>: Microbiology &amp; Immunology and Pathology, about 40 questions each. You must pass both areas; failing either means retaking the whole exam.</p>
  </div>
</section>

<div class="controls">
  <div class="field"><label for="q">Search</label><input type="search" id="q" placeholder="Try MI, thiamine, Graves, CV-18-C" autocomplete="off"></div>
  <div class="field"><label for="sea">Exam area</label>
    <select id="sea"><option value="">All exam areas</option></select></div>
  <div class="field"><label for="nd">Emphasis</label>
    <select id="nd"><option value="">Everything</option><option value="1">ND emphasis only</option></select></div>
</div>
<ul class="chips" id="sys-chips" aria-label="Filter by body system"></ul>
<p class="status" id="status" aria-live="polite"></p>

<div id="list"></div>

<section class="panel notes" aria-labelledby="notes-h">
  <h2 id="notes-h">About this list</h2>
  <p><strong>Source.</strong> NABNE, NPLEX Part I Biomedical Sciences Study Guide, revised March 2026, for the August 2026 administrations. <a href="https://www.nabne.org/pdf/NPLEX-Part-I-Biomedical-Sciences-Study-Guide-08-2026.pdf" target="_blank" rel="noopener">Open the study guide</a>.</p>
  <p><strong>Codes.</strong> System, competency number, category letter, condition number. CV-18-C3 is myocardial infarction: Cardiovascular competency 18, category C (ischemic heart disease), condition 3.</p>
  <p><strong>Added by us, not NABNE.</strong> The short names, the exam-area tags on each competency, the ND emphasis tag, and the course week. NABNE does not assign exam areas to competencies, so the tags show the usual fit; each question carries its own exam area. ND emphasis marks nutrition biochemistry, antioxidants, detoxification, exercise, and deficiency states.</p>
</section>
</main>

<footer>MedMasters Collaborative &middot; Dr. Sharilyn Rennie</footer>
</div>
"""

SCRIPT = r"""
<script>
(function(){
var BP=__BP__, C=__C__;
var SEA_ORDER=["Anatomy","Physiology","Biochemistry & Genetics","Microbiology & Immunology","Pathology"];
var SEA_BY_CODE={A:"Anatomy",P:"Physiology",B:"Biochemistry & Genetics",M:"Microbiology & Immunology",X:"Pathology"};
var state={q:"",sea:"",nd:"",sys:""};
function $(s){return document.querySelector(s);}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}

/* weight table */
var tb="",tot={q:0,c:0,k:0,n:0};
BP.systems.forEach(function(s){
  var mine=C.filter(function(c){return c.systemCode===s.code;});
  var k=mine.filter(function(c){return c.kind==="competency";}).length+1; /* +1: the conditions list is itself a numbered competency */
  var n=mine.reduce(function(a,c){return a+(c.conditions?c.conditions.length:0);},0);
  tot.q+=s.items;tot.c+=s.cases;tot.k+=k;tot.n+=n;
  tb+="<tr><th scope=\"row\">"+esc(s.full)+"</th><td class=\"num\">"+s.weight+"%</td><td class=\"num\">"+s.items+"</td><td class=\"num\">"+s.cases+"</td><td class=\"num\">"+k+"</td><td class=\"num\">"+n+"</td><td class=\"num\">"+s.week+"</td></tr>";
});
tb+="<tr><th scope=\"row\">Total</th><td class=\"num\">100%</td><td class=\"num\">"+tot.q+"</td><td class=\"num\">"+tot.c+"</td><td class=\"num\">"+tot.k+"</td><td class=\"num\">"+tot.n+"</td><td></td></tr>";
$("#wt-body").innerHTML=tb;

/* filters */
SEA_ORDER.forEach(function(s){var o=document.createElement("option");o.value=s;o.textContent=s;$("#sea").appendChild(o);});
var chips=[{code:"",name:"All systems"}].concat(BP.systems);
$("#sys-chips").innerHTML=chips.map(function(s){return "<li><button type=\"button\" class=\"chip-btn\" data-sys=\""+s.code+"\" aria-pressed=\""+(s.code===""?"true":"false")+"\">"+esc(s.name)+"</button></li>";}).join("");
$("#sys-chips").addEventListener("click",function(e){var b=e.target.closest("button");if(!b)return;state.sys=b.dataset.sys;
  document.querySelectorAll("#sys-chips button").forEach(function(x){x.setAttribute("aria-pressed",x===b?"true":"false");});render();});
$("#q").addEventListener("input",function(){state.q=this.value.trim().toLowerCase();render();});
$("#sea").addEventListener("change",function(){state.sea=this.value;render();});
$("#nd").addEventListener("change",function(){state.nd=this.value;render();});

function matches(c){
  if(state.sys&&c.systemCode!==state.sys)return false;
  if(state.nd&&!c.nd)return false;
  if(state.sea&&c.seaCodes.map(function(x){return SEA_BY_CODE[x];}).indexOf(state.sea)<0)return false;
  if(state.q){var hay=(c.code+" "+c.name+" "+c.can+" "+(c.conditions||[]).map(function(x){return x.code+" "+x.name;}).join(" ")).toLowerCase();
    if(hay.indexOf(state.q)<0)return false;}
  return true;
}
function tags(c){
  var t=c.seaCodes.map(function(x){return "<span class=\"tag\">"+esc(SEA_BY_CODE[x])+"</span>";}).join("");
  if(c.nd)t+="<span class=\"tag nd\">ND emphasis</span>";
  return "<div class=\"tags\">"+t+"</div>";
}
function row(c){
  var h="<li class=\"comp\"><div class=\"code\">"+esc(c.code)+"</div><div>";
  h+="<div class=\"name\">"+esc(c.name)+"</div>";
  if(c.kind==="conditions"){
    h+="<ul class=\"conds\">"+c.conditions.map(function(x){return "<li><span class=\"c\">"+esc(x.code.slice(c.code.length))+"</span>"+esc(x.name)+"</li>";}).join("")+"</ul>";
  }else{
    h+="<p class=\"stmt\">"+esc(c.can)+"</p>";
  }
  return h+tags(c)+"</div></li>";
}
function render(){
  var out="",shownK=0,shownSys=0;
  BP.systems.forEach(function(s){
    var mine=C.filter(function(c){return c.systemCode===s.code&&matches(c);});
    if(!mine.length)return;
    shownSys++;shownK+=mine.length;
    var comps=mine.filter(function(c){return c.kind==="competency";});
    var conds=mine.filter(function(c){return c.kind==="conditions";});
    out+="<section class=\"sys\" id=\"sys-"+s.code+"\" aria-labelledby=\"h-"+s.code+"\"><div class=\"sys-head\"><h2 id=\"h-"+s.code+"\">"+esc(s.full)+"</h2>";
    out+="<span class=\"meta\">"+s.weight+"% &middot; "+s.items+" questions &middot; "+s.cases+" cases &middot; Week "+s.week+", reinforced Week "+s.reinforce+"</span></div>";
    if(comps.length)out+="<h3 class=\"group\">Competencies</h3><ul class=\"comps\">"+comps.map(row).join("")+"</ul>";
    if(conds.length){var n=conds[0].num;out+="<h3 class=\"group\">Competency "+n+": conditions (pathogenesis, etiology, risk factors, complications, clinical features)</h3><ul class=\"comps\">"+conds.map(row).join("")+"</ul>";}
    out+="</section>";
  });
  $("#list").innerHTML=out||"<p class=\"empty\">Nothing matches. Clear the search or pick All systems.</p>";
  var filtered=state.q||state.sea||state.nd||state.sys;
  $("#status").textContent=filtered?("Showing "+shownK+" of "+C.length+" study units in "+shownSys+" system"+(shownSys===1?"":"s")+"."):(C.length+" study units across 11 systems.");
}
render();
})();
</script>
"""

HEIGHT = r"""
<script>
(function(){
  var id='nplex-competencies';
  function send(){try{parent.postMessage({id:id,height:document.documentElement.scrollHeight},'*');}catch(e){}}
  window.addEventListener('load',send);
  window.addEventListener('resize',send);
  if(window.ResizeObserver){new ResizeObserver(send).observe(document.body);}
})();
</script>
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap">'


def main(out):
    comps, _ = build()
    bp = blueprint_obj()
    script = SCRIPT.replace("__BP__", json.dumps(bp, ensure_ascii=False)).replace("__C__", json.dumps(comps, ensure_ascii=False))
    inner = f"<title>{TITLE}</title>\n{FONTS}\n{STYLE}\n{BODY}\n{script}\n{HEIGHT}"
    full = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
            f"<title>{TITLE}</title>\n{FONTS}\n{STYLE}\n</head>\n<body>\n{BODY}\n{script}\n{HEIGHT}\n</body>\n</html>\n")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "nplex-competencies.html"), "w", encoding="utf-8") as f:
        f.write(full)
    with open(os.path.join(out, "nplex-competencies-artifact.html"), "w", encoding="utf-8") as f:
        f.write(inner)

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto("file://" + os.path.abspath(os.path.join(out, "nplex-competencies.html")), wait_until="load", timeout=20000)
        pg.emulate_media(media="print", color_scheme="light")
        pg.wait_for_timeout(400)
        pg.pdf(path=os.path.join(out, "NPLEX-Part-I-Competencies.pdf"), format="Letter", print_background=True,
               display_header_footer=True,
               header_template="<div></div>",
               footer_template="<div style='width:100%;font-size:8pt;color:#4A6170;padding:0 0.6in;display:flex;justify-content:space-between;font-family:DM Sans,sans-serif'><span>NPLEX Part I Competencies &middot; NABNE study guide, revised March 2026</span><span><span class='pageNumber'></span> / <span class='totalPages'></span></span></div>",
               margin={"top": "0.55in", "bottom": "0.7in", "left": "0.6in", "right": "0.6in"})
        b.close()
    print("ok")


if __name__ == "__main__":
    main(sys.argv[1])
