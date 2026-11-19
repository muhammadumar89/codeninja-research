"""Hyper Engram: /hyper-engram/, the agentic memory of the Hyper stack, told the way a research lab would.

Umar, 19 Nov 2026: a training lab's platform page (same day: never say we do not train weights; then: professional platform language,
no "we train both" talk. Engram trains sovereign open weights models in their weights and their memory, on premises and air gapped), in our design system, that tells the world how we train
systems by compression and reinflation without changing weights. Sources: the memo Compression and Reinflation
(10 Oct 2026) and The Recursive Learning Loop (internal). Public rules kept here:
  - results are public, the PADI scoring method never is (numbers come from padi.load(), the same export /padi/ uses)
  - no counts from Engram, never the word "rows", no prompts, judges' rubrics or thresholds
  - no internal names (no coding agent product, no schedules, no collection names), no customer named
  - never "frozen weights", "no weight updates" or "we do not fine tune" on this page
  - "RSI Loop", never "cycle"; no hyphens or dashes in prose; never name another company's product
    python tools/product_pages.py     # writes hyper-engram/index.html with the other product pages
"""
import random
import brand
from ontology_page import BASE, E, MARK, CSS as OCSS, TYPE_JS, shell, sx, head

URL = f"{BASE}/hyper-engram/"
MEMO = f"{BASE}/memos/compression-and-reinflation/"


# The hero: a living 3D context graph that turns in perspective, nearer nodes brighter (Umar, 19 Nov 2026, after the context graph on a company builder's site:
# "Context is the moat" is what this page must show). Agents and domains cluster around one shared memory;
# each scene captures work in one agent cluster, compresses it into a versioned brief at the centre, trains,
# and reinflates it into a domain the work never touched. Labels are illustrative, never Engram counts.
CLUSTERS = ["AGENTS · PLANNING", "DOMAIN · MINING", "AGENTS · RESEARCH", "DOMAIN · PORTS", "AGENTS · BUILD", "DOMAIN · FINANCE",
            "AGENTS · BENCHMARK", "DOMAIN · ENERGY", "AGENTS · PREMORTEM", "DOMAIN · DEFENCE", "AGENTS · FIELD", "DOMAIN · CONTACT CENTRES",
            "AGENTS · REVIEW", "DOMAIN · HEALTH", "AGENTS · PRICING", "DOMAIN · PUBLIC SECTOR"]
SCENES = [
    (6, ["blind evaluation", "gap record", "missed requirement", "premortem note"], "ROUTING v7", 1, ["haul road design", "shift handover", "warning ownership"]),
    (10, ["site walkthrough", "operator correction", "tender clause"], "CITATIONS v4", 3, ["berth planning", "customs hold", "crane schedule"]),
    (4, ["design review", "failed build", "reviewer feedback", "sizing check"], "SIZING v9", 13, ["ward capacity", "triage queue", "records access"]),
    (2, ["new regulation", "standard update", "source check"], "COMPLIANCE v5", 7, ["permit to work", "emissions report", "outage plan"]),
    (8, ["failure story", "risk owner", "rollback plan"], "RELEASES v6", 15, ["case backlog", "citizen request", "records retention"]),
]

GRAPH_JS = r"""<script>(function(){
var cv=document.getElementById('cg');if(!cv||!cv.getContext)return;
var D=window.ENGRAM_GRAPH,x=cv.getContext('2d'),st=document.getElementById('cgst'),st2=document.getElementById('cgst2'),host=cv.parentElement;
var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function rng(a){return function(){a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
var r=rng(11),N=[],E=[],CL=[],K=D.c.length;function g(){return (r()+r()+r()-1.5)/1.5}
D.c.forEach(function(nm,i){var yy=1-(i+.5)/K*2,rd=Math.sqrt(1-yy*yy),th=i*2.39996,d=i%2?1:.8,o={x:Math.cos(th)*rd*d*1.12,y:yy*d*.6,z:Math.sin(th)*rd*d*1.12,n:[],nm:nm};
 var k=15+Math.floor(r()*9);for(var j=0;j<k;j++){N.push({x:o.x+g()*.17,y:o.y+g()*.13,z:o.z+g()*.17,c:i,s:1+r()*1.3});o.n.push(N.length-1)}CL.push(o)});
function d2(a,b){return(a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y)+(a.z-b.z)*(a.z-b.z)}
N.forEach(function(a,i){var s=CL[a.c].n.filter(function(j){return j!==i}).map(function(j){return[j,d2(a,N[j])]}).sort(function(p,q){return p[1]-q[1]});
 for(var k=0;k<2;k++)E.push([i,s[k][0],0]);if(r()<.45){var j=Math.floor(r()*N.length);if(N[j].c!==a.c)E.push([i,j,1])}if(r()<.08)E.push([i,-1,2])});
CL.forEach(function(o){var s=o.n.slice().sort(function(p,q){return N[p].y-N[q].y});o.pick=function(k){var out=[];for(var j=0;j<k;j++)out.push(s[Math.round(j*(s.length-1)/Math.max(1,k-1))]);return out}});
var O={x:0,y:0,z:0},W,H,cx,cy,S,mob,dpr,FD=2.6;
function size(){dpr=Math.min(2,window.devicePixelRatio||1);W=host.clientWidth;H=host.clientHeight;cv.width=W*dpr;cv.height=H*dpr;x.setTransform(dpr,0,0,dpr,0,0);mob=W<760;
 if(mob){cx=W*.5;cy=H*.47;S=Math.min(W*.42,H*.18)}else{cx=W*.53;cy=H*.45;S=Math.min(W*.25,H*.32,420)}}
size();window.addEventListener('resize',size);
var ya=0,pa=-.3,cyaw,syaw,cp,sp,oy=0,op=0,mx=0,my=0,spin=0,drag=null;
function prj(p){var X=p.x*cyaw+p.z*syaw,Z=-p.x*syaw+p.z*cyaw,Y=p.y*cp-Z*sp,Z2=p.y*sp+Z*cp,f=FD/(FD+Z2);return[cx+X*f*S,cy+Y*f*S,Z2,f]}
function dep(z){var q=(z+1.15)/2.3;return q<0?0:q>1?1:q}
function lerp3(a,b,u){return{x:a.x+(b.x-a.x)*u,y:a.y+(b.y-a.y)*u,z:a.z+(b.z-a.z)*u}}
function cl(v){return v<0?0:v>1?1:v}function ramp(t,a,b){return cl((t-a)/(b-a))}
host.addEventListener('pointermove',function(e){var b=host.getBoundingClientRect();mx=(e.clientX-b.left)/b.width-.5;my=(e.clientY-b.top)/b.height-.5;if(drag!==null){spin+=(e.clientX-drag)*.006;drag=e.clientX}});
cv.addEventListener('pointerdown',function(e){if(e.pointerType==='mouse'){drag=e.clientX;cv.style.cursor='grabbing'}});
window.addEventListener('pointerup',function(){drag=null;cv.style.cursor=''});
var M=[];function spawn(){M.push({e:E[Math.floor(Math.random()*E.length)],t:0,v:.00025+Math.random()*.0004})}
var T=9000,t0=performance.now(),last=t0,on=true,BX=null,lastSc=-1;
var SC=D.s.map(function(q){return{src:q[0],sl:q[1],br:q[2],dst:q[3],dl:q[4],sn:CL[q[0]].pick(q[1].length),dn:CL[q[3]].pick(q[4].length)}});
var FM='ui-monospace,"IBM Plex Mono",Menlo,monospace';
var BS={};
function boxes(key,ci,nodes,labs,a,col,P){if(a<=0||mob)return;var c=prj(CL[ci]),side=c[0]>=cx?1:-1,k=labs.length,X0=c[0]+side*.42*S;x.font='400 12px '+FM;
 var B=BS[key]||(BS[key]=[]);
 labs.forEach(function(l,j){var w=x.measureText(l).width+16,h=22,ty=c[1]+(j-(k-1)/2)*(h+9),tx=side>0?X0:X0-w;tx=Math.max(8,Math.min(W-w-8,tx));ty=Math.max(124,Math.min(H*.64,ty));
  if(!B[j])B[j]=[tx,ty];B[j][0]+=(tx-B[j][0])*.08;B[j][1]+=(ty-B[j][1])*.08;var bx=B[j][0],by=B[j][1],p=P[nodes[j]],ex=bx+w/2<p[0]?bx+w:bx;
  x.globalAlpha=a;x.strokeStyle=col;x.lineWidth=1;x.beginPath();x.moveTo(p[0],p[1]);x.lineTo(p[0],by);x.lineTo(ex,by);x.stroke();
  x.fillStyle='rgba(13,8,21,.92)';x.fillRect(bx,by-h/2,w,h);x.strokeRect(bx+.5,by-h/2+.5,w-1,h-1);x.fillStyle='#fff';x.textBaseline='middle';x.textAlign='left';x.fillText(l,bx+8,by+1);
  x.beginPath();x.arc(p[0],p[1],4.4*p[3],0,6.283);x.fillStyle=col;x.fill();x.beginPath();x.arc(p[0],p[1],9*p[3],0,6.283);x.globalAlpha=a*.5;x.stroke()});x.globalAlpha=1}
function pulses(nodes,inward,k,col){if(k<=0||k>=1)return;var C0=prj(O);nodes.forEach(function(ni,j){var q=cl(k*1.25-j*.08);if(q<=0||q>=1)return;var u=inward?q:1-q,e=u*u*(3-2*u),a=prj(N[ni]),p=prj(lerp3(N[ni],O,e));
 x.strokeStyle=col;x.globalAlpha=.5;x.lineWidth=1.2;x.beginPath();x.moveTo(a[0],a[1]);x.lineTo(C0[0],C0[1]);x.stroke();
 x.globalAlpha=1;x.fillStyle=col;x.beginPath();x.arc(p[0],p[1],3.4*p[3],0,6.283);x.fill();x.globalAlpha=.25;x.beginPath();x.arc(p[0],p[1],9*p[3],0,6.283);x.fill()});x.globalAlpha=1}
var PH=['01 CAPTURE','02 COMPRESS','03 TRAIN','04 REINFLATE'],lastS='',ord=N.map(function(_,i){return i});
function frame(now){if(!on){last=now;requestAnimationFrame(frame);return}
 var t=RM?4000:Math.max(0,now-t0),dt=Math.min(50,now-last);last=now;var si=RM?0:Math.floor(t/T)%SC.length,u=RM?6000:t%T,S_=SC[si];if(si!==lastSc){BS={};lastSc=si}
 oy+=(mx*.7-oy)*.04;op+=(my*.3-op)*.04;ya=(RM?.6:t*.00011)+spin+oy;pa=-.24+op;cyaw=Math.cos(ya);syaw=Math.sin(ya);cp=Math.cos(pa);sp=Math.sin(pa);
 var sa=ramp(u,0,500)*(1-ramp(u,5200,6000)),da=ramp(u,5600,6100)*(1-ramp(u,8200,8900)),ba=ramp(u,3500,3900)*(1-ramp(u,8200,8900));if(RM){sa=0;da=1;ba=1}
 var P=N.map(prj),C0=prj(O);x.clearRect(0,0,W,H);x.lineWidth=1;
 for(var i=0;i<E.length;i++){var e=E[i],a=P[e[0]],b=e[1]<0?C0:P[e[1]],q=1-.82*dep((a[2]+b[2])/2),hs=N[e[0]].c===S_.src&&sa>0,hd=N[e[0]].c===S_.dst&&da>0;
  x.strokeStyle=hs?'rgba(182,156,255,'+(q*(.1+.45*sa))+')':hd?'rgba(255,209,102,'+(q*(.1+.4*da))+')':'rgba(200,185,255,'+(q*(e[2]===2?.06:e[2]?.09:.17))+')';
  x.beginPath();x.moveTo(a[0],a[1]);x.lineTo(b[0],b[1]);x.stroke()}
 if(!RM){while(M.length<(mob?18:44))spawn();M=M.filter(function(m){m.t+=m.v*dt;if(m.t>=1)return false;var p=prj(lerp3(N[m.e[0]],m.e[1]<0?O:N[m.e[1]],m.t));x.fillStyle='rgba(215,205,255,'+(1-.8*dep(p[2]))+')';x.beginPath();x.arc(p[0],p[1],1.5*p[3],0,6.283);x.fill();return true})}
 ord.sort(function(p,q){return P[q][2]-P[p][2]});
 for(i=0;i<ord.length;i++){var ni=ord[i],n=N[ni],p=P[ni],q=1-.78*dep(p[2]);
  x.fillStyle=n.c===S_.src&&sa>0?'rgba(200,180,255,'+Math.max(q,sa)+')':n.c===S_.dst&&da>0?'rgba(255,209,102,'+Math.max(q,da)+')':'rgba(164,143,255,'+(.15+.75*q)+')';
  x.beginPath();x.arc(p[0],p[1],n.s*p[3]*(.7+.6*q),0,6.283);x.fill()}
 x.font='500 10px '+FM;x.textBaseline='alphabetic';CL.forEach(function(o,i){var c=prj(o),act=(i===S_.src&&sa>0)||(i===S_.dst&&da>0),q=1-dep(c[2]);if(mob||c[1]-.24*S*c[3]<112)return;
  x.fillStyle=act?'rgba(255,255,255,.95)':'rgba(225,215,255,'+(.1+.5*q)+')';x.textAlign='center';x.fillText(o.nm,Math.max(80,Math.min(W-80,c[0])),c[1]-.24*S*c[3])});
 if(!RM){pulses(S_.sn,true,ramp(u,2200,3600),'#c8b9ff');pulses(S_.dn,false,ramp(u,4600,5800),'#ffd166')}
 var tw=ramp(u,3600,4600);if(tw>0&&tw<1&&!RM){x.strokeStyle='rgba(255,209,102,'+(1-tw)*.8+')';x.lineWidth=1.4;x.beginPath();x.ellipse(cx,cy,10+tw*S*.7,(10+tw*S*.7)*Math.abs(sp)+4,0,0,6.283);x.stroke();x.beginPath();x.arc(cx,cy,10+tw*S*.5,0,6.283);x.globalAlpha=.5;x.stroke();x.globalAlpha=1;x.lineWidth=1}
 x.beginPath();x.arc(cx,cy,15+Math.sin(t*.003)*1.5,0,6.283);x.strokeStyle='rgba(255,255,255,.5)';x.stroke();x.beginPath();x.arc(cx,cy,7,0,6.283);x.fillStyle='#fff';x.fill();
 x.font='500 10px '+FM;x.textAlign='center';x.fillStyle='rgba(255,255,255,.85)';x.fillText('ONE SHARED MEMORY',cx,cy+34);
 if(ba>0){x.globalAlpha=ba;x.font='600 11px '+FM;var bt='BRIEF · '+S_.br,bw=x.measureText(bt).width+20;x.fillStyle='rgba(13,8,21,.92)';x.fillRect(cx-bw/2,cy-48,bw,24);x.strokeStyle='#ffd166';x.strokeRect(cx-bw/2+.5,cy-47.5,bw-1,23);x.fillStyle='#fff';x.textBaseline='middle';x.fillText(bt,cx,cy-35.5);x.textBaseline='alphabetic';x.globalAlpha=1}
 boxes('s',S_.src,S_.sn,S_.sl,sa,'rgba(200,185,255,.95)',P);boxes('d',S_.dst,S_.dn,S_.dl,da,'#ffd166',P);
 if(st){var ph=u<2200?0:u<3600?1:u<4600?2:3,lab=PH[ph]+'<br>'+[CL[S_.src].nm,'brief · '+S_.br,'into weights and memory',CL[S_.dst].nm][ph];if(RM)lab='04 REINFLATE<br>'+CL[S_.dst].nm;if(lab!==lastS){st.innerHTML=lab;if(st2)st2.innerHTML=lab.replace('<br>',' · ');lastS=lab}}
 if(!RM)requestAnimationFrame(frame)}
if('IntersectionObserver'in window)new IntersectionObserver(function(es){on=es[0].isIntersecting}).observe(host);
requestAnimationFrame(frame);if(RM)window.addEventListener('resize',function(){requestAnimationFrame(frame)});
})();</script>"""


def bowtie_svg():
    """The hero: experience pours in from the left, is compressed at the waist into one versioned principle,
    and is reinflated on the right into designs for places the memory never saw."""
    r = random.Random(7)
    W, H, wx, wy = 1600, 900, 800, 400
    srcs = [("RUNS", 230), ("CORRECTIONS", 340), ("BENCHMARK MISSES", 450), ("REAL REQUIREMENTS", 560), ("FIELD LEARNINGS", 670)]
    tgts = [("A mine", "Chile", 160), ("A contact centre", "Pakistan", 290), ("A hospital", "Ontario", 420), ("A port", "Saudi Arabia", 550)]
    o = [f'<svg class="bow" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" aria-hidden="true">',
         '<defs><radialGradient id="bwg"><stop offset="0" stop-color="#ffd166" stop-opacity=".55"/><stop offset=".4" stop-color="#5b2bff" stop-opacity=".35"/><stop offset="1" stop-color="#5b2bff" stop-opacity="0"/></radialGradient>'
         '<linearGradient id="bwf" x1="0" x2="1"><stop offset="0" stop-color="#a48fff" stop-opacity=".02"/><stop offset=".5" stop-color="#a48fff" stop-opacity=".16"/><stop offset="1" stop-color="#a48fff" stop-opacity=".02"/></linearGradient></defs>']
    # the bowtie silhouette
    o.append(f'<path class="sil" d="M40,70 C430,80 640,{wy - 40} {wx - 26},{wy - 8} L{wx + 26},{wy - 8} C960,{wy - 40} 1170,80 1560,70 L1560,750 C1170,740 960,{wy + 40} {wx + 26},{wy + 8} L{wx - 26},{wy + 8} C640,{wy + 40} 430,740 40,750 Z"/>')
    for x in range(80, 1560, 80):
        o.append(f'<line class="tick" x1="{x}" y1="808" x2="{x}" y2="816"/>')
    left, right = [], []
    for i in range(54):
        x, y = r.uniform(40, 520), r.uniform(90, 730)
        d = f"M{x:.0f},{y:.0f} C{x + 260:.0f},{y:.0f} {wx - 150},{wy} {wx},{wy}"
        left.append(d)
        o.append(f'<path class="fib" d="{d}"/>')
    for i in range(36):
        _, _, ty = tgts[i % 4]
        tx, ty = 1330 + r.uniform(-30, 10), ty + r.uniform(-34, 34)
        d = f"M{wx},{wy} C{wx + 150},{wy} {tx - 280:.0f},{ty:.0f} {tx:.0f},{ty:.0f}"
        right.append(d)
        o.append(f'<path class="fib r" d="{d}"/>')
    for i, d in enumerate(left):
        o.append(f'<circle class="pt" r="{r.choice([1.6, 2, 2.6])}"><animateMotion dur="{r.uniform(5, 8):.1f}s" begin="-{r.uniform(0, 8):.1f}s" repeatCount="indefinite" path="{d}" keyPoints="0;1" keyTimes="0;1" calcMode="spline" keySplines=".5 0 .9 .6"/></circle>')
    for i, d in enumerate(right):
        o.append(f'<circle class="pt r" r="{r.choice([1.8, 2.4])}"><animateMotion dur="{r.uniform(4, 6.5):.1f}s" begin="-{r.uniform(0, 6):.1f}s" repeatCount="indefinite" path="{d}" keyPoints="0;1" keyTimes="0;1" calcMode="spline" keySplines=".1 .4 .5 1"/></circle>')
    for lab, y in srcs:
        o.append(f'<text class="lb" x="64" y="{y - 52}">{lab}</text>')
    o.append(f'<circle cx="{wx}" cy="{wy}" r="120" fill="url(#bwg)" class="halo"/>')
    o.append(f'<g class="waist" transform="translate({wx},{wy})"><rect x="-74" y="-24" width="148" height="48" rx="2"/><text class="w1" y="-3" text-anchor="middle">BRIEF · ROUTING</text><text class="w2" y="14" text-anchor="middle">v7 · supersedes v6</text></g>')
    o.append(f'<text class="hd" x="{wx - 230}" y="{wy - 150}" text-anchor="middle">COMPRESS</text><text class="hd" x="{wx + 230}" y="{wy - 150}" text-anchor="middle">REINFLATE</text>')
    o.append(f'<text class="sub" x="{wx - 230}" y="{wy - 130}" text-anchor="middle">many observations, one principle</text><text class="sub" x="{wx + 230}" y="{wy - 130}" text-anchor="middle">one principle, a new design each time</text>')
    for a, b, y in tgts:
        o.append(f'<g class="tg" transform="translate(1350,{y})"><circle r="5"/><text x="16" y="-2">{a}</text><text class="c" x="16" y="15">{b.upper()}</text></g>')
    o.append(f'<g class="lock" transform="translate({wx},{wy + 92})"><rect x="-96" y="-15" width="192" height="30" rx="15"/><text y="5" text-anchor="middle">THE TRAINING SIGNAL</text></g>')
    o.append('</svg>')
    return "".join(o)


def loop_svg():
    """The recursive learning loop as a drawing: one master agent, two daily routines, the planner and the
    benchmark, who never speak to each other directly. They speak through Engram."""
    N = {"m": (190, 120, "Master agent", "runs each RSI Loop, changes the code"),
         "d": (1010, 120, "Distillation routine", "every morning: learnings into briefs"),
         "r": (1010, 500, "Corpus routine", "every morning: measures, lands entries"),
         "p": (600, 560, "Planner", "reads memory the moment it reasons"),
         "b": (190, 500, "Benchmark and premortem", "fresh tasks and blind sets")}
    E_ = [("m", "e", "M308,125 C420,130 480,200 522,258", "gap records, asks, demand"),
          ("e", "d", "M680,262 C760,200 820,120 888,115", "newest episode, open asks"),
          ("d", "e", "M892,140 C820,160 740,250 684,298", "versioned briefs"),
          ("e", "r", "M680,330 C760,360 830,480 888,490", "feedback, open asks"),
          ("r", "e", "M892,515 C800,515 720,430 676,368", "verified entries"),
          ("e", "p", "M582,386 L582,526", "memory, mirrored"),
          ("p", "e", "M618,528 L618,388", "plans, unmet asks"),
          ("m", "b", "M150,152 L150,466", "measures"),
          ("b", "m", "M230,468 L230,154", "misses"),
          ("m", "p", "M72,124 C18,170 18,602 120,602 L478,570", "code, tests, deploys")]
    o = ['<svg class="loop" viewBox="0 0 1200 640" role="img" aria-label="The recursive learning loop: a master agent, two daily routines, the planner and the benchmark, all reading and writing through Engram">',
         '<defs><marker id="la" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0,0 L8,4 L0,8 z"/></marker></defs>']
    for k, (a, b, d, lab) in enumerate(E_):
        o.append(f'<path id="le{k}" class="le" d="{d}" marker-end="url(#la)"/>')
    for k, (a, b, d, lab) in enumerate(E_):
        o.append(f'<circle class="lp" r="3.6"><animateMotion dur="{3.2 + (k % 4) * .5:.1f}s" begin="-{k * .7:.1f}s" repeatCount="indefinite"><mpath href="#le{k}"/></animateMotion></circle>')
    lp = {0: (440, 160, "middle"), 1: (770, 150, "end"), 2: (800, 236, "start"), 3: (812, 404, "start"), 4: (880, 556, "end"), 5: (570, 450, "end"), 6: (632, 500, "start"), 7: (138, 312, "end"), 8: (242, 312, "start"), 9: (300, 624, "middle")}
    for k, (a, b, d, lab) in enumerate(E_):
        x, y, an = lp[k]
        o.append(f'<text class="el" x="{x}" y="{y}" text-anchor="{an}">{E(lab)}</text>')
    # Engram: a store of strata, not a box
    o.append('<g class="cyl" transform="translate(600,250)"><path class="cb" d="M-80,0 L-80,110 A80,22 0 0 0 80,110 L80,0"/><ellipse class="ct" cx="0" cy="0" rx="80" ry="22"/>')
    for i, s in enumerate(["episodes", "feedback", "gap records", "briefs", "corpus"]):
        y = 26 + i * 18
        o.append(f'<path class="st" d="M-80,{y} A80,22 0 0 0 80,{y}"/><text class="sl" x="0" y="{y + 14}" text-anchor="middle">{s}</text>')
    o.append('<text class="cn" x="0" y="-36" text-anchor="middle">ENGRAM</text></g>')
    for k, (x, y, t, s) in N.items():
        w = 236
        o.append(f'<g class="nd n{k}" transform="translate({x - w / 2:.0f},{y - 30})"><rect width="{w}" height="60"/><rect class="bar" width="4" height="60"/><text class="t" x="16" y="26">{E(t)}</text><text class="s" x="16" y="45">{E(s)}</text></g>')
    o.append('</svg>')
    return "".join(o)


def glyph(k):
    g = {"cap": '<rect x="6" y="8" width="52" height="10"/><rect x="6" y="22" width="52" height="10"/><rect class="v" x="6" y="36" width="52" height="10"/>',
         "cmp": '<path d="M4,6 L28,22 L28,30 L4,46 Z"/><path class="v" d="M36,22 L60,6 L60,46 L36,30 Z"/><circle class="vs" cx="32" cy="26" r="3"/>',
         "rei": '<rect x="6" y="6" width="24" height="18"/><path class="vs" d="M34,15 L44,15 M40,11 L44,15 L40,19"/><rect class="v" x="46" y="6" width="14" height="18"/><path d="M6,32 L58,32 M6,40 L44,40 M6,48 L36,48"/>',
         "trn": '<circle cx="10" cy="12" r="4"/><circle cx="10" cy="40" r="4"/><circle class="v" cx="32" cy="8" r="4"/><circle class="v" cx="32" cy="26" r="4"/><circle class="v" cx="32" cy="44" r="4"/><circle cx="54" cy="26" r="4"/><path d="M14,12 L28,8 M14,12 L28,26 M14,40 L28,26 M14,40 L28,44 M36,8 L50,26 M36,26 L50,26 M36,44 L50,26"/>',
         "rec": '<circle cx="32" cy="26" r="20"/><circle class="v" cx="32" cy="26" r="9"/><path class="vs" d="M32,2 L32,10 M32,42 L32,50 M8,26 L16,26 M48,26 L56,26"/>'}[k]
    return f'<svg class="gly" viewBox="0 0 64 52" aria-hidden="true">{g}</svg>'


LEARN = [("Benchmark miss", "A conveyor design sensed belt misalignment and never said who acts on it.", "k"),
         ("Engineer correction", "The alarm went to the control room, which cannot stop a haul truck. Route it to the pit supervisor.", "k"),
         ("Real requirement", "A tender asks for alerts to reach “the responsible officer” within a minute. Responsible for what?", "k"),
         ("Field learning", "Operators ignore an alert that arrives without a decision attached to it.", "k"),
         ("Benchmark miss", "A gas reading crossed its limit. The design logged it and paged no one.", "k"),
         ("Engineer correction", "Name the reading that starts the clock, not only the threshold.", "k"),
         ("Earlier note", "Send every alert to the shift manager.", "x"),
         ("Earlier note", "Make critical alerts red.", "f")]
PRINCIPLE = "Every sensed warning names three things: the role that can act in time, the reading that starts the clock, and the options of the decision."
PLACES = {"mine": ("A mine in Chile", [("Warning", "A haul truck and a person on foot inside the proximity zone"), ("Who acts", "The pit supervisor on shift, never only the control room"),
                                       ("Clock starts", "At the first proximity warning, not at the second"), ("Options", "Stop the truck · reroute it · send an escort")]),
          "call": ("A contact centre in Pakistan", [("Warning", "Callers waiting longer than the service level allows"), ("Who acts", "The floor supervisor on duty"),
                                                   ("Clock starts", "When the first caller passes the agreed wait"), ("Options", "Open overflow · offer a callback · move agents from outbound")]),
          "ward": ("A hospital in Ontario", [("Warning", "A ward patient's early warning score rising"), ("Who acts", "The charge nurse, then the rapid response team"),
                                            ("Clock starts", "At the second rising score inside the hour"), ("Options", "Reassess at the bedside · call rapid response · escalate to the physician")])}


def bench():
    cards = "".join(f'<li class="lc {c}" style="--i:{i}"><span>{E(s)}</span>{E(t)}</li>' for i, (s, t, c) in enumerate(LEARN))
    chips = "".join(f'<button type="button" class="pc" data-p="{k}">{E(v[0])}</button>' for k, v in PLACES.items())
    return (f'<div class="bench" id="bench"><div class="bl"><div class="bh"><b>Experience</b><span>8 learnings · 4 sources</span></div><ul class="lcs">{cards}</ul>'
            '<button type="button" class="go" id="bcmp">Compress →</button></div>'
            '<div class="bm"><div class="bh"><b>Brief</b><span id="bver">routing · v6</span></div><div class="pr" id="bpr"><p class="wait">Press Compress. Six learnings become one principle, one contradiction is resolved and one note fades because it never mattered.</p></div>'
            f'<div class="bh t2"><b>Reinflate into</b><span>the model reads it here</span></div><div class="pcs">{chips}</div></div>'
            '<div class="br"><div class="bh"><b>Design</b><span id="bplace">no place yet</span></div><dl class="out" id="bout"><dt>Waiting</dt><dd>Compress, then pick a place. The same principle becomes a different design in each one, because the world it lands in is different.</dd></dl></div></div>'
            '<p class="note">Illustrative. The principle is one the platform learned this way; the learnings and places are drawn for this page.</p>')


def chart(j):
    cy = j["cycles"]
    bl = j.get("blind")
    pts = [(c["cycle"], c["platform_pct"], c["bare_pct"]) for c in cy]
    W, H, l, rr, t, b = 960, 340, 54, 120, 20, 44
    n = len(pts) + (1 if bl else 0)
    X = lambda i: l + i * (W - l - rr) / (n - 1)
    Y = lambda v: t + (100 - v) / 100 * (H - t - b)
    o = [f'<svg class="tr" viewBox="0 0 {W} {H}" role="img" aria-label="PADI by RSI Loop: Praxis platform against frontier AI on its own">']
    for v in (0, 25, 50, 75, 100):
        o.append(f'<line class="g" x1="{l}" x2="{W - rr + 30}" y1="{Y(v):.1f}" y2="{Y(v):.1f}"/><text class="ax" x="{l - 10}" y="{Y(v) + 4:.1f}" text-anchor="end">{v}%</text>')
    for k, col in ((1, "p"), (2, "f")):
        d = " ".join(f'{"M" if i == 0 else "L"}{X(i):.1f},{Y(p[k]):.1f}' for i, p in enumerate(pts))
        o.append(f'<path class="ln {col}" d="{d}"/>')
        o.extend(f'<circle class="dt {col}" cx="{X(i):.1f}" cy="{Y(p[k]):.1f}" r="3.4"/>' for i, p in enumerate(pts))
    for i, p in enumerate(pts):
        o.append(f'<text class="ax" x="{X(i):.1f}" y="{H - 18}" text-anchor="middle">{p[0]}</text>')
    if bl:
        i = len(pts)
        x0 = (X(i - 1) + X(i)) / 2
        o.append(f'<line class="sep" x1="{x0:.1f}" x2="{x0:.1f}" y1="{t}" y2="{H - b}"/><text class="ax" x="{X(i):.1f}" y="{H - 18}" text-anchor="middle">{bl["cycle"]} blind</text>')
        for k, col, v in ((1, "p", bl["platform_pct"]), (2, "f", bl["bare_pct"])):
            o.append(f'<circle class="dt {col} big" cx="{X(i):.1f}" cy="{Y(v):.1f}" r="6"/><text class="vl {col}" x="{X(i) + 14:.1f}" y="{Y(v) + 5:.1f}">{v}%</text>')
    o.append(f'<text class="ax" x="{l}" y="{H - 2}">RSI LOOP</text></svg>')
    return "".join(o)


CSS = r"""
.eg{--amb:#ffd166}
.oh.eh{background:radial-gradient(38% 50% at 50% 44%,rgba(91,43,255,.26),rgba(18,11,28,0) 70%),#0d0815}
.oh .cg{position:absolute;left:0;top:0;width:100%;height:100%;display:block;cursor:grab;touch-action:pan-y}
.cgh{position:absolute;left:clamp(16px,3vw,44px);top:clamp(96px,13vh,132px);max-width:340px;pointer-events:none}
.cgh .ey{font:500 10.5px var(--mono);letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.55);margin:0 0 14px}.cgh .ey::before{content:"";display:inline-block;width:5px;height:5px;background:#a48fff;margin-right:9px;vertical-align:1px}
.cgh .cgt{font:300 clamp(30px,3vw,46px)/1.05 var(--sans);letter-spacing:-.03em;margin:0 0 14px;color:#fff}.cgh .d{font:400 15px/1.5 var(--sans);color:rgba(255,255,255,.7);margin:0}
.cgc{position:absolute;right:clamp(16px,3vw,44px);top:clamp(96px,13vh,132px);width:250px;border:1px solid rgba(255,255,255,.35);background:rgba(13,8,21,.62);padding:14px 16px;font:400 10.5px/1.6 var(--mono);letter-spacing:.06em;text-transform:uppercase;color:rgba(255,255,255,.7)}
.cgc b{display:block;font-weight:500;color:#fff;padding-bottom:10px;margin-bottom:10px;border-bottom:1px solid rgba(255,255,255,.2)}.cgc p{margin:0 0 8px}
.cgm{display:none}.cgs{margin-top:12px;padding-top:10px;border-top:1px solid rgba(255,255,255,.2);color:#ffd166;min-height:3.2em}
.bowsheet{background:radial-gradient(38% 50% at 50% 44%,rgba(91,43,255,.26),rgba(18,11,28,0) 70%),#0d0815;margin-bottom:26px;overflow-x:auto}.bwi{position:relative;aspect-ratio:16/9;min-width:820px}.bwi .bow{position:absolute;left:0;top:0;width:100%;height:100%}
.bow .sil{fill:url(#bwf);stroke:rgba(200,185,255,.22);stroke-width:1}.bow .tick{stroke:rgba(200,185,255,.3)}
.bow .fib{fill:none;stroke:rgba(190,170,255,.07);stroke-width:1}.bow .fib.r{stroke:rgba(255,209,102,.08)}
.bow .pt{fill:#c8b9ff}.bow .pt.r{fill:#ffd166}
.bow .lb{font:500 10.5px var(--mono);letter-spacing:.16em;fill:rgba(225,215,255,.55)}
.bow .hd{font:500 12px var(--mono);letter-spacing:.3em;fill:#fff}.bow .sub{font:400 13px var(--sans);fill:rgba(255,255,255,.55)}
.bow .halo{animation:ehalo 4s ease-in-out infinite;transform-origin:800px 400px;transform-box:view-box}
.bow .waist rect{fill:#0d0815;stroke:#ffd166;stroke-width:1.2}.bow .w1{font:600 11px var(--mono);letter-spacing:.14em;fill:#fff}.bow .w2{font:400 10px var(--mono);fill:#ffd166}
.bow .tg circle{fill:#ffd166}.bow .tg text{font:400 17px var(--sans);fill:#fff}.bow .tg text.c{font:500 10px var(--mono);letter-spacing:.14em;fill:rgba(255,255,255,.5)}
.bow .lock rect{fill:rgba(13,8,21,.8);stroke:rgba(255,255,255,.3)}.bow .lock text{font:500 10px var(--mono);letter-spacing:.16em;fill:rgba(255,255,255,.75)}
@keyframes ehalo{50%{opacity:.55;transform:scale(1.12)}}
/* the loop sheet */
.loop{width:100%;height:auto;display:block;min-width:820px}
.loop .le{fill:none;stroke:rgba(23,19,31,.32);stroke-width:1.3}.loop marker path{fill:rgba(23,19,31,.6)}.loop .lp{fill:var(--vi)}
.loop .el{font:400 11px var(--mono);fill:var(--mut)}
.loop .nd rect{fill:#fff;stroke:var(--ink);stroke-width:1.1}.loop .nd .bar{fill:var(--vi);stroke:none}.loop .nd .t{font:600 15px var(--sans);fill:var(--ink)}.loop .nd .s{font:400 12px var(--sans);fill:var(--mut)}
.loop .nb .bar,.loop .nm .bar{fill:var(--ink)}
.loop .cyl .cb{fill:#ebe6ff;stroke:var(--vi);stroke-width:1.3}.loop .cyl .ct{fill:#fff;stroke:var(--vi);stroke-width:1.3}.loop .cyl .st{fill:none;stroke:rgba(91,43,255,.35)}
.loop .cyl .sl{font:500 10px var(--mono);letter-spacing:.06em;fill:var(--vi)}.loop .cyl .cn{font:600 12px var(--mono);letter-spacing:.3em;fill:var(--ink)}
.rail{display:grid;grid-template-columns:repeat(8,1fr);margin-top:26px;border-top:2px solid var(--ink)}
.rail div{padding:14px 12px 4px 0;font:400 13.5px/1.45 var(--sans);color:var(--mut)}.rail div+div{padding-left:12px;border-left:1px solid var(--rl)}
.rail b{display:block;font:500 11px var(--mono);letter-spacing:.1em;color:var(--vi);margin-bottom:6px}.rail strong{display:block;font:500 15px var(--sans);color:var(--ink);margin-bottom:4px}
/* overnight: how a later reader changes tomorrow's run */
.night{display:grid;grid-template-columns:1.05fr 1fr;gap:0;border:1px solid rgba(23,19,31,.35);background:#fff}
.steps{list-style:none;margin:0;padding:8px 0;counter-reset:s}.steps li{display:grid;grid-template-columns:86px 1fr;gap:16px;padding:18px 24px;border-bottom:1px solid var(--rl)}.steps li:last-child{border-bottom:0}
.steps time{font:500 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--vi);padding-top:3px}.steps h3{font:500 17px/1.3 var(--sans);margin:0 0 4px}.steps p{margin:0;color:var(--mut);font:400 14.5px/1.55 var(--sans)}
.gap{background:var(--plum);color:#e9e4ff;padding:26px;display:flex;flex-direction:column;gap:14px}
.gap .sx{color:rgba(255,255,255,.6)}.gap .sx b{color:var(--vi2)}
.gap pre{margin:0;background:#0b0712;border:1px solid rgba(255,255,255,.12);padding:16px 18px;overflow:auto;font:400 12.5px/1.65 var(--mono);white-space:pre-wrap}
.gap .k{color:#b69cff}.gap .s{color:#7ee2b8}.gap .c{color:#8a809f}.gap p{margin:0;font:400 14.5px/1.55 var(--sans);color:rgba(255,255,255,.72)}
.parts{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border:1px solid rgba(255,255,255,.18)}.parts div{padding:10px 12px;font:400 12.5px/1.45 var(--sans);color:rgba(255,255,255,.7)}.parts div+div{border-left:1px solid rgba(255,255,255,.18)}.parts b{display:block;font:500 10px var(--mono);letter-spacing:.12em;color:#ffd166;margin-bottom:4px}
/* the compression bench */
.bench{display:grid;grid-template-columns:1.15fr 1fr 1fr;background:#fff;border:1px solid rgba(23,19,31,.35);min-height:520px}
.bench>div{padding:20px;display:flex;flex-direction:column;gap:12px;min-width:0}.bench>div+div{border-left:1px solid var(--rl)}
.bh{display:flex;justify-content:space-between;align-items:baseline;gap:10px;font:500 11px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}.bh b{font-weight:500;color:var(--ink)}.bh.t2{margin-top:auto;padding-top:14px;border-top:1px solid var(--rl)}
.lcs{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
.lc{padding:8px 11px;background:#f5f3fb;border-left:3px solid rgba(91,43,255,.4);font:400 13.5px/1.42 var(--sans);transition:opacity .5s calc(var(--i)*70ms),transform .6s calc(var(--i)*70ms),background .4s,border-color .4s}
.lc span{display:block;font:500 9.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--vi);margin-bottom:2px}
.bench.done .lc.k{transform:translateX(18px);opacity:.38}.bench.done .lc.x{border-color:#e5484d;background:#fff4f4;opacity:.55;text-decoration:line-through}.bench.done .lc.f{opacity:.12;transform:translateX(-10px)}
.go{align-self:flex-start;font:500 14px var(--sans);padding:11px 18px;border:0;background:var(--ink);color:#fff;cursor:pointer;border-radius:2px}.go:hover{background:var(--vi)}.go[disabled]{background:#cfcadb;cursor:default}
.pr{flex:1;display:flex;flex-direction:column;justify-content:center}.pr .wait{color:var(--mut);font:400 14.5px/1.55 var(--sans);margin:0}
.pr .pp{font:400 20px/1.4 var(--sans);letter-spacing:-.01em;margin:0;padding:18px;border:1.5px solid var(--vi);background:#f7f5ff;animation:ein .6s cubic-bezier(.3,.7,.2,1)}
.pr ul{list-style:none;margin:12px 0 0;padding:0;font:400 12px/1.5 var(--mono);color:var(--mut)}.pr li::before{content:"· ";color:var(--vi)}
.pcs{display:flex;flex-direction:column;gap:6px}.pc{text-align:left;font:400 14.5px var(--sans);padding:10px 12px;border:1px solid var(--rl);background:#fff;color:var(--ink);cursor:pointer;border-radius:2px;transition:border-color .2s,background .2s}
.pc:hover{border-color:var(--vi)}.pc.on{background:var(--vi);border-color:var(--vi);color:#fff}.pc[disabled]{opacity:.45;cursor:default}
.out{margin:0;display:grid;gap:0}.out dt{font:500 10px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--vi);padding-top:14px}.out dd{margin:4px 0 0;padding-bottom:12px;border-bottom:1px dashed var(--rl);font:400 15px/1.45 var(--sans)}
.out.in dd,.out.in dt{animation:ein .5s both}.out dd:nth-of-type(2),.out dt:nth-of-type(2){animation-delay:.12s}.out dd:nth-of-type(3),.out dt:nth-of-type(3){animation-delay:.24s}.out dd:nth-of-type(4),.out dt:nth-of-type(4){animation-delay:.36s}
.note{font:400 13px var(--sans);color:var(--mut);margin:12px 0 0}
@keyframes ein{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
/* weights against context */
.cwt{width:100%;border-collapse:collapse;background:var(--paper);font:400 15.5px/1.45 var(--sans)}
.cwt th{text-align:left;font:500 10.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--mut);padding:12px 14px;border-bottom:2px solid var(--ink)}.cwt th:last-child{color:var(--vi)}
.cwt td{padding:15px 14px;border-bottom:1px solid var(--rl);vertical-align:top}.cwt td:first-child{font:500 13px var(--sans);color:var(--ink);width:24%}.cwt td:nth-child(2){color:var(--mut)}.cwt td:last-child{background:#f7f5ff}
.cwt tr{transition:background .2s}.cwt tbody tr:hover td:not(:last-child){background:#fff}
/* evidence */
.ev{display:grid;grid-template-columns:300px 1fr;gap:0;border:1px solid rgba(23,19,31,.35);background:#fff}
.tiles{border-right:1px solid var(--rl)}.tiles div{padding:20px 22px;border-bottom:1px solid var(--rl)}.tiles div:last-child{border-bottom:0}
.tiles b{display:block;font:300 46px/1 var(--sans);letter-spacing:-.04em;color:var(--ink);font-variant-numeric:tabular-nums}.tiles b span{font-size:.42em;color:var(--mut);letter-spacing:0;margin-left:4px}.tiles b.v{color:var(--vi)}
.tiles p{margin:8px 0 0;font:500 10.5px/1.5 var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--mut)}
.chartw{padding:22px;min-width:0}.chartw .sc{overflow-x:auto}.tr{width:100%;min-width:640px;height:auto;display:block}
.tr .g{stroke:rgba(23,19,31,.1)}.tr .ax{font:400 11px var(--mono);fill:var(--mut)}.tr .ln{fill:none;stroke-width:2}.tr .ln.p{stroke:var(--vi)}.tr .ln.f{stroke:rgba(23,19,31,.35)}
.tr .dt.p{fill:var(--vi)}.tr .dt.f{fill:#b9b4c6}.tr .sep{stroke:var(--ink);stroke-dasharray:3 4}.tr .vl{font:600 15px var(--sans)}.tr .vl.p{fill:var(--vi)}.tr .vl.f{fill:var(--mut)}
.key{display:flex;gap:18px;font:500 10.5px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--mut);margin-bottom:10px}.key i{display:inline-block;width:14px;height:3px;margin-right:7px;vertical-align:3px;background:var(--vi)}.key i.f{background:rgba(23,19,31,.35)}
.chartw p{font:400 14px/1.55 var(--sans);color:var(--mut);margin:12px 0 0;max-width:70ch}.chartw p a{color:var(--vi)}
/* laws */
.laws{display:grid;grid-template-columns:repeat(4,1fr);border-top:2px solid var(--ink)}.laws div{padding:20px 20px 24px 0;border-bottom:1px solid var(--rl)}.laws div:not(:nth-child(4n+1)){padding-left:20px;border-left:1px solid var(--rl)}
.laws b{display:block;font:500 11px var(--mono);letter-spacing:.1em;color:var(--vi);margin-bottom:8px}.laws h3{font:400 20px/1.25 var(--sans);letter-spacing:-.01em;margin:0 0 6px}.laws p{margin:0;color:var(--mut);font:400 14.5px/1.55 var(--sans)}
/* research */
.res{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border:1px solid rgba(23,19,31,.35);background:var(--paper)}
.res a{display:flex;flex-direction:column;gap:10px;padding:22px;text-decoration:none;min-height:230px;transition:background .25s}.res a+a{border-left:1px solid var(--rl)}.res a:hover{background:#fff}
.res .ty{font:500 10.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--vi)}.res h3{font:400 22px/1.2 var(--sans);letter-spacing:-.015em;margin:0}.res p{margin:0;color:var(--mut);font:400 14.5px/1.5 var(--sans)}.res .dt{margin-top:auto;font:400 12px var(--mono);color:var(--mut)}
@media (max-width:1000px){.night,.ev,.bench{grid-template-columns:1fr}.bench>div+div{border-left:0;border-top:1px solid var(--rl)}.tiles{border-right:0;border-bottom:1px solid var(--rl)}.rail{grid-template-columns:repeat(4,1fr)}.rail div:nth-child(5){border-left:0;padding-left:0}.laws,.res{grid-template-columns:1fr 1fr}.laws div:not(:nth-child(4n+1)){padding-left:0;border-left:0}.laws div:nth-child(even){padding-left:20px;border-left:1px solid var(--rl)}.res a:nth-child(3){border-left:0}.res a:nth-child(n+3){border-top:1px solid var(--rl)}}
@media (max-width:760px){.rail,.laws,.res,.parts{grid-template-columns:1fr}.rail div+div,.parts div+div{border-left:0;padding-left:0;border-top:1px solid var(--rl)}.laws div:nth-child(even){padding-left:0;border-left:0}.res a+a{border-left:0;border-top:1px solid var(--rl)}.cgc{display:none}.cgh{max-width:none;right:16px;top:84px}.cgm{display:block;margin:12px 0 0;font:500 10px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:#ffd166}.cgh .d{font-size:14px}.cwt td:first-child{width:auto}.cwt{font-size:14px}.steps li{grid-template-columns:1fr;gap:4px}}
@media (prefers-reduced-motion:reduce){.bow *,.loop *{animation:none!important}}
"""

JS = r"""<script>(function(){
var P=window.ENGRAM_PLACES||{},b=document.getElementById('bench');if(!b)return;
var go=document.getElementById('bcmp'),pr=document.getElementById('bpr'),ver=document.getElementById('bver'),out=document.getElementById('bout'),pl=document.getElementById('bplace'),cs=[].slice.call(b.querySelectorAll('.pc'));
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')}
cs.forEach(function(c){c.disabled=true});
go.addEventListener('click',function(){b.classList.add('done');go.disabled=true;go.textContent='Compressed';
 setTimeout(function(){ver.textContent='routing · v7';pr.innerHTML='<p class="pp">'+esc(window.ENGRAM_PRINCIPLE)+'</p><ul><li>distilled from 6 learnings, each one cited</li><li>1 contradiction resolved: one role cannot own every warning</li><li>1 note faded: it never changed a design</li><li>supersedes v6, which stays readable</li></ul>';
  cs.forEach(function(c){c.disabled=false});cs[0].click()},700)});
cs.forEach(function(c){c.addEventListener('click',function(){if(c.disabled)return;cs.forEach(function(x){x.classList.toggle('on',x===c)});var p=P[c.getAttribute('data-p')];pl.textContent=p[0];
 out.classList.remove('in');void out.offsetWidth;out.innerHTML=p[1].map(function(r){return '<dt>'+esc(r[0])+'</dt><dd>'+esc(r[1])+'</dd>'}).join('');out.classList.add('in')})});
})();</script>"""


def build():
    import json, padi
    j = padi.load()
    bl = (j or {}).get("blind") or (j or {}).get("latest") or {}
    hero = ('<section class="oh eh"><canvas id="cg" class="cg" role="img" aria-label="Context graph: agent and domain clusters around one shared memory. Work captured in one cluster is compressed into a versioned brief, trained, and reinflated into another domain."></canvas><div class="shade"></div>'
            '<div class="cgh"><p class="ey">Why it compounds</p><p class="cgt">Context is the moat.</p><p class="d">Every operation can host the same open weights models. Context is what compounds.</p><p class="cgm" id="cgst2">01 CAPTURE</p></div>'
            '<aside class="cgc"><b>Many agents. One memory.</b><p>Every agent works on its own. None of them starts from zero.</p><p>Runs compress into principles. Principles reinflate into new work.</p><p>Every run trains the system.</p><div class="cgs" id="cgst">01 CAPTURE</div></aside>'
            '<div class="hc">'
            f'<div class="wmb"><h1 class="wm" aria-label="Hyper Engram"><svg viewBox="0 0 38 30" aria-hidden="true"><path d="{MARK}"/></svg><span>Engram</span></h1><p class="wtag">Dedicated inference for your sovereign AI models.</p></div>'
            '<div class="tblk"><span>Product</span><span>Hyper Engram</span><span>Trains</span><span>Sovereign AI models</span>'
            '<span>Into</span><span>Weights and memory</span><span>Runs</span><span>On premises · air gapped</span>'
            f'<div class="acts"><a href="{brand.COMMERCIAL}">{brand.TALK} →</a><a href="#research">Read the research →</a></div></div></div></section>')
    statement = ('<section class="ost"><div class="wrap3"><div>' + sx(0, "Overview") + '</div><div>'
                 '<p class="st" data-type>Train sovereign AI models <em>in their weights and in their memory,</em> on premises and in air gapped environments.</p>'
                 '<p class="sub" data-after>Hyper Engram turns the work an operation does into training signal for the open weights models it hosts. Runs, outcomes and corrections are captured as episodes, compressed into versioned principles and applied two ways: post training into the model\'s weights, and agentic memory the model reads at inference. Training data, weights and memory never leave the perimeter.</p></div></div></section>')
    loop = ('<section class="osec"><div class="wrap3">' + head(1, "The learning loop", "Recursive improvement, <em>one loop at a time.</em>",
            "A master agent runs each RSI Loop. Two routines distil and verify what was learned every day. They never call each other directly: each reads and writes one shared memory, which the model reasons over at inference.")
            + '<div class="sheet"><div class="scrollx">' + loop_svg() + '</div><div class="tb"><span>Sheet 01</span><span>Recursive learning loop</span><span>Hyper Engram</span></div></div>'
            '<div class="rail">'
            + "".join(f'<div data-after><b>{a}</b><strong>{h}</strong>{t}</div>' for a, h, t in [
                ("A", "Read", "Where the last loop left the platform and both routines."), ("B", "Plan", "A short ranked list of changes, each with its measure."),
                ("C", "Build", "Small commits, every release tagged and reversible."), ("D", "Real requirements", "Designs on documents nobody wrote for a test."),
                ("E", "Benchmark", "Fresh tasks against frontier AI on its own."), ("F", "Premortem", "Would the design have caught a real incident?"),
                ("G", "Feed the routines", "Every finding written into memory for its owner."), ("H", "Close", "What the loop learned, read first by the next one.")])
            + '</div></div></section>')
    stages = [("01", "cap", "Capture", "Every run becomes training data.", "Each run is kept as an episode with its outcome, its feedback and the corrections a reviewer made, inside your perimeter."),
              ("02", "cmp", "Compress", "Distillation into principles.", "Daily routines distil raw learnings into versioned principles that cite their sources. Contradictions are resolved and what never mattered fades."),
              ("03", "trn", "Train", "Into the weights.", "Curated episodes and principles become post training data for the open weights models you host, trained on your own hardware."),
              ("04", "rec", "Reinflate", "Into memory, at inference.", "The model reads the compressed memory and expands it into the problem in front of it: this site, these regulations, these people.")]
    stage_html = ('<div class="specs">' + "".join(f'<div class="spec"><span class="no">{no}</span>{glyph(g)}<h3>{h}</h3><p><strong>{E(s)}</strong> {E(t)}</p></div>' for no, g, h, s, t in stages) + '</div>')
    platform = ('<section class="osec"><div class="wrap3">' + head(2, "Platform", "Four stages. <em>One training platform.</em>",
                "Capture, compress, train and reinflate. Every stage runs inside your perimeter, on premises or air gapped, on models you host.")
                + '<div class="bowsheet"><div class="bwi">' + bowtie_svg() + '</div></div>' + stage_html + '</div></section>')
    night = ('<section class="osec"><div class="wrap3">' + head(3, "Reinterpretation", "Learned tonight. <em>Used tomorrow morning.</em>",
             "Each routine opens its run by reading the feedback and gap records on its newest episodes. A rule recorded today changes tomorrow\'s behaviour, with no code change.")
             + '<div class="night"><ol class="steps">'
             + "".join(f'<li data-after><time>{a}</time><div><h3>{h}</h3><p>{t}</p></div></li>' for a, h, t in [
                 ("Day 1", "A run misses something", "A design senses the warning a real incident would have started with, and never says who must act on it."),
                 ("Evening", "A later reader finds it", "The master agent reads the run and files a gap record on its episode: what was missed, the fix, and a rule for next time, written in the routine's own terms."),
                 ("Day 2, first thing", "The routine reads before it acts", "Its intake lists every rule in force. The rule is now part of how it works, with no change to its code."),
                 ("Next loop", "The record closes, or it does not", "The next RSI Loop checks whether the gap closed. A record still open is the first item of the next plan.")])
             + '</ol><div class="gap">' + sx(3, "One gap record") +
             '<pre><span class="c">// filed on the routine\'s newest episode</span>\n{\n  <span class="k">gap</span>: <span class="s">"designs sense the warning but never name who acts"</span>,\n'
             '  <span class="k">fix</span>: <span class="s">"brief a routing principle from general practice"</span>,\n  <span class="k">found_by</span>: <span class="s">"master agent"</span>,\n  <span class="k">status</span>: <span class="s">"open"</span>,\n'
             '  <span class="k">rule_for_next_time</span>: <span class="s">"every sensed warning names the role\n    that acts, the reading that starts the clock\n    and the options of the decision"</span>\n}</pre>'
             '<div class="parts"><div><b>EPISODE</b>What the run did and measured.</div><div><b>FEEDBACK</b>What was wrong with how it worked, with a verdict.</div><div><b>GAP RECORDS</b>What a later reader found it missed.</div></div>'
             '<p>Every learner in the system, from the routines to the fleet, keeps its episodes in this one shape, so any reader can correct any writer.</p></div></div></div></section>')
    bench_s = ('<section class="osec" id="bench-s"><div class="wrap3">' + head(4, "Compression bench", "Compress once. <em>Reinflate anywhere.</em>",
               "Eight raw learnings are compressed into one principle, which the model reinflates into designs for operations it has never seen.")
               + '<div class="sheet">' + bench() + '<div class="tb"><span>Sheet 04</span><span>Compression and reinflation</span><span>Illustrative</span></div></div></div></section>')
    rows = [("Best for", "Stable skills used at high volume", "Knowledge that changes every month"),
            ("A new regulation arrives", "Joins the next training run", "One new entry, verified and live within hours"),
            ("Reading what was learned", "Measured through evaluation", "Every principle lists the learnings it came from"),
            ("A stronger base model arrives", "The training run is repeated on it", "The memory carries over on day one"),
            ("Undoing a lesson", "Roll back to an earlier checkpoint", "Retire one versioned principle"),
            ("Where it runs", "Inside your perimeter, on models you host", "Inside your perimeter, on your infrastructure")]
    vs = ('<section class="osec"><div class="wrap3">' + head(5, "Weights and memory", "Two training targets. <em>One platform.</em>",
          "Engram places each lesson where it does the most good. Stable skills used at volume are trained into the weights. Knowledge that changes with the operation is kept in memory, where it stays current, readable and reversible.")
          + '<table class="cwt"><thead><tr><th></th><th>Into the weights</th><th>Into memory</th></tr></thead><tbody>'
          + "".join(f'<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in rows) + '</tbody></table></div></section>')
    ev = ""
    if j:
        tasks_ahead = bl.get("platform_ahead_on_tasks")
        n_t = bl.get("tasks")
        tile_ahead = f'<div><b>{tasks_ahead}<span>of {n_t}</span></b><p>Unseen tasks where Praxis came out ahead</p></div>' if tasks_ahead is not None and n_t else ""
        ev = ('<section class="osec"><div class="wrap3">' + head(6, "Evidence", "Measured <em>every loop.</em>",
              "Praxis, trained on Engram, is measured on PADI, our benchmark for physical AI system design, against frontier AI on its own, on fresh tasks every RSI Loop.")
              + '<div class="ev"><div class="tiles">'
              f'<div><b class="v">{bl.get("platform_pct")}%</b><p>Praxis, RSI Loop {bl.get("cycle")}, blind</p></div>'
              f'<div><b>{bl.get("bare_pct")}%</b><p>Frontier AI on its own, same tasks</p></div>' + tile_ahead +
              f'<div><b>{j["benchmark"]["sectors_measured"]}</b><p>Industries measured, in three countries</p></div></div>'
              '<div class="chartw"><div class="key"><span><i></i>Praxis platform</span><span><i class="f"></i>Frontier AI on its own</span></div><div class="sc">' + chart(j) + '</div>'
              f'<p>Checks passed as a share of checks judged, each RSI Loop. Loop {bl.get("cycle")} is a blind evaluation on tasks the platform had never seen; earlier loops reused some tasks and show the trend. Results are public; the method stays private. <a href="{BASE}/padi/">Every figure on PADI →</a></p></div></div></div></section>')
    laws = [("Train where it belongs", "Stable skills go into the weights. Knowledge that changes goes into memory."),
            ("Meaning, never keywords", "Any decision about what a sentence means is put to a model and stored. Keyword scoring is banned."),
            ("Every claim stands on a source", "An entry needs a dated source. A principle needs the learnings it was distilled from."),
            ("Evaluation stays blind", "Held out tasks are never shown to the planner. Incident cases never feed the memory."),
            ("Two agents, two views", "Every writer has an adversarial verifier. Nothing verifies its own output."),
            ("The record is the context", "Commits, episodes and gap records carry the why. A session that lost its memory reads the log first."),
            ("Every release is reversible", "Each RSI Loop is tagged. A bad change is reverted by its own commit, a bad principle by its own version."),
            ("Sovereign by design", "Training data, weights and memory stay in your perimeter, on premises or air gapped.")]
    laws_s = ('<section class="osec"><div class="wrap3">' + head(7, "Principles", "Eight rules <em>every loop keeps.</em>", "They hold across every phase and every agent. A change that would bend one stops for human review.")
              + '<div class="laws">' + "".join(f'<div data-after><b>{k + 1:02d}</b><h3>{E(h)}</h3><p>{E(t)}</p></div>' for k, (h, t) in enumerate(laws)) + '</div></div></section>')
    res = [(MEMO, "Memo", "Compression and Reinflation", "Compression, reinflation, and why what a system learns should survive the next model.", "Muhammad Umar · 10 Oct 2026"),
           (f"{BASE}/agentic-memory-architecture/", "Architecture", "Agentic Memory Architecture", "Memory told as a bow tie: experience, a waist of nightly distillation, and context assembled for each design.", "23 Oct 2026"),
           (f"{BASE}/padi/", "Benchmark", "Physical AI Design Index", "Fresh tasks across 13 industries in three countries, Praxis against frontier AI on its own.", "Updated every RSI Loop"),
           (f"{BASE}/hyper-pragma/", "Product", "Memory at work in Hyper Pragma", "The same memory inside a product: every run graded, every lesson visible, every lesson revocable.", "Hyper stack")]
    res_s = ('<section class="osec" id="research"><div class="wrap3">' + head(8, "Research", "Read how <em>it works.</em>", "The argument, the architecture, the measurements and the product, each on its own page.")
             + '<div class="res">' + "".join(f'<a href="{u}"><span class="ty">{t}</span><h3>{E(h)}</h3><p>{E(p)}</p><span class="dt">{E(d)} →</span></a>' for u, t, h, p, d in res) + '</div></div></section>')
    cta = (f'<section><div class="wrap3"><div class="octa"><div>Project<b>Hyper Engram</b></div><div>Trains<b>Weights and memory</b></div>'
           f'<a class="t" href="{brand.COMMERCIAL}">{brand.TALK} <span>→</span></a><a class="s" href="{MEMO}">Read the memo <span>→</span></a></div></div></section>')
    faq = [("What is Hyper Engram?", "Hyper Engram is CodeNinja's platform for training sovereign AI models on premises and in air gapped environments. It trains open weights models in their weights and in their memory, from the runs, outcomes and corrections of the operation they serve."),
           ("How does Hyper Engram train a model?", "Runs are captured as episodes and compressed daily into versioned principles that cite their sources. Curated episodes and principles become post training data for the model's weights, and the same principles form an agentic memory the model reads at inference."),
           ("What is compression and reinflation?", "Compression turns many observations into one small principle, resolving contradictions and dropping what never mattered. Reinflation is the model expanding that principle into a new situation: a different country, operation or set of people. The idea follows Michael Levin's work on self improvising memory in living systems."),
           ("What goes into the weights and what into memory?", "Stable skills used at high volume are trained into the weights, where they are fastest and cheapest to serve. Knowledge that changes with the operation, such as regulations, equipment and procedures, is kept in memory, where it is current within hours and can be read and reversed."),
           ("What happens when a better base model is released?", "It is swapped in. The memory carries over unchanged, and the curated training data is applied to the new base model."),
           ("Where does Hyper Engram run?", "Inside the customer's perimeter: on premises, in a private cloud or fully air gapped, on models the customer hosts. Training data, weights and memory never leave it.")]
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    depth = ('<section class="odep"><div class="wrap3 dg"><aside>' + sx(9, "In depth") + '<h2 data-type>Questions about Hyper Engram</h2></aside><div class="doc">'
             + "".join(f'<h2>{E(q)}</h2><p>{E(a)}</p>' for q, a in faq) + '</div></div></section>')
    data = f'<script>window.ENGRAM_PRINCIPLE={json.dumps(PRINCIPLE)};window.ENGRAM_PLACES={json.dumps(PLACES)};window.ENGRAM_GRAPH={json.dumps({"c": CLUSTERS, "s": SCENES})};</script>'
    body = f'<main class="og eg">{hero}{statement}{loop}{platform}{night}{bench_s}{vs}{ev}{laws_s}{res_s}{cta}{depth}</main>{data}'
    title = "Hyper Engram: Train Sovereign AI Models On Premises and Air Gapped | CodeNinja Atoms"
    desc = "Hyper Engram trains sovereign AI models in their weights and in their memory, on premises and in air gapped environments, from every run of the operation."
    ld = [{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Hyper Engram", "applicationCategory": "DeveloperApplication", "description": desc, "url": URL,
           "creator": {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"},
           "featureList": ["Episodes with feedback and gap records", "Daily distillation into versioned principles", "Adversarial verification of every writer",
                           "Post training of open weights models on your hardware", "Agentic memory by compression and reinflation", "Memory carried across model upgrades", "Runs inside the customer's perimeter"],
           "isRelatedTo": [{"@type": "SoftwareApplication", "name": "Hyper Pragma", "url": f"{BASE}/hyper-pragma/"}, {"@type": "SoftwareApplication", "name": "Hyper Ontology", "url": f"{BASE}/hyper-ontology/"},
                           {"@type": "Article", "name": "Compression and Reinflation", "url": MEMO}]}, faq_ld]
    return shell(title, desc, URL, ld, OCSS + CSS, body, JS + GRAPH_JS + TYPE_JS)
