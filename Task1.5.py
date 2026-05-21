# Write a function that takes a list of numbers and returns the sum.
def sum_list(numbers):
    return sum(numbers)
print(sum_list([1, 2, 3, 4, 5]))

# Pass a list of strings to a function and return the longest string.
def longest_string(string):
    return max(string, key=len)
print(longest_string(["Harika", "Haru", "Har"]))

# Create a function that accepts a list and returns a new list with duplicates removed.
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
lst = [1, 2, 3, 1,]
print(remove_duplicates(lst))

# Write a function that takes a list of integers and returns only the even numbers.
def even_numbers(lst):
    result = []
    for item in lst:
        if item % 2 == 0:
            result.append(item)
    return result
lst = [2, 3, 4, 6]
print(even_numbers(lst))

# Pass a list of numbers and return the maximum and minimum values.
def find_max_min(num):
    return max(num), min(num)
num = [10, 60, 80]
maximum , minimum = find_max_min(num)
print("max:", maximum)
print("min:", minimum)

# Write a function that takes a list and returns it reversed.
def returns_it_reversed(lst):
    return lst[::-1]
lst = [7, 13, 90, 20]
print(returns_it_reversed(lst))

# Create a function that accepts a list of words and returns them sorted alphabetically.
def sorted_alphabetically(lst):
    return sorted(lst)
lst = ["Apple", "Banana", "Cherry"]
print(sorted_alphabetically(lst))

# Write a function that takes a list of integers and returns their average.
def return_their_average(lst):
    return sum(lst) / len(lst)
lst = [1, 2, 3, 4, 6]
print(return_their_average(lst))

# Pass a list of strings and return a list of their lengths.
def return_length(lst):
    return len(lst)
lst = ["Harika", "Haru", "Ha"]
print(return_length(lst))

# Write a function that takes a list of numbers and returns the product of all elements.
def product_elements(lst):
    result = 1
    for num in (lst):
        result *= num
    return result
lst = [1, 5, 4]
print(product_elements(lst))

# Write a function that takes a tuple of numbers and returns the sum.
def return_the_sum(t):
    result = 0
    for num in (t):
        result += num  
    return result
t = (1, 3, 5)
print(return_the_sum(t))

# Pass a tuple of strings and return the shortest string.
def shortest_string(t):
    return min(t, key = len)
t = ("Kiwi", "Cherry", "Apple")
print(shortest_string(t))

# Create a function that accepts a tuple and returns it as a list.
def return_list(t):
    return list(t)
t = (23, 24, 25, 26)
print(return_list(t))

# Write a function that takes a tuple of integers and returns the count of odd numbers.
def count_odd_numbers(t):
    result = 0
    for i in t:
        if i % 2 !=0:
            result += 1
    return result
t = (1, 3, 4, 9)
print(count_odd_numbers(t))

# Pass a tuple of numbers and return the second largest value.
def second_largest_value(t):
    return sorted(t)[-2]
t = (1, 2, 8, 9)
print(second_largest_value(t))

# Write a function that takes a tuple and returns it reversed.
def return_reversed(t):
    return t [::-1]
t = (9, 6, 7)
print(return_reversed(t))

# Create a function that accepts a tuple of words and returns them joined into a single string.
def single_string(t):
    return "".join(t)
t = ("Hello", "World")
print(single_string(t))

# Write a function that takes a tuple of integers and returns a tuple with each element squared.
def element_squared(t):
    result = []
    for i in t:
        result.append(i ** 2)
    return result
t = (1, 2, 3)
print(element_squared(t))

# Pass a tuple of strings and return the one with the maximum vowels.
def maximum_vowels(t):
    max_word = ""
    max_count = 0
    for word in t:
        count = 0
        for ch in word:
           if ch.lower() in "aeiou":
             count += 1
        if count > max_count:
           max_count = count
           max_word = word
    return max_word        
t = ("Harika", "Haru", "Har")
print(maximum_vowels(t))

# Write a function that takes a tuple and returns the number of unique elements.	
def unique_elements(t):
    unique_elements = []
    for i in t:
        if i not in unique_elements:
            unique_elements.append(i)
    return(len(unique_elements))
t = (1, 1, 2, 2, 3, 3, 4, 4)
print(unique_elements(t))

# Write a function that takes a string and returns it reversed.
def return_reversed(s):
    return s[::-1]
s = "Harika"
print(return_reversed(s))

# Pass a string and return the count of vowels.
def count_of_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count
s = "Harika"
print(count_of_vowels(s))

# Create a function that accepts a string and returns whether it is a palindrome.
def return_a_palindrome(s):
    if s == s[::-1]:
       return  True
    else:
       return  False
s = "level"
print(return_a_palindrome(s))

# Write a function that takes a string and returns the frequency of each character.
def frequency_character(s):
    frequency =  {}
    for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
    return frequency
s = "Harika"
print(frequency_character(s))

# Pass a string and return the first non-repeated character.
def non_repeating_character(s):
    frequency = {}
    for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
    for ch in s:
      if frequency[ch] == 1:
       return ch
s = "Harika"
print(non_repeating_character(s))

# Write a function that takes a string and returns it in uppercase.
def return_in_uppercase(s):
    result = ""
    for ch in s:
        result += ch.upper()
    return result
s = "harika"
print(return_in_uppercase(s))

# Create a function that accepts a string and returns the number of words.
def num_of_words(s):
    count = 0
    in_word = False
    for ch in s:
        if ch != " " and not in_word:
            count += 1
            in_word = True
        elif ch == " ":
            in_word = False

    return count
s = "I love python"
print(num_of_words(s))

# Write a function that takes a string and returns all unique characters.
def unique_character(s):
   frequency = {}
   result = ""
   for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
   for ch in s:
       if frequency[ch] == 1:
           result += ch
   return result
s = "Harika"
print(unique_character(s))

# Pass a string and return the most frequent character.
def frequent_character(s):
    frequency = {}
    result = ""
    for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
    for ch in s:
        if frequency [ch] != 1:
            result = ch
    return result
s = "Harika"
print(frequent_character(s))

# Write a function that takes a string and returns it without spaces.
def remove_spaces(s):
    result = ""
    for ch in s:
        if ch in s:
            if ch != " ":
                result += ch
    return result
s = "Hello World from chatGPT"
print(remove_spaces("Hello World from chatGPT"))

# Write a function that takes a dictionary and returns the sum of all values.
def sum_of_values(d):
    total = 0
    for value in d.values():
        total += value
    return total
my_dict = {"a" : 10,  "b" : 20, "c" : 30}
print(sum_of_values(my_dict))

# Pass a dictionary and return the key with the maximum value.
def max_value_key(d):
    max_key = None
    max_value = float('-inf')
    for key,value in d.items():
        if value > max_value:
            max_value = value
            max_key = key 
    return max_key
my_dict = {"a" : 11,  "b" : 25, "c" : 15}
print(max_value_key(my_dict))

# Create a function that accepts a dictionary and returns a list of all keys.
def list_keys(d):
    result = []
    for key in d:
         result.append(key)
    return result
my_dict = {"a" : 11,  "b" : 25, "c" : 15}
print(list_keys(my_dict))
            
# Write a function that takes a dictionary and returns a list of all values
def list_values(d):
    result = []
    for value in d.values():
        result.append(value)
    return result
my_dict = {"a" : 11,  "b" : 25, "c" : 15}
print(list_values(my_dict))  

# Pass a dictionary and return a new dictionary with keys and values swapped.
def swap_dict(d):
    result = {}
    for key, value in d.items():
        result[value] = key
    return result
my_dict = {"a" : 11,  "b" : 25, "c" : 15}
print(swap_dict(my_dict))  

# Write a function that takes a dictionary and returns the number of items.
def count_items(d):
    count = 0
    for i in d:
        count += 1
    return count
my_dict = {"a" : 11,  "b" : 25, "c" : 15}
print(count_items(my_dict))

# Create a function that accepts a dictionary and returns whether a given key exists.
def key_exists(d,key):
    for k in d:
        if k == key:
           return True
        else:
           return False
my_dict = {"a" : 11,  "b" : 25, "c" : 15}
print(key_exists(my_dict, "a"))
print(key_exists(my_dict, "d"))

# Write a function that takes a dictionary and returns the average of numeric values.
def average_values(d):
    return sum(d.values()) / len(d)
my_dict = {"a" : 11,  "b" : 25, "c" : 15}
print(average_values(my_dict))

# Pass a dictionary and return the key with the longest string value.
def longest_value_key(d):
    max_key = None
    max_len = 0
    for key, value in d.items():
        if  len(str(value)) > max_len:
            max_len = len(str(value))
            max_key = key
    return max_key
my_dict = {"Harika" : 11,  "Haru" : 25, "Har" : 15}
print(longest_value_key(my_dict))

# Write a function that takes a dictionary and returns a sorted list of keys.
def list_keys(d):
    result = []
    for keys in d:
        result.append(keys)
    return result
my_dict = {"Harika" : 11,  "Haru" : 25, "Har" : 15}
print(list_keys(my_dict))

# Write a function that takes a list of tuples and returns the tuple with the largest sum.
def largest_sum_tuple(t):
    max_tuple = None
    max_sum = float('-inf')
    for i in t:
        if sum(i) > max_sum:
            max_sum = sum(i)
            max_tuple = i
    return max_tuple
t = [(1,2),(3,4),(4,5)]
print(largest_sum_tuple(t))

# Pass a dictionary of lists and return the length of the longest list.
def longest_list_length(d):
    max_len = 0
    for value in d.values():
        if isinstance(value, list) and len(value) > max_len:
            max_len = len(value)
    return max_len
my_dict = {"a" : [1,2,3], "b" : [4,5,6], "c" : [7,8,9]}
print(longest_list_length(my_dict))

# Create a function that accepts a list of strings and returns a dictionary with word lengths.
def word_lengths(words):
    result = {}
    for word in words:
        result[word] = len(word)
    return result
words = ["Apple","Cat","Dog"]
print(word_lengths(words))

# Pass a list of dictionaries and return the dictionary with the maximum value for a given key.
def max_dict_by_key(lst,key):
    max_dict = None
    max_value = float('-inf')
    for d in lst:
        if key in d and d[key] > max_value:
            max_value = d[key]
            max_dict = d
    return max_dict
data = [{"name" : "A" , "marks" : 90}, {"name" : "B" , "marks" : 85}, {"name" : "C" , "marks" : 95}]
print(max_dict_by_key(data, "marks"))

# Write a function that takes a string and returns a dictionary with counts of each word.
def count_word(sentence):
    result = {}
    words = sentence.split()
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result
sentence = "apple banana apple orange banana apple"
print(count_word(sentence))
        
# Create a function that accepts a list of numbers and returns a tuple of (sum, average, max, min)
def stats(nums):
    total = 0
    maximum = nums[0]
    minimum = nums[0]
    for n in nums:
        total += n
        if n > maximum:
            maximum = n
        if n < minimum:
            minimum = n
    average = total / len(nums)
    return (total, average, maximum, minimum)
nums = [10,20,30,8]
print(stats(nums))

# Write a function that takes a tuple of strings and returns a list of strings sorted by length
def sort_by_length(t):
    lst = list(t)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) > len(lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
    return lst
words = ("apple", "hi", "banana", "cat")
print(sort_by_length(words))

# Pass a dictionary of tuples and return the tuple with the maximum length.
def longest_tuple(d): 
    max_tuple = None
    max_len = 0
    for value in d.values():
        if isinstance(value, tuple) and len(value) > max_len:
            max_len = len(value)
            max_tuple = value
    return max_tuple
my_dict = {"a" : (1,2,4), "b" : (3,4,5,8), "c" : (5,)}
print(longest_tuple(my_dict))

# Write a function that takes a list of strings and returns a dictionary grouping them by their first letter.
def group_by_first_letter(words):
    result = {}
    for word in words:
        first = word[0]
        if first in result:
            result[first].append(word)
        else:
            result[first] = [word]
    return result
words = ["apple", "ant", "banana", "ball", "cat", "car"]
print(group_by_first_letter(words))

# Write a function that takes an integer and returns whether it is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(10))

# Pass an integer to a function and return its factorial.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))

# Create a function that accepts an integer and returns the sum of its digits.
def sum_of_digits(n):
    total = 0
    n = abs(n) 
    while n > 0:
        total += n % 10
        n //= 10
    return total
print(sum_of_digits(1234))

# Write a function that takes an integer and returns whether it is an Armstrong number.
def is_armstrong(n):
    num_str = str(abs(n))
    power = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** power
    return total == abs(n)
print(is_armstrong(153))
print(is_armstrong(123))

# Pass an integer and return the reverse of its digits.
def reverse_number(n):
    rev = 0
    n = abs(n)
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev
print(reverse_number(12345))

# Write a function that takes an integer and returns whether it is a palindrome number.
def is_palindrome(n):
    original = n
    rev = 0
    n = abs(n)
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev == abs(original)
print(is_palindrome(121))
print(is_palindrome(123))

#  Create a function that accepts an integer and returns the count of even digits in it.
def count_even_digits(n):
    count = 0
    n = abs(n)
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            count += 1
        n //= 10
    return count
print(count_even_digits(123456))

# Write a function that takes an integer and returns the next Fibonacci number after it.
def next_fibonacci(n):
    a, b = 0, 1
    while b <= n:
        a, b = b, a + b
    return b
print(next_fibonacci(10))
print(next_fibonacci(21))

#  Pass an integer and return the greatest common divisor (GCD) of that integer and another fixed number.
def gcd_with_fixed(n, fixed=48):
    n = abs(n)
    while fixed != 0:
        n, fixed = fixed, n % fixed
    return n
print(gcd_with_fixed(24))   
print(gcd_with_fixed(18)) 

# Write a function that takes an integer and returns a list of all its divisors.
def get_divisors(n):
    n = abs(n)
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
print(get_divisors(12)) 

print('hello')