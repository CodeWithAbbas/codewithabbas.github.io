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

<style>
/* ---------- Research in Action ---------------------------------------- */
.ria {
  --ria-line: var(--global-divider-color, #e5e5e5);
  --ria-muted: var(--global-text-color-light, #828282);
  margin: 3.5rem 0 1rem;
  clear: both;
}
.ria-head { max-width: 46rem; margin-bottom: 1.75rem; }
.ria-eyebrow {
  font-size: .72rem; letter-spacing: .14em; text-transform: uppercase;
  color: var(--global-theme-color); margin: 0 0 .35rem; font-weight: 600;
}
.ria-head h2 { margin: 0 0 .6rem; font-weight: 600; line-height: 1.2; }
.ria-lede { color: var(--ria-muted); margin: 0; }

/* rail ---------------------------------------------------------------- */
.ria-rail {
  display: flex; gap: 1.25rem;
  overflow-x: auto; scroll-snap-type: x mandatory;
  padding: .25rem .25rem 1.5rem;
  margin-inline: -.25rem;
  scrollbar-width: thin;
}
.ria-rail::-webkit-scrollbar { height: 6px; }
.ria-rail::-webkit-scrollbar-thumb { background: var(--ria-line); border-radius: 3px; }

.ria-card {
  flex: 0 0 clamp(15rem, 74vw, 20rem);
  scroll-snap-align: start;
  border: 1px solid var(--ria-line);
  border-radius: 10px;
  overflow: hidden;
  background: var(--global-card-bg-color, transparent);
  display: flex; flex-direction: column;
  opacity: 0; transform: translateY(16px);
  transition: opacity .55s ease, transform .55s ease,
              box-shadow .25s ease, border-color .25s ease;
}
.ria-card.is-in { opacity: 1; transform: none; }
.ria-card:hover {
  border-color: var(--global-theme-color);
  box-shadow: 0 6px 22px rgba(0,0,0,.09);
}
.ria-media { aspect-ratio: 3/2; overflow: hidden; background: var(--ria-line); }
.ria-media img {
  width: 100%; height: 100%; object-fit: cover; display: block;
  transition: transform .5s ease;
}
.ria-card:hover .ria-media img { transform: scale(1.04); }

.ria-body { padding: 1rem 1.1rem 1.15rem; }
.ria-step {
  display: block; font-size: .7rem; letter-spacing: .12em;
  color: var(--global-theme-color); font-weight: 600; margin-bottom: .3rem;
}
.ria-body h3 { font-size: 1.02rem; margin: 0 0 .45rem; font-weight: 600; line-height: 1.3; }
.ria-body p  { font-size: .88rem; line-height: 1.55; color: var(--ria-muted); margin: 0; }
.ria-link {
  display: inline-block; margin-top: .6rem;
  font-size: .82rem; font-weight: 500; text-decoration: none;
}
.ria-link:hover { text-decoration: underline; }

/* quote ---------------------------------------------------------------- */
.ria-quote {
  margin: .5rem 0 0; padding-left: 1.1rem;
  border-left: 3px solid var(--global-theme-color);
  max-width: 46rem;
}
.ria-quote blockquote {
  margin: 0 0 .55rem; padding: 0; border: 0;
  font-size: 1.1rem; line-height: 1.45; font-style: italic;
}
.ria-quote figcaption { font-size: .85rem; line-height: 1.55; color: var(--ria-muted); }

@media (max-width: 576px) {
  .ria { margin-top: 2.5rem; }
  .ria-quote blockquote { font-size: 1rem; }
}
@media (prefers-reduced-motion: reduce) {
  .ria-card { opacity: 1; transform: none; transition: none; }
  .ria-media img { transition: none; }
  .ria-card:hover .ria-media img { transform: none; }
}
</style>

<script>
(function () {
  var cards = document.querySelectorAll('.ria-card');
  if (!cards.length) return;
  if (!('IntersectionObserver' in window) ||
      window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    cards.forEach(function (c) { c.classList.add('is-in'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      var i = Array.prototype.indexOf.call(cards, e.target);
      e.target.style.transitionDelay = Math.min(i, 4) * 70 + 'ms';
      e.target.classList.add('is-in');
      io.unobserve(e.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
  cards.forEach(function (c) { io.observe(c); });
})();
</script>


<section class="ria" aria-labelledby="ria-heading">
  <header class="ria-head">
    <p class="ria-eyebrow">Research in Action</p>
    <h2 id="ria-heading">From bench to conference floor</h2>
    <p class="ria-lede">A device does not need to announce what it is. Manufacturing leaves every chip with slightly different switching behaviour &mdash; overshoot, ringing, timing &mdash; and that signature survives anything an attacker can rewrite.</p>
  </header>

  <div class="ria-rail" role="list">
    <article class="ria-card" role="listitem">
      <div class="ria-media"><img src="/assets/img/research/hardware.jpg" alt="Instrumented test devices on the ISSF laboratory bench" loading="lazy" width="1100" height="733"></div>
      <div class="ria-body">
        <span class="ria-step">01</span>
        <h3>The physical signal</h3>
        <p>An attacker can copy firmware, a serial number, or a message. They cannot copy physics.</p>
      </div>
    </article>

    <article class="ria-card" role="listitem">
      <div class="ria-media"><img src="/assets/img/research/bench.jpg" alt="Array of test boards instrumented for measurement" loading="lazy" width="1100" height="733"></div>
      <div class="ria-body">
        <span class="ria-step">02</span>
        <h3>Same model, different device</h3>
        <p>Eight embedded devices across four hardware types, including same-model clone pairs. 99.5% real-time accuracy, with no firmware modification or protocol access.</p>
      </div>
    </article>

    <article class="ria-card" role="listitem">
      <div class="ria-media"><img src="/assets/img/research/labcar.jpg" alt="Testing at the ETAS LABCAR hardware-in-the-loop station" loading="lazy" width="1100" height="733"></div>
      <div class="ria-body">
        <span class="ria-step">03</span>
        <h3>Production hardware, not dev boards</h3>
        <p>Nine electrically identical production automotive ECUs, captured across thirteen sessions over several weeks. A fingerprint that holds only within one sitting cannot be deployed.</p>
      </div>
    </article>

    <article class="ria-card" role="listitem">
      <div class="ria-media"><img src="/assets/img/research/demo.jpg" alt="Presenting the live hardware demonstration at USENIX VehicleSec 2026" loading="lazy" width="1100" height="733"></div>
      <div class="ria-body">
        <span class="ria-step">04</span>
        <h3>Live at VehicleSec &rsquo;26</h3>
        <p>Real devices on the table in Baltimore. Attendees connected hardware and watched classification happen in real time.</p>
        <a class="ria-link" href="https://www.usenix.org/conference/vehiclesec26/presentation/ali-demo">Demo abstract &rarr;</a>
      </div>
    </article>

    <article class="ria-card" role="listitem">
      <div class="ria-media"><img src="/assets/img/research/talk.jpg" alt="Presenting Is Your ECU Really Yours at the VehicleSec 2026 podium" loading="lazy" width="1100" height="733"></div>
      <div class="ria-body">
        <span class="ria-step">05</span>
        <h3>Is Your ECU Really Yours?</h3>
        <p>The paper talk, alongside a lightning talk extending the method to production ECUs over the CAN bus.</p>
        <a class="ria-link" href="https://www.usenix.org/conference/vehiclesec26/presentation/ali">Read the paper &rarr;</a>
      </div>
    </article>
  </div>

  <figure class="ria-quote">
    <blockquote>The best part was not the presenting. It was the questions. Nobody asked whether it works.</blockquote>
    <figcaption>What they asked instead &mdash; whether a fingerprint survives thermal stress, whether it scales to thousands of devices, whether signatures begin to overlap &mdash; is now the experimental roadmap. <a class="ria-link" href="https://www.linkedin.com/in/engr-abbasali/">View on LinkedIn &rarr;</a></figcaption>
  </figure>
</section>

