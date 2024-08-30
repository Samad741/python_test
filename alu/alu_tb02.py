# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0
# Simple tests for an adder module
import os
import random
import sys
from pathlib import Path

import cocotb
from cocotb.triggers import Timer
from alu_model import alu_model


@cocotb.test()
async def alu_randomised_test(dut):
    """Test for adding 2 random numbers multiple times"""

    for i in range(10):
        A = random.randint(0, 15)
        B = random.randint(0, 15)
        Sel = random.randint(0, 3)

        dut.A.value = A
        dut.B.value = B
        dut.Sel.value = Sel

        await Timer(2, units="ns")
        print(f"A = {dut.A.value}, B = {dut.B.value}, Sel = {dut.Sel.value} and F = {dut.F.value}")
        assert dut.F.value == alu_model(
            A, B, Sel
        ), f"Randomised test failed with: {dut.A.value}, {dut.B.value}, {dut.Sel.value} and {dut.F.value}"

       # print(f"A={A}, B={B}, Sel={Sel}, Expected={expected} & 0xFF = {expected & 0xFF}, Got={dut.F.value} & 0xFF = {dut.F.value & 0xFF}")
       # assert dut.F.value & 0xFF == expected & 0xFF, f"Randomized test failed with A={A}, B={B}, Sel={Sel}, Expected={expected}, Got={dut.F.value}"
        