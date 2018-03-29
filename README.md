# FPGA Icestorm Template
This is my personal project structure and Makefile for the FPGA boards which features an iCE40 FPGA. This particular example is based on the [Icestorm Template here](https://github.com/tinyfpga/TinyFPGA-B-Series).

The purpose of this template is to provide a multi-directory structure that allows for clear file output and organisation.

## Code Generation
To generate your Verilog project, run: `python scripts/generate_verilog.v`

To generate a testbench from a Verilog top-level module, run: `python scripts/generate_testbench.py`

To generate a physical constraints file from a Verilog top-level module, run: `python scripts/generate_pcf.py`

## FPGA Workflow Commands
To synthesise then place and route, run: `make`

To simulate, run: `make sim`