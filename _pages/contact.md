---
layout: page
permalink: /contact/
title: contact
description: How to reach me.
nav: true
nav_order: 6
---

<div class="ct">

  <a class="ct-primary" href="mailto:mrabbas@umich.edu">
    <span class="ct-ico" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>
    </span>
    <span class="ct-primary-txt">
      <b>mrabbas@umich.edu</b>
      <small>Email is the best way to reach me &mdash; I read everything, and reply to most.</small>
    </span>
  </a>

  <div class="ct-grid">
    <section class="ct-block">
      <h3>Where I work</h3>
      <p>
        Information Systems, Security, and Forensics (ISSF) Laboratory<br>
        Department of Electrical and Computer Engineering<br>
        University of Michigan&ndash;Dearborn<br>
        4901 Evergreen Road, Dearborn, MI 48128
      </p>
      <p><a href="https://umdearborn.edu/people-um-dearborn/abbas-ali">University profile</a></p>
    </section>

    <section class="ct-block">
      <h3>Happy to hear about</h3>
      <ul>
        <li>Research collaborations in hardware security and cyber-physical systems</li>
        <li>Questions about the fingerprinting work, including things that did not make the papers</li>
        <li>Talks, demos and reviewing</li>
      </ul>
    </section>
  </div>

  <section class="ct-block">
    <h3>Elsewhere</h3>
    <div class="ct-links">
      <a href="https://scholar.google.com/citations?user=he1jXaIAAAAJ">Google Scholar</a>
      <a href="https://orcid.org/0009-0007-4065-1237">ORCID</a>
      <a href="https://github.com/CodeWithAbbas">GitHub</a>
      <a href="https://www.linkedin.com/in/engr-abbasali/">LinkedIn</a>
    </div>
  </section>

</div>

<style>
.ct{--ct-line:var(--global-divider-color,#e6e6e6);--ct-mut:var(--global-text-color-light,#828282);max-width:46rem}
.ct-primary{display:flex;align-items:center;gap:1rem;padding:1.15rem 1.25rem;margin:0 0 1.5rem;
  border:1px solid var(--ct-line);border-radius:12px;text-decoration:none;color:inherit;
  transition:border-color .25s ease,box-shadow .25s ease,transform .25s ease}
.ct-primary:hover{border-color:var(--global-theme-color);box-shadow:0 8px 24px rgba(0,0,0,.08);transform:translateY(-2px);text-decoration:none}
.ct-ico{flex:none;width:42px;height:42px;border-radius:50%;display:grid;place-items:center;
  border:1px solid var(--ct-line);color:var(--global-theme-color);transition:border-color .25s ease}
.ct-primary:hover .ct-ico{border-color:var(--global-theme-color)}
.ct-ico svg{width:20px;height:20px}
.ct-primary-txt{display:flex;flex-direction:column;gap:.15rem;min-width:0}
.ct-primary-txt b{font-size:1.05rem;word-break:break-all}
.ct-primary-txt small{color:var(--ct-mut);font-size:.84rem;line-height:1.45}

.ct-grid{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:.5rem}
@media (max-width:640px){.ct-grid{grid-template-columns:1fr;gap:1.25rem}}

.ct-block{margin-bottom:1.5rem}
.ct-block h3{font-size:.74rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600;
  color:var(--global-theme-color);margin:0 0 .55rem}
.ct-block p{font-size:.92rem;line-height:1.65;color:var(--ct-mut);margin:0 0 .5rem}
.ct-block ul{margin:0;padding-left:1.1rem}
.ct-block li{font-size:.92rem;line-height:1.6;color:var(--ct-mut);margin-bottom:.3rem}

.ct-links{display:flex;flex-wrap:wrap;gap:.5rem}
.ct-links a{display:inline-block;padding:.4rem .85rem;border:1px solid var(--ct-line);border-radius:999px;
  font-size:.85rem;text-decoration:none;transition:border-color .2s ease,color .2s ease,transform .2s ease}
.ct-links a:hover{border-color:var(--global-theme-color);color:var(--global-theme-color);transform:translateY(-1px);text-decoration:none}

@media (prefers-reduced-motion:reduce){
  .ct-primary,.ct-links a{transition:none}
  .ct-primary:hover,.ct-links a:hover{transform:none}
}
</style>
