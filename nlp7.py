import re

text = "My email is maidalachaitanya@gmail.com and phone number is 9876543210"

# Search for email
email_pattern = r'\w+@\w+\.\w+'
email = re.search(email_pattern, text)

if email:
    print("Email found:", email.group())

# Find all numbers
number_pattern = r'\d+'
numbers = re.findall(number_pattern, text)

print("Numbers found:", numbers)