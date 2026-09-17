---
layout: page
title: Hardware Design Projects
description: Processor, CNN accelerator and neural network RTL on Zynq
importance: 4
category: systems
---

#### 16-bit Microprocessor in VHDL

Single-cycle 16-bit CPU on Zynq-7020 — full datapath with ALU, register file,
instruction memory and control unit. Functionally verified and **timing closed at
143 MHz**. *(ECE 575)*

#### CNN Accelerator on PYNQ-Z2

Hardware/software co-design taken end to end: PyTorch training (**95.80% accuracy**
on the 43-class GTSRB dataset), Vitis HLS synthesis, INT8 quantisation and AXI
deployment. **89% hardware accuracy at 101 MHz** using 55% of available LUTs.
*(ECE 554)*

#### MNIST Neural Network in RTL

Pipelined MAC engines in VHDL for a fully-connected network. Fixed-point weights
held in BRAM, deployed on Zynq-7020 over AXI-Stream with ARM DMA. *(ECE 5752)*

---

Related journal work compares machine learning models for financial time-series
prediction, published in *PLOS ONE* (2023).
