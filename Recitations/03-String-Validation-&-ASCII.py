
# Problem 1
def insensitive_match(c1: str, c2: str) -> bool:
    return c1 == c2 or abs(ord(c1) - ord(c2)) == 32

def str_to_int(s: str) -> int:
    num = 0
    for c in s:
        if '0' <= c <= '9':
            num = num * 10 + (ord(c) - ord('0'))
        else:
            return -1 
    return num

def are_twins(psuid1: str, psuid2: str) -> bool:
    if not (insensitive_match(psuid1[0], psuid2[0]) and
            insensitive_match(psuid1[1], psuid2[1]) and
            insensitive_match(psuid1[2], psuid2[2])):
        return False

    num1, num2 = psuid1[3:], psuid2[3:]

    int_num1, int_num2 = str_to_int(num1), str_to_int(num2)
    if int_num1 == -1 or int_num2 == -1:
        return False
    
    return abs(int_num1 - int_num2) == 1


# Problem 2
def replace_char(s: str, replacement: str, target: str) -> str:
    result = ""

    for char in s:
        if char == target or abs(ord(char) - ord(target)) == 32:
            result += replacement
        else:
            result += char
    return result


# Problem 3
def find_first_vowel(s: str) -> int:
    vowels = "aeiouAEIOU"
   
    for i in range(len(s)):
        for v in vowels:
            if s[i] == v:
                return i
    return len(s)
