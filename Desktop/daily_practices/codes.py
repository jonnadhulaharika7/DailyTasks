# Create a Student class with name and marks and display the details.
class student:
    def display(self):
        print("student details")
s1 = student()
s1.display()

# Create an Employee class that accepts employee name, ID and salary.
class employee:
    def __init__(self,name,emp_id,salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    def display(self):
        print("name:",self.name)
        print("id:",self.emp_id)
        print("salary",self.salary)
e1 = employee("harika",101,50000)
e1.display()

# Count number of objects created
class student:
    college = "ABC college"
    count = 0
    def __init__(self,name):
        self.name = name
        student.count += 1
s1 = student("A")
s2 = student("B")
s3 = student("C")
print(student.count)

# Create a class method to change college name
class student:
    college = "ABC"
def __init__(self,name):
    self.name = name
@classmethod
def change_college(cls,new_college):
    cls.college = new_college
s1 = student("harika")
print(student.college)   
student.change_college("XYZ")
print(student.college) 

# Create a static method to check whether a number is even
class number:
    @staticmethod
    def is_even(n):
        return n % 2 == 0
print(number.is_even(10))
print(number.is_even(7))
       
# Create a bank account with private balance
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("insufficent balance")
    def get_balance(self):
        return self.__balance
account = BankAccount(10000)
account.deposit(5000)
account.withdraw(3000)
print(account.get_balance())

# MULTILEVEL INHERITANCE
class person:
    def show_person(self):
        print("person")
class employee(person):
    def show_employee(self):
        print("employee")
class manager(employee):
    def show_manager(self):
        print("manager")
m = manager()
m.show_person()
m.show_employee()
m.show_manager()

# MULTIPLE INHERITANCE
class father:
    def skills(self):
        print("driving")
class mother:
    def hoobies(self):
        print("cooking")
class child(father,mother):
    pass
c = child()
c.skills()
c.hoobies()

# METHOD OVERRIDING ⭐⭐⭐
class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        print("dog barks")
d = dog()
d.sound()    

# super() WITH METHOD OVERRIDING
class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        super().sound()
        print("dog barks")
d = dog()
d.sound()    

# POLYMORPHISM
class dog:
    def sound(Self):
        print("bark")
class cat:
    def sound(self):
        print("meow")
class cow:
    def sound(self):
        print("moo")
animals = [dog(),cat(),cow()]
for animal in animals:
    animal.sound()
    
# ABSTRACTION ⭐⭐⭐
from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        print("bark")
d = dog()
d.sound()

# Create an abstract Shape class
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(Self):
        return 3.14 * self.radius * self.radius
class rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
c = circle(5)
r = rectangle(10,5)
print(c.area())
print(r.area())
    
# File Handling + Exception ⭐⭐⭐⭐⭐
try:
    file = open("data.txt","r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found")
    
# Open and Read a File ⭐⭐⭐
file = open("data.txt","r")
content = file.read()
print(content)
file.close()

# readline() ⭐⭐⭐
file = open("data.txt","r")
line = file.readline()
print(line)
file.close()

# with open() ⭐⭐⭐⭐⭐
with open("data.txt","r") as file:
    content = file.read()
    print(content)
    
# Lambda with sorted() ⭐⭐⭐⭐⭐
numbers = [23,15,42,31,18]
result = sorted(numbers,key=lambda x:x % 10)
print(result)

# Generate numbers from 1 to 5
def numbers():
    for i in range(1,6):
        yield i
for num in numbers():
    print(num)
    
# Generate numbers one by one
def numbers():
    yield 10
    yield 20
    yield 30
gen = numbers()
print(next(gen))
print(next(gen))
print(next(gen))

Yes. For your mock test, you should know the difference between multitasking and multithreading and be able to write a simple practical program for both.

1. Multitasking ⭐⭐⭐

Multitasking means performing multiple tasks seemingly at the same time.

In Python, multitasking can be achieved using:

Multiple processes → multiprocessing
Multiple threads → threading
Simple example

Imagine:

Task 1 → Download a file
Task 2 → Read a file
Task 3 → Process data

These are different tasks.

2. Multithreading ⭐⭐⭐⭐⭐

Multithreading means running multiple threads within the same process.

Example:

Process
│
├── Thread 1 → Task 1
├── Thread 2 → Task 2
└── Thread 3 → Task 3
Practical example
import threading
import time


def task1():
    for i in range(3):
        print("Task 1:", i)
        time.sleep(1)




def task2():
    for i in range(3):
        print("Task 2:", i)
        time.sleep(1)




t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)


t1.start()
t2.start()


t1.join()
t2.join()


print("All tasks completed")

You may see output like:

Task 1: 0
Task 2: 0
Task 1: 1
Task 2: 1
Task 1: 2
Task 2: 2
All tasks completed

The exact order can vary.

3. Multitasking Using Processes ⭐⭐⭐⭐

If they ask you specifically to demonstrate multitasking using multiple processes, use multiprocessing.

from multiprocessing import Process
import time


def task1():
    for i in range(3):
        print("Task 1:", i)
        time.sleep(1)




def task2():
    for i in range(3):
        print("Task 2:", i)
        time.sleep(1)




p1 = Process(target=task1)
p2 = Process(target=task2)


p1.start()
p2.start()


p1.join()
p2.join()


print("All processes completed")

Here:

Process 1 → Task 1
Process 2 → Task 2
4. Multitasking vs Multithreading ⭐⭐⭐⭐⭐

This is very important for your mock test.

Multitasking	Multithreading
Multiple tasks are handled	Multiple threads execute within a process
Can use processes or threads	Specifically uses threads
Processes have separate memory	Threads share process memory
Processes are heavier	Threads are lightweight
multiprocessing can be used	threading is used
Better for CPU-bound work with processes	Often useful for I/O-bound work
Easy way to remember

Multitasking = multiple tasks

Task A
Task B
Task C

Multithreading = multiple threads

One Process
   ↓
Thread 1
Thread 2
Thread 3
5. Real-Time Multithreading Example ⭐⭐⭐⭐⭐

Suppose you need to:

Download File 1
Download File 2
Download File 3

Instead of waiting for each one sequentially, you can use threads.

import threading
import time


def download(file):
    print("Downloading", file)


    time.sleep(2)


    print("Downloaded", file)




files = ["file1", "file2", "file3"]


threads = []


for file in files:
    t = threading.Thread(target=download, args=(file,))
    threads.append(t)
    t.start()


for t in threads:
    t.join()


print("All downloads completed")
Why threading?

Downloading is an I/O-bound task, so threads are commonly useful.

6. Sequential vs Multithreading ⭐⭐⭐⭐⭐

This is a good practical question.

Sequential execution
import time


def task(name):
    print("Starting", name)
    time.sleep(2)
    print("Completed", name)




start = time.time()


task("Task 1")
task("Task 2")


end = time.time()


print("Time:", end - start)

Approximately:

4 seconds

because Task 2 starts after Task 1 finishes.

Multithreading
import threading
import time


def task(name):
    print("Starting", name)
    time.sleep(2)
    print("Completed", name)




start = time.time()


t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))


t1.start()
t2.start()


t1.join()
t2.join()


end = time.time()


print("Time:", end - start)

The tasks can overlap, so the elapsed time can be around 2 seconds rather than 4, though actual timing varies.

🔥 7. Most Important Mock Question
Question:

Create 3 threads to perform 3 different tasks simultaneously.

import threading


def task1():
    print("Reading data")




def task2():
    print("Processing data")




def task3():
    print("Writing data")




t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()


print("All tasks completed")

This covers:

Multitasking
Multithreading
Thread()
start()
join()
🚨 What to Study Before Your Mock

Prioritize these:

🔴 Must know
What is multitasking?
What is multithreading?
Difference between multitasking and multithreading
Create a thread
start()
join()
Passing arguments using args
Creating multiple threads
is_alive()
Lock and synchronization
🧠 One-line revision

Multitasking = handling multiple tasks.

Multithreading = executing multiple threads within one process.

start() = starts a thread.

join() = waits for a thread to finish.

Threads share memory; processes have separate memory.

For Python specifically, remember that threads are especially useful for I/O-bound work, while multiprocessing is generally preferred for CPU-bound parallelism because of Python's GIL.

give me codes

Sure. For your mock test, practice these codes directly. I’m giving you the most important practical programs for multitasking and multithreading.

1. Basic Multithreading ⭐⭐⭐⭐⭐
import threading


def task1():
    print("Task 1 is running")




def task2():
    print("Task 2 is running")




t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)


t1.start()
t2.start()


t1.join()
t2.join()


print("All tasks completed")
2. Multithreading with Arguments ⭐⭐⭐⭐⭐
import threading


def greet(name):
    print("Hello", name)




t1 = threading.Thread(target=greet, args=("Harika",))
t2 = threading.Thread(target=greet, args=("Rahul",))


t1.start()
t2.start()


t1.join()
t2.join()
3. Multiple Threads Using Loop ⭐⭐⭐⭐⭐
import threading


def task(number):
    print("Thread", number, "is running")




threads = []


for i in range(5):
    t = threading.Thread(target=task, args=(i,))
    threads.append(t)
    t.start()


for t in threads:
    t.join()


print("All threads completed")
4. Multithreading with sleep() ⭐⭐⭐⭐⭐
import threading
import time


def task(name):
    for i in range(3):
        print(name, i)
        time.sleep(1)




t1 = threading.Thread(target=task, args=("Thread 1",))
t2 = threading.Thread(target=task, args=("Thread 2",))


t1.start()
t2.start()


t1.join()
t2.join()


print("Completed")

The output order can vary because both threads are running concurrently.

5. Check Thread Status — is_alive() ⭐⭐⭐
import threading
import time


def task():
    time.sleep(2)
    print("Task completed")




t = threading.Thread(target=task)


print("Before start:", t.is_alive())


t.start()


print("After start:", t.is_alive())


t.join()


print("After join:", t.is_alive())

Typically:

Before start: False
After start: True
Task completed
After join: False
6. Get Current Thread Name ⭐⭐⭐
import threading


def task():
    print("Current thread:", threading.current_thread().name)




t1 = threading.Thread(target=task, name="Worker-1")
t2 = threading.Thread(target=task, name="Worker-2")


t1.start()
t2.start()


t1.join()
t2.join()
🔥 7. Multithreading — Shared Counter + Lock ⭐⭐⭐⭐⭐

This is very important.

import threading


counter = 0


lock = threading.Lock()




def increment():
    global counter


    for i in range(10000):
        with lock:
            counter += 1




t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)


t1.start()
t2.start()


t1.join()
t2.join()


print("Final counter:", counter)

Output:

Final counter: 20000
Why Lock?

Both threads are accessing the same:

counter

The lock ensures that only one thread modifies it at a time.

🔥 8. Multitasking Using Multiple Processes ⭐⭐⭐⭐⭐

If they ask you to demonstrate multitasking using processes, use multiprocessing.

from multiprocessing import Process


def task1():
    print("Task 1 is running")




def task2():
    print("Task 2 is running")




p1 = Process(target=task1)
p2 = Process(target=task2)


p1.start()
p2.start()


p1.join()
p2.join()


print("All processes completed")
9. Multiple Processes with Arguments
from multiprocessing import Process


def square(n):
    print("Square of", n, "=", n * n)




p1 = Process(target=square, args=(5,))
p2 = Process(target=square, args=(10,))
p3 = Process(target=square, args=(15,))


p1.start()
p2.start()
p3.start()


p1.join()
p2.join()
p3.join()

Output:

Square of 5 = 25
Square of 10 = 100
Square of 15 = 225
🔥 10. Three Different Tasks Using Threads ⭐⭐⭐⭐⭐
import threading
import time


def read_data():
    print("Reading data...")
    time.sleep(2)
    print("Reading completed")




def process_data():
    print("Processing data...")
    time.sleep(2)
    print("Processing completed")




def save_data():
    print("Saving data...")
    time.sleep(2)
    print("Saving completed")




t1 = threading.Thread(target=read_data)
t2 = threading.Thread(target=process_data)
t3 = threading.Thread(target=save_data)


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()


print("All tasks completed")
🔥 11. Sequential vs Multithreading ⭐⭐⭐⭐⭐
Sequential
import time


def task(name):
    print("Starting", name)
    time.sleep(2)
    print("Completed", name)




start = time.time()


task("Task 1")
task("Task 2")


end = time.time()


print("Time taken:", end - start)
Multithreading
import threading
import time


def task(name):
    print("Starting", name)
    time.sleep(2)
    print("Completed", name)




start = time.time()


t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))


t1.start()
t2.start()


t1.join()
t2.join()


end = time.time()


print("Time taken:", end - start)

The threaded version can finish significantly faster for this I/O-like sleep() workload because the waits overlap.

🚨 Practice These 5 First

If you don't have much time before your mock test:

1. Basic thread
threading.Thread(target=function)
2. Thread with arguments
threading.Thread(target=function, args=(value,))
3. Multiple threads using a loop
4. ⭐ Shared variable + Lock
5. ⭐ Multiple processes using Process

The start() + join() + args + Lock combination is the most important practical pattern to be comfortable writing from memory.

patterns,reverse of string and numbers in functions,

Absolutely. Since this is for your Python mock test, here are the most important practical programs for patterns + reverse of strings + reverse of numbers using functions.

🔥 1. Reverse a String Using Function ⭐⭐⭐⭐⭐
Q1. Reverse a string
def reverse_string(s):
    return s[::-1]




print(reverse_string("python"))

Output:

nohtyp
Without slicing — important for practical tests:
def reverse_string(s):
    rev = ""


    for char in s:
        rev = char + rev


    return rev




print(reverse_string("python"))
🔥 2. Reverse a Number Using Function ⭐⭐⭐⭐⭐
def reverse_number(n):
    rev = 0


    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10


    return rev




print(reverse_number(12345))

Output:

54321
Understand:

For 123:

digit = 3 → rev = 3
digit = 2 → rev = 32
digit = 1 → rev = 321
🔥 3. Check Palindrome String ⭐⭐⭐⭐⭐
def is_palindrome(s):
    return s == s[::-1]




print(is_palindrome("madam"))
print(is_palindrome("python"))

Output:

True
False
🔥 4. Check Palindrome Number ⭐⭐⭐⭐⭐
def is_palindrome(n):
    original = n
    rev = 0


    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10


    return original == rev




print(is_palindrome(121))
print(is_palindrome(123))

Output:

True
False
🔥 5. Reverse Words in a String ⭐⭐⭐⭐
def reverse_words(s):
    words = s.split()
    return " ".join(words[::-1])




print(reverse_words("I am learning Python"))

Output:

Python learning am I
🔥 6. Reverse Each Word ⭐⭐⭐⭐
def reverse_each_word(s):
    words = s.split()


    result = []


    for word in words:
        result.append(word[::-1])


    return " ".join(result)




print(reverse_each_word("I love Python"))

Output:

I evol nohtyP
🔥 PATTERNS USING FUNCTIONS
# 7. Square Star Pattern 
