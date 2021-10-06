# FPGA Icestorm Template
This is my personal project structure and Makefile for the FPGA boards which features an iCE40 FPGA. This particular example is based on the [Icestorm Template here](https://github.com/tinyfpga/TinyFPGA-B-Series). The template has been tested on both the TinyFPGA and the Upduino development boards.

The purpose of this template is to provide a multi-directory structure that allows for clear file output and organisation.

## Directories
- `docs` - Contains GitHub contribution documentation, as well as eventual location for generated project docs
- `examples` - Full projects using the template for reference
- `loads` - Files (.bin) to load onto the FPGA
- `par` - Place and route files (generated file and .pcf file)
- `scripts` - Python scripts to assist in various tasks
- `sim` - Testbench files and sim results
- `src`- Source design files
- `syn` - Synthesis generated files

## Tools Needed
- [Project Icestorm](https://github.com/cliffordwolf/icestorm)
- [NextPNR](https://github.com/YosysHQ/nextpnr)
- [Yosys](http://www.clifford.at/yosys/)
- [GTKWave](http://gtkwave.sourceforge.net/)
- [Make](https://www.gnu.org/software/make/manual/make.html)
- [Python 2.7](https://www.python.org/)

## Code Generation
To generate your Verilog project, run: `python scripts/generate_verilog.py`

To generate a testbench from a Verilog top-level module, run: `python scripts/generate_testbench.py`

To generate a physical constraints file from a Verilog top-level module, run: `python scripts/generate_pcf.py`

## FPGA Workflow Commands
To synthesise then place and route, run: `make`

To simulate, run: `make sim`
