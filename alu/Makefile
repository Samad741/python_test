# Select the simulator
SIM ?= verilator
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += ./alu.sv

VERILATOR_FLAGS += -Wno-lint -Wno-UNOPTFLAT -Wno-WIDTH
EXTRA_ARGS += --trace-fst --trace-structs $(VERILATOR_FLAGS)

simulate: clean clean_ run

clean_:
	rm -rf __pycache__ results.xml sim_build *.vcd *.fst

run:
	$(MAKE) sim MODULE=alu_tb02 TOPLEVEL=alu
include $(shell cocotb-config --makefiles)/Makefile.sim

