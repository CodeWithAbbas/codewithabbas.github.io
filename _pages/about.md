---
layout: about
title: about
permalink: /
subtitle: >
  PhD Student, <a href="https://umdearborn.edu/cecs/departments/electrical-and-computer-engineering">Electrical and Computer Engineering</a> ·
  University of Michigan-Dearborn

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <p>Information Systems, Security,<br>and Forensics (ISSF) Lab</p>
    <p>4901 Evergreen Road<br>Dearborn, MI 48128</p>

selected_papers: true
social: true

announcements:
  enabled: true
  scrollable: true
  limit: 5
---

<style>
  /* give the profile image more breathing room from the body text */
  .profile.float-right { padding-left: 2.5rem; }
  /* on narrow screens the image stacks above the text, so drop the gutter */
  @media (max-width: 768px) {
    .profile.float-right { padding-left: 0; }
  }
</style>

I am a PhD student and NSF-funded Graduate Student Research Assistant in the
Department of Electrical and Computer Engineering at the
[University of Michigan-Dearborn](https://umdearborn.edu), where I work in the
Information Systems, Security, and Forensics (ISSF) Laboratory with
[Prof. Hafiz Malik](https://umdearborn.edu/people-um-dearborn/hafiz-malik).

My research is on **securing cyber-physical systems at the hardware level**.
Modern vehicles and connected devices contain dozens of embedded computers, and
the assumption that each one is genuine and untampered with is rarely verified.
I build systems that check that assumption directly — using the physical
characteristics of the silicon itself.

Specifically, I work on:

- **Hardware fingerprinting** — identifying devices by manufacturing variations unique to each chip
- **FPGA-based intrusion detection** — detection that runs in real time, in the vehicle, rather than in the cloud
- **Side-channel analysis** — using electromagnetic and power measurements to detect tampering and counterfeit components

Before starting my PhD I spent two years as an **FPGA engineer**, building
high-performance digital systems in production. I received my BS in Electrical
Engineering from the [University of Engineering and Technology, Peshawar](https://www.uetpeshawar.edu.pk/),
graduating as a gold medalist.

<section class="ria" aria-labelledby="ria-heading">
  <header class="ria-head">
    <p class="ria-eyebrow"><span class="ria-dot"></span>Research in Action</p>
    <h2 id="ria-heading">From bench to conference floor</h2>
    <p class="ria-lede">A device does not need to announce what it is. Manufacturing leaves every chip with slightly different switching behaviour &mdash; overshoot, ringing, settling time. An attacker can copy firmware, a serial number, or a message. They cannot copy physics.</p>
    <svg class="ria-wave" viewBox="0 0 900 90" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path class="ria-wave-path" d="M0,62 L110,62 L118,16 L126,44 L132,26 L138,36 L144,30 L150,32 L240,32 L248,74 L256,50 L262,66 L268,58 L274,60 L370,60 L378,14 L386,42 L392,24 L398,34 L404,30 L500,30 L508,72 L516,48 L522,64 L528,56 L534,60 L630,60 L638,16 L646,44 L652,26 L658,36 L664,31 L760,31 L768,73 L776,49 L782,65 L788,57 L794,60 L900,60" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>
    </svg>
  </header>

  <ol class="ria-rail">
    <li class="ria-card">
      <span class="ria-node" aria-hidden="true"></span>
      <figure class="ria-media"><img src="/assets/img/research/hardware.jpg" alt="Instrumented test devices on the ISSF laboratory bench" loading="lazy" width="1100" height="733"></figure>
      <div class="ria-body">
        <span class="ria-step">01 &middot; The mechanism</span>
        <h3>Physics as identity</h3>
        <p>Two chips off the same reel switch slightly differently. That difference is measurable, and it is not something firmware can rewrite.</p>
      </div>
    </li>

    <li class="ria-card">
      <span class="ria-node" aria-hidden="true"></span>
      <figure class="ria-media"><img src="/assets/img/research/bench.jpg" alt="Array of test boards instrumented for measurement" loading="lazy" width="1100" height="733"></figure>
      <div class="ria-body">
        <span class="ria-step">02 &middot; The bench</span>
        <h3>Same make, same model</h3>
        <p>Eight devices across four hardware types, including boards of the same make and model.</p>
        <p class="ria-stat"><b>99.5%</b> real-time accuracy &mdash; no firmware changes, no protocol access</p>
      </div>
    </li>

    <li class="ria-card">
      <span class="ria-node" aria-hidden="true"></span>
      <figure class="ria-media"><img src="/assets/img/research/labcar.jpg" alt="Testing at the ETAS LABCAR hardware-in-the-loop station" loading="lazy" width="1100" height="733"></figure>
      <div class="ria-body">
        <span class="ria-step">03 &middot; Production hardware</span>
        <h3>Nine real ECUs, weeks apart</h3>
        <p>Electrically identical production automotive ECUs, captured across thirteen sessions over several weeks. A fingerprint that holds only within one sitting cannot be deployed.</p>
      </div>
    </li>

    <li class="ria-card">
      <span class="ria-node" aria-hidden="true"></span>
      <figure class="ria-media"><img src="/assets/img/research/demo.jpg" alt="Presenting the live hardware demonstration at USENIX VehicleSec 2026" loading="lazy" width="1100" height="733"></figure>
      <div class="ria-body">
        <span class="ria-step">04 &middot; Baltimore</span>
        <h3>Live on the table</h3>
        <p>Real devices at VehicleSec &rsquo;26, identified in real time purely from the analog shape of their switching signals.</p>
        <a class="ria-link" href="https://www.usenix.org/conference/vehiclesec26/presentation/ali-demo">Demo abstract</a>
      </div>
    </li>

    <li class="ria-card">
      <span class="ria-node" aria-hidden="true"></span>
      <figure class="ria-media"><img src="/assets/img/research/talk.jpg" alt="Presenting Is Your ECU Really Yours at the VehicleSec 2026 podium" loading="lazy" width="1100" height="733"></figure>
      <div class="ria-body">
        <span class="ria-step">05 &middot; The talk</span>
        <h3>Is Your ECU Really Yours?</h3>
        <p>The paper talk, alongside a lightning talk extending the method to production ECUs over the CAN bus.</p>
        <a class="ria-link" href="https://www.usenix.org/conference/vehiclesec26/presentation/ali">Read the paper</a>
      </div>
    </li>
  </ol>

  <figure class="ria-quote">
    <blockquote>Nobody asked whether it works. They asked whether it <em>survives</em>.</blockquote>
    <figcaption>
      How does the fingerprint hold when an engine heats the whole bay? What happens at a thousand
      devices instead of nine? When do two devices overlap and become indistinguishable?
      Every one of those is now on my experiment list.
      <a class="ria-link" href="https://www.linkedin.com/in/engr-abbasali/">View on LinkedIn</a>
    </figcaption>
  </figure>
</section>

<style>
/* ===== Research in Action ============================================= */
.ria{--ria-line:var(--global-divider-color,#e6e6e6);--ria-mut:var(--global-text-color-light,#828282);margin:3.75rem 0 1rem;clear:both}
.ria-head{max-width:46rem;margin-bottom:.5rem}
.ria-eyebrow{display:flex;align-items:center;gap:.5rem;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--global-theme-color);font-weight:600;margin:0 0 .4rem}
.ria-dot{width:7px;height:7px;border-radius:50%;background:currentColor;flex:none;animation:ria-pulse 2.4s ease-in-out infinite}
@keyframes ria-pulse{0%,100%{opacity:.35;transform:scale(.8)}50%{opacity:1;transform:scale(1)}}
.ria-head h2{margin:0 0 .6rem;font-weight:600;line-height:1.2}
.ria-lede{color:var(--ria-mut);margin:0}

/* signal trace under the header */
.ria-wave{display:block;width:100%;height:58px;margin:.9rem 0 .25rem;color:var(--global-theme-color);opacity:.5}
.ria-wave-path{stroke-dasharray:2600;stroke-dashoffset:2600}
.ria.is-live .ria-wave-path{animation:ria-draw 2.6s cubic-bezier(.22,.61,.36,1) forwards}
@keyframes ria-draw{to{stroke-dashoffset:0}}

/* timeline rail */
.ria-rail{list-style:none;display:flex;gap:1.35rem;overflow-x:auto;scroll-snap-type:x mandatory;
  padding:2rem .3rem 1.6rem;margin:0 -.3rem;position:relative;scrollbar-width:thin}
.ria-rail::before{content:"";position:absolute;top:calc(2rem - 13px);left:.3rem;right:.3rem;height:2px;
  background:var(--ria-line);transform:scaleX(0);transform-origin:left;transition:transform 1.5s cubic-bezier(.22,.61,.36,1) .25s}
.ria.is-live .ria-rail::before{transform:scaleX(1)}
.ria-rail::-webkit-scrollbar{height:6px}
.ria-rail::-webkit-scrollbar-thumb{background:var(--ria-line);border-radius:3px}

.ria-card{position:relative;flex:0 0 clamp(15.5rem,76vw,20.5rem);scroll-snap-align:start;
  border:1px solid var(--ria-line);border-radius:12px;overflow:hidden;display:flex;flex-direction:column;
  background:var(--global-card-bg-color,transparent);
  transition:box-shadow .3s ease,border-color .3s ease,transform .3s ease}
.ria-card:hover{border-color:var(--global-theme-color);box-shadow:0 10px 30px rgba(0,0,0,.10);transform:translateY(-3px)}
.ria-node{position:absolute;top:-13px;left:1.15rem;width:11px;height:11px;border-radius:50%;
  background:var(--global-bg-color,#fff);border:2px solid var(--ria-line);transition:border-color .3s ease,box-shadow .3s ease}
.ria-card:hover .ria-node{border-color:var(--global-theme-color);box-shadow:0 0 0 4px rgba(0,0,0,.05)}

.ria-media{aspect-ratio:3/2;overflow:hidden;background:var(--ria-line);margin:0}
.ria-media img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .6s cubic-bezier(.22,.61,.36,1)}
.ria-card:hover .ria-media img{transform:scale(1.05)}

.ria-body{padding:1rem 1.15rem 1.2rem}
.ria-step{display:block;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:var(--global-theme-color);font-weight:600;margin-bottom:.35rem}
.ria-body h3{font-size:1.03rem;margin:0 0 .45rem;font-weight:600;line-height:1.3}
.ria-body p{font-size:.875rem;line-height:1.55;color:var(--ria-mut);margin:0 0 .45rem}
.ria-body p:last-of-type{margin-bottom:0}
.ria-stat{border-top:1px solid var(--ria-line);padding-top:.55rem;margin-top:.65rem!important}
.ria-stat b{color:var(--global-theme-color);font-size:1.05rem}
.ria-link{display:inline-block;margin-top:.65rem;font-size:.82rem;font-weight:500;text-decoration:none}
.ria-link::after{content:" \2192";transition:margin-left .2s ease}
.ria-link:hover{text-decoration:underline}
.ria-link:hover::after{margin-left:.15rem}

.ria-quote{margin:.75rem 0 0;padding-left:1.15rem;border-left:3px solid var(--global-theme-color);max-width:46rem}
.ria-quote blockquote{margin:0 0 .55rem;padding:0;border:0;font-size:1.12rem;line-height:1.45;font-style:italic}
.ria-quote figcaption{font-size:.86rem;line-height:1.6;color:var(--ria-mut)}
.ria-quote .ria-link{margin-left:.15rem}

@media (max-width:576px){.ria{margin-top:2.5rem}.ria-wave{height:44px}.ria-quote blockquote{font-size:1rem}}
@media (prefers-reduced-motion:reduce){
  .ria-dot{animation:none}
  .ria-wave-path{stroke-dashoffset:0}
  .ria.is-live .ria-wave-path{animation:none}
  .ria-rail::before{transform:scaleX(1);transition:none}
  .ria-card,.ria-media img{transition:none}
  .ria-card:hover{transform:none}
  .ria-card:hover .ria-media img{transform:none}
}
</style>

<script>
(function () {
  function init() {
    var sec = document.querySelector('.ria');
    if (!sec) return;
    var cards = sec.querySelectorAll('.ria-card');
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // reveal via inline styles so a CSS purge can never strip the visible state
    if (reduce || !('IntersectionObserver' in window)) {
      sec.classList.add('is-live');
      return;
    }
    Array.prototype.forEach.call(cards, function (c) {
      c.style.opacity = '0';
      c.style.transform = 'translateY(18px)';
      c.style.transition = 'opacity .6s ease, transform .6s cubic-bezier(.22,.61,.36,1), box-shadow .3s ease, border-color .3s ease';
    });
    var show = function (c, i) {
      setTimeout(function () {
        c.style.opacity = '1';
        c.style.transform = 'none';
      }, Math.min(i, 4) * 90);
    };
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        if (e.target === sec) { sec.classList.add('is-live'); io.unobserve(sec); return; }
        show(e.target, Array.prototype.indexOf.call(cards, e.target));
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.1 });
    io.observe(sec);
    Array.prototype.forEach.call(cards, function (c) { io.observe(c); });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else { init(); }
})();
</script>
