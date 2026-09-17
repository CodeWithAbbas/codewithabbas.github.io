---
layout: page
title: Hardware Fingerprinting
description: Catching device substitution that passes every cryptographic check
importance: 1
category: research
---

A cloned device carrying valid stolen credentials passes cryptographic
authentication. Nothing in the protocol can tell it apart from the genuine
part, because as far as the protocol is concerned it *is* the genuine part.

This project authenticates devices below that layer — from the analog transients
in their switching signals, which come from manufacturing variation and cannot be
copied along with the firmware.

**Results**

- **99.5% real-time accuracy** across 8 devices and 4 hardware types, including
  same-model clone pairs
- Validated on **9 electrically identical production GCM 048 ECUs** from New Eagle
- **13 capture sessions over several weeks** — a fingerprint that holds only
  within a single sitting cannot be deployed

**How it runs**

Acquisition and inference happen on the board itself, with no host PC at any ECU:
125 MS/s DMA capture on a Red Pitaya STEMlab to resolve sub-microsecond switching
edges, feature extraction from raw waveforms, and ARM32 Docker inference.

Published at **USENIX VehicleSec '26**.

*Funded by the National Science Foundation. Information Systems, Security, and
Forensics (ISSF) Laboratory, UM-Dearborn.*
