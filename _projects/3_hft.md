---
layout: page
title: HFT Indicators on FPGA
description: First documented hardware architectures for Aroon, MACD and RSI
importance: 3
category: systems
---

High-frequency trading competes on microseconds, yet no hardware implementations
of the standard technical indicators existed in the literature. Designed the first
documented architectures for **Aroon, MACD and RSI** on Xilinx Zynq SoC, with the
latency-critical datapaths in programmable logic and everything else in software
on the ARM core.

**The division problem**

MACD required six hardware dividers, and synthesis time had become impractical.
Rather than spend area on them, reformulated the smoothing constants so each
division collapsed into a **constant multiply and a right shift** — which costs
nothing in hardware. All six dividers removed, and the longest path shortened.

**Results**

- **30× faster than software**
- MACD and RSI throughputs within **0.38 µs** — close enough to run concurrently
- Three RSI divider microarchitectures compared, combinational through fully pipelined
- Further latency reduction through critical path analysis, pipelining, folding
  and circuit replication

Published in *Alexandria Engineering Journal*, vol. 96, 2024.
