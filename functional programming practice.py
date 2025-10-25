from functools import reduce
from operator import mul, add

# Map Exercises

# 1. Triple all numbers in a list
numbers = [1, 2, 3, 4]
tripled = list(map(lambda x: x * 3, numbers))
print("Map 1 - Tripled numbers:", tripled)  # Output: [3, 6, 9, 12]

# 2. Add corresponding elements of three lists
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
summed = list(map(lambda x, y, z: x + y + z, a, b, c))
print("Map 2 - Sum of corresponding elements:", summed)  # Output: [12, 15, 18]

# 3. Convert a list of strings to lists of characters
words = ["apple", "banana", "cherry"]
chars = list(map(list, words))
print("Map 3 - List of characters:", chars)  # Output: [['a','p','p','l','e'], ...]

# 4. Create list of powers from bases and exponents
bases = [2, 3, 4]
exponents = [3, 2, 1]
powers = list(map(lambda x, y: x ** y, bases, exponents))
print("Map 4 - Powers:", powers)  # Output: [8, 9, 4]

# 5. Square all elements in a list
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print("Map 5 - Squares:", squares)  # Output: [1, 4, 9, 16]


# Filter Exercises

# 1. Filter odd numbers
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Filter 1 - Even numbers:", evens)  # Output: [2, 4]

# 2. Keep strings with length <= 5
strings = ["hi", "hello", "welcome", "dog"]
short_strings = list(filter(lambda s: len(s) <= 5, strings))
print("Filter 2 - Short strings:", short_strings)  # Output: ['hi', 'hello', 'dog']

# 3. Filter palindromes
words = ["radar", "level", "world", "python"]
palindromes = list(filter(lambda w: w == w[::-1], words))
print("Filter 3 - Palindromes:", palindromes)  # Output: ['radar', 'level']

# 4. Filter numbers > 50
numbers = [10, 55, 30, 70, 25]
greater_than_50 = list(filter(lambda x: x > 50, numbers))
print("Filter 4 - Numbers > 50:", greater_than_50)  # Output: [55, 70]


# Reduce Exercises

# 1. Product of numbers
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print("Reduce 1 - Product:", product)  # Output: 24

# 2. Maximum number
numbers = [10, 50, 20, 70, 30]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print("Reduce 2 - Maximum:", maximum)  # Output: 70

# 3. Concatenate list of strings
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda x, y: x + y, words)
print("Reduce 3 - Concatenated string:", sentence)  # Output: Hello World!

# 4. Factorial of a number
num = 5
factorial = reduce(mul, range(1, num + 1))
print("Reduce 4 - Factorial of 5:", factorial)  # Output: 120


# Combined Practice

# 1. Square numbers, filter those >= 50, sum remaining
numbers = [4, 5, 6, 7, 8]
squared = map(lambda x: x ** 2, numbers)
filtered = filter(lambda x: x >= 50, squared)
total = reduce(lambda x, y: x + y, filtered)
print("Combined 1 - Sum of squares >= 50:", total)  # Output: 149 (64 + 81 + 4 etc.)

# 2. From exam scores, filter passing, map to grades, reduce to count grades
scores = [85, 70, 55, 40, 90, 65]
passing = filter(lambda x: x >= 60, scores)

def to_grade(score):
    if score >= 85:
        return 'A'
    elif score >= 70:
        return 'B'
    else:
        return 'C'

grades = map(to_grade, passing)

def count_grades(acc, grade):
    acc[grade] = acc.get(grade, 0) + 1
    return acc

grade_counts = reduce(count_grades, grades, {})
print("Combined 2 - Grade counts:", grade_counts)  # Output: {'A': 2, 'B': 2, 'C': 1}
