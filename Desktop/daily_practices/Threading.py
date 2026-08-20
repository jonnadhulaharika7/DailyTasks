# Create a thread that prints numbers from 1 to 5.
import threading
def print_numbers():
    for i in range(1,6):
        print(i)
t = threading.Thread(target = print_numbers)
t.start()
t.join()
print("Main thread completed")

# Create two threads. One should print numbers and another should print letters.
import threading
def print_numbers():
    for i in range(1,7):
        print("number:", i)
def characters():
    for ch in "Harika":
        print("letters:", ch)
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = characters)
t1.start()
t1.join()
t2.start()
t2.join()
print("Main thread complete")

# What happens if we don't use join()?
import threading
import time
def task():
    for i in range(1,6):
        time.sleep(2)
        print(i)
t = threading.Thread(target = task)
t.start()
print("Main completed")

# Create a thread that accepts two numbers and prints their sum.
import threading
def add(a,b):
    print("sum:",a + b)
t = threading.Thread(target = add, args = (10,20))
t.start()
t.join()

# Find the current thread name
import threading
def task():
    print("current thread:", threading.current_thread().name)
t = threading.Thread(target = task, name = "Worker-1")
t.start()
t.join()   

# Check whether a thread is still running.
import threading 
import time
def task():
    time.sleep(3)
    print("Thread completed")
t = threading.Thread(target = task)
t.start
print("Alive:",t.is_alive())
t.join
print("Alive:",t.is_alive())

# Write a Python program to create a thread.
import threading
def task():
    print("Task completed")
t = threading.Thread(target = task)
t.start()
t.join()

# Create two threads that execute two different functions
import threading
def numbers():
    for i in range(1,6):
        print("numbers:", i)
def characters():
    for ch in "Harika":
        print("characters:",ch)
t1 = threading.Thread(target = numbers)
t2 = threading.Thread(target = characters)
t1.start()
t1.join()

t2.start()
t2.join()

