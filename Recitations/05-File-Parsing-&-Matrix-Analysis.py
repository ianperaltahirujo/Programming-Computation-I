
# Problem 1
def extract_emails(file_name):
    emails = []
    file = open(file_name, "r")
    
    line = file.readline()
    while line:
        words = line.strip().split()
        for word in words:
            if "@" in word and "." in word:
                emails.append(word)
        line = file.readline()
    
    file.close()
    return emails


# Problem 2
def palindrome_counter(file_name):
    count = 0
    file = open(file_name, "r")
    
    line = file.readline()
    while line:
        words = line.strip().split()
        for word in words:
            if word == word[::-1]:
                count += 1
        line = file.readline()
    
    file.close()
    return count


# Problem 3
def get_largest(matrix):
    largest = None
    for row in matrix:
        for num in row:
            if largest is None or num > largest:
                largest = num
    return largest


# Problem 4
def get_row_average(matrix):
    averages = []
    
    for row in matrix:
        total = 0
        count = 0
        
        for num in row:
            total += num
            count += 1
        
        averages.append(total / count)
    
    return averages

