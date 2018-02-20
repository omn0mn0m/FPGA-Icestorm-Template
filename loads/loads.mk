include ../Makefile.inc

all: $(PROJ).bin

%.bin: $(PAR)/%.asc
	icepack $< $@
	
prog: $(PROJ).bin
	iceprog $<

sudo-prog: $(PROJ).bin
	@echo 'Executing prog as root!!!'
	sudo iceprog $<

clean:
	rm -f $(PROJ).bin
	
.SECONDARY:
.PHONY: all prog sudo-prog clean