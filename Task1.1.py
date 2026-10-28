# Store your name, age, and city in variables and print them.

name = "Haru"
age = 20
city = "Nellore"

print("name:", name)
print("age:", age)
print("city:", city)

# Create a tuple with 5 fruits and print the third fruit.

t = ("apple", "banana", "orange", "grapes", "pineapple")
print(t[3])

# Store marks of 3 subjects in a dictionary and print the marks of "Math".

d = {85 : 'English', 90 : 'Math', 95 : 'Science'}
print(d.get(90))

# Write a program to store 3 integers and print their sum.

a = [10, 20, 30]
total = sum(a)
print(total)

# Create a tuple of 4 colors and print the last color.

t = ("Black", "Brown", "White", "Pink" )
print(t[3])

# Store employee details (name, ID, department) in a dictionary and print the department.

employee = {'name' : 'Haru', 'ID' : '12345', 'department' : 'CSE'}
print("employee:", employee["department"])

# Write a program to store a float, int, and string in variables and print their types

a = 2.07
b = 99
c = "Haru"
print(type(a))
print(type(b))
print(type(c))

# Check if "Python" is present in "I am learning Python programming".

s = "I am learning python programming"
print("python in s")

# Print only the first 5 characters of "Hello World".

a = "Hello World"
print(a[:5])

# Concatenate two strings "Good" and "Morning"

a =  "Good"
b = "Morning"
print(a+b)

# Count how many times "o" appears in "Hello World".

a = "Hello World"
"Hello World". count("o")

# Reverse the string "Python".

s =  "Python"
reverse = s[::-1]
print(reverse)

# Check if a string entered by the user starts with "A".

a = "Apple"
"Apple".startswith("A")

# Check if "apple" contains "p

a = "apple"
print("p in a")

# Take two numbers and print their sum, difference, product, and quotient.

a = 10
b = 15

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# Check if 25 is greater than 20 and less than 30.

a = 25
b = 20
c = 30
print(a > b and a < c)

# Ask the user for two numbers. Print "Both are positive" if both are greater than 0, else "At least one is not positive".

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > 0 and num2 > 0:
    print("Both are positive")
else:
    print("At least one is not positive")

# Check if a number is divisible by both 2 and 3.

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
if a % 2 == 0 and b % 3 == 0:
  print("Divisible by both 2 and 3")
else:
  print("Not divisible by 2 and 3")

# Check if "a" is in "apple".

a = "apple"
print("a in a")

# Check if a number is between 1 and 100 (inclusive).

num = int(input("Enter a number: "))

if 1 <= num <= 100:
  print(f"The number {num} is between 1 and 100")
else:
  print(f"The number {num} is NOT between 1 and 100.")

# Compare two strings "cat" and "dog".

a = "cat"
b = "dog"
if a == b:
  print("True")
else:
  print("False")

# Check if a number is positive, negative, or zero.

num = int(input("Enter a number:"))
if num > 0:
  print(" Number is Positive")
elif num < 0:
  print("Number is  Negative")
else:
  print(" Number is Zero")

# Ask the user to enter their age. If age ≥ 18, print "Eligible to vote", else "Not eligible".

num = int(input("Enter your age:"))
if num >= 18:
  print("Eligible to vote")
else:
  print("Note eligible to vote")

# Check if a given number is even or odd.

num = int(input("Enter the number:"))
if num % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

# Input a number and check if it is divisible by 5.

num = int(input("Enter the number:"))
if num % 5 == 0:
  print("The number is divisible by 5")
else:
  print("The number is not divisible by 5")

# Ask the user to enter a password. If it matches "admin123", print "Access Granted", else "Access Denied"

a = input("Enter the password:")
if a == "admin123":
  print("Access Granted")
else:
  print("Access Denied")

# Check if a character entered by the user is a vowel or consonant.

a = input("Enter the character:")
if a in "aeiouAEIOU":
  print("The character is vowel")
else:
  print("The character is not vowel")

# Check if a given year is a leap year.

a = int(input("Enter the year:"))
if a % 4 == 0:
  print("The year is a leap year")
else:
  print("The year is a not leap year")

# Ask the user for marks. Print "Grade A" if marks ≥ 90, "Grade B" if ≥ 75, "Grade C" if ≥ 50, else "Fail".

a = int(input("Enter the marks:"))
if a >= 90:
  print("Grade A")
elif a >= 75:
  print("Grade B")
elif a >= 50:
  print("Grade C")
else:
  print("Fail")

# Check if a number is odd and greater than 50.

a = int(input("Enter the number:"))
if a % 2 != 0 and a > 50:
  print("The number is odd and greater than 50")
else:
  print("The number is not odd and not greater than 50")

# Create a tuple with 6 numbers. Print the largest and smallest number.

t = (7, 13, 10, 9, 8, 12)
print("Largest number is:", max(t))
print("Smallest number is:", min(t))

# Check if 50 exists in (10, 20, 30, 40, 50, 60).

a = (10, 20, 30, 40, 50, 60)
if 50 in a:
  print("50 exists in the tuple")
else:
  print("50 does not exists in the tuple")

# Store 5 colors in a tuple. Ask the user to enter a color name. Check if it exists.

t = ("Black", "White", "Brown", "Pink", "Blue")
a = input("Enter the color ")
if a in t:
  print("color exists")
else:
  print("Does not exists")

# Print the length of a tuple (1, 2, 3, 4, 5)

t = (1, 2, 3, 4, 5)
print(len(t))

# Create a tuple with 4 strings. Print them one by one using indexing.

t = ("Harika", "Haru", "Har", "H")
print(t[0])
print(t[1])
print(t[2])
print(t[3])

# Create a dictionary with 3 countries as keys and their capitals as values. Print the capital of "India".

d = {"India" : "New Delhi", "Japan" : "Tokyo", "UK" : "London"}
print(d.get("India"))

# Add a new country-capital pair to an existing dictionary.

d = {"India" : "Newdelhi", "Japan" : "Tokyo", "UK" : "London"}
d ["France"] = "Paris"
print(d)

# Given a dictionary of student marks, check if "Anita" is present as a key. If yes, print her marks.

d = {"Anita" : 80, "Harika" : 90, "Haru" : 95}
print(d.get("Anita"))

# Create a dictionary with usernames and passwords. Ask the user to enter a username and password. If both match, print "Login Successful", else "Login Failed".

d = {"Harika" : "12345", "Haru" : "54321"}
username = input("Enter the username:")
password = input("Enter the password:")
if username in d and d[username] == password:
  print("Login successful")
else:
  print("Login failed")

# Print all keys of a dictionary.

d = {"Harika" : 80, "Haru" : 96}
print(d.keys())

# Create a dictionary with 3 items and their prices. Ask the user to enter an item name. Print the price if it exists, else "Item not found"

d = {"flour" : 100, "rice" : 500, "sugar" : 200}
item_name = input("Enter the item name:")
if item_name in d:
  print("price:", d[item_name])
else:
  print("Item not found")

# Create a list of 5 numbers and print the first and last elements

a = [10, 20, 30, 40, 50]
print(a[0])
print(a[-1])

# Add a new element to a list.

a = [10, 20, 30, 40]
a.append(50)
print(a)

# Remove an element from a list.

a = [10, 20, 30, 40, 50]
a.remove(10)
print(a)

# Create a list of 4 colors and print its length

a = ["Black", "White", "Brown", "Pink"]
len_list = len(a)
print(len_list)

# Check if "red" exists in a list of colors

a = ["Red", "White", "Black", "Brown"]
if "Red" in a:
  print("Red exists in list of colors")
else:
  print("Red does not exists in list of colors")

# Print the second to fourth elements of a list.

a = [10, 20, 30, 40, 50, 60, 70]
a[2:4]

# Print the last 3 elements of a list.

a = [10, 20, 30, 40, 50]
print(a[-1], a[-2], a[-3])

# Store 5 names in a list and print the name at index 2.

a = ["Harika", "Haru", "Har", "Ha", "H"]
print(a[2])

# Reverse a list.

a = ["Harika", "Haru", "Har", "Ha", "H"]
reverse = a[::-1]
print(reverse)

# Replace the second element of a list with "Python".

a = ["Harika", "Haru", "Har", "Ha", "H"]
a[1] = "Python"
print(a)

# Create a list of 5 numbers. Check if a number entered by the user exists in the list.

a = [10, 20, 30, 40, 50]
num = int(input("Enter a number:"))
if num in a:
  print("Number exists in the list")
else:
  print("Number does not exists in the list")

# Store 5 subjects in a list. Ask the user to enter a subject name. If it exists, print "Found", else "Not Found".

a = ["Telugu", "Hindi", "English", "Maths", "Science"]
subject_name = input("Enter the subject name:")
if subject_name in a:
  print("Found")
else:
  print("Not found")

# Create a list of marks. If the average is ≥ 50, print "Pass", else "Fail".

a = [97, 60, 70, 80, 90]
average = sum(a) / len(a)
if average >= 50:
  print("Pass")
else:
  print("Fail")

# Check if the first and last elements of a list are equal.

a = [10, 20, 30, 40, 50]
if a[0] == a[-1]:
  print("True")
else:
  print("False")

# Create a list of strings. Print "Contains Python" if "Python" is in the list.

a = ["Python", "Java", "Spark", "AWS"]
list_of_strings = input("Enter the string:")
if list_of_strings in a:
  print("Contains python")
else:
  print("Not found")

# Create a list of 5 numbers. Print the largest and smallest numbers.

a = [10, 20, 30, 40, 50]
print(max(a))
print(min(a))

# Count how many times "apple" appears in a list.

a = ["apple", "apple", "orange", "Pineapple"]
print(a.count("apple"))

# Store 5 numbers in a list. Print only the even numbers.

nums = [2, 2, 7, 8, 6, 9, 3]
for n in nums:
  if n % 2 == 0:
    print(n)

# Check if a list is empty.

list = []
print(len(list))

# Create a list of 5 numbers. If all numbers are positive, print "All Positive", else "Contains Negative".

a = [10, -1, 88, 66, 54]
if all(n > 0 for n in a):
  print("All positive")
else:
  print("Contains negative")

# Store 5 numbers in a tuple. Check if the number 10 is present.

a = (10, 20, 30, 40, 50)
num = int(input("Enter the number:"))
if num in a:
  print("Number exists")
else:
  print("Number does not exists")

# Create a dictionary with student names as keys and marks as values. Check if "Rahul" is in the dictionary.

d = {"Harika" : 85, "Haru": 90, "Har" : 70}
name = input("Enter the name:")
if name in d:
  print("Name exists")
else:
  print("Does not exists")

# Take a string input and check if it contains "Python".

a = input("Enter the string:")
if "Python" in a:
  print("Contains python")
else:
  print("Not found")

# Ask the user for two numbers. Print "Equal" if they are equal, "First is greater" if the first is larger, else "Second is greater".

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
if num1 == num2:
  print("Equal")
elif num1 > num2:
  print("First is greater")
else:
  print("Second is greater")

# Check if a number is divisible by 2 OR 5.

num = int(input("Enter a number:"))
if num % 2 == 0 or num % 5 == 0:
  print("Divisible by 2 or 5")
else:
  print("Not divisible by 2 or 5")

# Create a dictionary with 3 employees and their salaries. Print the salary of the employee with the highest pay.

d = {"Harika" : 100000, "Haru" : 200000, "Har" : 90000}
print(d.get("Haru"))

# Check if a string entered by the user contains both "a" and "b".

str = input("Enter the string:")
if "a" in str and "b" in str:
  print("Contains both a and b")
else:
  print("Does not contain both a and b")

# Store 5 subjects in a tuple. Ask the user to enter a subject name. If it exists, print "Subject Found", else "Not Found".

a = ("Telugu", "Hindi", "English", "Maths", "Science")
subject_name = input("Enter the subject name:")
if subject_name in a:
  print("Subject found")
else:
  print("Not found")

# Check if a number entered by the user is both even and between 10 and 50.

num = int(input("Enter the number:"))
if num % 2 == 0 and num > 10 < 50:
  print("Number is even and between 10 and 50")
else:
  print("Number is not even and not in between 10 and 50")

# Convert a string to uppercase.

a = "harika"
"harika".upper()

# Convert a string to lowercase.

a = "HARIKA"
"HARIKA".lower()

# Remove extra spaces from a string.

a = " Haru "
" Haru ".strip()

# Replace one word in a string with another.

a = ["Harika", "AWS", "Har"]
a[1] = "Python"
print(a)

# Split a string into a list of words.

str = "Hello world"
words = "Hello World".split()
print(words)

# Join a list of words into a single string.

str = ["Hello", "GoodMorning", "Mam"]
words = " ".join(str)
print(repr(words))

# Count how many times a letter appears in a string

a = "h", "h", "i", "h", "r"
a.count("h")

# Find the position of a character in a string.

a = "Harika"
a.find("H")

# Check if a string contains only letters and numbers.

str = "abc123"
if str.isalnum():
  print("String contains only letters and numbers")
else:
  print("String does not contains only letters and numbers")

# Check if a string contains only digits.

str = "12345"
if str.isdigit():
  print("string contains only digits")
else:
  print("string does not contains only digits")

# Add an element to the end of a list

a = [10, 20, 30, 40]
a.append(50)
print(a)

# Add multiple elements to a list at once.

a = [10, 20]
a.extend([30, 40, 50])
print(a)

# Insert an element at a specific position in a list.

a = [10, 20, 40, 50]
a.insert(2, 30)
print(a)

# Remove a specific element from a list.

a = [10, 50, 20, 30]
a.pop(1)
print(a)

# Remove the last element from a list.

a = [10, 20, 30]
a.pop(2)
print(a)

# Arrange the elements of a list in ascending order.

a = [70, 20, 30, 40, 50]
a.sort()
print(a)

# Reverse the order of elements in a list.

a = [70, 20, 30, 40, 50]
a.reverse()
print(a)

# Find the position of an element in a list.

a = [70, 20, 30, 40, 50]
a.index(50)

# Count how many times a number appears in a list.

a = [70, 20, 30, 40, 50, 50]
a.count(50)

# Remove all elements from a list.

a = [70, 20, 30, 40, 50, 50]
a.clear()
print(a)

# Print all keys of a dictionary.

a =  {"Harika" : 100000, "Haru" : 200000, "Har" : 90000}
print(a.keys())

# Print all values of a dictionary.

a =  {"Harika" : 100000, "Haru" : 200000, "Har" : 90000}
print(a.values())

# Print all key-value pairs of a dictionary.

a =  {"Harika" : 100000, "Haru" : 200000, "Har" : 90000}
print(a)

# Access the value of a key safely.

a =  {"Harika" : 100000, "Haru" : 200000, "Har" : 90000}
a.get("Harika")

# Add a new key-value pair to a dictionary.

a =  {"Harika" : 100000, "Haru" : 200000, "Har" : 90000}
a["H"] = 80000
print(a)

# Remove a specific key from a dictionary.

a =  {"Harika" : 100000, "Haru" : 200000, "Har" : 90000}
del a["Har"]
print(a)

# Remove the last inserted item from a dictionary.

a =  {"Harika" : 100000, "Haru" : 200000, "Har" : 90000}
key , value = a.popitem()
print(a)

# Check if a key exists in a dictionary.

a =  {"Harika" : 100000, "Haru" : 200000, "Har" : 90000}
if "Haru" in a:
  print("key exists")

# Create a dictionary with given keys and the same default value

keys = ["a", "b", "c"]
default_value = 0

my_dict = dict.fromkeys(keys, default_value)
print(my_dict)

# Make a copy of a dictionary.

original = {"a": 1, "b": 2}

copy_dict = original.copy()
print(copy_dict)