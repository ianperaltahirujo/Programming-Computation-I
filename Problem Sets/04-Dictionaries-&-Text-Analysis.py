

# Problem 1.1
def invert_dict(d: dict) -> dict:
    """
    Inverts a dictionary by making its values keys and its keys values (stored in a list).
    
    Args:
        d (dict): Input dictionary with immutable keys.
    
    Returns:
        dict: Inverted dictionary where values from d become keys.
    """
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)
    return inverted


# Problem 1.2
def char_frequency(s: str) -> dict:
    """
    Counts the frequency of each alphabet character in a string (case-insensitive).

    Args:
        s (str): Input string.

    Returns:
        dict: Dictionary of character frequencies.
    """
    freq = {}
    for char in s:
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + 32)  
        if 'a' <= char <= 'z':
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq


# Problem 1.3
def find_missing_pangram_chars(s: str) -> list:
    """
    Finds missing characters needed to make a string a pangram.

    Args:
        s (str): Input string.

    Returns:
        list: Sorted list of missing characters.
    """
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    present_chars = []
    
    for char in s:
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + 32)  
        if 'a' <= char <= 'z' and char not in present_chars:
            present_chars.append(char)

    missing_chars = []
    for char in alphabet:
        if char not in present_chars:
            missing_chars.append(char)
    
    return missing_chars


# Problem 1.4
def are_anagrams(s1: str, s2: str) -> bool:
    """
    Determines if two strings are anagrams, ignoring spaces, non-letters, and case.

    Args:
        s1 (str): First string.
        s2 (str): Second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    freq1 = {}
    freq2 = {}

    for char in s1:
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + 32)
        if 'a' <= char <= 'z':
            if char in freq1:
                freq1[char] += 1
            else:
                freq1[char] = 1

    for char in s2:
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + 32)
        if 'a' <= char <= 'z':
            if char in freq2:
                freq2[char] += 1
            else:
                freq2[char] = 1

    return freq1 == freq2


# Problem 1.5
def find_anagram_pairs(words: list) -> list:
    """
    Finds pairs of indices where words are anagrams of each other.
    
    Args:
        words (list): List of words.
    
    Returns:
        list: List of tuples containing index pairs.
    """
    pairs = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if are_anagrams(words[i], words[j]):
                pairs.append((i, j))
    return pairs


# Problem 1.6
def is_steady(s: str) -> bool:
    """
    Determines if a string is steady (all letters appear the same number of times).

    Args:
        s (str): Input string.

    Returns:
        bool: True if the string is steady, False otherwise.
    """
    if not s:
        return True

    freq = char_frequency(s)
    values = list(freq.values())
    
    first_value = values[0]
    for value in values:
        if value != first_value:
            return False
    
    return True


# Problem 1.7 
def nearly_equal(s1: str, s2: str) -> bool:
    """
    Determines if two strings are nearly equal (frequency differences ≤ 2 for each letter).

    Args:
        s1 (str): First string.
        s2 (str): Second string.

    Returns:
        bool: True if nearly equal, False otherwise.
    """
    freq1 = char_frequency(s1)
    freq2 = char_frequency(s2)

    all_chars = []
    for char in freq1:
        if char not in all_chars:
            all_chars.append(char)
    for char in freq2:
        if char not in all_chars:
            all_chars.append(char)

    for char in all_chars:
        if abs(freq1.get(char, 0) - freq2.get(char, 0)) > 2:
            return False

    return True


# Problem 1.8
def is_isomorphic(s1: str, s2: str) -> bool:
    """
    Determines if two strings are isomorphic (one-to-one mapping between characters).

    Args:
        s1 (str): First string.
        s2 (str): Second string.

    Returns:
        bool: True if the strings are isomorphic, False otherwise.
    """
    if len(s1) != len(s2):
        return False
    
    mapping = {}
    used_chars = []

    for i in range(len(s1)):
        char1 = s1[i]
        char2 = s2[i]

        if char1 in mapping:
            if mapping[char1] != char2:
                return False
        else:
            if char2 in used_chars:
                return False
            mapping[char1] = char2
            used_chars.append(char2)
    
    return True


def main():
    """Runs test cases for all functions."""
    
    # invert_dict tests
    assert invert_dict({'a': 1, 'b': 2, 'c': 1, 'd': 2, 3.75: 7}) == {1: ['a', 'c'], 2: ['b', 'd'], 7: [3.75]}
    assert invert_dict({}) == {}  
    assert invert_dict({'x': 10}) == {10: ['x']}  
    assert invert_dict({'a': 1, 'b': 'test', 'c': 1, 'd': 'test'}) == {1: ['a', 'c'], 'test': ['b', 'd']} 
    
    # char_frequency tests
    assert char_frequency("~ABC abc!!!!!!! !!!!!!  ") == {'a': 2, 'b': 2, 'c': 2}
    assert char_frequency("") == {}  
    assert char_frequency("123456!@#$%^") == {}  
    assert char_frequency("AaBbCc") == {'a': 2, 'b': 2, 'c': 2}  
    
    # find_missing_pangram_chars tests
    assert find_missing_pangram_chars("The quick brown fox") == ['a', 'd', 'g', 'j', 'l', 'm', 'p', 's', 'v', 'y', 'z']
    assert find_missing_pangram_chars("") == list("abcdefghijklmnopqrstuvwxyz")  
    assert find_missing_pangram_chars("abcdefghijklmnopqrstuvwxyz") == [] 
    
    # are_anagrams tests
    assert are_anagrams("Lis ten", "Silent!") is True
    assert are_anagrams("", "") is True  
    assert are_anagrams("Hello", "Oellh!!") is True  
    assert are_anagrams("abcd", "abcc") is False  
    
    # find_anagram_pairs tests
    assert find_anagram_pairs(["Lis Ten", "silent", "enli st", "inlet s", "google"]) == [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    assert find_anagram_pairs(["apple", "orange", "banana"]) == []  
    assert find_anagram_pairs(["aa", "aa", "aa"]) == [(0, 1), (0, 2), (1, 2)]  
    
    # is_steady tests
    assert is_steady("ARE era") is True
    assert is_steady("") is True
    assert is_steady("aaabb") is False 
    
    # nearly_equal tests
    assert nearly_equal("sesame", "SundrivE") is True
    assert nearly_equal("", "") is True 
    assert nearly_equal("aaa", "bbb") is False 
    
    # is_isomorphic tests
    assert is_isomorphic("egg", "add") is True
    assert is_isomorphic("", "") is True  
    assert is_isomorphic("abc", "aaa") is False  
    
    print("All tests passed!")

if __name__ == "__main__":
    main()
