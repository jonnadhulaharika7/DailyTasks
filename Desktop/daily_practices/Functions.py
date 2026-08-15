# 1. Prime Number
# Question: Write a function to check whether a number is prime or not.
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(7))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))

# 2. Factorial
# Question: Write a function to find the factorial of a number.
# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
#     return result
# print(factorial(5))
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
print(factorial(5))

# Armstrong Number
# Question: Write a function to check whether a number is an Armstrong number.
# def is_amstrong(n):
#     num_str = str(abs(n))
#     power = len(num_str)
#     total = 0
#     for digit in num_str:
#         total = int(digit) ** power
#     return total(abs(n))
# print(is_amstrong(153))
# def is_amstrong(n):
#     num_str = str(abs(n))
#     power = len(num_str)
#     total = 0
#     for digit in num_str:
#         total += int(digit) ** power
#     return total == abs(n)
# print(is_amstrong(153))
def is_amstrong(n):
    num_str = str(abs(n))
    power = len(num_str)
    total = 0
    for digit in num_str:
        total = total + int(digit) ** power
    return total == abs(n)
print(is_amstrong(153))

# Fibonacci
# def is_fibonacci(n):
#     a,b = 0,1
#     while b <= n:
#         a,b = b,a+b
#     return b
# print(is_fibonacci(10))
def is_fibonacci(n):
    a,b = 0,1
    while b <= n:
        a,b = b,a+b
    return b
print(is_fibonacci(21))

# Palindrome 
def is_palindrome(n):
    original = n
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev*10 + n % 10
        n = n//10
    return rev == abs(original)
print(is_palindrome(121))

# Find the largest of three numbers
def largest(a,b,c):
    if a >=b and a >= c:
        return a 
    elif a <= b and b >= c:
        return b
    else:
        return c
print(largest(89,67,90))

# Write a function that counts the number of vowels in a string.
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count
print(count_vowels("python programming"))

# Write a function to find the largest element in a list without using max().
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
print(find_largest([10,25,7,40,15]))

# Find Second Largest Number
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]
print()

# sum of digits
def sum_digits(n):
    total = 0
    n = abs(n)
    while n > 0:
        total = total + n % 10
        n = n // 10
    return total
print(sum_digits(12345))

# count digits in number
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count = count + 1
        n = n//10
    return count
print(count_digits(12345))

# find even and odd from a list
def even_odd_numbers(n):
    even = []
    odd = []
    for num in n:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even,odd
even,odd = even_odd_numbers([1,2,3,4,5])
print("even:",even)
print("odd:",odd)

# count frequency of each character
def character_frequency(n):
    frequency = {}
    for ch in n:
        if ch in frequency:
            frequency[ch] = frequency[ch] + 1
        else:
            frequency[ch] = 1
    return frequency 
print(character_frequency("hello"))
        
# Remove duplicates from a list
def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result
print(remove_duplicates([1,3,4,4,5]))   

# find common elements between two lists
def common_elements(list1,list2):
    result = []
    for item in list1:
        if item in list2 not in result:
            result.append(item)
print(common_elements([1,2,3] , [3,4,5]))

# 