import pytest
from alu_model import alu_model  # Import the ALU function

@pytest.mark.parametrize("a, b, sel, expected", [
    (3, 2, 0, 5),   # Test case for addition: 3 + 2 = 5
    (7, 3, 1, 4),   # Test case for subtraction: 7 - 3 = 4
    (2, 3, 2, 6),   # Test case for multiplication: 2 * 3 = 6
    (8, 2, 3, 4),   # Test case for division: 8 / 2 = 4
    (8, 0, 3, 0),   # Test case for division by zero: 8 / 0 = 0
    (8, 0, 4, 0)    # Test case for invalid sel value, should return 0
])
def test_alu_operations(a, b, sel, expected):
    """Test ALU operations with various inputs."""
    result = alu_model(a, b, sel)
    assert result == expected, f"Test failed with A={a}, B={b}, Sel={sel}: Expected {expected}, got {result}"

def test_randomized_operations():
    """Test ALU operations with randomized inputs."""
    import random

    for _ in range(100):  # Run 100 randomized tests
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

        result = alu_model(a, b, sel)
        assert result == expected, f"Randomized test failed with A={a}, B={b}, Sel={sel}: Expected {expected}, got {result}"
