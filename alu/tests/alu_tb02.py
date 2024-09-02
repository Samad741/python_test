# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0
# Simple tests for an adder module
#import os
import random
#import sys
#from pathlib import Path

import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer
from alu_model import alu_model


@cocotb.test()
async def alu_basic_test(dut):
    """Test ALU operations"""
    # Test vectors
    test_vectors = [
        {"A": 3, "B": 2, "Sel": 0, "Expected": 5},   # A + B = 3 + 2 = 5
        {"A": 7, "B": 3, "Sel": 1, "Expected": 4},   # A - B = 7 - 3 = 4
        {"A": 2, "B": 3, "Sel": 2, "Expected": 6},   # A * B = 2 * 3 = 6
        {"A": 8, "B": 2, "Sel": 3, "Expected": 4},   # A / B = 8 / 2 = 4
        {"A": 8, "B": 0, "Sel": 3, "Expected": 0}    # A / B = 8 / 0 = 0 (division by zero)
    ]

    for vector in test_vectors:
        dut.A.value = vector["A"]
        dut.B.value = vector["B"]
        dut.Sel.value = vector["Sel"]

        await Timer(5,units="ns")  # Wait 5 ns

        assert dut.F.value == vector["Expected"], f"Test failed with A={vector['A']}, B={vector['B']}, Sel={vector['Sel']}"
        
@cocotb.coroutine       
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
        
        n = 8  # Example bit width

        # Convert the value to an integer
        raw_value = int(dut.F.value)
        
        # Check if the value is negative in two's complement
        if raw_value >= 2**(n-1):
            signed_value = raw_value - 2**n
        else:
            signed_value = raw_value
        assert signed_value == alu_model(
            A, B, Sel
        ), f"Randomised test failed with: {dut.A.value}, {dut.B.value}, {dut.Sel.value} and {dut.F.value}"

       # print(f"A={A}, B={B}, Sel={Sel}, Expected={expected} & 0xFF = {expected & 0xFF}, Got={dut.F.value} & 0xFF = {dut.F.value & 0xFF}")
       # assert dut.F.value & 0xFF == expected & 0xFF, f"Randomized test failed with A={A}, B={B}, Sel={Sel}, Expected={expected}, Got={dut.F.value}"
# Registering the randomized test
factory = TestFactory(alu_randomised_test)
factory.generate_tests()
        
