# Problem 1.1
def how_many(rows):
    """Calculate the total number of pool balls in a triangular arrangement.
    
    Args:
        rows (int): The number of rows in the triangle.
    
    Returns:
        int: The total number of pool balls, or -1 if input is invalid.
    """
    if not isinstance(rows, int) or rows < 0:
        return -1
    return ((rows * (rows + 1)) // 2)

# Problem 1.2
import math

def get_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points in a 2D plane.
    
    Args:
        x1, y1 (float): Coordinates of the first point.
        x2, y2 (float): Coordinates of the second point.
    
    Returns:
        float: The distance between the two points.
    """
    return float(math.sqrt((x2 - x1) ** 2 + (y2 - y1) **2))

# Problem 1.3
def is_triangle(side_a, side_b, side_c):
    """Determine if three side lengths can form a valid triangle.
    
    Args:
        side_a, side_b, side_c (float): Side lengths of the triangle.
    
    Returns:
        bool: True if the sides form a valid triangle, False otherwise.
    """
    if any(side <= 0 for side in (side_a, side_b, side_c)):
        return False
    # Triangle Inequality Theorem
    return side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a 

# Problem 1.4
def almost_equal(a, b, max=1e-9):
    """Check if two floating-point numbers are almost equal within a given tolerance.
    
    Args:
        a, b (float): Numbers to compare.
        max (float, optional): Tolerance level. Defaults to 1e-9.
    
    Returns:
        bool: True if numbers are nearly equal, False otherwise.
    """
    return abs(a - b) < max

def is_right_triangle(vrtx_x1, vrtx_y1, vrtx_x2, vrtx_y2, vrtx_x3, vrtx_y3):
    """Determine whether the points form a right triangle.

    Args:
        vrtx_x1, vrtx_y1 (float): First vertex coordinates.
        vrtx_x2, vrtx_y2 (float): Second vertex coordinates.
        vrtx_x3, vrtx_y3 (float): Third vertex coordinates.
        
    Returns true if the points form a right triangle, False otherwise.
    """
# Compute the distances between all pairs of points
    side1 = get_distance(vrtx_x1, vrtx_y1, vrtx_x2, vrtx_y2)
    side2 = get_distance(vrtx_x1, vrtx_y1, vrtx_x3, vrtx_y3)
    side3 = get_distance(vrtx_x2, vrtx_y2, vrtx_x3, vrtx_y3)
    hypotenuse = max(side1, side2, side3)
    if hypotenuse == side1:
        return almost_equal(side2 ** 2 + side3 ** 2, hypotenuse ** 2)
    elif hypotenuse == side2:
        return almost_equal(side1 ** 2 + side3 ** 2, hypotenuse ** 2)
    else:
        return almost_equal(side1 ** 2 + side2 ** 2, hypotenuse ** 2)

# Problem 1.5

def get_chinese_zodiac(year):
    """Return the Chinese zodiac sign for the given year.

    Args:
        year (int): The year to determine the zodiac sign.

        Returns: 
            int: the corresponding Chinese zodiac sign."""
    if year % 12 == 0:
        return "monkey"
    elif year % 12 ==1:
        return "rooster"
    elif year % 12 == 2:
        return "dog"
    elif year % 12 == 3:
        return "pig"
    elif year % 12 == 4:
        return "rat"
    elif year % 12 == 5:
        return "ox"
    elif year % 12 == 6:
        return "tiger"
    elif year % 12 == 7:
        return "rabbit"
    elif year % 12 == 8:
        return "dragon"
    elif year % 12 == 9:
        return "snake"
    elif year % 12 == 10:
        return "horse"
    else:
        return "sheep"

# Problem 1.6

def is_even_positive(num):
    """Check if the input is an integer, positive, and even.

    Args:
        num (int): The number to check.
        
    Returns:
        int: true if the number is a positive even integer, False otherwise."""
    return isinstance(num, int) and num > 0 and num % 2 == 0

# Problem 2.1
def heat_index(temp, humidity):
    """Calculate the heat index using the standard formula.

Args:
        temp (float): Temperature in Fahrenheit.
        humidity (float): Humidity percentage.

Returns:
        float: the calculated heat index.
        """
    C1, C2, C3, C4, C5, C6, C7, C8, C9 = -42.379, 2.04901523, 10.14333127, -0.22475541, -6.83783e-3, -5.481717e-2, 1.22874e-3, 8.5282e-4, -1.99e-6
    return (C1 + C2 * temp + C3 * humidity + C4 * temp * humidity + C5* temp**2 + C6* humidity**2 + C7 * temp**2 * humidity + C8 * temp * humidity**2 + C9 * temp**2 * humidity **2)

# Problem 2.2
def round_to_two(decimal):
    """Round a floating-point number to two decimal places using the Half Round-Up method.
    
    Args:
        decimal (float): The number to round.
    
    Returns:
        float: The rounded number.
    """
    approx_decimal = decimal * 100
    if approx_decimal % 1 >= 0.5:
        approx_decimal = approx_decimal // 1 + 1
    else:
        approx_decimal = approx_decimal // 1
    return float(approx_decimal / 100)

# Problem 2.3
def get_apparent_temperature(temp, humidity):
    """Calculate and display the apparent temperature based on heat index.
    
    Args:
        temp (float): Temperature in Fahrenheit.
        humidity (float): Humidity percentage.
    
    Displays:
        str: The apparent temperature message.
    
    Returns:
        float: The apparent temperature.
    """
    app_temp = heat_index(temp, humidity)
    rounded_temp = round_to_two(temp)
    rounded_humidity = round_to_two(humidity)
    rounded_app_temp = round_to_two(app_temp)
    print(f"{rounded_temp} F and {rounded_humidity} % humidity feels like {rounded_app_temp} F")
    return float(app_temp)

# Problem 3.1

def get_maximum(num_1, num_2):
    """Return the maximum of two integers using a single conditional.
    
    Args:
        num_1, num_2 (int): Two integers to compare.
    
    Returns:
        int: The larger of the two integers.
    """
    return int(num_1 if num_1 > num_2 else num_2)

# Problem 3.2
def get_maximum_below(num_1, num_2, num_limit):
    """Return the maximum number below a given limit.
    
    Args:
        num_1, num_2 (int): Two integers to compare.
        num_limit (int): The upper limit for selection.
    
    Returns:
        int: The maximum number below the limit, or the other number if one exceeds the limit.
    """
    if num_1 >= num_limit:
        return num_2
    elif num_2 >= num_limit:
        return num_1
    else:
        return get_maximum(num_1, num_2)

# Problem 3.3
def get_the_best(num_1, num_2, num_3, num_4, num_5):
    """Return the middle-most integer from five unique integers.
    
    Args:
        num_1, num_2, num_3, num_4, num_5 (int): Five unique integers.
    
    Returns:
        int: The median of the five integers.
    """
# Step 1: Find the maximum of the five numbers
    max_1 = get_maximum(get_maximum(num_1, num_2), get_maximum(num_3, get_maximum(num_4, num_5)))
# Step 2: Find the maximum below the first maximum
    max_2 = get_maximum_below(num_1, num_2, max_1)
    max_2 = get_maximum_below(max_2, num_3, max_1)
    max_2 = get_maximum_below(max_2, num_4, max_1)
    max_2 = get_maximum_below(max_2, num_5, max_1)
# Step 3: Find the maximum below the second maximum
    max_3 = get_maximum_below(num_1, num_2, max_2)
    max_3 = get_maximum_below(max_3, num_3, max_2)
    max_3 = get_maximum_below(max_3, num_4, max_2)
    max_3 = get_maximum_below(max_3, num_5, max_2)
    return max_3


# Tests
def main():
   # Part 1 Tests
   print(how_many(5))
   print(how_many('3'))

   print(get_distance(5, 12, 8, 9))
   print(get_distance(-8, 5.95, 5, 0))

   print(is_triangle(3, 4, 5))
   print(is_triangle(3, -4, 5))
   print(is_triangle(2.5, 3.75, 5.1))

   print(is_right_triangle(0, 0, 3, 0, 0, 4))
   print(is_right_triangle(1, 2, 5, 1, 3, 5))
   print(is_right_triangle(2.0, 3, 2, -1, 6, -1))
   print(is_right_triangle(3, 0, 1.5, 2.6, 0, 0))

   print(get_chinese_zodiac(2003))
   print(get_chinese_zodiac(2023))
   print(get_chinese_zodiac(2020))
   print(get_chinese_zodiac(2031))

   print(is_even_positive(12))
   print(is_even_positive(12.0))
   print(is_even_positive("hello"))
   print(is_even_positive(33))
   print(is_even_positive(-12))

   # Part 2 Tests
   print(heat_index(97.5, 46))
   print(heat_index(80, 97.3))

   print(round_to_two(85.6397))
   print(round_to_two(98.75))
   print(round_to_two(8.1))

   print(get_apparent_temperature(85.6397, 80.7306))
   print(get_apparent_temperature(76, 98.75))
   print(get_apparent_temperature(83, 48))

   # Part 3 Tests
   print(get_maximum(5, 7))
   print(get_maximum(4, 2))

   print(get_maximum_below(4, 2, 12))
   print(get_maximum_below(4, 2, 1))

   print(get_the_best(6, 8, 10, 2, 4))
   print(get_the_best(32, 83, 772, 1000, 1983))
if __name__ == "__main__":
    main()
