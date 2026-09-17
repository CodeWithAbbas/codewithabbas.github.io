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

  <div class="ria-railwrap">
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
  <p class="ria-hint"><span class="ria-hint-bar"><i></i></span>Drifting &mdash; hover to pause, click to hold</p>
  </div>

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

.ria-wave{display:block;width:100%;height:58px;margin:.9rem 0 .25rem;color:var(--global-theme-color);opacity:.5}
.ria-wave-path{stroke-dasharray:2600;stroke-dashoffset:2600}
.ria.is-live .ria-wave-path{animation:ria-draw 2.6s cubic-bezier(.22,.61,.36,1) forwards}
@keyframes ria-draw{to{stroke-dashoffset:0}}

/* ---- rail ---- */
.ria-railwrap{position:relative}
.ria-rail{list-style:none;display:flex;gap:1.35rem;overflow-x:auto;
  padding:2rem .3rem 1.6rem;margin:0 -.3rem;position:relative;
  overscroll-behavior-x:contain;scrollbar-width:none;-ms-overflow-style:none}
.ria-rail::-webkit-scrollbar{display:none}
/* snapping only once the visitor has taken control */
.ria-rail.is-manual{scroll-snap-type:x mandatory}
.ria-rail.is-manual .ria-card{scroll-snap-align:start}

.ria-rail::before{content:"";position:absolute;top:calc(2rem - 13px);left:.3rem;right:.3rem;height:2px;
  background:var(--ria-line);transform:scaleX(0);transform-origin:left;
  transition:transform 1.5s cubic-bezier(.22,.61,.36,1) .25s}
.ria.is-live .ria-rail::before{transform:scaleX(1)}

/* edge fades so cards drift in and out rather than clipping hard */
.ria-railwrap::before,.ria-railwrap::after{content:"";position:absolute;top:0;bottom:0;width:3.5rem;pointer-events:none;z-index:2;opacity:0;transition:opacity .4s ease}
.ria-railwrap::before{left:-.3rem;background:linear-gradient(to right,var(--global-bg-color,#fff),transparent)}
.ria-railwrap::after{right:-.3rem;background:linear-gradient(to left,var(--global-bg-color,#fff),transparent)}
.ria-railwrap.has-fade::before,.ria-railwrap.has-fade::after{opacity:1}

.ria-card{position:relative;flex:0 0 clamp(15.5rem,76vw,20.5rem);
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

/* motion-state hint */
.ria-hint{display:flex;align-items:center;gap:.45rem;font-size:.7rem;letter-spacing:.06em;
  color:var(--ria-mut);margin:.1rem 0 0;min-height:1.1rem;opacity:0;transition:opacity .45s ease}
.ria-railwrap.has-fade .ria-hint{opacity:.75}
.ria-hint-bar{width:26px;height:2px;background:var(--ria-line);border-radius:2px;overflow:hidden;position:relative}
.ria-hint-bar i{position:absolute;inset:0;background:var(--global-theme-color);transform-origin:left;
  transform:scaleX(0);animation:ria-sweep 3.2s linear infinite}
.ria-rail.is-paused ~ .ria-hint .ria-hint-bar i,
.ria-rail.is-manual ~ .ria-hint .ria-hint-bar i{animation-play-state:paused}
@keyframes ria-sweep{0%{transform:scaleX(0)}100%{transform:scaleX(1)}}

.ria-quote{margin:.75rem 0 0;padding-left:1.15rem;border-left:3px solid var(--global-theme-color);max-width:46rem}
.ria-quote blockquote{margin:0 0 .55rem;padding:0;border:0;font-size:1.12rem;line-height:1.45;font-style:italic}
.ria-quote figcaption{font-size:.86rem;line-height:1.6;color:var(--ria-mut)}
.ria-quote .ria-link{margin-left:.15rem}

@media (max-width:576px){.ria{margin-top:2.5rem}.ria-wave{height:44px}.ria-quote blockquote{font-size:1rem}
  .ria-railwrap::before,.ria-railwrap::after{width:1.75rem}}
@media (prefers-reduced-motion:reduce){
  .ria-dot,.ria-hint-bar i{animation:none}
  .ria-wave-path{stroke-dashoffset:0}
  .ria.is-live .ria-wave-path{animation:none}
  .ria-rail::before{transform:scaleX(1);transition:none}
  .ria-rail{scroll-snap-type:x mandatory}
  .ria-card,.ria-media img{transition:none}
  .ria-card:hover{transform:none}
  .ria-card:hover .ria-media img{transform:none}
}
</style>

<script>
(function () {
  var SPEED = 62;        // px per second
  var START_DELAY = 900; // let the reveal settle before drifting

  function init() {
    var sec  = document.querySelector('.ria');
    if (!sec) return;
    var rail = sec.querySelector('.ria-rail');
    if (!rail) return;

    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var cards  = Array.prototype.slice.call(rail.querySelectorAll('.ria-card'));

    // ---- reveal ------------------------------------------------------
    if (reduce || !('IntersectionObserver' in window)) {
      sec.classList.add('is-live');
      rail.classList.add('is-manual');
      return;                                   // no drifting at all
    }
    cards.forEach(function (c) {
      c.style.opacity = '0';
      c.style.transform = 'translateY(18px)';
      c.style.transition = 'opacity .6s ease, transform .6s cubic-bezier(.22,.61,.36,1),' +
                           ' box-shadow .3s ease, border-color .3s ease';
    });

    var started = false;
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        if (e.target === sec) {
          sec.classList.add('is-live');
          cards.forEach(function (c, i) {
            setTimeout(function () { c.style.opacity = '1'; c.style.transform = 'none'; },
                       Math.min(i, 4) * 90);
          });
          io.unobserve(sec);
          if (!started) { started = true; setTimeout(startDrift, START_DELAY); }
        }
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.1 });
    io.observe(sec);

    // ---- auto-drift --------------------------------------------------
    function startDrift() {
      // seamless loop: duplicate the set once, reset at the halfway mark
      var half = rail.scrollWidth;
      if (rail.clientWidth >= half - 4) return;   // everything already fits
      cards.forEach(function (c) {
        var clone = c.cloneNode(true);
        clone.setAttribute('aria-hidden', 'true');
        clone.style.opacity = '1';
        clone.style.transform = 'none';
        Array.prototype.forEach.call(clone.querySelectorAll('a'), function (a) {
          a.setAttribute('tabindex', '-1');
        });
        rail.appendChild(clone);
      });
      rail.parentNode.classList.add('has-fade');

      var hovering = false, offscreen = false, hidden = false, manual = false;
      var carry = 0, last = 0, raf = 0;

      function paused() { return hovering || offscreen || hidden; }
      function syncClass() {
        rail.classList.toggle('is-paused', paused() && !manual);
      }

      function takeControl() {
        if (manual) return;
        manual = true;
        rail.classList.add('is-manual');
        rail.classList.remove('is-paused');
        cancelAnimationFrame(raf);
      }

      function step(t) {
        if (manual) return;
        if (!last) last = t;
        var dt = Math.min((t - last) / 1000, 0.05);   // clamp after tab switches
        last = t;
        if (!paused()) {
          carry += SPEED * dt;
          var whole = Math.floor(carry);
          if (whole) {
            carry -= whole;
            rail.scrollLeft += whole;
            if (rail.scrollLeft >= half) rail.scrollLeft -= half;
          }
        }
        raf = requestAnimationFrame(step);
      }
      raf = requestAnimationFrame(step);

      // pause while the pointer or keyboard focus is on the rail
      rail.addEventListener('mouseenter', function () { hovering = true;  syncClass(); });
      rail.addEventListener('mouseleave', function () { hovering = false; last = 0; syncClass(); });
      rail.addEventListener('focusin',    function () { hovering = true;  syncClass(); });
      rail.addEventListener('focusout',   function () { hovering = false; last = 0; syncClass(); });

      // any deliberate interaction hands control over for good
      ['pointerdown', 'wheel', 'touchstart', 'keydown'].forEach(function (ev) {
        rail.addEventListener(ev, takeControl, { passive: true });
      });

      // don't burn frames off-screen or in a background tab
      new IntersectionObserver(function (es) {
        offscreen = !es[0].isIntersecting; last = 0; syncClass();
      }, { threshold: 0 }).observe(rail);
      document.addEventListener('visibilitychange', function () {
        hidden = document.hidden; last = 0; syncClass();
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else { init(); }
})();
</script>
