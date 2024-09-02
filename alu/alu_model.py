def alu_model(a: int, b: int, sel: int) -> int:
    if sel == 0:
        result = a + b
        return a + b
    elif sel == 1:
        return a - b
    elif sel == 2:
        return a * b
    elif sel == 3:
        return a // b if b != 0 else 0  
        # Use integer division and handle division by zero
    else:
        return 0

        
#def alu_model(a: int, b: int, sel: int) -> str:
#    if sel == 0:
#        result = a + b
#    elif sel == 1:
#        result = a - b
#    elif sel == 2:
#        result = a * b
#    elif sel == 3:
#        result = a // b if b != 0 else 0  # Handle division by zero
#    else:
#        result = 0
#
#    # Convert the result to binary and return
#    return bin(result)