"""Agentic Memory Architecture: /agentic-memory-architecture/, one page under Research.

How Praxis keeps memory, told as Michael Levin's bow tie (Self-Improvising Memory, Entropy 2024).
Architecture only, by Umar's ruling of 23 Oct 2026: no counts from Engram, never the word
"rows" (say entries or learnings), no prompts, judges, scoring or thresholds. Memo shell, light.
    python tools/memory_page.py     # site_index.py runs it; seo.py runs last
"""
import html, json, re
from pathlib import Path
import brand, blog, memos

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://codeatoms.ai"
SLUG = "agentic-memory-architecture"
OUT = ROOT / SLUG
E = lambda s: html.escape(str(s), quote=True)

TITLE = "Agentic Memory Architecture"
SUB = "How Praxis keeps what it learns outside the model, so the reasoning can be replaced and the memory stands."
DESC = ("How CodeNinja built agentic memory for Praxis on Engram: Michael Levin's bow tie model of memory, "
        "the left wing of experience, the waist of nightly distillation and commissioning, the right wing where each "
        "design assembles its own context, and the reinforcement loop that changes memory and never weights.")
DATE = "2026-10-23"
LEVIN = "https://www.mdpi.com/1099-4300/26/6/481"

CSS = """
.memo .body h2{max-width:none}
.memo .body .tw{overflow-x:auto;margin:30px 0}
.memo .body table{width:100%;border-collapse:collapse;font-size:16px;line-height:1.5}
.memo .body th{text-align:left;font-weight:500;color:var(--ink);padding:10px 14px 10px 0;border-bottom:1px solid var(--ink);vertical-align:bottom}
.memo .body td{padding:12px 14px 12px 0;border-bottom:1px solid var(--rule-l);vertical-align:top}
.memo .body td:first-child,.memo .body th:first-child{white-space:nowrap;color:var(--ink);font-weight:500;width:9em}
.memo .body pre{background:var(--ink);color:var(--on-dark);font:400 13.5px/1.7 var(--mono);padding:26px 28px;margin:30px 0;overflow-x:auto;border-radius:0}
.memo .body pre .c{color:var(--muted-d)}
.memo .body figure{margin:48px 0}
.memo .body figcaption{margin-top:14px;font-size:14.5px;color:var(--muted-l);line-height:1.5}
.memo .body ol{counter-reset:n;list-style:none;padding-left:0}.memo .body ol li{counter-increment:n;padding-left:2.2em;position:relative}
.memo .body ol li::before{content:counter(n);position:absolute;left:0;top:.1em;font-family:var(--mono);font-size:12px;color:var(--muted-l)}
.memo .body .next{margin:56px 0 0;padding-top:24px;border-top:1px solid var(--ink);font-size:15px}.memo .body .next a{color:var(--ink)}
"""


def p(s):
    return f"<p>{blog.inline(s)}</p>"


def figure():
    """The bow tie as a live panel: the shape in the site's own hand, and a small script that runs the
    night routines and one birth across it in a loop, with a console log beneath. Still a readable
    diagram with JavaScript off or reduced motion on."""
    ink, mute, red, on = "#F2F2F0", "#A3A6AE", "#E31E30", "#D9C3A3"
    f = 'font-family="Inter Tight,Helvetica Neue,Arial,sans-serif"'
    m = 'font-family="Geist Mono,Menlo,monospace" font-size="13" letter-spacing=".06em"'
    return f"""<figure class="live" id="bowtie"><div class="panel">
<div class="bar"><span class="dot"></span><span class="ttl">PRAXIS MEMORY · LIVE</span><span class="phase" id="bt-phase">THE BOW TIE</span><span class="clk" id="bt-clock"></span></div>
<svg viewBox="0 0 1200 560" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="bt-title">
<title id="bt-title">The bow tie: experience on the left, distillation and commissioning at the waist, the room and the design on the right, reinforcement returning to the left</title>
<defs><clipPath id="bt-l"><path d="M120 90 L590 230 L590 290 L120 430 Z"/></clipPath><clipPath id="bt-r"><path d="M1080 90 L610 230 L610 290 L1080 430 Z"/></clipPath></defs>
<path id="bt-wl" d="M120 90 L590 230 L590 290 L120 430 Z" fill="rgba(255,255,255,.025)" stroke="{ink}" stroke-width="1.1"/>
<path id="bt-wr" d="M1080 90 L610 230 L610 290 L1080 430 Z" fill="rgba(255,255,255,.025)" stroke="{ink}" stroke-width="1.1"/>
<rect id="bt-waist" x="590" y="230" width="20" height="60" fill="{ink}"/>
<line id="bt-door" x1="150" y1="104" x2="150" y2="416" stroke="{on}" stroke-width="1" stroke-dasharray="3 4" opacity=".55"/>
<text x="120" y="62" {m} fill="{mute}">LEFT WING · EXPERIENCE</text>
<text x="1080" y="62" {m} fill="{mute}" text-anchor="end">RIGHT WING · THE PRESENT</text>
<text x="600" y="62" {m} fill="{mute}" text-anchor="middle">THE WAIST · COMPRESSION</text>
<text x="150" y="84" {m} fill="{on}" opacity=".8">THE DOOR</text>
<g {f} font-size="23" fill="{ink}">
<text x="170" y="190">Reference</text><text x="170" y="250">Learnings</text><text x="170" y="310">Episodes</text><text x="170" y="370">Asks</text>
</g>
<g {f} font-size="15" fill="{mute}">
<text x="170" y="211">sourced, dated, with an honesty line</text><text x="170" y="271">raw sentences of domain knowledge</text>
<text x="170" y="331">every design, its measure, its feedback</text><text x="170" y="391">what a design needed and memory lacked</text>
</g>
<g {f} font-size="19" fill="{ink}" text-anchor="middle">
<text id="bt-dist" x="600" y="180">Distillation</text><text id="bt-comm" x="600" y="340">Commissioning</text>
</g>
<g {f} font-size="14" fill="{mute}" text-anchor="middle">
<text x="600" y="202">learnings become briefs</text><text x="600" y="362">misses become sourced entries</text>
</g>
<rect id="bt-room" x="740" y="190" width="300" height="64" fill="none" stroke="{mute}" stroke-width="1" stroke-dasharray="3 4" opacity=".5"/>
<g {f} font-size="23" fill="{ink}">
<text x="760" y="218">The room</text><text id="bt-design-t" x="760" y="312">The design</text>
</g>
<g {f} font-size="15" fill="{mute}">
<text x="760" y="240">context assembled for one requirement</text><text x="760" y="334">architecture, scope ledger, contract</text>
</g>
<rect id="bt-design" x="740" y="286" width="300" height="62" fill="none" stroke="{ink}" stroke-width="1" opacity="0"/>
<path id="bt-ret" d="M1000 478 C1000 540 200 540 200 478" fill="none" stroke="{red}" stroke-width="1.3" stroke-dasharray="4 5" opacity=".8"/>
<path d="M206 486 L198 474 L212 476 Z" fill="{red}"/>
<text x="600" y="536" {m} fill="{red}" text-anchor="middle">REINFORCEMENT · LESSONS, OUTCOMES AND ASKS RETURN AS EXPERIENCE</text>
<text x="120" y="470" {m} fill="{mute}">THE HIGH DIMENSIONAL PAST</text>
<text x="1080" y="470" {m} fill="{mute}" text-anchor="end">A READER THE WRITER NEVER MET</text>
<g id="bt-dots"></g>
</svg>
<ol class="log" id="bt-log" aria-live="off"></ol>
</div><figcaption>Figure 1. Memory in Praxis as a bow tie, running. Entries pass the door into the left wing. Two nightly routines compress them at the waist. A requirement arrives on the right, a room is assembled, a design is written and judged, and what it learns returns along the red path as new experience. The log is illustrative: generic entries, no customer, no real record.</figcaption></figure>"""


LIVE_CSS = """
.memo figure.live{margin:40px 0 56px}
.memo .panel{background:#0B0C10;border:1px solid rgba(255,255,255,.14);padding:0 0 6px}
.memo .panel .bar{display:flex;align-items:center;gap:12px;padding:11px 16px;border-bottom:1px solid rgba(255,255,255,.12);font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:#A3A6AE}
.memo .panel .bar .dot{width:7px;height:7px;border-radius:50%;background:#E31E30;box-shadow:0 0 0 0 rgba(227,30,48,.5);animation:btp 1.6s infinite}
@keyframes btp{0%{box-shadow:0 0 0 0 rgba(227,30,48,.5)}70%{box-shadow:0 0 0 7px rgba(227,30,48,0)}100%{box-shadow:0 0 0 0 rgba(227,30,48,0)}}
.memo .panel .bar .ttl{color:#D9C3A3}.memo .panel .bar .phase{margin-left:auto;color:#F2F2F0}.memo .panel .bar .clk{font-variant-numeric:tabular-nums}
.memo .panel svg{display:block;width:100%;height:auto;padding:8px 10px 0}
.memo .panel svg #bt-waist{transition:fill .3s}.memo .panel svg .hot{fill:#D9C3A3}
.memo .panel svg #bt-dist,.memo .panel svg #bt-comm,.memo .panel svg #bt-design-t{transition:fill .3s}.memo .panel svg text.on{fill:#D9C3A3}
.memo .panel svg #bt-room{transition:stroke .3s,opacity .3s}.memo .panel svg #bt-room.on{stroke:#D9C3A3;opacity:1}
.memo .panel svg #bt-design{transition:opacity .4s}
.memo .panel .log{list-style:none;margin:0;padding:10px 16px 8px;border-top:1px solid rgba(255,255,255,.12);height:9.6em;overflow:hidden;font-family:var(--mono);font-size:12.5px;line-height:1.6;color:#A3A6AE}
.memo .panel .log li{margin:0;padding-left:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;animation:btin .25s ease-out}
.memo .panel .log li b{font-weight:400;color:#D9C3A3;display:inline-block;width:7.5em}.memo .panel .log li i{font-style:normal;color:#F2F2F0}
.memo .panel .log li.no b{color:#E31E30}.memo .panel .log li .t{color:#666874;margin-right:10px}
.memo .body .panel .log li::before{content:none}
@keyframes btin{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
@media (max-width:640px){.memo .panel .log{font-size:11px;height:8.8em}.memo .panel .bar{flex-wrap:wrap;gap:8px 12px;font-size:10px}.memo .panel .bar .phase{margin-left:0;width:100%;order:3}.memo .panel .bar .clk{margin-left:auto}}
@media (prefers-reduced-motion:reduce){.memo .panel .bar .dot{animation:none}.memo .panel .log li{animation:none}}
"""

LIVE_JS = r"""<script>(function(){
var svg=document.querySelector('#bowtie svg');if(!svg)return;
var still=matchMedia('(prefers-reduced-motion: reduce)').matches;
var NS='http://www.w3.org/2000/svg',dots=document.getElementById('bt-dots'),log=document.getElementById('bt-log'),phase=document.getElementById('bt-phase'),clk=document.getElementById('bt-clock');
var waist=document.getElementById('bt-waist'),room=document.getElementById('bt-room'),design=document.getElementById('bt-design'),ret=document.getElementById('bt-ret'),RL=ret.getTotalLength();
var dist=document.getElementById('bt-dist'),comm=document.getElementById('bt-comm'),dtext=document.getElementById('bt-design-t');
function pad(n){return (n<10?'0':'')+n}
function tick(){var d=new Date();clk.textContent=pad(d.getHours())+':'+pad(d.getMinutes())+':'+pad(d.getSeconds())}tick();setInterval(tick,1000);
function say(k,t,no){var li=document.createElement('li');if(no)li.className='no';var d=new Date();li.innerHTML='<span class="t">'+pad(d.getHours())+':'+pad(d.getMinutes())+':'+pad(d.getSeconds())+'</span><b>'+k+'</b><i>'+t+'</i>';log.appendChild(li);while(log.children.length>6)log.removeChild(log.firstChild)}
function P(s){phase.textContent=s}
var live=[];function dot(x,y,c,r){var e=document.createElementNS(NS,'circle');e.setAttribute('r',r||4);e.setAttribute('fill',c||'#F2F2F0');e.setAttribute('cx',x);e.setAttribute('cy',y);dots.appendChild(e);return e}
function go(e,x1,y1,x2,y2,ms,done){var t0=performance.now();(function f(n){var k=Math.min(1,(n-t0)/ms),s=k<.5?2*k*k:-1+(4-2*k)*k;e.setAttribute('cx',x1+(x2-x1)*s);e.setAttribute('cy',y1+(y2-y1)*s);if(k<1)requestAnimationFrame(f);else if(done)done(e)})(t0)}
function fade(e,ms){var t0=performance.now();(function f(n){var k=Math.min(1,(n-t0)/ms);e.setAttribute('opacity',1-k);if(k<1)requestAnimationFrame(f);else e.remove()})(t0)}
function yIn(x){var top=90+(x-120)*140/470,bot=430-(x-120)*140/470;return top+8+Math.random()*(bot-top-16)}
function stream(n,gap,color,toX,toY,onArrive){var i=0;(function one(){if(i++>=n)return;var x=122,y=yIn(170+Math.random()*120);var e=dot(x,y,color);go(e,x,y,toX,toY,1400+Math.random()*500,function(d){d.remove();if(onArrive)onArrive()});setTimeout(one,gap)})()}
function refuse(){var e=dot(122,yIn(180),'#E31E30');go(e,122,e.getAttribute('cy'),148,e.getAttribute('cy'),500,function(d){fade(d,400)})}
var ENT=['rules · United States · clause with its section · verified this week','tooling · a model class, licence named, size named','hardware · an edge box class, power and temperature range','case study · a past deployment, outcome recorded','approach · a method, its precondition, its failure mode','history · a past failure and what it cost'];
var LRN=['a founder note on test cell sign off','a talk on condition monitoring at the edge','a paper on read only machine interfaces','a build note on clock discipline across gateways'];
var cycle=0;
function night(){P('NIGHT · DISTILLATION');dist.classList.add('on');waist.classList.add('hot');
 say('door','accepted · '+ENT[cycle%ENT.length]);
 stream(14,220,'#F2F2F0',590,260,null);
 setTimeout(function(){say('distill','merged near duplicates · one rule kept, sources kept')},900);
 setTimeout(function(){say('distill','contradiction resolved · newest, most used reading wins')},2000);
 setTimeout(function(){say('distill','promoted a principle good designs relied on · demoted one a corrected design leaned on')},3000);
 setTimeout(function(){say('distill','brief · new version written · nothing deleted');var b=dot(610,260,'#D9C3A3',4.5);go(b,610,260,760,222,900,function(d){fade(d,600)})},3900);
 setTimeout(function(){dist.classList.remove('on');comm.classList.add('on');P('NIGHT · COMMISSIONING');say('measure','corpus measured against what practitioners ask · a miss found');
  say('writer','staged a sourced entry · '+ENT[(cycle+2)%ENT.length]);stream(6,260,'#D9C3A3',590,260,null);
  setTimeout(function(){say('verifier','could not ground one claim against its source · removed',true);refuse()},1200);
  setTimeout(function(){say('door','landed what survived · superseded entry named, not deleted')},2200);
  setTimeout(function(){comm.classList.remove('on');waist.classList.remove('hot');birth()},3400)},5000)}
function birth(){P('BIRTH · THE ROOM');room.classList.add('on');
 say('requirement','received · a physical operation, a country, a sector');var q=dot(1078,260,'#F2F2F0',4);go(q,1078,260,1040,222,900,function(d){fade(d,500)});
 setTimeout(function(){say('room','reference filtered by domain and the country whose law binds · aged · deduplicated');for(var i=0;i<5;i++)(function(i){var e=dot(610,245+i*7,'#F2F2F0');go(e,610,245+i*7,750+i*40,222,800+i*120,function(d){fade(d,400)})})(i)},900);
 setTimeout(function(){say('room','the rest ride as title lines · inflated only if the model calls for one by name')},1900);
 setTimeout(function(){say('room','doctrine ranked by fit · cited by number in the scope items it shaped');var b=dot(610,260,'#D9C3A3',4.5);go(b,610,260,900,222,800,function(d){fade(d,400)})},2600);
 setTimeout(function(){say('room','fleet record read lesson by lesson · house scope first, then the sector')},3400);
 setTimeout(function(){P('BIRTH · REASONING');say('reason','one conversation over the room · architecture, scope ledger, contract');room.classList.remove('on');dtext.classList.add('on');design.setAttribute('opacity','1')},4200);
 setTimeout(function(){say('judge','episode filed with its measure · design cleared the floor')},5600);
 setTimeout(function(){P('REINFORCEMENT');var e=dot(1000,478,'#E31E30',4);var t0=performance.now();(function f(n){var k=Math.min(1,(n-t0)/2600);var p=ret.getPointAtLength(RL*k);e.setAttribute('cx',p.x);e.setAttribute('cy',p.y);if(k<1)requestAnimationFrame(f);else fade(e,500)})(t0);
  say('feedback','an engineer corrected one scope item · written as a lesson the next birth reads');
  setTimeout(function(){say('outcomes','the principles this design cited ride back to distillation with the verdict')},1100);
  setTimeout(function(){say('asks','one question the room could not answer · commissioned for the corpus')},2000);
  setTimeout(function(){say('night','briefs and corpus changed · the model did not');design.setAttribute('opacity','0');dtext.classList.remove('on');cycle++;setTimeout(night,1600)},3000)},6600)}
if(still){say('door','accepted · '+ENT[0]);say('distill','brief · new version written · nothing deleted');say('room','reference, doctrine, fleet record and standing memory assembled for one requirement');say('reason','one conversation over the room · architecture, scope ledger, contract');say('feedback','lessons, outcomes and asks return as experience');P('THE BOW TIE');design.setAttribute('opacity','1');return}
var started=false;var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting&&!started){started=true;night()}})},{threshold:.2});io.observe(svg);
})();</script>"""


def body_html():
    s = []
    s.append('<h2 id="the-model">The model</h2>')
    s.append(p("Most memory systems for software agents treat memory as storage: write a sentence, fetch the same sentence later. "
               "Fidelity in, fidelity out. Praxis is built on a different model of memory, taken from the biologist Michael Levin's 2024 paper "
               f"[Self-Improvising Memory]({LEVIN}) in Entropy."))
    s.append(p("Levin's claim is that living systems keep memory the way a bow tie is shaped."))
    s.append(p("**Left wing.** The high dimensional past: everything that happened, in full detail, in the body and the environment that existed then."))
    s.append(p("**The waist.** A narrow bottleneck the past must pass through to persist at all. The compression strips correlations and contingent detail. "
               "What survives the waist is not a record of the past but its salient pattern. Once the correlations are gone the stored pattern no longer "
               "resembles the experience that produced it, and it cannot be played back."))
    s.append(p("**Right wing.** A future self decodes the compressed pattern into whatever its present context needs. That self is never the one that wrote "
               "the memory. It has a different body, a different environment and different goals, so decoding is not retrieval. It is interpretation, and "
               "Levin is explicit that creative, adaptive confabulation is the feature that makes memory useful rather than the bug that makes it unreliable."))
    s.append(p("Three consequences follow, and all three matter for an engineering platform."))
    s.append("<ol>"
             "<li>" + blog.inline("**Salience over fidelity.** Evolution does not optimise memory for accurate replay. It optimises for what is still actionable "
                                  "later. A caterpillar's memory of where food was does not survive metamorphosis as a map; it survives as a relationship that a "
                                  "butterfly with a rebuilt brain can act on.") + "</li>"
             "<li>" + blog.inline("**Memories are messages between agents separated across time.** The writer cannot know the reader's situation, so the reader "
                                  "must do work. Reading memory is an act of sense making by the present, not a lookup into the past.") + "</li>"
             "<li>" + blog.inline("**The persistence paradox.** A system that never changes becomes obsolete; a system that changes is no longer the one that "
                                  "remembered. Planaria regrow a head and keep learned behaviour. Centenarians keep childhood memories through decades of "
                                  "molecular turnover. Identity persists as a process that trades fidelity to the past for patterns that still generalise. "
                                  "Memory therefore cannot live in the part of the system that is replaced.") + "</li></ol>")
    s.append(p("Levin extends the bow tie to every scale, from the egg that compresses an adult body into a cell to the genome that compresses a lineage, and "
               "he calls the arrangement polycomputing: the same stored pattern computes different things for different readers, and that freedom is where "
               "new capability comes from without catastrophic forgetting."))

    s.append('<h2 id="why-it-fits">Why it fits</h2>')
    s.append(p("Praxis is a platform on which an engineer designs a physical AI system for an estate they have never seen, in a sector they may not know, and "
               "comes out with a design a ten year engineer would recognise. The model that reasons is a frontier class open weights model, self hosted. "
               "Its weights never change."))
    s.append(p("So the platform's memory has to carry everything the model does not know and everything the platform learns, and it has to survive the model "
               "being swapped. That is the persistence paradox stated as a procurement requirement. The bow tie answers it: compress experience into patterns "
               "that do not depend on the reasoner, and let each new design read those patterns in its own context."))

    s.append('<h2 id="left-wing">Left wing</h2>')
    s.append(p("Everything the platform experiences enters as entries in Engram, CodeNinja's system of record for agent memory. Each entry has a source, a date "
               "and an honesty line that says what it cannot vouch for. Entries arrive through one validating door that refuses by name anything without a "
               "source, a jurisdiction where a law needs one, or a verified date. No customer of the platform is ever named in an entry."))
    s.append(p("Four kinds of experience land there."))
    s.append('<div class="tw"><table><thead><tr><th>Experience</th><th>What an entry is</th></tr></thead><tbody>'
             '<tr><td>Reference</td><td>' + blog.inline("A sourced fact a builder can act on: a regulation clause, a model or hardware class, a precedent, a method, "
                                                       "a past failure. Six lenses: rules, tooling, hardware, case studies, approach, history.") + '</td></tr>'
             '<tr><td>Learning</td><td>' + blog.inline("A raw sentence of domain knowledge from a talk, a paper, a build or a founder's note, with tags.") + '</td></tr>'
             '<tr><td>Episode</td><td>' + blog.inline("A design the platform produced, with its measured quality, and every line of feedback a person filed on it.") + '</td></tr>'
             '<tr><td>Ask</td><td>' + blog.inline("A question a design needed answered and the memory could not supply.") + '</td></tr>'
             '</tbody></table></div>')
    s.append(p("The reference corpus holds thousands of entries across the six lenses. The learnings number in the tens of thousands. Every design episode "
               "since the platform went live is kept. The counts move every night and are not the point; the shape is."))

    s.append('<h2 id="the-waist">The waist</h2>')
    s.append(p("Two routines run every night and do the compression. Neither touches the model. Both write only through the door."))
    s.append(p("**Distillation.** The raw learnings are folded into design briefs, one per domain tag, each a short ranked list of principles. Four operations "
               "and nothing else: merge near duplicates into one rule, resolve contradictions with the newest and most used reading winning, promote rules "
               "that good outcomes relied on and demote rules implicated in corrected ones, and mark as stale what was never used and never repeated. Every "
               "principle keeps the identifiers of the learnings it came from, so any rule on any design can be walked back to its sources. Every new brief "
               "is a new version; nothing is deleted."))
    s.append(p("This is salience over fidelity made literal. Tens of thousands of learnings stand behind a few hundred briefs. The sentences are gone. "
               "The relationships that still bind are kept, with their provenance."))
    s.append(p("**Commissioning.** The reference corpus is measured each morning against what practitioners in each sector expect it to answer, in two of the "
               "countries the platform serves. Where it falls short, writer agents stage new sourced entries and adversarial verifier agents remove what they "
               "cannot ground against the source. The door lands what survives. Superseded entries are never deleted; the new entry names what it replaces, "
               "and the planner's supersession index drops the old one from view."))
    s.append(p("The compression ratio is the point. Thousands of rules become the handful that bind in this country and this sector. Tens of thousands of "
               "learnings become a few hundred briefs, which become twenty lines on the table when a design begins."))

    s.append('<h2 id="right-wing">Right wing</h2>')
    s.append(p("A design in Praxis is called a birth. Before the model is asked anything, the platform assembles a room: the context the model will reason "
               "over for this requirement and no other. Assembly is deterministic code, not a search by similarity."))
    s.append("<ul>"
             "<li>" + blog.inline("**Reference** is filtered by the requirement's domain and by the country whose law binds, aged by verification date, "
                                  "de duplicated through supersession, and laid out under a fixed budget. Entries that fit ride in full. The rest ride as one "
                                  "title line each, and the model may call for any of them by name during reasoning. That call is the inflation step: a line "
                                  "becomes the full text only when the present design needs it.") + "</li>"
             "<li>" + blog.inline("**Doctrine** is read by a fit judge that marks which principles of the sector's brief and the cross sector briefs bear on "
                                  "this requirement. The planner receives them ranked and must cite them by number in the scope items they shaped.") + "</li>"
             "<li>" + blog.inline("**The fleet record** is read lesson by lesson, house scope first, then the sector's, up to a budget, together with the "
                                  "sector's rated past designs.") + "</li>"
             "<li>" + blog.inline("**Standing memory**, the project's own notes and the engineer's working preferences, rides last.") + "</li></ul>")
    s.append(p("The model then reasons once over that room, in a single conversation, carrying its own thinking from part to part, and writes the design in "
               "three parts: the architecture, the scope ledger, the contract."))
    s.append(p("This is Levin's right wing. The same compressed principle, read by two births in different countries and sectors, produces two different "
               "scope items, because the requirement in front of the planner decides what the memory means today. The platform does not retrieve a past "
               "decision. It re decides, with the past as a message it has to interpret."))
    s.append(p("What a reader can verify on any Praxis design: every cited principle resolves to a brief version, every brief version resolves to its source "
               "learnings, and every reference line resolves to a dated source. The design is a document whose every claim can be walked back to an entry "
               "the customer owns."))

    s.append('<h2 id="reinforcement">Reinforcement</h2>')
    s.append(p("Levin's bow tie is a funnel. Praxis closes it into a loop, so the right wing's output becomes the next left wing's input. This is recursive "
               "self improvement on Engram, and it changes memory, never weights."))
    s.append(p("**At the design.** Every birth is judged after reasoning against a rubric and filed as an episode with its score. Below a floor it is reasoned "
               "again with the verdict as a directive. A person's feedback on the design becomes lessons the next birth reads. The principles the design "
               "cited ride back to the distillation routine as outcomes, so a principle that good designs relied on rises and one that corrected designs "
               "leaned on falls. The asks a design could not answer become commissions for the corpus routine."))
    s.append(p("**At the platform.** A master agent runs improvement cycles on the platform itself: it reads what the routines did and owe, reads the misses "
               "from an independent benchmark of physical AI design, changes the platform, births real public requirements on production, and files what it "
               "learned as gap records on the routines' own episodes. The routines read those at the start of their next run. The agents never talk to each "
               "other directly. They talk through Engram."))
    s.append(p("**At the substrate.** Because every one of these signals is an entry in memory and not a weight, the reasoning model can be replaced and the "
               "memory stands. The platform has moved its reasoning between model providers with no change to what it remembers. New head, same memory."))
    s.append(p("What is published about the benchmark is its results. How it scores is not published."))

    s.append('<h2 id="in-pseudo-code">In pseudo code</h2>')
    code = """<span class="c"># every night, outside the platform</span>
briefs   &lt;- distill(learnings, outcomes)         <span class="c"># merge, resolve, promote or demote, mark stale</span>
corpus   &lt;- commission(measure(corpus) misses)   <span class="c"># write, verify adversarially, land through the door</span>

<span class="c"># per design, inside the platform, before the first model call</span>
room     &lt;- assemble(corpus, briefs, lessons, episodes | requirement, country, sector)
design   &lt;- reason(model, room)                  <span class="c"># one conversation, three parts, citations by number</span>
episode  &lt;- judge(design) ; file(episode)

<span class="c"># the loop</span>
lessons  &lt;- feedback(person, design)
outcomes &lt;- citations(design) with the episode's verdict
asks     &lt;- what the room could not supply
<span class="c"># tomorrow night, briefs and corpus change; the model does not</span>"""
    s.append(f"<pre>{code}</pre>")
    s.append(p("The functions named here exist. Their internals, the prompts, the judges and the thresholds are not described on this page."))

    s.append('<h2 id="glossary">Glossary</h2>')
    gl = [("Engram", "CodeNinja's system of record for agent memory. Every entry has a source, a date and an honesty line."),
          ("The door", "The single validating entry point to the memory. Refuses by name."),
          ("Brief", "A versioned, ranked list of design principles for one domain tag, each principle traceable to its sources."),
          ("Room", "The context assembled for one design before the model is called."),
          ("Birth", "One design produced by the platform from one requirement."),
          ("Episode", "The record of one design or one routine run, with its measure, feedback and gap records."),
          ("Inflation", "A reference that rode into the room as a title line being expanded to full text on the model's call.")]
    s.append('<div class="tw"><table><thead><tr><th>Term</th><th>Meaning on this page</th></tr></thead><tbody>'
             + "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td></tr>" for a, b in gl) + "</tbody></table></div>")
    s.append(p(f"Reference: Michael Levin, Self-Improvising Memory: A Perspective on Memories as Agential, Dynamically Reinterpreting Cognitive Glue, "
               f"Entropy 26(6), 481, 2024. [Read the paper]({LEVIN})."))
    s.append(f'<p class="next">Read next: <a href="{BASE}/memos/compression-and-reinflation/">Compression and Reinflation</a>, the memo this architecture '
             f'grew out of, and <a href="{BASE}/praxis/">Praxis</a>, the platform that runs it.</p>')
    return "\n".join(s)


def page():
    a = blog.AUTHORS["Muhammad Umar"]
    body = (f'<article class="memo"><p class="eyebrow">Research · CodeNinja</p><h1>{E(TITLE)}</h1><p class="dek">{E(SUB)}</p>'
            f'<div class="body">{figure()}{body_html()}</div>'
            f'<p class="after">CodeNinja is a Middle Eastern American artificial intelligence lab and system of context company. '
            f'We build sovereign systems that enterprises own, harden and run inside their own perimeter, and '
            f'<a href="{BASE}/praxis/">Praxis</a>, the platform that designs them.</p></article>')
    url = f"{BASE}/{SLUG}/"
    ld = [{"@context": "https://schema.org", "@type": "TechArticle", "headline": TITLE, "alternativeHeadline": SUB, "description": DESC,
           "url": url, "mainEntityOfPage": url, "image": f"{url}cover.png", "datePublished": DATE, "dateModified": DATE, "inLanguage": "en",
           "license": "https://creativecommons.org/licenses/by/4.0/", "about": ["agentic memory", "memory architecture", "physical AI", "sovereign AI"],
           "citation": {"@type": "ScholarlyArticle", "name": "Self-Improvising Memory", "author": "Michael Levin", "url": LEVIN, "datePublished": "2024"},
           "author": {"@type": "Organization", "@id": f"{BASE}/#org", "name": "CodeNinja Atoms"},
           "publisher": {"@type": "Organization", "@id": f"{BASE}/#org", "name": "CodeNinja Atoms", "url": f"{BASE}/"}}]
    h = memos.shell(f"{SLUG}/", f"{TITLE} | How Praxis keeps memory outside the model", DESC, body, ld, f"{url}cover.png")
    return (h.replace("</style></head>", CSS + LIVE_CSS + "</style></head>", 1).replace("Memos are CC BY 4.0", "This page is CC BY 4.0")
            .replace("</body>", LIVE_JS + "</body>", 1))


def markdown_copy():
    txt = re.sub(r"<pre>.*?</pre>", "", body_html(), flags=re.S)
    txt = re.sub(r"<figure>.*?</figure>", "", txt, flags=re.S)
    txt = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n## \1\n", txt)
    txt = re.sub(r"<li>", "- ", txt); txt = re.sub(r"<tr><td>(.*?)</td><td>(.*?)</td></tr>", r"- \1: \2", txt)
    txt = re.sub(r"<[^>]+>", "", txt)
    txt = html.unescape(re.sub(r"\n{3,}", "\n\n", txt)).strip()
    return (f"# {TITLE}\n\n{SUB}\n\nBy Muhammad Umar, Cofounder, CodeNinja, {blog.nice_date(DATE)}.\nCanonical: {BASE}/{SLUG}/\n"
            f"License: CC BY 4.0\nPublisher: CodeNinja Atoms (https://codeatoms.ai)\n\n{txt}\n")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    memos._cover({"title": TITLE, "subtitle": SUB, "cover_line": "Memory as a bow tie, after Michael Levin", "author": "Muhammad Umar",
                  "author_role": "Cofounder, CodeNinja", "date": DATE}, OUT)
    (OUT / "index.html").write_text(page(), encoding="utf-8")
    (OUT / "index.md").write_text(markdown_copy(), encoding="utf-8")
    print(f"memory page: /{SLUG}/")


if __name__ == "__main__":
    main()
