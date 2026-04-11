

# Problem 1
def filter_even(lst):
    result = []
    index = 0
    while index < len(lst):
        if lst[index] % 2 == 0:
            result.append(lst[index])
        index += 1
    return result

my_list = [52, 10, 9, 7, 23, -50, -3]
print(filter_even(my_list)) 
print(my_list) 


# Problem 2
def filter_even_destructive(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 != 0:
            del lst[i]
        else:
            i += 1

my_list = [52, 10, 9, 7, 23, -50, -3]
filter_even_destructive(my_list)
print(my_list) 


# Problem 3
def is_palindrome(lst):
    for i in range(len(lst) // 2):
        if lst[i] != lst[len(lst) - 1 - i]:
            return False
    return True


# Problem 4
def multiply(pol_1, pol_2):
    result = [0] * (len(pol_1) + len(pol_2) - 1)
    for i in range(len(pol_1)):
        for j in range(len(pol_2)):
            result[i + j] += pol_1[i] * pol_2[j]
    return result

