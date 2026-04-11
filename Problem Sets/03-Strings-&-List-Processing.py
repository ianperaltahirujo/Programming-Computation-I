

# Problem 1
def is_consonant(char: str) -> bool:
    """
    Determines if a character is a consonant.

    Args:
        char (str): A single character.

    Returns:
        (bool) True if the character is a consonant, False otherwise.
    """
    vowels = "aeiouAEIOU"
    return char.isalpha() and char not in vowels

def count_consonants(s: str) -> int:
    """
    Counts the number of consonants in a given string.

    Args:
        s (str): Input string.

    Returns:
        (int) The number of consonants in the string.
    """
    count = 0
    for char in s:
        if is_consonant(char):
            count += 1
    return count


# Problem 1.2
def get_even_sum(lst: list) -> int:
    """
    Computes the sum of even numbers in a list.

    Args:
        lst (list): List of integers.

    Returns:
        (int) The sum of even numbers in the list.
    """
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total


# Problem 1.3
def get_second(s: str) -> str:
    """
    Retrieves the second word from a comma-separated string, removing spaces.

    Args:
        s (str): A comma-separated string containing at least two words.

    Returns:
        (str) The second word with leading and trailing spaces removed.
    """
    start = 0
    comma_count = 0
    for i in range(len(s)):
        if s[i] == ',':
            comma_count += 1
            if comma_count == 1:
                start = i + 1
            elif comma_count == 2:
                return s[start:i].strip()
    return ""


# Problem 2.1
def replace_vowels_in_list(words: list) -> None:
    """
    Mutates a list by replacing all vowels in each word with 'q'.

    Args:
        words (list): List of strings.
    
    Returns:
        None: The function modifies the input list in place and does not return a new list.
    """
    vowels = "aeiouAEIOU"
    for i in range(len(words)):
        new_word = ""
        for char in words[i]:
            if char in vowels:
                new_word += 'q'
            else:
                new_word += char
        words[i] = new_word


# Problem 2.2
def is_rotation(txt_1: str, txt_2: str) -> bool:
    """
    Determines if one string is a rotation of another.

    Args:
        txt_1 (str): The original string.
        txt_2 (str): The potential rotated version.

    Returns:
        (bool) True if txt_2 is a rotation of txt_1, False otherwise.
    """
    if len(txt_1) != len(txt_2):
        return False
    return txt_2 in (txt_1 + txt_1)


# Problem 2.3
def words_with_vowels(s: str) -> list:
    """
    Extracts words that contain at least one vowel from a string.
    
    Args:
        s (str): Input string.
    
    Returns:
        (list) List of words containing at least one vowel.
    """
    vowels = "aeiouAEIOU"
    words = []
    word = ""
    result = []
    
    for char in s + " ":
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            word += char
        elif word:
            words += [word]
            word = ""
    
    for w in words:
        has_vowel = False
        for char in w:
            if char in vowels:
                has_vowel = True
        if has_vowel:
            result += [w]
    return result


# Problem 2.4
def most_vowels_word(s: str) -> str:
    """
    Finds the word with the most vowels in a string.

    Args:
        s (str): Input string.

    Returns:
        (str) The word with the highest number of vowels.
    """
    words = words_with_vowels(s)
    max_vowel_count, max_word = 0, ""
    for word in words:
        count = 0
        for char in word:
            if char in "aeiouAEIOU":
                count += 1
        if count > max_vowel_count:
            max_vowel_count = count
            max_word = word
    return max_word


# Problem 2.5
def normalize_list(lst: list) -> list:
    """
    Normalizes values in the list to be between 0 and 1.

    Args:
        lst (list): List of integers.

    Returns:
        (list) A list with values normalized between 0 and 1.
    """
    min_val = min(lst)
    max_val = max(lst)

    if min_val == max_val:
        return [0.5] * len(lst)
    normalized = [0] * len(lst)
    for i in range(len(lst)):
        normalized[i] = (lst[i] - min_val) / (max_val - min_val)
    return normalized


# Problem 2.6
def get_closest_pair(lst: list) -> tuple:
    """
    Returns the pair of numbers with the smallest absolute difference.

    Args:
        lst (list): List of integers.

    Returns:
        (tuple) The pair of closest numbers.
    """
    if len(lst) < 2:
        return ()  

    min_diff = float('inf')
    pair = (lst[0], lst[1])  

    for i in range(len(lst)):  
        for j in range(i + 1, len(lst)):  
            diff = abs(lst[i] - lst[j])
            if diff < min_diff:
                min_diff = diff
                pair = (lst[i], lst[j])

    return pair


# Problem 2.7
def first_non_repeating_letter(s: str) -> str:
    """
    Returns the first non-repeating letter in the string.

    Args:
        s (str): Input string.

    Returns:
        (str) The first non-repeating letter in lowercase or an empty string if none exists.
    """
    counts = {} 
    
    for char in s:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'): 
            lower_char = char.lower()
            counts[lower_char] = counts.get(lower_char, 0) + 1

    for char in s:
        lower_char = char.lower()
        if (('a' <= char <= 'z') or ('A' <= char <= 'Z')) and counts[lower_char] == 1:
            return lower_char 

    return ""


###################Tests######################

def main():
    # Testing count_consonants
    assert count_consonants("Data Science!") == 6
    assert count_consonants("Supercalifragilistic") == 12
    assert count_consonants("!!!??") == 0
    
   # Testing get_even_sum
    assert get_even_sum([4, 8, 12, 16]) == 40
    assert get_even_sum([7, 3, 1]) == 0
    assert get_even_sum([-2, -4, -6]) == -12
    
    # Testing get_second
    assert get_second('java, python, c++') == 'python'
    assert get_second('x, y, z') == 'y'
    assert get_second('onlyoneword') == ""
    
    # Testing replace_vowels_in_list
    test_list = ['banana', 'grapefruit', 'kiwi']
    replace_vowels_in_list(test_list)
    assert test_list == ['bqnqnq', 'grqpqfrqqt', 'kqwq']
    
    # Testing is_rotation
    assert is_rotation('python', 'honpyt') is True
    assert is_rotation('apple', 'leapp') is True
    assert is_rotation('hello', 'helol') is False
    
    # Testing words_with_vowels
    assert words_with_vowels("Why do we code?") == ["do", "we", "code"]
    assert words_with_vowels("nthng hr") == []
    assert words_with_vowels("Enjoy learning Python") == ["Enjoy", "learning", "Python"]
    
    # Testing most_vowels_word
    assert most_vowels_word("A beautiful sentence") == "beautiful"
    assert most_vowels_word("sky why try") == ""
    assert most_vowels_word("Understanding is key") == "Understanding"
    
    # Testing normalize_list
    assert normalize_list([100, 200, 300]) == [0.0, 0.5, 1.0]
    assert normalize_list([-5, 0, 5]) == [0.0, 0.5, 1.0]
    assert normalize_list([9, 9, 9]) == [0.5, 0.5, 0.5]
    
    # Testing get_closest_pair
    assert get_closest_pair([1, 2, 3, 10]) == (1, 2)
    assert get_closest_pair([15, 30, 45, 60]) == (15, 30)
    assert get_closest_pair([1000]) == ()
    
    # Testing first_non_repeating_letter
    assert first_non_repeating_letter("racecar") == "e"
    assert first_non_repeating_letter("noon") == ""
    assert first_non_repeating_letter("Alphabet") == "l"
    
    print("All tests passed!")

if __name__ == "__main__":
    main()
