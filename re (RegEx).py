import re

pattern = re.compile(r"[A-Za-z0-9.]+@[A-Za-z0-9.]+\.[A-Za-z0-9]+")
new_pattern = re.compile(r"(\+?\d{1,3}[-\s]?)?(\(?\d{3}\)?[-\s]?)?\d{3}[-\s]?\d{4}")

test_numbers = [
    "ahmed@gmail.com",
    "(555) 123-4567",
    "555-987-6543",
    "+44 207 123 4567",
    "1234567890",
]

for number in test_numbers:
    if pattern.fullmatch(number):
        print(f"Valid: {number}")
    else:
        print(f"Invalid: {number}")

for number in test_numbers:
    if new_pattern.fullmatch(number):
        print(f'Valid : {number}')
    else:
        print(f'Invalid : {number}')
