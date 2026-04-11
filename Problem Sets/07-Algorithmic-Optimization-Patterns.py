

# Problem 1.1
def move_vowels(text: str) -> str:
    """
    Reverses the vowels in the input string while keeping consonants in place.

    Args:
        text (str): A non-empty string of characters.

    Displays:
        The transformed string where vowels are reversed, but consonants remain in place.

    Returns:
        (str) A new string with consonants in their original positions and vowels reversed.
    """
    vowels = "aeiouAEIOU"
    text_list = list(text) 
    left, right = 0, len(text) - 1  

    while left < right:
        
        while left < right and text_list[left] not in vowels:
            left += 1
      
        while left < right and text_list[right] not in vowels:
            right -= 1
     
        if left < right:
            text_list[left], text_list[right] = text_list[right], text_list[left]
            left += 1
            right -= 1

    result = ""
    for char in text_list:
        result += char  

    return result


# Problem 1.2
def move_to_back(lst: list[int], numbers: list[int]) -> None:
    """
    Moves elements found in `numbers` to the end of `lst`, preserving the order of other elements.

    Args:
        lst (list[int]): The list to mutate.
        numbers (list[int]): The list of elements to move to the back.

    Displays:
        The modified list where specified numbers are moved to the back.

    Returns:
        None
    """
    n = len(lst)
    temp = [0] * n
    slow = 0

    for i in range(n):
        if lst[i] not in numbers:
            temp[slow] = lst[i]
            slow += 1

    for num in numbers:
        for i in range(n):
            if lst[i] == num:
                temp[slow] = lst[i]
                slow += 1

    for i in range(n):
        lst[i] = temp[i]


# Problem 1.3
def is_peak(nums: list[int]) -> bool:
    """
    Determines if the list follows a "peak" pattern, where every element 
    is either greater or smaller than both of its neighbors.

    Args:
        nums (list[int]): A list of integers.

    Displays:
        Whether the given list follows the peak pattern.

    Returns:
        (bool) True if the list is a "peak" list, False otherwise.
    """
    for i in range(1, len(nums) - 1):
        if not ((nums[i] > nums[i-1] and nums[i] > nums[i+1]) or 
                (nums[i] < nums[i-1] and nums[i] < nums[i+1])):
            return False
    return True


# Probem 1.4
def max_in_window(nums: list[int], w: int) -> list[int]:
    """
    Returns a list of the maximum values for each sliding window of size `w`.

    Args:
        nums (list[int]): A list of integers.
        w (int): The size of the sliding window.

    Displays:
        A sequence of maximum values computed for each window.

    Returns:
        (list[int]) A list containing the maximum values for each sliding window.
    """
    if w <= 0 or w > len(nums):
        return []
    
    max_vals = []
    left = 0
    right = w - 1
    
    while right < len(nums):
        current_max = nums[left]
        for i in range(left, right + 1):
            if nums[i] > current_max:
                current_max = nums[i]
        max_vals_length = len(max_vals)
        temp = [0] * (max_vals_length + 1)
        for i in range(max_vals_length):
            temp[i] = max_vals[i]
        temp[max_vals_length] = current_max
        max_vals = temp
        left += 1
        right += 1
    
    return max_vals


def main():
        # Testing move_vowels
    assert move_vowels("apple") == "eppla"  
    assert move_vowels("abcde") == "ebcda" 
    assert move_vowels("Hello, World!") == "Hollo, Werld!"

    # Testing move_to_back
    my_lst = [10, 20, 30, 40, 50]
    move_to_back(my_lst, [20, 40])
    assert my_lst == [10, 30, 50, 20, 40]  
    
    my_lst = [1, 1, 1, 1, 1]
    move_to_back(my_lst, [1])
    assert my_lst == [1, 1, 1, 1, 1]
    
    my_lst = [9, 8, 7, 6, 5]
    move_to_back(my_lst, [8, 6])
    assert my_lst == [9, 7, 5, 8, 6]  
    
    # Testing is_peak
    assert is_peak([1, 3, 2, 4, 3, 5, 4]) == True  
    assert is_peak([10, 9, 8, 7]) == False  
    assert is_peak([5]) == True  
    
    # Testing max_in_window
    assert max_in_window([1, 2, 3, 4, 5], 2) == [2, 3, 4, 5] 
    assert max_in_window([10, 20, 30], 3) == [30]  
    assert max_in_window([5, 5, 5, 5], 2) == [5, 5, 5]  

    print("All tests passed!")


if __name__ == "__main__":
    main()