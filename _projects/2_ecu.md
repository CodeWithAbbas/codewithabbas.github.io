---
layout: page
title: Embedded Acquisition on Zynq
description: Moving capture into programmable logic for standalone deployment
importance: 2
category: research
---

The Red Pitaya prototype proved the method but depended on a general-purpose
instrument. For deployment the acquisition front end had to become part of the
device.

Ported the front end onto **Zynq-7000** with the **AD9467-FMC 16-bit ADC**, moving
capture into programmable logic with DMA into PS DDR — a standalone embedded
system rather than an instrument on a bench.

**Separating signature from artifact**

A fingerprint that is really an artifact of the measuring equipment is worthless.
Cross-validated **three ADCs against three probes in every combination**.
Accuracy held at **100%**.

Published at **IEEE CSR 2025** (Chania, Greece).

**Where it goes next**

Currently extending beyond automotive ECUs to drones, robotic arms, GPUs, battery
management systems and hardware-in-the-loop test stations — testing whether one
physical mechanism, manufacturing variation in switching behaviour, holds across
every class of embedded device.
