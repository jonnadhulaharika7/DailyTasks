class Student:
    def display(self):
        print("I am a student")
s1 = Student()
s1.display()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
s1 = Student("Harika", 22)
s1.display()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(self.name, self.salary)
e1 = Employee("Harika", 50000)
e2 = Employee("Rahul", 60000)      
e1.display()
e2.display()

class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
d = Dog()
d.eat()
d.bark()

class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
c = Car()
c.start()
c.drive()



# Create a Student class
class student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("course:",self.course)
student = student("Harika",22,"Python")
student.display()

# Instance Variables
class student:
    def __init__(self,name,emp_id,salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    def display(self):
        print("name:",self.name)
        print("emp_id:",self.emp_id)
        print("salary:",self.salary)
student1 = student("Harika",101,70000)
student2 = student("Haru",102,80000)
student3 = student("Har",103,90000)
student1.display()
student2.display()
student3.display()

# Class Variables (shared by all object of that class)
class storeitem():
    discount_percentage = 10
item1 = storeitem()
item2 = storeitem()
print(f"item1 discount:{item1.discount_percentage}%")
print(f"item2 discount: {item2.discount_percentage}%")
storeitem.discount_percentage = 25
print(f"item1 new discount:{item1.discount_percentage}%")
print(f"item2 new discount:{item2.discount_percentage}%")

# Instance variables (value is unique to that object)
class gameprofile:
    def __init__(self,username,level):
        self.username = username
        self.level = level
player1 = gameprofile("Harika",5)
player2 = gameprofile("Haru",6)
player1.level = 4
print(f"player1 : {player1.username} is at level {player1.level}")
print(f"player2 : {player2.username} is at level {player2.level}")

# create an Employee class where all employees belong to the same company.
class employee:
    company = "ABC Technologies"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)
        print("company:",employee.company)
employee1 = employee("Harika",90000)
employee2 = employee("Haru",80000)
employee1.display()
employee2.display()

# Constructor
class bankaccount:
    def __init__(self,name,account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount
    def display(self):
        print("name:",self.name)
        print("account_number:",self.account_number)
        print("balance:",self.balance)
account1 = bankaccount("Harika",12345)
account1.deposit(5000)
account1.display()

# Create a Product class with:
# product name
# price
# quantity
# Create a method that calculates the total price.
class product:
    def __init__(self,productname,price,quantity):
        self.productname = productname
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price * self.quantity
product = product("laptop",50000,2)
print(product.total_price())

# Create a Patient class with:
# patient name
# age
# disease
# Create two patient objects and display their details.
class patient:
    def __init__(self,patientname,age,disease):
        self.patientname = patientname
        self.age = age
        self.disease = disease
    def display(self):
        print("patientname:",self.patientname)
        print("age:",self.age)
        print("disease:",self.disease)
p1 = patient("Harika",20,"Fever")
p2 = patient("Haru",20,"Cold")
p1.display()
p2.display()

# Class Variable + Instance Variable
# Create a Student class where:
# school_name is common for all students.
# name and marks are different for every student.
class student:
    school_name = "ABC school"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("name:",self.name)
        print("marks:",self.marks)
        print("school_name:",student.school_name)
student1 = student("Haru",95)
student2 = student("Harika",98)
student1.display()
student2.display()

# Constructor + Calculation
# Create a Rectangle class with length and width.
# Calculate:
# area
# perimeter
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
r = Rectangle(10,5)
print("area:",r.area())
print("perimeter:",r.perimeter())
        
# Single Inheritance 
# Create an Employee class with a method login().
# Create a Developer class that inherits from Employee.
# Add a write_code() method to Developer.
class Employee:
    def login(self):
        print("Employee logged in")
class Developer(Employee):
    def write_code(self):
        print("Developer is writing code")
developer = Developer()
developer.login()
developer.write_code()

# Single Inheritance + Constructor
# Create a Person class that accepts:
# name
# age
# Create an Employee child class that additionally accepts:
# employee ID
# salary
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Employee(person):
    def __init__(self,name,age,employeeID,salary):
        super().__init__(name,age)
        self.employeeID = employeeID
        self.salary = salary
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("employeeID:",self.employeeID)
        print("salary:",self.salary)
e = Employee("Harika",20,101,100000)
e.display()

# Multilevel Inheritance 
# Create:
# Company
#    ↓
# Employee
#    ↓
# Developer
# Each class should have one method.
class Company:
    def Company_details(self):
        print("ABC Technologies")
class Employee(Company):
    def Employee_details(self):
        print("Employee works in this company")
class Developer(Employee):
    def Developer_details(self):
        print("Developer writes code")
d = Developer()
d.Company_details()
d.Employee_details()
d.Developer_details()

# Multilevel Inheritance + Constructor
# Create:
# Person
#    ↓
# Employee
#    ↓
# Manager
# Store:
# Person → name
# Employee → employee ID
# Manager → department
class Person:
    def __init__(self,name):
        self.name = name
class Employee(Person):
    def __init__(self,name,employeeID):
        super().__init__(name)
        self.employeeID = employeeID
class Manager(Employee):
    def __init__(self,name,employeeID,department):
        super().__init__(name,employeeID)
        self.department = department
    def display(self):
        print("name:",self.name)
        print("employeeID:",self.employeeID)
        print("department:",self.department)
M = Manager("Harika",101,"Data Engineering")
M.display()

# Multiple Inheritance
# Create:
# Python
# AWS
#    ↓
# DataEngineer
# Python should contain a Python skill.
# AWS should contain an AWS skill.
# DataEngineer should inherit both.
class Python:
    def python_skill(self):
        print("Knows Python")
class AWS:
    def AWS_skill(self):
        print("Knows AWS")
class DataEngineer(Python, AWS):
    def data_engineer(self):
        print("Works as DataEngineer")  
D = DataEngineer()
D.python_skill()
D.AWS_skill()
D.data_engineer()

# Hierarchical Inheritance
# Create a Vehicle parent.
# Create:
# Car
# Bike
# Bus
# All should inherit from Vehicle.
class Vehicle:
    def start(self):
        print("vehicle started")
class Car(Vehicle):
    def drive(self):
        print("car is driving")
class Bike(Vehicle):
    def ride(self):
        print("bike is riding")
class Bus(Vehicle):
    def transport(self):
        print("bus is transport for passengers")
bus = Bus()
bike = Bike()
car = Car()

bus.start()
bus.transport()

bike.start()
bike.ride()

car.start()
car.drive()

# Polymorphism
# Create three classes:
# UPI
# Card
# Cash
# Each should have the same method:pay()
class UPI:
    def pay(self):
        print("payment made using UPI")
class Card:
    def pay(self):
        print("payment made using card")
class Cash:
    def pay(self):
        print("payemnt made using cash")
upi = UPI()
card = Card()
cash = Cash()
upi.pay()
card.pay()
cash.pay()

# Polymorphism
# Create:
# Developer
# Tester
# Manager
# Each should have a work() method.
class Developer:
    def work(self):
        print("Developer writes code")
class Tester:
    def work(self):
        print("Tester tests the code")
class Manager:
    def work(self):
        print("Manager manages the team")
manager = Manager()
tester = Tester()
developer = Developer()
manager.work()
tester.work()
developer.work()

# Change Class Variable
# Create an Employee class with:
# company = "ABC"
# Create two employees.
# Create a class method change_company() that changes the company name.
class Employee:
    company = "ABC"
    def __init__(self,name):
        self.name = name
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
    def display(self):
        print("name:",self.name)
        print("company:",self.company)
e1 = Employee("Harika")
e2 = Employee("Haru")
e1.display()
e2.display()
Employee.change_company("XYZ")
e1.display()
e2.display()    

# Instance Variable vs Class Variable
class Employee:
    company = "ABC"
    def __init__(self,name):
        self.name = name
    def display(self):
        print("name:",self.name)
        print("company:",Employee.company)
e1 = Employee("Harika")
e2 = Employee("Haru")
e1.display()
e2.display()

# Static Method
# Create a Calculator class with static methods:
# add()
# subtract()
# multiply()
class calculator:
    @staticmethod
    def add(a,b):
        return a + b
    @staticmethod
    def subtract(a,b):
        return a - b
    @staticmethod
    def multiply(a,b):
        return a * b
print(calculator.add(10,5))
print(calculator.subtract(10,5))
print(calculator.multiply(10,5))

