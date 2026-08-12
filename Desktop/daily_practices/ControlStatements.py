# Write a program to check whether a number is positive, negative, or zero.
a = int(input("enter a number:"))
if a > 0:
    print("number is positive")
elif a < 0:
    print("number is negative")
else:
    print("number is zero")
# Check whether a number is even or odd.
a = int(input("enter a number:"))
if a % 2 == 0:
    print("number is even")
else:
    print("number is odd")
# Find the largest of two numbers.
a = int(input("enter a number:"))
b = int(input("enter a number:"))
if a > b:
    print("a is largest number")
else:
    print("b is largest number")
# Find the largest of three numbers.
a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))
if a > b > c:
    print("a is largest number")
elif a < b > c:
    print("b is largest number")
else:
    print("c is largest number")
# Check whether a year is a leap year.
a = int(input("enter a year:"))
if a % 4 == 0:
    print("given year is a leap year")
else:
    print("given year is not a leap year")
# Check whether a number is divisible by both 3 and 5.
a = int(input("enter a number:"))
if a % 3 == 0 and a % 5 == 0:
    print("number is divisible by both 3 and 5")
else:
    print("number is not divisible by both 3 and 5")
# Take marks as input and print the grade.
a = int(input("enter marks:"))
if a >= 80:
    print("grade A")
elif a >= 60:
    print("grade B")
else:
    print("grade C")
    
# for loop
# Print numbers from 1 to 10.
for i in range(1, 11):
    print(i)
# Print all even numbers from 1 to 50.
for i in range(1,51):
    if i % 2 == 0:
        print(i)
# Find the sum of numbers from 1 to 100.
# total = 0
# for i in range(1, 101):
#     total = total + i
# print(total)
total = 0
for i in range(1, 101):
    total = total + i
print(total)
# Find the factorial of a number.
# a = int(input("enter a number:"))
# factorial = 1
# for i in range (1, a + 1):
#     factorial = factorial * i
# print("factorial:",factorial)
a = int(input("enter a number:"))
factorial = 1
for i in range(1, a + 1):
    factorial = factorial * i
print("factorial:",factorial)
# Print the multiplication table of a given number.
a = int(input("enter a number:"))
for i in range(1, 11):
    print(a, "x", i,"=",a * i)
# Check whether a number is prime.
n = int(input("enter a number:"))
if n <= 1:
    print("prime numbers can not be negative")
else:
    for i in range(2, n):
        if n % i == 0:
            print("not a prime number")
            break
    else:
        print("prime number") 
# Find the sum of digits of a number.
num = int(input("enter a number:"))
total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10
print("sum of digits:",total)

# while loop
# Reverse a number using a while loop.
num = int(input("enter a number:"))
reverse = 0
while num > 0:
    digit = num  % 10
    reverse = reverse * 10 + digit
    num = num//10
print("reverse of number:",reverse)
# Count the number of digits in a number.
num = int(input("enter a number:"))
count = 0
while num > 0:
    num = num//10
    count = count + 1
print("count of number:",count)
# Keep taking numbers from the user until they enter 0.
num = int(input("enter a number:"))
while num !=0:
    print("you entered:",num)
    num = int(input("enter a number:"))
print("loop ended")
# Find the factorial using a while loop.
n = int(input("enter a number:"))
factorial = 1
while n > 0:
    factorial = factorial * n
    n = n - 1
print("factorial:",factorial)

# break / continue / nested loops
# Print numbers from 1 to 20, but stop when the number reaches 10 using break.
for i in range(1, 21):
    if i == 10:
        break
    print(i)
# Print numbers from 1 to 20 but skip multiples of 3 using continue.
for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)


