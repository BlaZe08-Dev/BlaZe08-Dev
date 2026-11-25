<!-- PROFILE README: BlaZe08-Dev -->

<div align="center">

<img src="https://raw.githubusercontent.com/BlaZe08-Dev/BlaZe08-Dev/main/assets/profile-hero.svg" width="100%" alt="Animated dark operations-dashboard-inspired profile hero for Neelesh Malakar, featuring project status, engineering focus and activity panels" />

<br/>

**Think clearly. Build deliberately. Keep iterating.**

<!-- CURRENT-PROJECT:START -->
<div align="center">
  <sub>◉ CURRENTLY BUILDING · AUTOMATIC DETECTION · UPDATED 25 Nov 2026, 01:59 PM IST</sub><br/>
  <a href="https://github.com/BlaZe08-Dev"><img src="https://img.shields.io/badge/FOCUS-AWAITING%20ACTIVITY%20SIGNAL-8DA697?style=for-the-badge&logo=github&logoColor=070708" alt="Current project: AWAITING ACTIVITY SIGNAL" /></a><br/>
  <code>10 COMMITS TO ACTIVATE</code> &nbsp;·&nbsp; <code>CHECKED HOURLY</code><br/>
  <sub>Last qualifying activity: No project has reached the daily threshold yet · Threshold: 10 commits/day</sub>
</div>
<!-- CURRENT-PROJECT:END -->

<p>
  <a href="https://github.com/BlaZe08-Dev"><img src="https://img.shields.io/badge/GITHUB-BlaZe08--Dev-8DA697?style=flat-square&logo=github&logoColor=black" alt="GitHub" /></a>
  <img src="https://komarev.com/ghpvc/?username=BlaZe08-Dev&style=flat-square&color=8DA697&label=PROFILE+VIEWS" alt="Profile views" />
  <a href="https://github.com/BlaZe08-Dev/MiniCloud"><img src="https://img.shields.io/badge/FLAGSHIP-MINICLOUD-8DA697?style=flat-square&logo=go&logoColor=black" alt="Flagship project MiniCloud" /></a>
</p>

<code>AI & DATA SCIENCE</code> &nbsp;·&nbsp; <code>SOFTWARE ENGINEERING</code> &nbsp;·&nbsp; <code>DISTRIBUTED SYSTEMS</code>

<br/>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:070708,50:8DA697,100:070708&height=2&section=header" width="100%" alt="" />

</div>

## ⟡ 00 — THE BUILDER'S LOG

I'm **Neelesh Malakar**, an AI & Data Science undergraduate who enjoys building practical software and understanding the systems underneath it.

My interests sit at the intersection of **backend engineering, distributed systems, full-stack development and applied AI**. I learn by shipping projects, investigating failure modes and improving the architecture—not just by collecting frameworks.

| CURRENT INTERESTS | HOW I APPROACH BUILDING |
|:---|:---|
| Distributed systems & backend architecture | Understand the constraints before choosing the design |
| AI integration & developer tooling | Use AI where it adds measurable value |
| Full-stack applications | Build complete workflows, not disconnected screens |
| Systems thinking & reliability | Test assumptions, document trade-offs and learn from failures |

<blockquote>
  <strong>My engineering principle:</strong> Don't just make it work. Understand why it works, where it breaks, and what it takes to make it dependable.
</blockquote>

## ◉ 01 — THE CORE SYSTEM

<div align="center">

<a href="https://github.com/BlaZe08-Dev/MiniCloud">
  <img src="https://img.shields.io/badge/PROJECT-MINICLOUD-8DA697?style=for-the-badge&logo=go&logoColor=black" alt="MiniCloud" />
</a>
&nbsp;
<img src="https://img.shields.io/badge/RELEASE-v1.1.0-151514?style=for-the-badge&logo=github&logoColor=8DA697" alt="Version 1.1.0" />
&nbsp;
<img src="https://img.shields.io/badge/STATUS-LEARNING%20%2F%20PRE--PRODUCTION-111111?style=for-the-badge" alt="Learning and pre-production status" />

### Distributed Job Execution Platform

**MiniCloud** is my individual Go-based project exploring the engineering realities of distributed job execution: coordination, worker capacity, durable state, leases, retries and recovery.

</div>

**What is implemented**
- A coordinator service that accepts jobs, registers workers, tracks heartbeats and dispatches attempts.
- Independent worker processes that pull and execute allowlisted tasks with bounded concurrency.
- PostgreSQL as the durable source of truth for jobs, attempts, workers and execution records.
- A CLI for job submission, status inspection, attempt history and worker-capacity monitoring.
- Assignment-based round-robin and FIFO-pull dispatch policies, bounded retries and lease-based attempt handling.

**Animated architecture**

<div align="center">

<img src="https://raw.githubusercontent.com/BlaZe08-Dev/BlaZe08-Dev/main/assets/minicloud-architecture.svg" width="100%" alt="Animated MiniCloud architecture showing client submission, coordinator dispatch, worker execution and heartbeats, and PostgreSQL persistence" />

<sub>Moving packets illustrate job submission, worker dispatch, heartbeats, execution results and durable-state updates. This is the current v1.1.0 topology—not a future-state design.</sub>

</div>

**Engineering note:** MiniCloud v1.1.0 is a learning-oriented, pre-production system. It is not multi-tenant and its API/worker endpoints do not yet provide authentication, authorization or TLS. It must not be exposed to untrusted networks. AI-assisted dispatch and coordinator failover remain post-V1 design ideas, not implemented capabilities.

<div align="center">

[![Explore MiniCloud](https://img.shields.io/badge/EXPLORE%20REPOSITORY-ED3426?style=for-the-badge&logo=github&logoColor=black)](https://github.com/BlaZe08-Dev/MiniCloud)

</div>

## ⌘ 02 — PROJECT FIELDNOTES

A selection of individual and collaborative work. Team projects are labelled as collaborative; repository ownership does not imply sole authorship.

<div align="center">

<img src="https://raw.githubusercontent.com/BlaZe08-Dev/BlaZe08-Dev/main/assets/project-dashboard.svg" width="100%" alt="Animated portfolio dashboard highlighting MiniCloud, Harmoniq and collaborative engineering projects" />

</div>

### ↳ 01 / INDEPENDENT BUILDS

<table>
<tr>
<td width="50%" valign="top">

<strong>01 / MINICLOUD</strong>

<sub>GO · DISTRIBUTED SYSTEMS</sub>

<br/><img src="https://raw.githubusercontent.com/BlaZe08-Dev/BlaZe08-Dev/main/assets/project-animations/minicloud.svg" width="100%" height="76" alt="Animated MiniCloud illustration showing CLI submission, coordinator dispatch, worker pool and PostgreSQL storage" />

A distributed job-execution platform built to explore coordinator/worker orchestration, durable job state, dispatch policies and failure handling.

<a href="https://github.com/BlaZe08-Dev/MiniCloud">SOURCE ↗</a>

</td>
<td width="50%" valign="top">

<strong>02 / HARMONIQ</strong>

<sub>PYTHON · FLASK · JAVASCRIPT · JAMENDO API</sub>

<br/><img src="https://raw.githubusercontent.com/BlaZe08-Dev/BlaZe08-Dev/main/assets/project-animations/harmoniq.svg" width="100%" height="76" alt="Animated Harmoniq music player with album art, equalizer and playback timeline" />

A music discovery and playback web app with search, queue and playlist workflows, playback controls, recently played tracks and a responsive listening interface.

<a href="https://github.com/BlaZe08-Dev/Harmoniq">SOURCE ↗</a> · <a href="https://harmoniq-yvun.onrender.com">LIVE DEMO ↗</a>

</td>
</tr>
</table>

### ↳ 02 / TEAM-ENGINEERED BUILDS

<sub>Built with Raunak and other teammates. Contributions are collaborative, not presented as solo projects.</sub>

<table>
<tr>
<td width="50%" valign="top">

<strong>03 / KAVACH PAY</strong>

<sub>NEXT.JS · NODE / HONO · POSTGRESQL · FRAUD RISK</sub>

<br/><img src="https://raw.githubusercontent.com/BlaZe08-Dev/BlaZe08-Dev/main/assets/project-animations/kavach.svg" width="100%" height="76" alt="Animated Kavach Pay UPI request, signal analysis and risk decision illustration" />

A simulated UPI-style payment experience with a deterministic fraud-risk engine that explains suspicious payment and collect-request signals in plain language. Hackathon prototype; payment rails and data are synthetic.

<a href="https://github.com/raunaksahahere/kavachPay">SOURCE ↗</a>

</td>
<td width="50%" valign="top">

<strong>04 / WEBTHREATDETECTION</strong>

<sub>CYBERSECURITY · REACT · PYTHON · WEB3</sub>

<br/><img src="https://raw.githubusercontent.com/BlaZe08-Dev/BlaZe08-Dev/main/assets/project-animations/webthreat.svg" width="100%" height="76" alt="Animated WebThreatDetection evidence scanner and report workflow illustration" />

An evidence-based investigation tool for suspicious URLs, messages, raw emails and QR codes, with explainable findings and an on-chain report-integrity registry.

<a href="https://github.com/raunaksahahere/webThreatDetection">SOURCE ↗</a>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<strong>05 / ROGUESIGNAL</strong>

<sub>MULTIPLAYER · GAME SYSTEMS · SOCIAL DEDUCTION</sub>

<br/><img src="https://raw.githubusercontent.com/BlaZe08-Dev/BlaZe08-Dev/main/assets/project-animations/roguesignal.svg" width="100%" height="76" alt="Animated RogueSignal top-down multiplayer arena with player proximity and task station" />

A first-person multiplayer social-deduction game concept for 4–10 players, built around roles, tasks, sabotage and proximity-based interaction.

<a href="https://github.com/raunaksahahere/RogueSignal">SOURCE ↗</a>

</td>
<td width="50%" valign="top">

<strong>06 / LOOPSPILL</strong>

<sub>REMOTE SENSING · SATELLITE DATA · AIS</sub>

<br/><img src="https://raw.githubusercontent.com/BlaZe08-Dev/BlaZe08-Dev/main/assets/project-animations/loopspill.svg" width="100%" height="76" alt="Animated LoopSpill satellite oil-spill detection, drift trajectory and AIS attribution illustration" />

A satellite-based oil-spill investigation workflow combining radar detection, backward drift modelling and vessel/AIS attribution to estimate likely spill origins.

<a href="https://github.com/raunaksahahere/LoopSpill">SOURCE ↗</a>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<strong>07 / LOOPSATELLITE</strong>

<sub>EARTH OBSERVATION · TIME SERIES · GEOSPATIAL AI</sub>

<br/><img src="https://raw.githubusercontent.com/BlaZe08-Dev/BlaZe08-Dev/main/assets/project-animations/loopsatellite.svg" width="100%" height="76" alt="Animated LoopSatellite wetland observation and water time-series illustration" />

A wetland-monitoring system for the East Kolkata Wetlands. Deterministic satellite-derived water measurements and seasonal anomaly detection support evidence-backed investigation.

<a href="https://github.com/raunaksahahere/LoopSatellite">SOURCE ↗</a>

</td>
<td width="50%" valign="top">

<strong>08 / JOCKY</strong>

<sub>COLLABORATIVE PROJECT · PRIVATE REPOSITORY</sub>

<br/><img src="https://raw.githubusercontent.com/BlaZe08-Dev/BlaZe08-Dev/main/assets/project-animations/jocky.svg" width="100%" height="76" alt="Animated JOCKY private collaborative project illustration" />

A collaborative project. The repository is private, so implementation details are intentionally not expanded here.

<a href="https://github.com/raunaksahahere/JOCKY">REPOSITORY LINK ↗</a>

</td>
</tr>
</table>

## ⬡ 03 — THE ENGINEERING TOOLCHAIN

<div align="center">

<sub>TOOLS AND TECHNOLOGIES I'VE WORKED WITH THROUGH PROJECTS AND PRACTICE</sub>

<table>
<tr>
<td width="33%" align="center" valign="top">

<strong>01 / LANGUAGES</strong>

<sub>Core programming</sub>

<br/><br/>

<img src="https://skillicons.dev/icons?i=go,python,c,js,ts&theme=dark" alt="Go, Python, C, JavaScript and TypeScript" />

</td>
<td width="33%" align="center" valign="top">

<strong>02 / APPLICATIONS</strong>

<sub>Web and backend</sub>

<br/><br/>

<img src="https://skillicons.dev/icons?i=flask,nextjs,react,nodejs,tailwind&theme=dark" alt="Flask, Next.js, React, Node.js and Tailwind CSS" />

</td>
<td width="33%" align="center" valign="top">

<strong>03 / SYSTEMS & TOOLS</strong>

<sub>Data and workflow</sub>

<br/><br/>

<img src="https://skillicons.dev/icons?i=postgres,git,github,linux,docker,vscode&theme=dark" alt="PostgreSQL, Git, GitHub, Linux, Docker and VS Code" />

</td>
</tr>
</table>

<code>GO</code> <code>PYTHON</code> <code>FULL-STACK</code> <code>POSTGRESQL</code> <code>LINUX</code> <code>GIT</code>

</div>

## ▤ 04 — CONTRIBUTION TELEMETRY

<div align="center">

<img src="https://raw.githubusercontent.com/BlaZe08-Dev/BlaZe08-Dev/main/assets/commit-telemetry.svg" width="100%" alt="Animated all-time commit telemetry banner" />

<img width="49%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=BlaZe08-Dev&layout=compact&hide_border=true&bg_color=10100f&title_color=8DA697&text_color=FAFAF9" alt="Most used languages" />

<br/>

<img width="70%" src="https://streak-stats.demolab.com?user=BlaZe08-Dev&theme=dark&hide_border=true&background=10100f&ring=8DA697&fire=ED3426&currStreakLabel=8DA697" alt="GitHub contribution streak" />

</div>

## ⌁ 05 — OPEN CHANNELS

<div align="center">

<a href="mailto:neeleshmalakar@gmail.com"><img src="https://img.shields.io/badge/EMAIL-8DA697?style=for-the-badge&logo=gmail&logoColor=black" alt="Email Neelesh" /></a>
<a href="https://www.linkedin.com/in/neeleshmalakar/"><img src="https://img.shields.io/badge/LINKEDIN-ED3426?style=for-the-badge&logo=linkedin&logoColor=black" alt="LinkedIn" /></a>
<a href="https://www.instagram.com/neels_archive/"><img src="https://img.shields.io/badge/INSTAGRAM-8DA697?style=for-the-badge&logo=instagram&logoColor=black" alt="Instagram" /></a>
<a href="https://medium.com/@Neelesh08"><img src="https://img.shields.io/badge/MEDIUM-ED3426?style=for-the-badge&logo=medium&logoColor=black" alt="Medium" /></a>
<a href="https://www.credly.com/users/neelesh-malakar"><img src="https://img.shields.io/badge/CREDLY-8DA697?style=for-the-badge&logo=credly&logoColor=black" alt="Credly" /></a>
<a href="https://github.com/BlaZe08-Dev"><img src="https://img.shields.io/badge/GITHUB-ED3426?style=for-the-badge&logo=github&logoColor=black" alt="GitHub" /></a>

<br/><br/>

```bash
$ echo "Keep building. Keep questioning. Keep engineering."
```

<strong><code>[ SYSTEM STATUS: ALWAYS BUILDING ]</code></strong>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ED3426,50:4E4D44,100:070708&height=110&section=footer" width="100%" alt="" />

</div>

<!-- END PROFILE README -->
