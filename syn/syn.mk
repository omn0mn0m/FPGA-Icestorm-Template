include ../Makefile.inc

all: $(PROJ)_syn.v

%.json: $(SRC)/%.v
	yosys -p 'synth_ice40 -top $(PROJ) -json $@' $<
	
%_syn.v: %.json
	yosys -p 'read_json $^; write_verilog $@'
	
clean:
	rm -f $(PROJ).json $(PROJ)_syn.v
	
.SECONDARY:
.PHONY: all clean
