

# Problem 1.1
def primes_count(start: int, stop: int) -> int:
    """
    Displays all prime numbers between start and stop (inclusive) and returns their count.

    Args:
        start (int): Starting integer.
        stop (int): Stopping integer.

    Returns:
        int: Count of prime numbers, or -1 if start > stop.
    """
    if start > stop:
        print("ERROR")
        return -1

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_count = 0
    for num in range(start, stop + 1):
        if is_prime(num):
            print(num)
            prime_count += 1
    return prime_count


# Problem 1.2
def decay(amount: int, years: int) -> float:
    """
    Calculates the remaining amount of Cobalt-60 after a given number of years.

    Args:
        amount (int): Initial amount in grams.
        years (int): Number of years.

    Returns:
        float: Remaining amount rounded to two decimal places using Half Round-Up method.
    """

    def half_round_up(value: float, decimals: int = 2) -> float:
        """Rounds using the Half Round-Up method."""
        factor = 10 ** decimals
        return int(value * factor + 0.5) / factor 

    remaining_amount = float(amount)  

    for _ in range(years):
        remaining_amount *= 0.88 

    return half_round_up(remaining_amount, 2)


# Problem 1.3
def prefix_sum(start: int, stop: int):
    """
    Displays the running sum from start to stop (inclusive).

    Args:
        start (int): Starting integer.
        stop (int): Stopping integer.

    Returns:
        None, but returns -1 if start > stop.
    """
    if start > stop:
        print("ERROR")
        return -1 

    total = 0
    for num in range(start, stop + 1):
        total += num
        print(total)  


# Problem 2.1
def divisors_count(num: int) -> int:
    """
    Returns the number of divisors of a positive integer.

    Args:
        num (int): The input integer.

    Returns:
        int: The number of divisors.
    """
    count = 0
    divisor = 1
    while divisor <= num:
        if num % divisor == 0:
            count += 1
        divisor += 1
    return count


# Problem 2.2
def count_digits(num: int) -> int:
    """
    Counts the number of digits in an integer.

    Args:
        num (int): The input integer.

    Returns:
        int: The number of digits.
    """
    num = abs(num)
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count if count > 0 else 1


# Problem 2.3
def divisible_by(limit: int, divisor: int) -> int:
    """
    Displays all numbers <= limit divisible by divisor.

    Args:
        limit (int): The upper limit.
        divisor (int): The divisor.

    Returns:
        int: The count of displayed numbers.
    """
    count = 0
    current = divisor
    while current <= limit:
        if current % divisor == 0:
            print(current)
            count += 1
        current += 1
    return count


# Problem 3.1
def is_armstrong_number(num: int) -> bool:
    """
    Checks if a number is an Armstrong number.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if it's an Armstrong number, False otherwise.
    """
    original = num
    digit_count = count_digits(num)
    total = 0
    while num > 0:
        digit = num % 10
        power = 1
        for _ in range(digit_count):
            power *= digit
        total += power
        num //= 10
    return total == original


# Problem 3.2
def factorial_sum(n: int) -> int:
    """
    Calculates the sum of factorials from 1! to n!.

    Args:
        n (int): The upper limit.

    Returns:
        int: The sum of factorials.
    """
    total = 0
    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        total += fact
    return total


# Problem 3.3
def is_perfect_number(num: int) -> bool:
    """
    Checks if a number is a perfect number.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if perfect, False otherwise.
    """
    total = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            total += i
    return total == num


# Problem 3.4
def temp_sum(start: int, end: int) -> float:
    """
    Calculates the sum of Fahrenheit equivalents of Celsius temperatures from start to end (increments of 5).

    Args:
        start (int): Starting Celsius temperature.
        end (int): Ending Celsius temperature.

    Returns:
        float: The sum of Fahrenheit equivalents.
    """
    total = 0.0
    c = start
    while c <= end:
        f = (c * 9 / 5) + 32
        total += f
        c += 5
    return total

    
# Problem 3.5
def estimate(start_population: int, target_population: int) -> int:
    """
    Determines the time in hours to reach or exceed a target population with doubling every hour.

    Args:
        start_population (int): Initial population.
        target_population (int): Target population.

    Returns:
        int: The time in hours.
    """
    hours = 0
    while start_population < target_population:
        start_population *= 2
        hours += 1
    return hours


# Problem 3.6
def classify(n: int) -> None:
    """
    Classifies numbers from 2 to n as abundant, deficient, or perfect.

    Args:
        n (int): The upper limit.
    """
    for num in range(2, n + 1):
        total = 0
        for i in range(1, num):
            if num % i == 0:
                total += i
        if total > num:
            print("{} is abundant".format(num))
        elif total < num:
            print("{} is deficient".format(num))
        else:
            print("{} is perfect".format(num))


# Problem 3.7
def get_steps(num: int) -> int:
    """
    Counts the steps to reduce a number to zero.

    Args:
        num (int): The input number.

    Returns:
        int: The number of steps, or -1 if invalid.
    """
    if not type(num) is int or num < 0:  
        return -1
    steps = 0
    while num > 0:
        num = num // 2 if num % 2 == 0 else num - 1
        steps += 1
    return steps


#######################################################################################

    
def main():

    # Testing primes_count
    assert(primes_count(2, 10) == 4) 
    assert(primes_count(20, 30) == 2)  
    assert(primes_count(50, 50) == 0)  

    # Testing decay
    assert(decay(100, 2) == 77.44)
    assert(decay(500, 10) == 139.25)
    assert(decay(25, 0) == 25.0)  

    # Testing prefix_sum
    prefix_sum(1, 5)
    prefix_sum(4, 8)
    prefix_sum(10, 12)

    # Testing divisors_count
    assert(divisors_count(100) == 9)
    assert(divisors_count(1) == 1)
    assert(divisors_count(37) == 2) 

    # Testing count_digits
    assert(count_digits(100000) == 6)
    assert(count_digits(0) == 1) 
    assert(count_digits(-98765) == 5)

    # Testing divisible_by
    assert(divisible_by(15, 5) == 3)  
    assert(divisible_by(25, 7) == 3)  
    assert(divisible_by(9, 3) == 3)  

    # Testing is_armstrong_number
    assert(is_armstrong_number(9474) is True)
    assert(is_armstrong_number(407) is True)
    assert(is_armstrong_number(99) is False)

    # Testing factorial_sum
    assert(factorial_sum(6) == 873) 
    assert(factorial_sum(3) == 9)  
    assert(factorial_sum(8) == 46233)

    # Testing is_perfect_number
    assert(is_perfect_number(28) is True)
    assert(is_perfect_number(12) is False)
    assert(is_perfect_number(496) is True)

    # Testing temp_sum
    assert(round(temp_sum(-10, 10), 2) == 160.0)
    assert(round(temp_sum(0, 50), 2) == 847.0)
    assert(round(temp_sum(-5, 5), 2) == 96.0)

    # Testing estimate
    assert(estimate(5, 80) == 4)
    assert(estimate(2, 64) == 5)
    assert(estimate(100, 100) == 0)

    # Testing classify
    classify(30)  
    classify(12)  
    classify(100)

    # Testing get_steps
    assert(get_steps(27) == 8)
    assert(get_steps(1) == 1)
    assert(get_steps(1024) == 11)

    pass

if __name__ == "__main__":
    main()

    