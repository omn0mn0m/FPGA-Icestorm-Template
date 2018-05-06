include ../Makefile.inc

sim: $(PROJ).vcd
	gtkwave $<
	
%_tb: %_tb.v $(SRC)/%.v  $(SRC_SUB_FILES)
	iverilog -o $@ $^

%.vcd: %_tb
	vvp $< +vcd=$@
	
%_syntb: %_tb.v %_syn.v
	iverilog -o $@ $^ `yosys-config --datdir/ice40/cells_sim.v`

%_syntb.vcd: %_syntb
	vvp -N $< +vcd=$@
	
clean:
	rm -f $(PROJ)_tb $(PROJ).vcd

.SECONDARY:
.PHONY: clean sim
