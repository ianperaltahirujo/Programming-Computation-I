

# Problem 1.1
def skipping(n):
    """
    Returns the sum of every other integer from n down to 0 (inclusive).

    Args:
        n (int): A non-negative integer

    Returns:
        int: The sum of every other number from n to 0
    """
    if n <= 0:
        return 0
    return n + skipping(n - 2)


# Problem 1.2
def zig_zag(n):
    """
    Returns a zig-zag string of stars with decreasing and increasing pattern.

    Args:
        n (int): A non-negative integer

    Returns:
        str: Zig-zag star pattern string
    """
    if n == 0:
        return ""
    return ('*' * n) + '\n' + zig_zag(n - 1) + ('\n' if n != 1 else '') + ('*' * n)


# Problem 1.3
def product_of_digits(n):
    """
    Returns the product of the digits of n, excluding zeros.

    Args:
        n (int): A positive integer

    Returns:
        int: Product of non-zero digits
    """
    if n < 10:
        return n if n != 0 else 1
    last = n % 10
    rest_product = product_of_digits(n // 10)
    return rest_product * last if last != 0 else rest_product


# Problem 2.1
def near_by_unique(n):
    """
    Removes adjacent repeated digits from an integer.

    Args:
        n (int): A positive integer

    Returns:
        int: Integer with adjacent duplicates removed
    """
    if n < 10:
        return n
    last = n % 10
    rest = near_by_unique(n // 10)
    if rest % 10 == last:
        return rest
    return rest * 10 + last


# Problem 2.2
def combine_lists(list1, list2, op):
    """
    Applies an arithmetic operation element-wise to two lists.

    Args:
        list1 (list): First list
        list2 (list): Second list
        op (str): Operation ('+', '-', '*', '/')

    Returns:
        list: Resulting list
    """
    if not list1:
        return []
    if op == '+':
        result = list1[0] + list2[0]
    elif op == '-':
        result = list1[0] - list2[0]
    elif op == '*':
        result = list1[0] * list2[0]
    elif op == '/':
        result = list1[0] / list2[0]
    else:
        raise ValueError("Invalid operation")
    return [result] + combine_lists(list1[1:], list2[1:], op)


# Problem 2.3
def to_evens(lst):
    """
    Returns a new list with odd values increased by 1 (non-mutative).

    Args:
        lst (list): Input list of integers

    Returns:
        list: Modified list
    """
    if not lst:
        return []
    head = lst[0] + 1 if lst[0] % 2 != 0 else lst[0]
    return [head] + to_evens(lst[1:])


# Problem 2.4
def to_evens_destructive(lst):
    """
    Modifies the input list in place, incrementing odd values by 1.

    Args:
        lst (list): List to be modified

    Returns:
        None
    """
    def helper(index):
        if index >= len(lst):
            return
        if lst[index] % 2 != 0:
            lst[index] += 1
        helper(index + 1)

    helper(0)


# Problem 3.1
def gcd(a, b):
    """
    Returns the greatest common divisor of a and b using Euclidean algorithm.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: GCD
    """
    if b == 0:
        return a
    return gcd(b, a % b)

def right_cumulative_gcd(lst):
    """
    Returns a list where each element is the GCD of itself and all elements to the right.

    Args:
        lst (list): A list of positive integers

    Returns:
        list: List of right cumulative GCDs
    """
    def helper(index):
        if index == len(lst) - 1:
            return [lst[index]]
        rest = helper(index + 1)
        return [gcd(lst[index], rest[0])] + rest

    return helper(0)

def main():
    # Part 1
    assert skipping(11) == 36
    assert skipping(10) == 30
    assert skipping(1) == 1

    assert zig_zag(1) == "*\n*"
    assert zig_zag(2) == "**\n*\n*\n**"
    assert zig_zag(3) == "***\n**\n*\n*\n**\n***"

    assert product_of_digits(1024) == 8
    assert product_of_digits(5009) == 45
    assert product_of_digits(1111) == 1

    # Part 2
    assert near_by_unique(22224666666782) == 246782
    assert near_by_unique(111223344) == 1234
    assert near_by_unique(100000) == 10

    assert combine_lists([1, 2], [3, 4], '+') == [4, 6]
    assert combine_lists([2, 2], [3, 4], '*') == [6, 8]
    assert combine_lists([5, 5], [2, 2], '-') == [3, 3]

    assert to_evens([1, 2, 3]) == [2, 2, 4]
    assert to_evens([0, 7, 8]) == [0, 8, 8]
    assert to_evens([-1, -2, -3]) == [0, -2, -2]

    my_list = [1, 2, 3]
    to_evens_destructive(my_list)
    assert my_list == [2, 2, 4]

    my_list = [1, 5, 6, 9]
    to_evens_destructive(my_list)
    assert my_list == [2, 6, 6, 10]

    my_list = [2, 4, 6]
    to_evens_destructive(my_list)
    assert my_list == [2, 4, 6]

    # Part 3
    assert right_cumulative_gcd([20, 50, 15, 40, 10]) == [5, 5, 5, 10, 10]
    assert right_cumulative_gcd([10, 5]) == [5, 5]
    assert right_cumulative_gcd([3, 9, 27]) == [3, 9, 27]

    print('Tests passed!')
    
if __name__ == "__main__":
    main()
