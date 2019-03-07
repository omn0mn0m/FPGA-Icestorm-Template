# Makefile borrowed from https://github.com/cliffordwolf/icestorm/blob/master/examples/icestick/Makefile
#
# The following license is from the icestorm project and specifically applies to this file only:
#
#  Permission to use, copy, modify, and/or distribute this software for any
#  purpose with or without fee is hereby granted, provided that the above
#  copyright notice and this permission notice appear in all copies.
#
#  THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
#  WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
#  MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
#  ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
#  WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
#  ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
#  OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

include Makefile.inc

all: syn par loads

doc:
	@$(MAKE) -C doc -f loads.mk

loads:
	@$(MAKE) -C loads -f loads.mk

par:
	@$(MAKE) -C par -f par.mk

sim:
	@$(MAKE) -C sim -f sim.mk

syn:
	@$(MAKE) -C syn -f syn.mk

prog:
	@$(MAKE) -C loads prog -f loads.mk

sudo-prog:
	@$(MAKE) -C loads sudo-prog -f loads.mk

clean:
	@$(MAKE) -C loads clean -f loads.mk
	@$(MAKE) -C par clean -f par.mk
	@$(MAKE) -C sim clean -f sim.mk
	@$(MAKE) -C syn clean -f syn.mk

.SECONDARY:
.PHONY: all clean prog sudo-prog doc loads par sim syn
