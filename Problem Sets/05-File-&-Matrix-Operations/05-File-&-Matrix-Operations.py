"""
Course  : CMPSC 131, Spring 2025
File    : PS6.py 
Name    : Ian Peralta Hirujo
GitHub User: IanePeralta

Collaboration Statement: I worked on this assignment by myself, using only course materials.
"""


# Problem 1.1
def sum_of_rows(filename: str) -> list[float]:
    """
    Reads a file containing comma-separated numerical values, computes the sum of each row, 
    and returns a list of row sums rounded to two decimals.

    Args:
        filename (str): Name of the file (txt or csv)

    Returns:
        list[float]: List of row sums, each rounded to two decimal places
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    result = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            values = stripped.split(',')
            row_sum = 0
            for v in values:
                row_sum += float(v.strip())
            result.append(round(row_sum, 2))
    return result


# Problem  1.2
def sum_of_columns(filename: str) -> list[float]:
    """
    Reads a file containing comma-separated numerical values, computes the sum of each column, 
    and returns a list of column sums rounded to two decimals.

    Args:
        filename (str): Name of the file (txt or csv)

    Returns:
        list[float]: List of column sums, each rounded to two decimal places
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    matrix = []
    max_cols = 0
    for line in lines:
        stripped = line.strip()
        if stripped:
            row = []
            for val in stripped.split(','):
                row.append(float(val.strip()))
            matrix.append(row)
            if len(row) > max_cols:
                max_cols = len(row)

    col_sums = []
    for _ in range(max_cols):
        col_sums.append(0.0)

    for row in matrix:
        for i in range(len(row)):
            col_sums[i] += row[i]

    result = []
    for val in col_sums:
        result.append(round(val, 2))
    return result



# Problem  2.1
def my_min(values: list[int]) -> int:
    minimum = values[0]
    for v in values:
        if v < minimum:
            minimum = v
    return minimum

def my_max(values: list[int]) -> int:
    maximum = values[0]
    for v in values:
        if v > maximum:
            maximum = v
    return maximum

def min_max_per_row(filename: str) -> list[tuple[int, int]]:
    """
    Reads a file of comma-separated whole numbers, returns list of tuples (min, max) per row.

    Args:
        filename (str): File name to read

    Returns:
        list[tuple[int, int]]: Min and max values for each row
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    result = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            parts = stripped.split(',')
            row = []
            for val in parts:
                row.append(int(val.strip()))
            min_val = my_min(row)
            max_val = my_max(row)
            result.append((min_val, max_val))
    return result


# Problem 2.2
def average_of_columns(filename: str) -> list[float]:
    """
    Reads a file of comma-separated values and computes average per column.

    Args:
        filename (str): The file name

    Returns:
        list[float]: Column averages, rounded to two decimal places
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    matrix = []
    max_cols = 0
    for line in lines:
        stripped = line.strip()
        if stripped:
            row = []
            for val in stripped.split(','):
                row.append(float(val.strip()))
            matrix.append(row)
            if len(row) > max_cols:
                max_cols = len(row)

    sums = []
    counts = []
    for _ in range(max_cols):
        sums.append(0.0)
        counts.append(0)

    for row in matrix:
        for i in range(len(row)):
            sums[i] += row[i]
            counts[i] += 1

    result = []
    for i in range(max_cols):
        result.append(round(sums[i] / counts[i], 2))
    return result


# Problem 2.3
def zero_below(table: list[list[int]], threshold: int) -> None:
    """
    Modifies the 2D list in place by replacing values below threshold with zero.

    Args:
        table (list[list[int]]): A 2D list of integers
        threshold (int): The threshold value

    Returns:
        None
    """
    for row in table:
        for i in range(len(row)):
            if row[i] < threshold:
                row[i] = 0


# Problem 3.1 
def buy_ticket(filename: str, seat: str) -> bool:
    """
    Attempts to book a ticket by converting 'O' to 'X' at the specified seat.

    Args:
        filename (str): File containing seat layout
        seat (str): Seat position like 'A1' or 'b3'

    Returns:
        bool: True if ticket booked successfully, False otherwise
    """
    seat = seat.strip()
    row_char = seat[0]
    col_str = seat[1:]

    ascii_code = ord(row_char)
    if 97 <= ascii_code <= 122: 
        row_char = chr(ascii_code - 32)

    try:
        col_num = int(col_str) - 1
    except ValueError:
        return False

    row_idx = ord(row_char) - ord('A')

    with open(filename, 'r') as file:
        lines = file.readlines()

    layout = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            layout.append(stripped.split(' '))

    if row_idx >= len(layout) or col_num >= len(layout[row_idx]):
        return False

    if layout[row_idx][col_num] != 'O':
        return False

    layout[row_idx][col_num] = 'X'

    with open(filename, 'w') as file:
        for i in range(len(layout)):
            row = layout[i]
            file.write(' '.join(row))
            if i != len(layout) - 1:
                file.write('\n')

    return True

###########################################

def main():
    print("Testing sum_of_rows")
    assert sum_of_rows("/Users/hyper/CMPSC/ps6-IanePeralta/numbers.csv") == [7.09, 15.55, 25.52]
    assert sum_of_rows("/Users/hyper/CMPSC/ps6-IanePeralta/testcase3.txt") == [6.0, 22.0]
    assert isinstance(sum_of_rows("/Users/hyper/CMPSC/ps6-IanePeralta/numbers.csv"), list)

    print("Testing sum_of_columns")
    assert sum_of_columns("/Users/hyper/CMPSC/ps6-IanePeralta/numbers.csv") == [13.05, 16.43, 18.68]
    assert sum_of_columns("/Users/hyper/CMPSC/ps6-IanePeralta/testcase3.txt") == [5.0, 7.0, 9.0, 7.0]
    assert isinstance(sum_of_columns("/Users/hyper/CMPSC/ps6-IanePeralta/numbers.csv"), list)

    print("Testing min_max_per_row")
    assert min_max_per_row("/Users/hyper/CMPSC/ps6-IanePeralta/testcase3.txt") == [(1, 3), (4, 7)]
    assert isinstance(min_max_per_row("/Users/hyper/CMPSC/ps6-IanePeralta/testcase3.txt")[0], tuple)
    assert min_max_per_row("/Users/hyper/CMPSC/ps6-IanePeralta/testcase3.txt")[1][1] == 7

    print("Testing average_of_columns")
    assert average_of_columns("/Users/hyper/CMPSC/ps6-IanePeralta/numbers.csv") == [4.35, 5.48, 6.23]
    assert average_of_columns("/Users/hyper/CMPSC/ps6-IanePeralta/testcase3.txt") == [2.5, 3.5, 4.5, 7.0]
    assert isinstance(average_of_columns("/Users/hyper/CMPSC/ps6-IanePeralta/testcase3.txt")[0], float)

    print("Testing zero_below")
    table = [[1, 6, 5], [3, -1], [6, 85, 12]]
    zero_below(table, 6)
    assert table == [[0, 6, 0], [0, 0], [6, 85, 12]]
    table2 = [[-1], [0], [100]]
    zero_below(table2, 1)
    assert table2 == [[0], [0], [100]]

    print("Testing buy_ticket")
    assert not buy_ticket("/Users/hyper/CMPSC/ps6-IanePeralta/seats.txt", "a1")  
    with open("/Users/hyper/CMPSC/ps6-IanePeralta/seats.txt", "w") as f:
        f.write("X O O O\nO X O O\nO O O O\n")
    assert buy_ticket("/Users/hyper/CMPSC/ps6-IanePeralta/seats.txt", "B3")      
    assert not buy_ticket("/Users/hyper/CMPSC/ps6-IanePeralta/seats.txt", "A10") 

    print("All tests passed!")

if __name__ == "__main__":
    main()

