# Select the simulator
SIM ?= verilator
TOPLEVEL_LANG ?= verilog

# Verilog source files
VERILOG_SOURCES += ./rtl/alu.sv

# Verilator flags
VERILATOR_FLAGS += -Wno-lint -Wno-UNOPTFLAT -Wno-WIDTH

# Extra arguments
EXTRA_ARGS += --trace-fst --trace-structs $(VERILATOR_FLAGS)

simulate: clean clean_ run

clean_:
	rm -rf __pycache__ results.xml sim_build *.vcd *.fst

run:
	$(MAKE) sim MODULE=alu_tb02 TOPLEVEL=alu EXTRA_ARGS="$(EXTRA_ARGS)" PYTHONPATH="./tests:./model"

# Include Cocotb makefiles
include $(shell cocotb-config --makefiles)/Makefile.sim

