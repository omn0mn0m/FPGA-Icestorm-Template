include ../Makefile.inc

all: $(PROJ).rpt

%.asc: $(PIN_DEF) $(SYN)/%.json
	nextpnr-ice40 --lp8k --package cm81 --json $(filter-out $<, $^)  --pcf $< --asc $@
#	arachne-pnr -d 8k -P cm81 -o $@ -p $^
	
%.rpt: %.asc
	icetime -d $(DEVICE) -mtr $@ $<

clean:
	rm -f $(PROJ).asc $(PROJ).rpt
	
.SECONDARY:
.PHONY: all clean
