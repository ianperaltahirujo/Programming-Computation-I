
# Problem 1
def hailstone(num: int) -> int:
    """
    Prints the hailstone sequence starting at num and returns the number of steps.
    """
    steps = 0  
    
    while num != 1:
        print(num)
        if num % 2 == 0:
            num //= 2  
        else:
            num = 3 * num + 1 
        steps += 1
    
    print(1) 
    return steps + 1  

# Problem 2
def get_factor(num: int) -> int:
    """
    Returns the largest integer smaller than num that evenly divides num.
    """
    factor = num - 1
    while num % factor != 0:
        factor -= 1
    return factor

print(get_factor(15))
print(get_factor(11))

# Problem 3
def has_twins(num: int, digit: int) -> bool:
    """
    Returns True if num has two consecutive digits with the value of digit, False otherwise.
    """
    prev_digit = -1
    num = abs(num)
    
    while num > 0:
        current_digit = num % 10
        if current_digit == digit and prev_digit == digit:
            return True
        prev_digit = current_digit
        num //= 10
    
    return False

print(has_twins(155231, 1))
print(has_twins(-155231, 5))
print(has_twins(123456, 3))