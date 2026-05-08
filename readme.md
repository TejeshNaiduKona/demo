---
title: README
emoji: 🏃
colorFrom: green
colorTo: indigo
sdk: static
pinned: false
---
<style>
/* ---------- scoped to .bsh so it can't leak into the README around it ---------- */
.bsh {
--cream: #f6efe1;
--paper: #fbf6e8;
--walnut: #5a3a22;
--bark:  #3a2516;
--ink:   #2a2118;
--copper:#c98a3c;
--rust:  #8a4a2b;
--moss:  #5a6b3a;
--sage:  #7a8c4a;
--sun:   #e6a85c;
--mush:  #b8553a;
--line:  #8a6a48;
max-width: 1000px;
margin: 0 auto;
padding: 0;
color: var(--ink);
font-family: Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
font-size: 16px;
line-height: 1.55;
background:
radial-gradient(ellipse at 20% 10%, rgba(201,138,60,0.08), transparent 50%),
radial-gradient(ellipse at 80% 90%, rgba(90,107,58,0.08), transparent 50%),
repeating-linear-gradient(0deg, rgba(138,106,72,0.025) 0 1px, transparent 1px 3px),
var(--cream);
border: 2px solid var(--walnut);
border-radius: 14px;
box-shadow:
inset 0 0 0 1px var(--cream),
inset 0 0 0 6px var(--walnut),
inset 0 0 0 8px var(--cream),
inset 0 0 0 9px var(--copper),
0 6px 24px rgba(58,37,22,0.18);
overflow: hidden;
}
.bsh * { box-sizing: border-box; }
.bsh .pad { padding: 36px 44px; }

/* ---------- type ---------- */
.bsh h1, .bsh h2, .bsh h3 { font-family: Georgia, "Iowan Old Style", serif; color: var(--bark); margin: 0; letter-spacing: -0.01em; }
.bsh h1 { font-size: 56px; line-height: 0.95; font-weight: 700; }
.bsh h2 { font-size: 28px; line-height: 1.1; font-weight: 700; }
.bsh h3 { font-size: 18px; line-height: 1.2; font-weight: 700; }
.bsh p  { margin: 0 0 12px 0; }
.bsh .small { font-size: 13px; }
.bsh .mono { font-family: "SFMono-Regular", Menlo, Consolas, monospace; }
.bsh .caps { text-transform: uppercase; letter-spacing: 0.18em; font-size: 11px; font-weight: 700; }
.bsh .muted { color: var(--walnut); opacity: 0.78; }
.bsh a { color: var(--rust); text-decoration: underline; text-decoration-style: dotted; text-underline-offset: 3px; }
.bsh a:hover { color: var(--bark); text-decoration-style: solid; }
/* ---------- top strip ---------- */
.bsh .strip {
display: flex; align-items: center; justify-content: space-between; gap: 24px;
padding: 14px 44px;
background: var(--bark);
color: var(--cream);
border-bottom: 1px dashed rgba(246,239,225,0.35);
}
.bsh .strip .who { display: flex; gap: 24px; flex-wrap: wrap; align-items: center; }
.bsh .strip .who span.caps { color: var(--sun); }
.bsh .strip .dates { font-family: Georgia, serif; font-style: italic; font-size: 14px; color: var(--cream); }
.bsh .strip .dates b { color: var(--sun); font-style: normal; font-weight: 700; letter-spacing: 0.02em; }
/* ---------- header ---------- */
.bsh .header { padding: 44px 44px 28px; position: relative; }
.bsh .header::before {
content: "";
position: absolute; left: 44px; right: 44px; bottom: 18px; height: 1px;
background: var(--walnut);
box-shadow: 0 4px 0 -1px var(--cream), 0 5px 0 -1px var(--walnut);
}
.bsh .eyebrow { display: inline-flex; align-items: center; gap: 10px; color: var(--rust); font-weight: 700; }
.bsh .eyebrow .dingbat { font-size: 16px; opacity: 0.7; }
.bsh .title-row { display: flex; align-items: flex-end; justify-content: space-between; gap: 20px; margin-top: 12px; flex-wrap: wrap; }
.bsh .title-row h1 em { font-style: italic; color: var(--rust); }
.bsh .seal {
width: 110px; height: 110px; flex-shrink: 0;
border-radius: 50%;
background: var(--paper);
border: 2px dashed var(--walnut);
box-shadow: inset 0 0 0 6px var(--paper), inset 0 0 0 7px var(--copper);
display: flex; align-items: center; justify-content: center;
color: var(--bark);
text-align: center;
font-family: Georgia, serif;
font-size: 11px;
line-height: 1.15;
letter-spacing: 0.08em;
text-transform: uppercase;
font-weight: 700;
transform: rotate(-6deg);
position: relative;
}
.bsh .seal::before {
content: "✦"; position: absolute; top: 8px; left: 50%; transform: translateX(-50%); font-size: 10px; color: var(--copper);
}
.bsh .seal::after {
content: "✦"; position: absolute; bottom: 8px; left: 50%; transform: translateX(-50%); font-size: 10px; color: var(--copper);
}
.bsh .seal .seal-inner { padding: 0 8px; }
/* ---------- section header ---------- */
.bsh .section { padding: 40px 44px; border-top: 1px solid rgba(138,106,72,0.25); position: relative; }
.bsh .section.no-rule { border-top: none; }
.bsh .section-label {
display: inline-flex; align-items: center; gap: 10px;
color: var(--moss); font-weight: 700;
margin-bottom: 14px;
}
.bsh .section-label .ornament { color: var(--copper); }
.bsh .section h2 { margin-bottom: 8px; }
.bsh .lede { font-size: 17px; line-height: 1.6; max-width: 68ch; color: var(--bark); }
/* ---------- intro pull ---------- */
.bsh .intro p + p { margin-top: 12px; }
.bsh .intro .pull {
border-left: 3px double var(--copper);
padding: 4px 0 4px 16px;
margin: 18px 0 6px;
font-style: italic;
color: var(--bark);
font-size: 17px;
}
/* ---------- two-track grid ---------- */
.bsh .tracks { display: grid; grid-template-columns: 1fr 1fr; gap: 22px; margin-top: 18px; }
.bsh .track {
background: var(--paper);
border: 1.5px dashed var(--walnut);
border-radius: 10px;
padding: 24px 22px 22px;
position: relative;
transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.bsh .track:hover {
transform: translateY(-2px);
box-shadow: 0 8px 18px rgba(58,37,22,0.12);
}
.bsh .track .chap {
position: absolute; top: -12px; left: 18px;
background: var(--cream); color: var(--moss);
padding: 2px 10px; border: 1px solid var(--moss); border-radius: 999px;
font-size: 10px; letter-spacing: 0.18em; font-weight: 700; text-transform: uppercase;
}
.bsh .track .ico {
font-size: 36px; line-height: 1; margin-bottom: 10px;
filter: drop-shadow(0 2px 0 rgba(58,37,22,0.08));
}
.bsh .track h3 {
font-size: 22px; line-height: 1.15; margin-bottom: 8px; color: var(--bark);
}
.bsh .track p { font-size: 15px; line-height: 1.55; color: var(--ink); margin-bottom: 14px; }
.bsh .track .judged { border-top: 1px dotted var(--line); padding-top: 12px; margin-top: 4px; }
.bsh .track .judged .caps { color: var(--rust); margin-bottom: 8px; display: block; }
.bsh .track ul { list-style: none; margin: 0; padding: 0; }
.bsh .track ul li { font-size: 14px; line-height: 1.5; padding-left: 20px; position: relative; margin-bottom: 6px; color: var(--bark); }
.bsh .track ul li::before { content: "✦"; position: absolute; left: 0; top: 0; color: var(--copper); font-size: 12px; }
/* ---------- constraints ---------- */
.bsh .constraints { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 18px; }
.bsh .constraint {
border: 1.5px solid var(--walnut);
border-radius: 8px;
padding: 20px 18px 18px;
background: linear-gradient(180deg, var(--paper) 0%, var(--cream) 100%);
position: relative;
}
.bsh .constraint .num {
position: absolute; top: -16px; left: 16px;
width: 32px; height: 32px; border-radius: 50%;
background: var(--bark); color: var(--sun);
display: flex; align-items: center; justify-content: center;
font-family: Georgia, serif; font-weight: 700; font-size: 16px;
border: 3px solid var(--cream);
}
.bsh .constraint h3 { font-size: 16px; margin-bottom: 6px; color: var(--bark); }
.bsh .constraint p { font-size: 14px; line-height: 1.5; margin: 0; color: var(--ink); }
/* ---------- merit badges ---------- */
.bsh .sash {
margin-top: 22px;
background:
repeating-linear-gradient(135deg, rgba(58,37,22,0.04) 0 8px, transparent 8px 16px),
var(--paper);
border: 1.5px dashed var(--walnut);
border-radius: 12px;
padding: 28px 26px 26px;
position: relative;
}
.bsh .sash::before, .bsh .sash::after {
content: ""; position: absolute; left: 50%; transform: translateX(-50%);
width: 60px; height: 12px;
background:
linear-gradient(90deg, transparent 0 6px, var(--copper) 6px 100%) no-repeat,
linear-gradient(90deg, var(--copper) 0 100%) no-repeat;
background-size: 100% 2px, 100% 100%;
background-position: 0 0, 0 0;
}
.bsh .sash::before { top: -1px; background: var(--copper); border-radius: 0 0 4px 4px; height: 6px; width: 80px; }
.bsh .sash::after { bottom: -1px; background: var(--copper); border-radius: 4px 4px 0 0; height: 6px; width: 80px; }
.bsh .badges {
display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px 20px;
margin-top: 8px;
}
.bsh .badge {
display: flex; gap: 14px; align-items: flex-start;
padding: 8px;
border-radius: 10px;
transition: background 0.18s ease;
}
.bsh .badge:hover { background: rgba(201,138,60,0.10); }
.bsh .badge .patch {
width: 76px; height: 76px; flex-shrink: 0;
border-radius: 50%;
background: var(--cream);
border: 2px dashed var(--walnut);
box-shadow:
inset 0 0 0 5px var(--cream),
inset 0 0 0 6px var(--copper),
0 3px 0 rgba(58,37,22,0.12);
display: flex; align-items: center; justify-content: center;
font-size: 30px;
transition: transform 0.25s ease, box-shadow 0.25s ease;
position: relative;
}
.bsh .badge:hover .patch {
transform: rotate(-6deg) scale(1.04);
box-shadow:
inset 0 0 0 5px var(--cream),
inset 0 0 0 6px var(--rust),
0 5px 0 rgba(58,37,22,0.18);
}
.bsh .badge .patch.moss   { background: #eaeed8; }
.bsh .badge .patch.copper { background: #f6e3c4; }
.bsh .badge .patch.rust   { background: #f1d6c7; }
.bsh .badge .patch.sun    { background: #f7e8c6; }
.bsh .badge .patch.cream  { background: #f3e8d0; }
.bsh .badge .patch.olive  { background: #e8e7c8; }
.bsh .badge .meta { flex: 1; min-width: 0; padding-top: 4px; }
.bsh .badge .meta .name { font-weight: 700; font-size: 15px; color: var(--bark); margin-bottom: 2px; }
.bsh .badge .meta .desc { font-size: 13px; line-height: 1.45; color: var(--ink); }
.bsh .badge .meta .tag {
display: inline-block; margin-top: 6px;
font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase; font-weight: 700;
color: var(--moss);
}
.bsh .badge .meta .tag.tentative { color: var(--rust); }
/* ---------- numbered ledger ---------- */
.bsh .ledger {
border: 1px solid var(--walnut);
border-radius: 8px;
overflow: hidden;
background: var(--paper);
margin-top: 18px;
}
.bsh .ledger .row {
display: grid; grid-template-columns: 56px 1fr; align-items: stretch;
border-bottom: 1px dashed rgba(138,106,72,0.45);
}
.bsh .ledger .row:last-child { border-bottom: none; }
.bsh .ledger .row .n {
background: var(--bark); color: var(--sun);
display: flex; align-items: center; justify-content: center;
font-family: Georgia, serif; font-weight: 700; font-size: 22px;
border-right: 1px dashed rgba(246,239,225,0.3);
}
.bsh .ledger .row:hover .n { background: var(--rust); color: var(--cream); }
.bsh .ledger .row .body { padding: 14px 18px; }
.bsh .ledger .row .body .name { font-weight: 700; color: var(--bark); font-size: 16px; }
.bsh .ledger .row .body .desc { font-size: 14px; color: var(--ink); margin-top: 2px; }
/* ---------- resources ---------- */
.bsh .resources { display: grid; grid-template-columns: 1fr 1fr; gap: 10px 22px; margin-top: 14px; }
.bsh .resources a {
display: flex; align-items: center; justify-content: space-between;
padding: 10px 14px; border: 1px dashed var(--walnut); border-radius: 6px;
background: var(--paper); text-decoration: none; color: var(--bark);
font-size: 14px; font-weight: 700;
transition: background 0.15s ease, transform 0.15s ease;
}
.bsh .resources a:hover { background: var(--cream); transform: translateX(2px); border-style: solid; }
.bsh .resources a .arr { color: var(--rust); font-family: Georgia, serif; }
/* ---------- timeline / map ---------- */
.bsh .map {
margin-top: 18px;
background:
radial-gradient(circle at 12% 22%, rgba(90,107,58,0.10), transparent 22%),
radial-gradient(circle at 88% 78%, rgba(201,138,60,0.10), transparent 24%),
var(--paper);
border: 1.5px solid var(--walnut);
border-radius: 10px;
padding: 22px 22px 18px;
position: relative;
}
.bsh .map .map-head { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 14px; }
.bsh .map .map-head .compass { font-size: 22px; color: var(--rust); }
.bsh .stops { position: relative; padding: 6px 0 0; }
.bsh .stops::before {
content: ""; position: absolute; left: 43px; top: 18px; bottom: 18px;
border-left: 2px dashed var(--copper);
}
.bsh .stop {
display: grid; grid-template-columns: 76px 160px 1fr; align-items: center; gap: 14px;
padding: 10px 6px; border-radius: 6px; position: relative;
transition: background 0.15s ease;
}
.bsh .stop:hover { background: rgba(201,138,60,0.08); }
.bsh .stop .pin {
width: 38px; height: 38px; border-radius: 50%;
background: var(--cream);
border: 2px solid var(--walnut);
box-shadow: inset 0 0 0 3px var(--cream), inset 0 0 0 4px var(--copper);
display: flex; align-items: center; justify-content: center;
font-family: Georgia, serif; font-weight: 700; color: var(--bark); font-size: 14px;
margin-left: 19px; position: relative; z-index: 1;
}
.bsh .stop:hover .pin { background: var(--sun); }
.bsh .stop .when { font-style: italic; color: var(--rust); font-size: 14px; }
.bsh .stop .what { color: var(--bark); }
.bsh .stop .what b { color: var(--bark); font-weight: 700; }
.bsh .stop .what .note { display: block; font-size: 13px; color: var(--ink); opacity: 0.85; }
/* ---------- final cta ---------- */
.bsh .cta {
background:
repeating-linear-gradient(45deg, rgba(58,37,22,0.04) 0 6px, transparent 6px 12px),
linear-gradient(180deg, #2f1f12, var(--bark));
color: var(--cream);
padding: 36px 44px 40px;
text-align: center;
border-top: 6px double var(--copper);
position: relative;
}
.bsh .cta h2 { color: var(--cream); font-size: 38px; }
.bsh .cta h2 em { color: var(--sun); font-style: italic; }
.bsh .cta p { color: rgba(246,239,225,0.85); font-size: 16px; max-width: 56ch; margin: 10px auto 22px; }
.bsh .cta .button {
display: inline-block; padding: 14px 26px;
background: var(--sun); color: var(--bark);
border: 2px solid var(--sun);
border-radius: 999px;
font-weight: 700; font-size: 16px; text-decoration: none;
letter-spacing: 0.04em;
box-shadow: 0 4px 0 rgba(0,0,0,0.25);
transition: transform 0.15s ease, box-shadow 0.15s ease, background 0.15s ease;
}
.bsh .cta .button:hover {
background: var(--cream); border-color: var(--cream);
transform: translateY(-2px);
box-shadow: 0 6px 0 rgba(0,0,0,0.3);
}
.bsh .cta .links { margin-top: 18px; font-size: 13px; }
.bsh .cta .links a { color: var(--sun); margin: 0 10px; }
.bsh .cta .placeholder { display: block; margin-top: 10px; font-size: 11px; color: rgba(246,239,225,0.5); font-style: italic; letter-spacing: 0.1em; text-transform: uppercase; }
/* ---------- responsive ---------- */
@media (max-width: 760px) {
.bsh .pad, .bsh .header, .bsh .section, .bsh .strip, .bsh .cta { padding-left: 22px; padding-right: 22px; }
.bsh h1 { font-size: 40px; }
.bsh .tracks, .bsh .constraints, .bsh .badges, .bsh .resources { grid-template-columns: 1fr; }
.bsh .stop { grid-template-columns: 76px 1fr; }
.bsh .stop .when { grid-column: 2; padding-left: 0; }
.bsh .stop .what { grid-column: 2; }
.bsh .seal { display: none; }
}
/* ---------- decorative svg dividers ---------- */
.bsh .ornament-rule {
display: flex; align-items: center; gap: 12px;
color: var(--copper);
margin: 18px 0 22px;
}
.bsh .ornament-rule::before, .bsh .ornament-rule::after {
content: ""; flex: 1; height: 0;
border-top: 1px solid var(--walnut);
border-bottom: 1px solid var(--walnut);
height: 3px;
}
</style>
<div class="bsh">
<!-- top strip -->
<div class="strip">
<div class="who">
<span><span class="caps">Hosted by</span> &nbsp;<b style="color:#f6efe1; font-family:Georgia,serif;">Gradio</b> · <b style="color:#f6efe1; font-family:Georgia,serif;">Hugging Face</b></span>
<span><span class="caps">Sponsored by</span> &nbsp;<span class="mono" style="color:#f6efe1; opacity:0.7;">[ coming soon ]</span>
<span><span class="caps">Cash Prizes</span> &nbsp;<span class="mono" style="color:#f6efe1; opacity:0.7;"><b>$15k</b></span></span>
</div>
<div class="dates"><b>May 29</b> – <b>June 8, 2026</b></div>
</div>
<!-- header -->
<header class="header">
<div class="title-row">
<div style="flex:1; min-width: 0;">
<div class="eyebrow caps"><span class="dingbat">✦</span> The Build Small Hackathon <span class="dingbat">✦</span></div>
<h1 style="margin-top: 10px;">Making AI <em>Fun</em><br>Again.</h1>
</div>
<div class="seal" aria-hidden="true">
<div class="seal-inner">Build<br>Small<br>·<br>2026</div>
</div>
</div>
</header>
<!-- intro -->
<section class="section no-rule intro">
<div class="section-label caps"><span class="ornament">❋</span> Chapter Zero — Why this exists</div>
<p class="lede">The pace of AI over the last year has been anxiety-inducing. Labs release larger and larger models that do more of the things that make us feel human — writing, drawing, speaking, coding. No wonder more than half of us think the risks of AI outweigh the benefits.</p>
<div class="pull">We're sponsoring a hackathon to take things back to how they felt in 2021 — when models were small enough to tinker with, and the vibe was fun and hopeful about how this technology could improve our lives.</div>
<p style="margin-top: 14px;">This hackathon is different. Rather than using a giant LLM to ship yet another B2B SaaS, we want you to <b>think small</b>. Armed with only <b>32 billion parameters</b>, solve a problem someone you know is facing — or build something whimsical.</p>
</section>
<!-- two tracks -->
<section class="section">
<div class="section-label caps"><span class="ornament">❋</span> Two Tracks · Pick your trail</div>
<h2>Choose your own adventure.</h2>
<div class="tracks">
<div class="track">
<span class="chap">Chapter One</span>
<div class="ico">🏡</div>
<h3>Backyard AI</h3>
<p>Solve a real problem for someone you actually know. Pick a person — a neighbor, a parent, a small-business owner on your street — and build something that makes their day measurably better.</p>
<div class="judged">
<span class="caps">Judged on</span>
<ul>
<li>Problem is specific and real</li>
<li>The person actually <em>used it</em></li>
<li>Honest fit between problem and the small-model constraint</li>
<li>Polish of the Gradio app</li>
</ul>
</div>
</div>
<div class="track">
<span class="chap">Chapter Two</span>
<div class="ico">🍄</div>
<h3>An Adventure in Thousand&nbsp;Token Wood</h3>
<p>Build something delightful that wouldn't exist without AI. Wander somewhere weirder. A toy, a tiny game, a strange interactive story, an art experiment that surprises you. The AI should be doing the fun thing — not just helping you build it. Strange is good. Joyful is the bar.</p>
<div class="judged">
<span class="caps">Judged on</span>
<ul>
<li>Genuinely delightful (would you show a friend?)</li>
<li>AI is load-bearing for the experience</li>
<li>Originality of concept</li>
<li>Polish of the Gradio app</li>
</ul>
</div>
</div>
</div>
</section>
<!-- constraints -->
<section class="section">
<div class="section-label caps"><span class="ornament">❋</span> The Constraints — Three rules of the trail</div>
<h2>Pack light.</h2>
<div class="constraints">
<div class="constraint">
<div class="num">1</div>
<h3>Small Models Only</h3>
<p>Total parameters must be <b>≤ 32 billion</b>. The model fits on a laptop. So should your ambition.</p>
</div>
<div class="constraint">
<div class="num">2</div>
<h3>Built on Gradio</h3>
<p>Your app must be a <b>Gradio app</b>, hosted as a <b>Hugging Face Space</b>. That's the canvas.</p>
</div>
<div class="constraint">
<div class="num">3</div>
<h3>Show, Don't Tell</h3>
<p>A short <b>demo video</b> and a <b>social-media post</b> are part of the submission. Make it sing.</p>
</div>
</div>
</section>
<!-- bonus quests -->
<section class="section">
<div class="section-label caps"><span class="ornament">❋</span> Bonus Quests · Six earnable merit badges</div>
<h2>Stack 'em on your sash.</h2>
<p class="lede" style="margin-top: 6px;">None required. Each one grants extra points for your submission. Hover a patch to see it lift.</p>
<div class="sash">
<div class="badges">
<div class="badge">
<div class="patch sun">🔌</div>
<div class="meta">
  <div class="name">Off the Grid</div>
  <div class="desc">No cloud APIs. The whole thing runs on the model in front of you.</div>
  <span class="tag">Local-first</span>
</div>
</div>
<div class="badge">
<div class="patch moss">🎯</div>
<div class="meta">
  <div class="name">Well-Tuned</div>
  <div class="desc">Your app uses a fine-tuned model you've published on Hugging Face.</div>
  <span class="tag">Fine-tuned</span>
</div>
</div>
<div class="badge">
<div class="patch rust">🎨</div>
<div class="meta">
  <div class="name">Off-Brand</div>
  <div class="desc">A custom frontend that pushes past the default Gradio look.</div>
  <span class="tag">Custom UI</span>
</div>
</div>
<div class="badge">
<div class="patch copper">🦙</div>
<div class="meta">
  <div class="name">Llama Champion</div>
  <div class="desc">Your model runs through the llama.cpp runtime.</div>
  <span class="tag">llama.cpp</span>
</div>
</div>
<div class="badge">
<div class="patch cream">📡</div>
<div class="meta">
  <div class="name">Sharing is Caring</div>
  <div class="desc">You shared your agent trace on the Hub for everyone to learn from.</div>
  <span class="tag">Open trace</span>
</div>
</div>
<div class="badge">
<div class="patch olive">📓</div>
<div class="meta">
  <div class="name">Field Notes</div>
  <div class="desc">You wrote a blog post or report about what you built and what you learned.</div>
  <span class="tag tentative">Tentative</span>
</div>
</div>
</div>
</div>
</section>
<!-- how to participate -->
<section class="section">
<div class="section-label caps"><span class="ornament">❋</span> How to Participate</div>
<h2>Four steps. No application. No waitlist.</h2>
<div class="ledger">
<div class="row">
<div class="n">I</div>
<div class="body">
<div class="name">Register</div>
<div class="desc">Join this org on Hugging Face. <a href="https://huggingface.co/spaces/build-small-hackathon/registration"><span>Register on the app.</span></a></div>
</div>
</div>
<div class="row">
<div class="n">II</div>
<div class="body">
<div class="name">Find your people</div>
<div class="desc">Hop into the Gradio Discord. AMAs. Connect with Gradio and HF folks. Potential teammates live there.</div>
</div>
</div>
<div class="row">
<div class="n">III</div>
<div class="body">
<div class="name">Build &amp; ship</div>
<div class="desc">Build your Gradio app and host it as a Space under this org.</div>
</div>
</div>
<div class="row">
<div class="n">IV</div>
<div class="body">
<div class="name">Submit</div>
<div class="desc">Drop your Space link, a short demo video, and a social post by the deadline.</div>
</div>
</div>
</div>
</section>
<!-- resources -->
<section class="section">
<div class="section-label caps"><span class="ornament">❋</span> How to Get Started · Tools for the trail</div>
<h2>Useful trailheads.</h2>
<div class="resources">
<a href="https://github.com/huggingface/ml-intern"><span>📓 &nbsp;ML Intern</span><span class="arr">→</span></a>
<a href="https://www.gradio.app/guides/quickstart"><span>📚 &nbsp;Gradio Guides</span><span class="arr">→</span></a>
<a href="https://huggingface.co/blog/introducing-gradio-server"><span>🛠 &nbsp;Gradio's gr.Server — fully custom UIs</span><span class="arr">→</span></a>
<a href="https://github.com/ggml-org/llama.cpp"><span>🦙 &nbsp;Getting Started with Llama.cpp</span><span class="arr">→</span></a>
</div>
</section>
<!-- timeline / map -->
<section class="section">
<div class="section-label caps"><span class="ornament">❋</span> Timeline · A hand-drawn map</div>
<h2>Two weekends in the woods.</h2>
<div class="map">
<div class="map-head">
<span class="caps muted">Trail map</span>
<span class="compass" aria-hidden="true">✦ N ✦</span>
</div>
<div class="stops">
<div class="stop">
<div class="pin">I</div>
<div class="when">May 07, 2026</div>
<div class="what"><b>Registration opens.</b><span class="note">Sign up, join Discord, start sketching.</span></div>
</div>
<div class="stop">
<div class="pin">II</div>
<div class="when">May 29, 2026</div>
<div class="what"><b>Hack window begins.</b><span class="note">Two weekends to build, ship, and demo.</span></div>
</div>
<div class="stop">
<div class="pin">III</div>
<div class="when">Mid-window</div>
<div class="what"><b>Live AMA.</b><span class="note">Ask the sponsors and Gradio team anything.</span></div>
</div>
<div class="stop">
<div class="pin">IV</div>
<div class="when">June 8, 2026</div>
<div class="what"><b>Submissions close.</b><span class="note">Space, demo video, social post locked in.</span></div>
</div>
<div class="stop">
<div class="pin">V</div>
<div class="when">[date TBD]</div>
<div class="what"><b>Winners announced.</b><span class="note">Per track, plus bonus-quest leaderboard.</span></div>
</div>
</div>
</div>
</section>
<!-- final cta -->
<div class="cta">
<h2>Build something <em>small</em>.</h2>
<p>Two weekends. Two tracks. The model on your laptop. The neighbor next door.</p>
<a href="https://huggingface.co/spaces/build-small-hackathon/registration" class="button">→ &nbsp; Register on Hugging Face &nbsp; ←</a>
<p class="registration_info" style="color: rgba(255,255,255,0.65);">
  Registrations are open till May 27!
</p>  
<div class="links">
<a href="https://discord.gg/YHECTft87Z">Join the community on Discord</a> · <a href="https://www.gradio.app/docs">Gradio docs</a>
</div>
</div>
</div>