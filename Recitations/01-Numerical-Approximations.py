

# Problem 1

def get_sum(start: int, stop: int, multiple: int):
    """ 
    Displays numbers from start to stop divisible 
    by the multiple value and returns their sum.

    Args:
        start (int): The starting integer (inclusive).
        stop (int): The stopping integer (inclusive).
        multiple (int): The divisor to check divisibility.

    Returns:
        int: The sum of all divisible numbers, or 0 if none are found.
    """
    out = 0
    for number in range(start, stop + 1):
        if number % multiple == 0:
            print(number)
            out += number

    return out


# Problem 2

def sum_multiples_xor(stop: int) -> int:
    """
    Sums numbers from 1 to `stop` that are divisible by 3 or 7 but not both.

    Args:
    stop (int): The stopping integer (inclusive).

    Returns:
    int: The sum of all numbers divisible by 3 or 7 but not both.
    If input is negative, returns -1 and prints an error message.
    """
    if stop < 1:
        print("Input must be positive")
        return -1

    total_sum = 0
    count = 0

    for number in range(1, stop + 1):
        divisible_by_3 = (number % 3 == 0)
        divisible_by_7 = (number % 7 == 0)
        if divisible_by_3 ^ divisible_by_7:
            count += 1
            total_sum += number

    print("Count of numbers summed:", count)
    return total_sum


# Problem 3

def get_sqrt(num: float, iterations: int) -> float:
    """
    Approximates the square root of a given number using Newton's method.

    Args:
        num (float): The number whose square root is to be approximated.
        iterations (int): The number of iterations to refine the result.

    Returns:
        float: The approximated square root.
    """
    if num < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    x = num / 2

    for _ in range(iterations):
        x = 0.5 * (x + num / x)

    return x

def main():

# Problem 1
    print(get_sum(1, 10, 3))

# Problem 2
    print(sum_multiples_xor(20))

# Problem 3
    print(get_sqrt(36, 15))
    print(get_sqrt(125, 3))
    print(get_sqrt(125, 20))
    print(get_sqrt(2, 9))


   
if __name__ == "__main__":
    main()
