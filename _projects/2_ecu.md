---
layout: page
title: Embedded Acquisition on Zynq
description: Moving capture into programmable logic for standalone deployment
img: assets/img/research/hardware.jpg
importance: 2
category: research
---

The Red Pitaya prototype proved the method but depended on a general-purpose
instrument. For deployment the acquisition front end had to become part of the
device.

Ported the front end onto **Zynq-7000** with the **AD9467-FMC 16-bit ADC**: capture
in programmable logic, DMA into PS DDR, and the PS/PL boundary crossed with custom
AXI-Lite control and AXI-Stream data IP — a standalone embedded system rather than
an instrument on a bench.

**Separating signature from artifact**

A fingerprint that is really an artifact of the measuring equipment is worthless.
Cross-validated **three ADCs against three probes in every combination**.
Accuracy held at **100%**.

**My role** — RTL and IP design for the capture path (ADC interface, AXI-Stream
DMA into DDR), Vivado integration, and the cross-validation study. Second author
on the CSR paper.

**Tools** — Vivado, Vitis, VHDL/Verilog, AXI-Lite and AXI-Stream, Zynq-7000 PS/PL,
AD9467-FMC, ILA for on-silicon debug.

**Links** — [paper (IEEE CSR 2025)](https://doi.org/10.1109/CSR64739.2025.11130113)

**Where it goes next**

Currently extending beyond automotive ECUs to drones, robotic arms, GPUs, battery
management systems and hardware-in-the-loop test stations — testing whether one
physical mechanism, manufacturing variation in switching behaviour, holds across
every class of embedded device.
