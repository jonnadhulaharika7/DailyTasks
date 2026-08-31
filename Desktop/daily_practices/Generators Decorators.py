# Create a generator that produces numbers from 1 to 5.
def numbers():
    for i in range(1,6):
        yield i
x = numbers()
for value in x:
    print(value)
    
# Create a generator that produces even numbers from 1 to 10.
def even_numbers():
    for i in range(1,11):
        if i % 2 == 0:
            yield i
for value in even_numbers():
    print(value)
    
# Generator Using next()
def numbers():
    for i in range(10,51,10):
        yield i
x = numbers()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Create a generator that generates the squares of numbers from 1 to 5.
def squares():
    for i in range(1,6):
        yield i * i
for value in  squares():
    print(value)
    
# Reverse a String Using Generator
def reverse_string(text):
    for i in range(len(text) -1,-1,-1):
        yield text[i]
for char in reverse_string("python"):
    print(char)
    
# Write a generator that accepts n and generates the first n even numbers.
def even_numbers(n):
    for i in range(1, n+1):
        yield i * 2
for value in even_numbers(5):
    print(value)
    
# Generator for File Line
def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()
for  line in read_file("data.txt"):
    print(line)

# Infinite Generator
def numbers():
    i = 1
    while True:
        yield i
        i += 1
x = numbers()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Generate numbers from N to 1
def reverse_numbers(n):
    for i in range(n,0,-1):
        yield i
for value in reverse_numbers(5):
    print(value)

# Generate odd numbers
def odd_numbers(n):
    for i in range(1, n + 1):
        if  i %  2 != 0:
            yield i
for value in odd_numbers(10):
    print(value)

# Generate cubes
def cubes(n):
    for i in range(1, n + 1):
        yield i ** 3
for value in cubes(5):
    print(value)
    
# Create a generator that produces each element of a list.
def generate_list(numbers):
    for num in numbers:
        yield num
numbers = [10,20,30,40,50]
for value in generate_list(numbers):
    print(value)
    
# Generate only positive numbers
def positive_numbers(numbers):
    for num in numbers:
        if num > 0:
            yield num
numbers = [-10,20,-5,30,-2,40]
for value in positive_numbers(numbers):
    print(value)
    
# Generate only positive numbers
def negative_numbers(numbers):
    for num in numbers:
        if num < 0:
            yield num
numbers = [-10,20,-5,30,-2,40]
for value in negative_numbers(numbers):
    print(value)
    
# Generate even elements from a list
def even_elements(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num
numbers = [10,15,22,31,40,55,60]
for value in even_elements(numbers):
    print(value)
    
# Generate characters from a string
def characters(text):
    for char in text:
        yield char
for char in characters("Harika"):
    print(char)

# Generate vowels
def vowels(text):
    for char in text:
        if char.lower() in "aeiou":
            yield char
for char in vowels("Hello Python World"):
    print(char)


