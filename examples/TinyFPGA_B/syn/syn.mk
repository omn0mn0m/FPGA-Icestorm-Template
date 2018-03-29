include ../Makefile.inc

all: $(PROJ)_syn.v

%.blif: $(SRC)/%.v
	yosys -p 'synth_ice40 -top $(PROJ) -blif $@' $<
	
%_syn.v: %.blif
	yosys -p 'read_blif -wideports $^; write_verilog $@'
	
clean:
	rm -f $(PROJ).blif $(PROJ)_syn.v
	
.SECONDARY:
.PHONY: all clean