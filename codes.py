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

# Square Star Pattern
def square_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end = " ")
        print()
square_pattern(5)

# Right Triangle
def right_triangle(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end = " ")
        print()
right_triangle(5)

# Inverted Triangle
def inverted_triangle(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end = " ")
        print()
inverted_triangle(5)

# Number Triangle
def number_triangle(n):
    for i in range(1,n+1):
        for  j in range(1,i+1):
            print(j,end = "")
        print()
number_triangle(5)

# Repeated Number Triangle
def repeated_number(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end = "")
        print()
repeated_number(5)

# Adding values to tuples
# d = (1,2,3)
# lst = list(d)
# lst.append(4)
# d = tuple(lst)
# print(d)

# Inverted Number Pattern
def inverted_numbers(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end = "")
        print()
inverted_numbers(5)