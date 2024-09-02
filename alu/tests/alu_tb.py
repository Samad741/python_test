import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer
import random

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
async def run_randomized_test(dut):
    """Run a randomized test of the ALU"""
    for _ in range(10):  # Run 100 randomized tests
        a = random.randint(0, 15)
        b = random.randint(0, 15)
        sel = random.randint(0, 3)

        if sel == 0:
            expected = a + b
        elif sel == 1:
            expected = a - b
        elif sel == 2:
            expected = a * b
        elif sel == 3:
            expected = a // b if b != 0 else 0

        dut.A.value = a
        dut.B.value = b
        dut.Sel.value = sel

        await Timer(10,units="ns")  # Wait 5 ns
        print(f"A={a}, B={b}, Sel={sel}, Expected={expected} & 0xFF = {expected & 0xFF}, Got={dut.F.value} & 0xFF = {dut.F.value & 0xFF}")
        assert dut.F.value & 0xFF == expected & 0xFF, f"Randomized test failed with A={a}, B={b}, Sel={sel}, Expected={expected}, Got={dut.F.value}"
        

# Registering the randomized test
factory = TestFactory(run_randomized_test)
factory.generate_tests()
