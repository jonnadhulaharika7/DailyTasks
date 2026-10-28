# Write a loop that prints only the even numbers from a list.

a = [2, 6, 7, 9, 2]
for num in a:
  if num % 2 == 0:
    print(num)

# Given a list of integers, use a loop and conditionals to separate positive and negative numbers into two new lists.

a = [2, 6, -7, 9, -2]
positive = []
negative = []
for num in a:
  if num > 0:
    positive.append(num)
  elif num < 0:
    negative.append(num)
print("postive numbers:", positive)
print("negative numbers:", negative)

# Write a loop that prints "Big" if a list element is greater than 50, otherwise print "Small".

a = [60, 70, 80, 80, 100]
for num in a:
  if num > 50:
    print("Big")
  else:
    print("small")

# Use a loop to count how many elements in a list are divisible by 3.

a = [3, 30, 6, 9,]
count = 0
for num in a:
  if num % 3 == 0:
    count += 1
print("count of numbers devisible by 3 is", count)

# Write a loop that replaces all negative numbers in a list with 0.

a = [-1, -2, -3, -4, -5]
new_value = 0
count = 0
for num in a:
  if num < 0:
    a[count] = new_value
    count += 1
print(a)

# Write a loop that prints elements of a tuple only if they are greater than 10.

a = (13, 15, 7, 9, 6)
for num in a:
  if num > 10:
    print(num)

# Given a tuple of numbers, use a loop to print "Odd" or "Even" for each element.

a = (2, 5, 6, 7, 9, 10)
for num in a:
  if num % 2 == 0:
    print("Even")
  else:
    print("Odd")

# Write a loop that finds the largest odd number in a tuple.

a = (2, 9, 3, 6, 5)
largest_num = 0
for num in a:
  if num % 2 != 0 and num > largest_num:
     largest_num = num
print("largest odd number is:", largest_num)

# Use a loop to count how many elements in a tuple are prime numbers.

nums = (2, 4, 5, 8, 11, 13, 15)

count = 0

for num in nums:
    is_prime = True

    if num < 2:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

    if is_prime:
        count += 1

print("Prime count:", count)

# Write a loop that prints "High" if a tuple element is above 100, otherwise "Low".

a = (200, 300, 40, 500)
for num in a:
  if num > 100:
    print("High")
  else:
    print("Low")

# Write a loop that prints only odd numbers from a set.

a = {2, 7, 8, 9, 5}
for num in a:
  if num % 2 != 0:
    print(num)

# Given a set of integers, use a loop to remove all numbers less than 5.

a = { 6, 8, 9, 3}
for num in a.copy():
  if num < 5:
    a.remove(num)
    print(a)

# Write a loop that prints "Found" if the set contains the number 10, otherwise "Not Found".

a = {10, 30, 50}
for num in a:
  if num == 10:
    print("Found")
  else:
    print("Not found")

# Use a loop to build a new set containing only squares of even numbers from another set.

a = {4, 8, 7, 6, 9}
new_set = set()
for num in a:
  if num % 2 == 0:
    new_set.add(num**2)
  print(new_set)

# Write a loop that prints "Duplicate" if an element already exists in a set while iterating through a list.

a = [1, 1, 3, 8,]
new_set = set()
for num in a:
  if num in new_set:
    print("Duplicate")
  else:
    new_set.add(num)

# Write a loop that counts vowels in a string using conditionals.

a = "Harika"
count = 0
for char in a:
   if char in "aeiouAEIOU":
    print(char)
    count += 1
print("count of vowels in string:", count)

# Use a loop to print "Digit" if a character is numeric, otherwise print "Letter".

a = "12345"
for char in a:
  if char.isdigit():
    print("Digit")
  else:
    print("Letter")

# Write a loop that prints only uppercase characters from a string.

a = "Harika"
for char in a:
  if char.isupper():
     print(char)

# Given a string, use a loop to count how many times "a" appears.

a = "Harika"
count = 0
for char in a:
  if char == "a":
    print(char)
    count += 1
print("Count of a:", count)

# Write a loop that prints "Palindrome" if a string reads the same forward and backward, otherwise "Not Palindrome".

text = "madam"

reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

if text == reversed_text:
    print("Palindrome")
else:
    print("Not Palindrome")

# Write a loop that prints dictionary keys only if their values are greater than 50.

dic = {"a" : 60, "b" : 40, "c" : 87}
for key, value in dic.items():
  if value > 50:
    print(key)

# Given a dictionary of student names and marks, use a loop to print "Pass" if marks ≥ 40, otherwise "Fail

dic = {"a" : 90, "b" : 80, "c" : 55}
for key, value in dic.items():
  if value > 40:
    print("Pass")
  else:
    print("Fail")

# Write a loop that counts how many dictionary values are even.

dic = {"a" : 6, "b" : 8, "c" : 6}
count = 0
for key, value in dic.items():
  if value % 2 == 0:
    count += 1
    print(value)
print("count of even numbers:", count)

# Use a loop to print "Starts with A" if a key begins with "A", otherwise print "Other".

dic = {"A" : 3, "B" : 8, "C" : 7}
for key, value in dic.items():
  if key.startswith("A"):
    print("starts with A")
  else:
    print("other")

# Write a loop that finds the maximum value in a dictionary and prints the corresponding key.

dic = {"a" : 6, "b" : 8, "c" : 6}
for key, value in dic.items():
  if value == max(dic.values()):
    print(key)

# Write a loop that prints numbers from 1 to 20, but skips multiples of 5.

for i in range(1, 21):
  if i % 5 == 0:
    continue
  print(i)

# Use a loop to print numbers from 1 to 15, but stop when you reach 10.

for i in range(1, 16):
  if i == 10:
    continue
  print(i)

# Write a loop that prints "Prime" if a number is prime, otherwise "Not Prime", for numbers 2–20.

for num in range(2, 21):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "Prime")
    else:
        print(num, "Not Prime")

# Use a loop to print squares of numbers from 1 to 10, but only if the square is less than 50.

for i in range(1, 11):
  square = i ** 2
  if square < 50:
    print(square)

# Write a loop that iterates through a list of tuples (name, age) and prints "Adult" if age ≥ 18, otherwise "Minor".

people = [("Harika" , 20) , ("Haru" , 18) , ("Har" , 15)]
for name, age in people:
  if age >= 18:
    print("Adult")
  else:
    print("Minor")