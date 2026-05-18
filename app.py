""
Build Small — Gradio + Hugging Face Hackathon
Org README Space.
This Space renders the hackathon landing page using gr.HTML().
Custom CSS strips Gradio's default container so the design renders edge-to-edge.
"""

import gradio as gr


HEAD_HTML = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,300..900,0..100&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Caveat:wght@500;700&display=swap" rel="stylesheet">
"""

# Override Gradio's default container so the landing page renders edge-to-edge
CUSTOM_CSS = """
.gradio-container {
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
    background: #F2EAD8 !important;
}
.gradio-container > .main, .gradio-container > .wrap, .main, .wrap {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}
.app, .container, .contain {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}
footer { display: none !important; }
.show-api { display: none !important; }
.built-with { display: none !important; }
body { background: #F2EAD8 !important; }
"""

LANDING_HTML = r"""
<style>
  :root {
    --paper: #F2EAD8;
    --paper-deep: #E8DEC6;
    --ink: #1E1A12;
    --ink-soft: #4A3F2E;
    --moss: #3D5A3A;
    --moss-deep: #2A3F28;
    --ember: #B8501E;
    --ember-soft: #D67A3F;
    --gold: #B98C2C;
    --sage: #8FA689;
    --twilight: #2C3338;
    --rule: rgba(30, 26, 18, 0.18);
  }
  /* Scoped reset for the landing wrapper only */
  .build-small * { box-sizing: border-box; margin: 0; padding: 0; }
  .build-small {
    background: var(--paper);
    color: var(--ink);
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 19px;
    line-height: 1.55;
    overflow-x: hidden;
    background-image:
      radial-gradient(circle at 20% 10%, rgba(184,80,30,0.04) 0%, transparent 40%),
      radial-gradient(circle at 80% 90%, rgba(61,90,58,0.05) 0%, transparent 45%),
      url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0.12  0 0 0 0 0.10  0 0 0 0 0.07  0 0 0 0.08 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
    width: 100%;
    min-height: 100vh;
  }
  .build-small .display { font-family: 'Fraunces', 'Times New Roman', serif; font-variation-settings: "SOFT" 100, "opsz" 144; }
  .build-small .hand { font-family: 'Caveat', cursive; }
  /* ========= NAV ========= */
  .build-small nav {
    position: sticky; top: 0; z-index: 50;
    backdrop-filter: blur(8px);
    background: rgba(242, 234, 216, 0.85);
    border-bottom: 1px solid var(--rule);
  }
  .build-small nav .inner {
    max-width: 1200px; margin: 0 auto;
    padding: 18px 32px;
    display: flex; justify-content: space-between; align-items: center;
    gap: 24px;
  }
  .build-small .brand {
    font-family: 'Fraunces', serif;
    font-weight: 600;
    font-size: 18px;
    letter-spacing: 0.02em;
    font-variation-settings: "SOFT" 100;
  }
  .build-small .brand .sm { color: var(--ember); font-style: italic; }
  .build-small nav ul {
    display: flex; gap: 28px; list-style: none;
    font-family: 'EB Garamond', serif;
    font-size: 16px;
  }
  .build-small nav a { color: var(--ink-soft); text-decoration: none; transition: color 0.2s; }
  .build-small nav a:hover { color: var(--ember); }
  .build-small .register-btn {
    background: var(--ink);
    color: var(--paper);
    padding: 10px 22px;
    border-radius: 999px;
    font-family: 'Fraunces', serif;
    font-size: 14px;
    font-weight: 500;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    transition: transform 0.2s, background 0.2s;
    text-decoration: none;
  }
  .build-small .register-btn:hover { background: var(--ember); color: var(--paper); transform: translateY(-1px); }
  /* ========= HERO ========= */
  .build-small .hero {
    max-width: 1200px;
    margin: 0 auto;
    padding: 80px 32px 60px;
    position: relative;
    text-align: center;
  }
  .build-small .hero .kicker {
    font-family: 'Caveat', cursive;
    font-size: 26px;
    color: var(--ember);
    margin-bottom: 12px;
    transform: rotate(-1.5deg);
    display: inline-block;
  }
  .build-small .hero h1 {
    font-family: 'Fraunces', serif;
    font-variation-settings: "SOFT" 100, "opsz" 144, "wght" 600;
    font-size: clamp(64px, 12vw, 168px);
    line-height: 0.92;
    letter-spacing: -0.03em;
    color: var(--ink);
    margin: 8px 0 24px;
  }
  .build-small .hero h1 em {
    font-style: italic;
    color: var(--ember);
    font-variation-settings: "SOFT" 100, "opsz" 144, "wght" 500;
  }
  .build-small .hero .lede {
    font-size: 22px;
    line-height: 1.5;
    color: var(--ink-soft);
    max-width: 640px;
    margin: 0 auto 36px;
  }
  .build-small .hero .meta-row {
    display: inline-flex;
    gap: 32px;
    align-items: center;
    padding: 14px 28px;
    border: 1px solid var(--rule);
    border-radius: 999px;
    background: rgba(255,255,255,0.4);
    font-size: 15px;
    color: var(--ink-soft);
    flex-wrap: wrap;
    justify-content: center;
  }
  .build-small .hero .meta-row .dot { color: var(--ember); }
  .build-small .hero .meta-row strong { color: var(--ink); font-weight: 500; }
  .build-small .scribble {
    display: block;
    margin: 0 auto;
    width: 120px;
    color: var(--ember);
    opacity: 0.6;
  }
  /* ========= INTRO ========= */
  .build-small .intro {
    max-width: 720px;
    margin: 80px auto;
    padding: 0 32px;
    text-align: center;
  }
  .build-small .intro h2 {
    font-family: 'Fraunces', serif;
    font-variation-settings: "SOFT" 80;
    font-size: 38px;
    font-weight: 400;
    font-style: italic;
    color: var(--moss-deep);
    margin-bottom: 24px;
    line-height: 1.2;
  }
  .build-small .intro p {
    font-size: 19px;
    color: var(--ink-soft);
    margin-bottom: 18px;
  }
  .build-small .intro p strong { color: var(--ink); font-weight: 600; }
  /* ========= TRACKS ========= */
  .build-small .tracks {
    max-width: 1280px;
    margin: 100px auto 80px;
    padding: 0 32px;
  }
  .build-small .section-label {
    text-align: center;
    font-family: 'Caveat', cursive;
    font-size: 28px;
    color: var(--ember);
    margin-bottom: 8px;
    transform: rotate(-1deg);
  }
  .build-small .section-title {
    text-align: center;
    font-family: 'Fraunces', serif;
    font-variation-settings: "SOFT" 100;
    font-size: 56px;
    font-weight: 400;
    line-height: 1;
    margin-bottom: 60px;
    color: var(--ink);
  }
  .build-small .track-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    border-top: 1px solid var(--rule);
    border-bottom: 1px solid var(--rule);
  }
  .build-small .track {
    padding: 56px 48px;
    position: relative;
  }
  .build-small .track:first-child { border-right: 1px solid var(--rule); }
  .build-small .track .chapter {
    font-family: 'Caveat', cursive;
    font-size: 22px;
    color: var(--ember);
    margin-bottom: 12px;
  }
  .build-small .track .illustration {
    height: 140px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 24px;
  }
  .build-small .track h3 {
    font-family: 'Fraunces', serif;
    font-variation-settings: "SOFT" 100, "wght" 500;
    font-size: 42px;
    line-height: 1.05;
    margin-bottom: 18px;
  }
  .build-small .track-1 h3 { color: var(--moss-deep); }
  .build-small .track-2 h3 { color: var(--ember); font-style: italic; }
  .build-small .track .subtitle {
    font-family: 'EB Garamond', serif;
    font-style: italic;
    font-size: 19px;
    color: var(--ink-soft);
    margin-bottom: 28px;
  }
  .build-small .track .body { color: var(--ink-soft); margin-bottom: 28px; }
  .build-small .track .judging {
    border-top: 1px dashed var(--rule);
    padding-top: 24px;
  }
  .build-small .track .judging-label {
    font-family: 'Fraunces', serif;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: var(--ink-soft);
    margin-bottom: 12px;
  }
  .build-small .track .judging ul { list-style: none; }
  .build-small .track .judging li {
    padding: 8px 0;
    font-size: 17px;
    color: var(--ink);
    display: flex;
    gap: 12px;
  }
  .build-small .track .judging li::before {
    content: "✦";
    color: var(--ember);
    flex-shrink: 0;
  }
  .build-small .track-1 .judging li::before { color: var(--moss); }
  /* ========= RULES ========= */
  .build-small .rules {
    max-width: 1080px;
    margin: 100px auto;
    padding: 0 32px;
  }
  .build-small .rules-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0;
  }
  .build-small .rule-card {
    padding: 36px 28px;
    text-align: center;
    border-right: 1px solid var(--rule);
  }
  .build-small .rule-card:last-child { border-right: none; }
  .build-small .rule-card .icon {
    font-family: 'Fraunces', serif;
    font-size: 38px;
    color: var(--ember);
    margin-bottom: 12px;
    font-variation-settings: "SOFT" 100;
    font-style: italic;
  }
  .build-small .rule-card h4 {
    font-family: 'Fraunces', serif;
    font-size: 20px;
    font-weight: 500;
    margin-bottom: 8px;
    font-variation-settings: "SOFT" 100;
  }
  .build-small .rule-card p {
    font-size: 16px;
    color: var(--ink-soft);
    line-height: 1.5;
  }
  .build-small .rule-card .pending {
    display: inline-block;
    margin-top: 8px;
    font-family: 'Caveat', cursive;
    font-size: 15px;
    color: var(--ember);
  }
  /* ========= HOW IT WORKS (new section, from README) ========= */
  .build-small .how-it-works {
    max-width: 1080px;
    margin: 100px auto;
    padding: 0 32px;
  }
  .build-small .steps {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
    margin-top: 16px;
  }
  .build-small .step {
    padding: 32px 24px;
    border: 1px solid var(--rule);
    border-radius: 4px;
    background: rgba(255,255,255,0.35);
    position: relative;
  }
  .build-small .step .num {
    font-family: 'Fraunces', serif;
    font-style: italic;
    font-variation-settings: "SOFT" 100;
    font-size: 48px;
    color: var(--ember);
    line-height: 1;
    margin-bottom: 14px;
  }
  .build-small .step h4 {
    font-family: 'Fraunces', serif;
    font-size: 22px;
    font-weight: 500;
    font-variation-settings: "SOFT" 80;
    margin-bottom: 8px;
    color: var(--ink);
  }
  .build-small .step p {
    font-size: 16px;
    color: var(--ink-soft);
    line-height: 1.5;
  }
  .build-small .step p strong { color: var(--ink); font-weight: 600; }
  /* ========= BONUS QUESTS ========= */
  .build-small .bonus {
    background: var(--paper-deep);
    padding: 100px 32px;
    border-top: 1px solid var(--rule);
    border-bottom: 1px solid var(--rule);
    position: relative;
    overflow: hidden;
  }
  .build-small .bonus::before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
      url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0.10  0 0 0 0 0.08  0 0 0 0 0.05  0 0 0 0.10 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
    pointer-events: none;
    opacity: 0.5;
  }
  .build-small .bonus-inner {
    max-width: 1080px;
    margin: 0 auto;
    position: relative;
  }
  .build-small .bonus .intro-text {
    text-align: center;
    max-width: 580px;
    margin: 0 auto 50px;
    color: var(--ink-soft);
    font-size: 18px;
  }
  .build-small .bonus-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
  }
  .build-small .badge {
    background: var(--paper);
    border: 1px solid var(--rule);
    padding: 24px 20px;
    border-radius: 4px;
    transition: transform 0.2s, box-shadow 0.2s;
    position: relative;
  }
  .build-small .badge:hover {
    transform: translateY(-3px) rotate(-0.5deg);
    box-shadow: 0 12px 30px rgba(30,26,18,0.10);
  }
  .build-small .badge .name {
    font-family: 'Fraunces', serif;
    font-size: 20px;
    font-weight: 500;
    color: var(--ember);
    margin-bottom: 6px;
    font-variation-settings: "SOFT" 100;
    font-style: italic;
  }
  .build-small .badge .desc {
    font-size: 15px;
    color: var(--ink-soft);
    line-height: 1.45;
  }
  .build-small .badge.tentative::after {
    content: "tentative";
    position: absolute;
    top: 10px;
    right: 12px;
    font-family: 'Caveat', cursive;
    font-size: 13px;
    color: var(--ember-soft);
    transform: rotate(8deg);
  }
  /* ========= TIMELINE ========= */
  .build-small .timeline-section {
    max-width: 900px;
    margin: 100px auto;
    padding: 0 32px;
  }
  .build-small .timeline {
    position: relative;
    padding-left: 28px;
    border-left: 2px dashed var(--rule);
  }
  .build-small .milestone {
    margin-bottom: 36px;
    position: relative;
  }
  .build-small .milestone::before {
    content: "";
    position: absolute;
    left: -36px;
    top: 8px;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: var(--ember);
    border: 3px solid var(--paper);
    box-shadow: 0 0 0 1px var(--ember);
  }
  .build-small .milestone .date {
    font-family: 'Caveat', cursive;
    font-size: 22px;
    color: var(--ember);
    margin-bottom: 4px;
  }
  .build-small .milestone .title {
    font-family: 'Fraunces', serif;
    font-size: 22px;
    font-weight: 500;
    margin-bottom: 4px;
    font-variation-settings: "SOFT" 80;
  }
  .build-small .milestone .desc {
    color: var(--ink-soft);
    font-size: 17px;
  }
  /* ========= SUBMIT BLOCK ========= */
  .build-small .submit {
    max-width: 1080px;
    margin: 100px auto;
    padding: 0 32px;
  }
  .build-small .submit-card {
    background: var(--twilight);
    color: var(--paper);
    padding: 80px 60px;
    border-radius: 8px;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  .build-small .submit-card::before {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 30% 20%, rgba(184,80,30,0.25), transparent 60%),
                radial-gradient(circle at 80% 90%, rgba(143,166,137,0.18), transparent 55%);
  }
  .build-small .submit-card > * { position: relative; }
  .build-small .submit-card .scribble-light { color: var(--ember-soft); opacity: 0.8; }
  .build-small .submit-card h2 {
    font-family: 'Fraunces', serif;
    font-variation-settings: "SOFT" 100, "opsz" 144;
    font-size: 64px;
    font-weight: 500;
    line-height: 1;
    margin: 24px 0 20px;
  }
  .build-small .submit-card h2 em { color: var(--ember-soft); font-style: italic; }
  .build-small .submit-card p {
    color: rgba(242, 234, 216, 0.8);
    font-size: 19px;
    max-width: 540px;
    margin: 0 auto 36px;
  }
  .build-small .submit-btn {
    display: inline-block;
    background: var(--paper);
    color: var(--ink);
    padding: 18px 40px;
    border-radius: 999px;
    font-family: 'Fraunces', serif;
    font-size: 16px;
    font-weight: 500;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    text-decoration: none;
    transition: background 0.2s, transform 0.2s;
  }
  .build-small .submit-btn:hover { background: var(--ember-soft); color: var(--paper); transform: translateY(-2px); }
  /* ========= SPONSORS ========= */
  .build-small .sponsors {
    max-width: 1080px;
    margin: 0 auto 100px;
    padding: 0 32px;
    text-align: center;
  }
  .build-small .sponsors h3 {
    font-family: 'Fraunces', serif;
    font-size: 14px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.25em;
    color: var(--ink-soft);
    margin-bottom: 32px;
  }
  .build-small .sponsor-row {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 60px;
    flex-wrap: wrap;
    opacity: 0.7;
  }
  .build-small .sponsor-placeholder {
    font-family: 'Fraunces', serif;
    font-style: italic;
    color: var(--ink-soft);
    font-size: 18px;
    border: 1px dashed var(--rule);
    padding: 16px 32px;
    border-radius: 4px;
  }
  /* ========= FOOTER ========= */
  .build-small .page-footer {
    border-top: 1px solid var(--rule);
    padding: 40px 32px;
    text-align: center;
    color: var(--ink-soft);
    font-size: 15px;
  }
  .build-small .page-footer a { color: var(--ember); text-decoration: none; }
  /* ========= RESPONSIVE ========= */
  @media (max-width: 760px) {
    .build-small .track-grid { grid-template-columns: 1fr; }
    .build-small .track:first-child { border-right: none; border-bottom: 1px solid var(--rule); }
    .build-small .rules-grid { grid-template-columns: 1fr; }
    .build-small .rule-card { border-right: none; border-bottom: 1px solid var(--rule); }
    .build-small .rule-card:last-child { border-bottom: none; }
    .build-small .steps { grid-template-columns: 1fr 1fr; }
    .build-small nav ul { display: none; }
    .build-small .submit-card { padding: 56px 28px; }
    .build-small .submit-card h2 { font-size: 44px; }
    .build-small .hero { padding: 56px 24px 40px; }
    .build-small .section-title { font-size: 40px; }
    .build-small .track { padding: 40px 28px; }
  }
  @media (max-width: 480px) {
    .build-small .steps { grid-template-columns: 1fr; }
  }
  /* ========= ANIMATION ========= */
  @keyframes build-small-rise {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
  .build-small .hero .kicker, .build-small .hero h1, .build-small .hero .lede, .build-small .hero .meta-row {
    animation: build-small-rise 0.8s ease-out backwards;
  }
  .build-small .hero .kicker { animation-delay: 0.05s; }
  .build-small .hero h1 { animation-delay: 0.18s; }
  .build-small .hero .lede { animation-delay: 0.4s; }
  .build-small .hero .meta-row { animation-delay: 0.55s; }
</style>
<div class="build-small">
<nav>
  <div class="inner">
    <div class="brand">Build <span class="sm">Small</span></div>
    <ul>
      <li><a href="#tracks">Tracks</a></li>
      <li><a href="#rules">Rules</a></li>
      <li><a href="#how">How it works</a></li>
      <li><a href="#bonus">Extra Credit</a></li>
      <li><a href="#timeline">Timeline</a></li>
    </ul>
    <a href="#register" class="register-btn">Register</a>
  </div>
</nav>
<!-- ============================ HERO ============================ -->
<section class="hero">
  <div class="kicker">~ a hackathon for small things ~</div>
  <h1>Build <em>Small.</em></h1>
  <p class="lede">A two-week hackathon for tiny weights, big ideas, and the things you can build close to home — hosted by Gradio &amp; Hugging Face.</p>
  <div class="meta-row">
    <span><strong>Two tracks</strong></span>
    <span class="dot">✦</span>
    <span><strong>Models ≤ 22GB</strong></span>
    <span class="dot">✦</span>
    <span><strong>Built on Gradio</strong></span>
    <span class="dot">✦</span>
    <span><strong>Open to everyone</strong></span>
  </div>
</section>
<!-- ============================ INTRO ============================ -->
<section class="intro">
  <svg class="scribble" viewBox="0 0 120 20" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
    <path d="M2 12 Q15 2, 30 12 T60 12 T90 12 T118 12" />
  </svg>
  <h2 style="margin-top: 32px;">The internet is full of giant models doing giant things. This isn't that.</h2>
  <p>For two weeks, we want to see what you can do with <strong>small models</strong>, <strong>tight constraints</strong>, and <strong>care for the people right around you</strong>. Build for one neighbor. Build something that runs on the laptop you already own. Build something a child could love.</p>
  <p style="margin-top: 24px;">Pick a track, ship a Gradio app, and tell us a story.</p>
</section>
<!-- ============================ TRACKS ============================ -->
<section class="tracks" id="tracks">
  <div class="section-label">~ choose your path ~</div>
  <h2 class="section-title">Two Tracks.</h2>
  <div class="track-grid">
    <!-- TRACK 1 -->
    <div class="track track-1">
      <div class="chapter">Chapter One</div>
      <div class="illustration">
        <svg width="180" height="120" viewBox="0 0 180 120" fill="none" stroke="#3D5A3A" stroke-width="1.4" stroke-linecap="round">
          <path d="M0 95 Q90 88, 180 95" />
          <path d="M50 95 L50 65 L75 50 L100 65 L100 95 Z" />
          <path d="M68 95 L68 80 L82 80 L82 95" />
          <circle cx="62" cy="72" r="2.5" />
          <circle cx="88" cy="72" r="2.5" />
          <path d="M85 50 L85 42" />
          <path d="M84 38 Q86 36, 88 38 Q86 40, 88 42" stroke-dasharray="2 2" opacity="0.6" />
          <path d="M135 95 L135 75" />
          <circle cx="135" cy="68" r="14" />
          <path d="M10 95 L10 86 M18 95 L18 86 M26 95 L26 86 M34 95 L34 86 M42 95 L42 86" />
          <path d="M8 88 L44 88" />
          <circle cx="155" cy="22" r="8" />
          <path d="M155 8 L155 4 M155 36 L155 40 M141 22 L137 22 M169 22 L173 22 M145 12 L142 9 M165 12 L168 9" />
        </svg>
      </div>
      <h3>Backyard AI</h3>
      <p class="subtitle">Solve a real problem for someone you actually know.</p>
      <p class="body">Pick a person — a neighbor, a parent, a small business owner on your street — and build something that makes their day measurably better. Walk over. Watch them use it. The closer the problem, the better the project.</p>
      <div class="judging">
        <div class="judging-label">Judging Criteria</div>
        <ul>
          <li>The problem is specific and real (not invented for the demo)</li>
          <li>The person it was built for actually used it</li>
          <li>Honest fit between problem, solution, and the small-model constraint</li>
          <li>Polish and craft of the Gradio app</li>
        </ul>
      </div>
    </div>
    <!-- TRACK 2 -->
    <div class="track track-2">
      <div class="chapter">Chapter Two</div>
      <div class="illustration">
        <svg width="180" height="120" viewBox="0 0 180 120" fill="none" stroke="#B8501E" stroke-width="1.4" stroke-linecap="round">
          <path d="M0 100 Q90 92, 180 100" />
          <path d="M30 100 Q60 80, 90 90 T160 70" stroke-dasharray="3 3" opacity="0.6" />
          <path d="M48 100 L48 95 Q43 95, 43 90 Q43 85, 53 85 Q63 85, 63 90 Q63 95, 58 95 L58 100" />
          <circle cx="48" cy="89" r="0.8" fill="#B8501E" />
          <circle cx="55" cy="87" r="0.8" fill="#B8501E" />
          <path d="M22 100 L22 96 Q19 96, 19 93 Q19 90, 25 90 Q31 90, 31 93 Q31 96, 28 96 L28 100" />
          <path d="M85 100 L85 70" />
          <path d="M78 75 L85 70 L92 75 M75 80 L85 75 L95 80 M73 86 L85 80 L97 86" />
          <path d="M125 100 L125 65" />
          <path d="M117 70 L125 65 L133 70 M114 76 L125 70 L136 76 M111 83 L125 76 L139 83" />
          <path d="M155 25 L155 19 L159 22 L153 22 L157 19 Z" />
          <circle cx="148" cy="35" r="1" fill="#B8501E" />
          <circle cx="170" cy="40" r="1" fill="#B8501E" />
        </svg>
      </div>
      <h3>An Adventure in Thousand Token Wood</h3>
      <p class="subtitle">Build something delightful that wouldn't exist without AI.</p>
      <p class="body">Wander somewhere weirder. A toy, a tiny game, a strange interactive story, an art experiment that surprises you. The AI should be doing the fun thing — not just helping you build it. Strange is good. Joyful is the bar.</p>
      <div class="judging">
        <div class="judging-label">Judging Criteria</div>
        <ul>
          <li>Genuinely delightful — would you show a friend?</li>
          <li>The AI is load-bearing for the experience</li>
          <li>Originality of concept (we've seen the chatbot)</li>
          <li>Polish and craft of the Gradio app</li>
        </ul>
      </div>
    </div>
  </div>
</section>
<!-- ============================ RULES ============================ -->
<section class="rules" id="rules">
  <div class="section-label">~ rules of the land ~</div>
  <h2 class="section-title">The Constraints.</h2>
  <div class="rules-grid">
    <div class="rule-card">
      <div class="icon">①</div>
      <h4>Small Models Only</h4>
      <p>Any model that fits inside <strong>22 GB</strong> of memory.</p>
      <span class="pending">↳ pending team sign-off</span>
    </div>
    <div class="rule-card">
      <div class="icon">②</div>
      <h4>Built on Gradio</h4>
      <p>Your app must be a Gradio app, hosted as a Hugging Face Space.</p>
    </div>
    <div class="rule-card">
      <div class="icon">③</div>
      <h4>Show, Don't Tell</h4>
      <p>A short demo video and a social-media post about your project are part of the submission.</p>
    </div>
  </div>
</section>
<!-- ============================ HOW IT WORKS ============================ -->
<section class="how-it-works" id="how">
  <div class="section-label">~ getting started ~</div>
  <h2 class="section-title">How It Works.</h2>
  <div class="steps">
    <div class="step">
      <div class="num">1</div>
      <h4>Register</h4>
      <p>Join this Hugging Face org. That's your ticket in — no application, no waitlist.</p>
    </div>
    <div class="step">
      <div class="num">2</div>
      <h4>Find Your People</h4>
      <p>Hop into the Gradio Discord channel. Office hours, AMAs, and teammates live there.</p>
    </div>
    <div class="step">
      <div class="num">3</div>
      <h4>Build &amp; Ship</h4>
      <p>Build your Gradio app and host it as a Space under this org during the hack window.</p>
    </div>
    <div class="step">
      <div class="num">4</div>
      <h4>Submit</h4>
      <p>Drop your <strong>Space link</strong>, a short <strong>demo video</strong>, and a <strong>social post</strong> by the deadline.</p>
    </div>
  </div>
</section>
<!-- ============================ BONUS ============================ -->
<section class="bonus" id="bonus">
  <div class="bonus-inner">
    <div class="section-label">~ extra credit ~</div>
    <h2 class="section-title">Bonus Quests.</h2>
    <p class="intro-text">None of these are required. Each one bumps you up the leaderboard. Stack them like badges on a scout sash.</p>
    <div class="bonus-grid">
      <div class="badge">
        <div class="name">Off the Grid</div>
        <div class="desc">No cloud APIs. The whole thing runs on the model in front of you.</div>
      </div>
      <div class="badge">
        <div class="name">Well-Tuned</div>
        <div class="desc">Your app uses a fine-tuned model you've published on Hugging Face.</div>
      </div>
      <div class="badge">
        <div class="name">Off-Brand</div>
        <div class="desc">A custom frontend that pushes past the default Gradio look.</div>
      </div>
      <div class="badge">
        <div class="name">Llama ChamPion</div>
        <div class="desc">Your model runs through the llama.cpp runtime.</div>
      </div>
      <div class="badge">
        <div class="name">Sharing is Caring</div>
        <div class="desc">You shared your agent trace on the Hub.</div>
      </div>
      <div class="badge tentative">
        <div class="name">Field Notes</div>
        <div class="desc">You wrote a blog post or report about what you built and what you learned.</div>
      </div>
    </div>
  </div>
</section>
<!-- ============================ TIMELINE ============================ -->
<section class="timeline-section" id="timeline">
  <div class="section-label">~ when ~</div>
  <h2 class="section-title">Timeline.</h2>
  <div class="timeline">
    <div class="milestone">
      <div class="date">Week of [date TBD]</div>
      <div class="title">Registration opens</div>
      <div class="desc">Sign up on the Hugging Face org, join the Discord channel, start sketching ideas.</div>
    </div>
    <div class="milestone">
      <div class="date">[date TBD]</div>
      <div class="title">Hack window begins</div>
      <div class="desc">Two weeks to build, ship, and demo.</div>
    </div>
    <div class="milestone">
      <div class="date">Mid-window</div>
      <div class="title">Live AMA + office hours</div>
      <div class="desc">Drop in to ask the Gradio team anything about your build.</div>
    </div>
    <div class="milestone">
      <div class="date">[date TBD]</div>
      <div class="title">Submissions close</div>
      <div class="desc">Demo video, public Space, and social post — locked in.</div>
    </div>
    <div class="milestone">
      <div class="date">[date TBD]</div>
      <div class="title">Winners announced</div>
      <div class="desc">Per track, plus the leaderboard for bonus quests stacked.</div>
    </div>
  </div>
</section>
<!-- ============================ SUBMIT ============================ -->
<section class="submit" id="register">
  <div class="submit-card">
    <svg class="scribble scribble-light" viewBox="0 0 120 20" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
      <path d="M2 12 Q15 2, 30 12 T60 12 T90 12 T118 12" />
    </svg>
    <h2>Build something <em>small.</em></h2>
    <p>Two weeks. Two tracks. The model on your laptop. The neighbor next door. Let's make some little things.</p>
    <a href="#" class="submit-btn">Register on Hugging Face →</a>
  </div>
</section>
<!-- ============================ SPONSORS ============================ -->
<section class="sponsors">
  <h3>Hosted by · Sponsored by</h3>
  <div class="sponsor-row">
    <div class="sponsor-placeholder">Gradio</div>
    <div class="sponsor-placeholder">Hugging Face</div>
    <div class="sponsor-placeholder">[ Sponsor TBD ]</div>
    <div class="sponsor-placeholder">[ Sponsor TBD ]</div>
  </div>
</section>
<div class="page-footer">
  <p>Made with care by the Gradio team — questions? <a href="#">Find us on Discord</a></p>
</div>
</div>
"""


with gr.Blocks(
    title="Build Small — A Gradio + Hugging Face Hackathon",
) as demo:
    gr.HTML(LANDING_HTML)


if __name__ == "__main__":
    demo.launch(
        css=CUSTOM_CSS,
        head=HEAD_HTML,
        theme=gr.themes.Base(),
    ) 