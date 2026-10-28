# 1.Reverse an integer
#  Write a program to reverse a number.
def reverse_number(num):
    rev = 0
    while num != 0:
        n = num % 10
        rev = rev * 10 + n 
        num = num // 10
    print(rev)
reverse_number(12345)

# Sum of digits
# Find the sum of all digits in a number.
def sum_digits(num):
    sum = 0
    while num != 0:
        n = num % 10
        sum = sum + n
        num = num // 10
    print(sum)
sum_digits(246)

# Count digits
# Count how many digits are present in an integer.
def count_digits(num):
    count = 0
    while num !=0:
        n = num % 10
        count = count + 1
        num = num // 10
    print(count)
count_digits(12345)

# Check palindrome number
# Check whether a number reads the same forwards and backwards.
def palindrome_number(num):
    rev = 0
    while num !=0:
        n = num % 10
        rev = rev * 10 + n
        num = num // 10
    print(rev)
palindrome_number(153)

# Find largest digit
# Find the largest digit in a number.
def largest_digit(num):
    largest = 0
    while num != 0:
        n = num % 10
        if n > largest:
            largest = n
        num = num // 10
    print(largest)
largest_digit(58329)

# Find smallest digit
# Find the smallest digit
def smallest_digit(num):
    smallest = 9
    while num != 0:
        n = num % 10
        if n < smallest:
            smallest = n
        num = num // 10
    print(smallest)
smallest_digit(58329)

# Count even and odd digits
# Count how many even and odd digits are present.
def count_even_odd_digits(num):
    even_count = 0
    odd_count = 0
    while num != 0:
        n = num  % 10
        if n % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
        num = num // 10
    print(even_count)
    print(odd_count)
count_even_odd_digits(1234567)

# Armstrong number
# Check whether a number is an Armstrong number.
def amstrong_number(num):
    p = len(str(num))
    sum = 0
    original_number = num
    while num != 0:
        digit = num % 10
        sum = sum + digit ** p
        num = num // 10
    print(original_number == sum)
amstrong_number(153)

# prime number
# Check whether a given number is prime.
def prime_number(num):
    for divisior in range(2,num):
        if num % divisior == 0:
            return False
    return True
print(prime_number(17))

# Factorial
# Find the factorial of a number.
def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result
print(factorial(5))

# fibonacci 
def fibonacci(num):
    a , b = 0, 1
    while b <=  num:
        a , b = b , a + b
    return b
print(fibonacci(10))

# Level 2 — Lists
# Reverse a list
# Do it without using reverse().
def reverse_list(num):
    result = []
    for i in range(len(num),0,-1):
        result.append(i)
    return result
print(reverse_list([1,2,3,4,5]))

# Remove duplicates without losing order
def remove_duplicates(num):
    result = []
    for n in num:
        if n not in result:
         result.append(n)
    return result
print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))

# Find largest element
def largest_element(num):
    largest = num[0]
    for n in num:
        if n > largest:
            largest = n
    return largest
print(largest_element([10,25,3,78,45]))

# Find Smallest element
def smallest_element(num):
    smallest = num[3]
    for n in num:
        if n < smallest:
            smallest = n
    return smallest
print(smallest_element([10,25,3,78,45]))
            
# Sum of list
def sum_list(num):
    total = 0
    for n in num:
        total += n
    return total
print(sum_list([10,20,30,40]))

# Count even and odd numbers
def even_odd_numbers(num):
    even = 0
    odd = 0
    for n in num:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd
even,odd = even_odd_numbers([1,2,3,4,5,6])
print("even:",even)
print("odd:",odd)

# Common elements
def common_elements(list1,  list2):
    result = []
    for num in list1:
        if num in list2:
            result.append(num)
    return result
print(common_elements([1,2,3,4,5],
                      [3,4,5,6,7]))

# Separate positive and negative
def positive_negative(num):
    positive = []
    negative = []
    for n in num:
        if n >= 0:
            positive.append(n)
        else:
            negative.append(n)
    return positive, negative
positive, negative = positive_negative([-2,5,-8,10,-3,7])
print("positive:",positive)
print("negative:",negative)

# Move zeros to end
def move_zeros(num):
    result = []
    zero_count = 0
    for n in num:
     if n == 0:
        zero_count += 1
    else:
        result.append(n)
    for i in range(zero_count):
     result.append(0)
    return result
print(move_zeros([0,1,0,3,12]))

# Strings
# Reverse string
def reverse_string(text):
    result = " "
    for char in text:
        result = char + result
    return result
print(reverse_string("Harika"))

# String palindrome
def string_palindrome(text):
    reverse = ""
    for ch in text:
        reverse = ch + reverse
    return text == reverse
print(string_palindrome("madam"))

# Count vowels
def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count
print(count_vowels("python programming"))

# Count vowels and consonants
def count_vowels_consonants(text):
    vowels = 0
    consonants = 0
    for char in text.lower():
        if char in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1
    return vowels, consonants
vowels, consonants = count_vowels_consonants("hello")
print("vowels:", vowels)
print("consonants:", consonants) 

# Character frequency
def character_frequency(text):
    count = {}
    for char in text:
        count[char] = count.get(char, 0) + 1
    return count
print(character_frequency("hello"))

# Remove spaces
def remove_spaces(text):
    result = ""
    for char in text:
        if char != " ":
            result += char
    return result 
print(remove_spaces("python is easy"))

# First non-repeated character
def first_non_repeated(text):
    count = {}
    for char in text:
        count[char] = count.get(char, 0) + 1
    for char in text:
        if count[char] == 1:
            return char
    return None
print(first_non_repeated("aabbcde"))

# Remove duplicate characters
def remove_duplicate_characters(text):
    result = ""
    for char in text:
        if char not in result:
            result += char
    return result
print(remove_duplicate_characters("programming"))

# Find longest word
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(longest_word("python is very powerful"))

# Dictionaries
# Get all keys    
def get_keys(data):
    return list(data.keys())
student = {
    "name" : "Harika",
    "age"  : 22,
    "course" : "python"
}
print(get_keys(student))

# Find highest value
def highest_value(data):
    highest_key = ""
    highest_value = float('-inf')
    for key, value in data.items():
        if value > highest_value:
            highest_value = value
            highest_key = key
    return highest_key, highest_value
marks = {
    "Math": 85,
    "Python": 95,
    "SQL": 90,
    "AWS": 88
}
print(highest_value(marks))

# Frequency of list elements
def frequency(numbers):
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
    return count
print(frequency([1,2,2,3,3,3,4]))

# Word frequency
def word_frequency(text):
    words = text.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count
text = "python is easy and python is powerful" 
print(word_frequency(text))

# Merge dictionaries
def merge_dicts(dict1, dict2):
    result = {}
    for key, value in dict1.items():
        result[key] = value
    for key, value in dict2.items():
        result[key] = value
    return result 
print(merge_dicts(
    {"a" : 10, "b" : 20},
    {"c" : 30, "d" : 40}
))

# Find duplicate values
def duplicate_values(data):
    seen = []
    duplicates = []
    for value in data.values():
        if value in seen:
            if value  not in duplicates:
                duplicates.append(value)
        else:
            seen.append(value)
    return duplicates
data = {
    "a" : 10,
    "b" : 20,
    "c" : 10,
    "d" : 30,
    "e" : 20
} 
print(duplicate_values(data))

# Sort dictionary by values
def sort_by_value(data):
    return dict(
        sorted(
            data.items(),
            key=lambda item : item[1]
        )
    )
marks = {
    "A" : 75,
    "B" : 95,
    "C" : 65,
    "D" : 85
}
print(sort_by_value(marks))

