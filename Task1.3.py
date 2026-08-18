# Write a loop that prints numbers from 1 to 10, but stops completely when the number is 6.
for i in range(1, 11):
    if i == 6:
        break
    print(i)
    
# Write a loop that prints numbers from 1 to 10, but skips printing the number 5.
for i in range (1, 11):
    if i == 5:
        continue
    print(i)

# Write a loop that prints only odd numbers between 1 and 10 using continue.
for i in range (1, 11):
    if i % 2 == 0:
        continue
    print(i)
    
# Write a loop that prints numbers from 1 to 20, but breaks when the number is divisible by 7.
for i in range(1, 21):
    if i % 7 == 0:
        break
    print(i)
    
# Write a loop that prints numbers from 1 to 10, but skips all even numbers.
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
    
# Write a loop that prints numbers from 1 to 10, but stops when the number is greater than 8.
for i in range(1, 11):
    if i > 8:
        break
    print(i)
    
# Write a loop that prints numbers from 1 to 15, but skips numbers divisible by 3.
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)
    
# Write a loop that prints numbers from 1 to 10, but breaks when the number is equal to 4.
for i in range(1, 11):
    if i == 4:
        break
    print(i)
    
# Write a loop that prints numbers from 1 to 10, but skips printing 2 and 7.
for i in range (1, 11):
    if i == 2 or i == 7:
        continue
    print(i)
    
# Write a loop that prints numbers from 1 to 10, but breaks when the number is 9.
for i in range(1, 11):
    if i == 9:
        break
    print(i)
    
# Write a program that checks if a number is even or odd using a ternary operator.
num = 8
result = "Even" if num % 2 == 0 else "Odd"
print(result)

# Write a program that prints "Positive" if a number is greater than 0, otherwise "Negative or Zero".
num = 7
result = "Positive" if num > 0 else "Negative or zero"
print(result)

# Write a program that prints "Adult" if age ≥ 18, otherwise "Minor"
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)

# Write a program that prints "Pass" if marks ≥ 40, otherwise "Fail"
marks = 90
result = "Pass" if marks >= 40 else "Fail"
print(result)

# Write a program that prints "Big" if a number > 100, otherwise "Small".
num = 150
result = "Big" if num > 100 else "Small"
print(result)

# Write a program that prints "Equal" if two numbers are the same, otherwise "Not Equal".
num1 = 7
num2 = 13
result = "Equal" if num1 == num2 else "Not equal"
print(result)

# Write a program that prints "Divisible by 5" if a number is divisible by 5, otherwise "Not Divisible".
num = 20
result = "Divisible by 5" if num % 5 == 0 else "Not Divisible"
print(result)

# Write a program that prints "Leap Year" if a year is divisible by 4, otherwise "Not Leap Year".
year = 2024
result = "Leap year" if year % 4 == 0 else "Not leap year"
print(result)

# Write a program that prints "Yes" if a number is positive, otherwise "No".
num = -7
result = "yes" if num >= 0 else "No"
print(result)

# Write a program that prints "First" if a > b, otherwise "Second".
a = 6
b = 10
result = "First" if a > b  else "Second"
print(result)

# Write a function add_numbers(a, b) that returns the sum of two numbers. Call it with add_numbers(3, 5).
def add_numbers(a, b):
    return a + b
result = add_numbers(3, 5)
print(result)

# Create a function multiply(x, y) that multiplies two numbers. Call it with positional arguments.
def multiply(X, Y):
    return X * Y
result = multiply(5, 2)
print(result)

# Define a function greet(name) that prints "Hello, <name>!". Call it with "Alice".
def greet(name):
    print(f"Hello {name}!")
greet("Alice")

# Write a function power(base, exponent) that returns base ** exponent. Call it with power(2, 3).
def function_power(base, exponent):
    return base ** exponent
result = function_power(2, 3)
print(result)

# Create a function area_rectangle(length, width) that returns the area. Call it with area_rectangle(10, 5).
def area_rectangle(length, width):
    return length * width
result = area_rectangle(10, 5)
print(result)

# Modify greet(name) to accept a keyword argument. Call it as greet(name="Bob").
def greet(name):
    print(name)
greet(name = "Bob")

# Write a function introduce(name, age) that prints "My name is <name> and I am <age> years old." Call it using keyword arguments.
def introduce(name, age):
    print(f"My name is {name} I am {age} years old")
introduce(name = "Haru", age = 20)

# Create a function calculate_price(item, price) and call it with keyword arguments.
def calculate_price(item, price):
    total = price
    print(f"Item {item} price total is {total}")
calculate_price(item = "Laptop", price = 60000)

# Write a function student_info(name, grade) and call it as student_info(grade="A", name="John").
def student_info(name, grade):
    print(f"grade {grade} and my name is {name}")
student_info(grade = "A", name = "John")

# Define book_details(title, author) and call it using keyword arguments.
def book_details(title, author):
    print(f"Book title is {title} and the author is {author}")
book_details(title = "Python", author = "van rossum")

# Write a function greet(name="Guest") that prints "Hello, <name>!". Call it without passing a name.
def greet (name = "Haru"):
    print(f"Hello, {name}!")
greet()

# Create a function discount(price, percent=10) that applies a discount. Call it with and without the percent.
def discount(price, percent=10):
    return price - (price * percent / 100)
print(discount(100))
print(discount(100, 20))

# Define welcome_message(message="Welcome to Python!"). Call it without arguments.
def welcome_message(message = "welcome to python!"):
    print(f"welcome_message, {message}")
welcome_message()

# Write a function circle_area(radius, pi=3.14) that calculates area. Call it with only radius.
def circle_area(radius, pi=3.14):
    return pi * radius * radius
result = circle_area(5)
print(result)

# Create print_date(day, month="March", year=2026) and call it with just day.
def print_date(day, month="March", year=2026):
    print(day, month, year)
print_date(19)

# Write order_food(item, quantity=1) and call it with order_food("Pizza").
def order_food(item, quantity=1):
    print(f"item {item}, quantity=1")
order_food("Pizza")

# Create travel(destination, days=7) and call it with travel("Paris", days=10).
def travel(destination, days=7):
    print(f"destination {destination}, days {days}")
travel("Paris", days=10)

# Define movie_ticket(movie, price=200, seat="Regular"). Call it with positional and keyword arguments.
def movie_ticket(movie, price=200, seat="Regular"):
   print(f"movie: {movie}")
   print(f"price: {price}")
   print(f"seat: {seat}")
movie_ticket("Hii Nanna") # positional arguments
movie_ticket(movie = "Kushi", price=300, seat="Premium") # Keyword arguments

# Write exam_score(student, subject="Math", score=100) and call it with mixed arguments.
def exam_score(student, subject="Math", score=100):
    print(f"student: {student}")
    print(f"subject: {subject}")
    print(f"score: {score}")
exam_score("Haru", score=90, subject="English")

# Create car_rental(car, days=5, insurance=True) and call it with both positional and keyword arguments.
def car_rental(car, days=5, insurance=True):
    print(f"car : {car}")
    print(f"days: {days}")
    print(f"insurance: {insurance}")
car_rental("Hyundai") # positional arguments
car_rental(car="Audi", days=10, insurance=True)

# Write a function sum_all(*args) that returns the sum of all numbers passed.
def sum_all(a, b):
    return a + b
result = sum_all(10, 20)
print(result)

# Create print_names(*args) that prints all names given.
def print_names(*args):
    for name in args:
        print(name)
result = print_names("Harika", "Haru", "Har")

# Define multiply_all(*args) that multiplies all numbers.
def multiply_all(a, b, c):
    return a * b * c
result = multiply_all(5, 5, 2)
print(result)

# Write max_number(*args) that returns the largest number.
def max_number(*args):
    return max(args)
result = max_number(10, 20, 30)
print(result)

# Create average(*args) that calculates the average of numbers.
def average(*args):
    return sum(args) / len(args)
result = average(5, 5, 8)
print(result)    

# Write a function print_info(**kwargs) that prints all key-value pairs.
def print_info(**kwargs):
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
print_info(name = "Haru", age = 20, city = "Nellore")

# Create student_profile(**kwargs) that prints student details.
def student_profile(**kwargs):
    for name, subject, marks in kwargs.items():
        print(name, subject, marks)
print_info(name = "Haru", subject = "English", marks = 90)

# Define car_details(**kwargs) that prints car attributes.
def car_details(**kwargs):
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
car_details(brand = "Hyundai", year = 2000, color = "White")

# Write employee_data(**kwargs) that prints employee info.
def employee_data(**kwargs):
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
employee_data(name = "Haru", salary = 60000, department = "IT" )

# Create settings(**kwargs) that prints configuration settings.
def settings(**kwargs):
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
settings(theme = "dark", volume = "High", language = "English")

# Write mixed_function(*args, **kwargs) that prints both.
def mixed_function(*args, **kwargs):
    print("positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
mixed_function( 10 , 20, 30 , name = "Haru", marks = 90, subject = "English") 

# Create register_user(*args, **kwargs) that prints positional and keyword arguments.
def register_user(*args, **kwargs):
    print("positional arguments:")
    for arg in args:
        print(arg)
    print("keyword arguments:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
register_user(1, "Haru", "Developer", username = "Haru", email = "Haru@000" )

# Define shopping_cart(*args, **kwargs) that prints items and details.
def shopping_cart(*args, **kwargs):
    print("positional arguments:")
    for arg in args:
        print(arg)
    print("keyword arguments:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
shopping_cart("milk", "bread", "sugar", delivery = "Home", total = 760)
    
# Write event_details(*args, **kwargs) that prints event info.
def event_details(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("keyword arguments:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
event_details("harika", "haru", "har", event = "wedding", date = 10-10-2026)

# Create log_data(*args, **kwargs) that prints logs.
def log_data(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("keyword arguments:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
log_data("Error started", "Retry attempt", level="ERROR", time="10:30 AM", user="admin")
    
# Write a function calculate_total(price, quantity=1, tax=5) that returns total cost.
def calculate_total(price, quantity=1, tax=5):
    total = price * quantity
    total += total * (tax / 100)
    return total
print(calculate_total(100))

# Create greet_people(*args, greeting="Hello") that greets multiple people.
def greet_people(*args, greeting="Hello"):
    for name in args:
     print(f"{greeting}, {name}!")
greet_people("Harika", "Haru", "Har")

# Define student_report(name, *args, **kwargs) that prints name, subjects, and extra info.
def student_report(name, *args, **kwargs):
    print(f"name: {name}")
    print("/nsub:")
    for subs in args:
        print(subs)
    print("/nExtra info:")
    for keys, values in kwargs.items():
     print(f"{keys} : {values}")
student_report(
          "Haru",
          "English", "Maths", "Science",
           age = 16,
           grade = "A"
)

# Write recipe(ingredient1, ingredient2, *args, **kwargs) that prints recipe details.
def recipe(ingredient1, ingredient2, *args, **kwargs):
    print("main ingredients:")
    print(ingredient1)
    print(ingredient2)
    
    print("/n extra items:")
    for item in args:
        print(item)
    for keys, values in kwargs.items():
     print(f"{keys} : {values}")
recipe(
    "flour", "Maida",
    "sugar", "milk", "butter", "eggs",
     name = "cake",
     time = "45 min"
)

# Create bank_account(name, balance=0, **kwargs) that prints account info.
def bank_account(name, balance=0, **kwargs):
    print(f"account holder: {name}")
    print(f"balance: {balance}")
    print("/n other details:")
    for keys, values in kwargs.items():
     print(f"{keys} : {values}")
bank_account(
    "Haru",
    5000,
    age = 16,
    accounttype = "savings"
)
            
# Write flight_booking(destination, *args, **kwargs) that prints booking details
def flight_booking(destination, *args, **kwargs):
    print(f"destination : {destination}")
    if args:
     print("services:")
    for item in args:
        print(item)
    for keys, values in kwargs.items():
     print(f"{keys} : {values}")
flight_booking( destination = "tirumala", services = "window seat", passenger = "Haru", class_type = "business")

# Create hotel_reservation(name, nights=1, **kwargs) that prints reservation info.
def hotel_reservation(name, nights=1, **kwargs):
    print(f"name : {name}")
    print(f"nights : {nights}")
    for keys, values in kwargs.items():
     print(f"{keys} : {values}")
hotel_reservation(name = "Haru", nights = 1, amount = 3000, age = 16)

# Define order_summary(item, quantity=1, *args, **kwargs) that prints order details.
def order_summary(item, quantity=1, *args, **kwargs):
    print(f"item : {item}")
    print(f"quantity : {quantity}")
    for item in args:
        print(args)
    for keys, values in kwargs.items():
     print(f"{keys} : {values}")
order_summary(item = "rice", quantity = 1, price = 1000, total = 1000)

# Write game_score(player, *args, **kwargs) that prints scores.
def game_score(player, *args, **kwargs):
    print(f"player :{player}")
    if args:
        print("scores:")
        for scores in args:
            print(scores)
        for keys, values in kwargs.items():
         print(f"{keys} : {values}")
game_score("name", 10, 20, 30, status = "winner", game = "cricket")

# Create conference_registration(name, *args, **kwargs) that prints registration details.
def conference_registration(name, *args, **kwargs):
    print(f"name : {name}")
    print("sessions:")
    for sessions in args:
        print(sessions)
    for keys, values in kwargs.items():
         print(f"{keys} : {values}")
conference_registration("Haru", "AI workshop", fee = 4000, city = "Hyderabad")

# Write calculator(operation, *args) that performs sum, multiply, etc.
def calculator(operation, *args):
    if operation == "sum":
        result = sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result = result * num
    else:
        result = "Invalid operation"
    print(f"result : {result}")
calculator("sum", 10, 20, 30)
calculator("multiply", 3, 6, 1)

# Create profile(name, age, *args, **kwargs) that prints full profile.
def profile(name, age, *args, **kwargs):
    print(f"name : {name}")
    print(f"age : {age}")
    print("password:")
    for password in args:
        print(password)
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
profile("Haru", 20, "Haru0", email = "H@123")

# Define task_manager(task, priority="Medium", *args, **kwargs) that prints task details.
def  task_manager(task, priority="Medium", *args, **kwargs):
    print(f"task : {task}")
    print(f"priority : {priority}")
    print("Additional notes:")
    for note in args:
        print(note)
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
task_manager("complete python project", "Medium", "submit before friday", name = "Haru", status = "inprogress")

# Write music_playlist(*args, **kwargs) that prints songs and playlist info.
def music_playlist(*args, **kwargs):
    print("songs:")
    for songs in args:
        print(songs)
    print("playlist info:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
music_playlist("Raanjhanaa", "Anuvanuvuu", "Om namo bhagavate vasudevaya", total_songs = 3, creator = "Haru")

# Create smart_home(device, *args, **kwargs) that prints device settings.
def smart_home(device, *args, **kwargs):
    print(f"device : {device}")
    print("commands:")
    for commands in args:
        print(commands)
    print("device settings:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
smart_home("smart light", "turn on", room = "living room", status = "active" )





# Write a loop that prints numbers from 1 to 10, but stops completely when the number is 6.
for i in range(1, 11):
    if i == 6:
        break
    print(i)
    
# Write a loop that prints numbers from 1 to 10, but skips printing the number 5.
for i in range (1, 11):
    if i == 5:
        continue
    print(i)

# Write a loop that prints only odd numbers between 1 and 10 using continue.
for i in range (1, 11):
    if i % 2 == 0:
        continue
    print(i)
    
# Write a loop that prints numbers from 1 to 20, but breaks when the number is divisible by 7.
for i in range(1, 21):
    if i % 7 == 0:
        break
    print(i)
    
# Write a loop that prints numbers from 1 to 10, but skips all even numbers.
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
    
# Write a loop that prints numbers from 1 to 10, but stops when the number is greater than 8.
for i in range(1, 11):
    if i > 8:
        break
    print(i)
    
# Write a loop that prints numbers from 1 to 15, but skips numbers divisible by 3.
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)
    
# Write a loop that prints numbers from 1 to 10, but breaks when the number is equal to 4.
for i in range(1, 11):
    if i == 4:
        break
    print(i)
    
# Write a loop that prints numbers from 1 to 10, but skips printing 2 and 7.
for i in range (1, 11):
    if i == 2 or i == 7:
        continue
    print(i)
    
# Write a loop that prints numbers from 1 to 10, but breaks when the number is 9.
for i in range(1, 11):
    if i == 9:
        break
    print(i)
    
# Write a program that checks if a number is even or odd using a ternary operator.
num = 8
result = "Even" if num % 2 == 0 else "Odd"
print(result)

# Write a program that prints "Positive" if a number is greater than 0, otherwise "Negative or Zero".
num = 7
result = "Positive" if num > 0 else "Negative or zero"
print(result)

# Write a program that prints "Adult" if age ≥ 18, otherwise "Minor"
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)

# Write a program that prints "Pass" if marks ≥ 40, otherwise "Fail"
marks = 90
result = "Pass" if marks >= 40 else "Fail"
print(result)

# Write a program that prints "Big" if a number > 100, otherwise "Small".
num = 150
result = "Big" if num > 100 else "Small"
print(result)

# Write a program that prints "Equal" if two numbers are the same, otherwise "Not Equal".
num1 = 7
num2 = 13
result = "Equal" if num1 == num2 else "Not equal"
print(result)

# Write a program that prints "Divisible by 5" if a number is divisible by 5, otherwise "Not Divisible".
num = 20
result = "Divisible by 5" if num % 5 == 0 else "Not Divisible"
print(result)

# Write a program that prints "Leap Year" if a year is divisible by 4, otherwise "Not Leap Year".
year = 2024
result = "Leap year" if year % 4 == 0 else "Not leap year"
print(result)

# Write a program that prints "Yes" if a number is positive, otherwise "No".
num = -7
result = "yes" if num >= 0 else "No"
print(result)

# Write a program that prints "First" if a > b, otherwise "Second".
a = 6
b = 10
result = "First" if a > b  else "Second"
print(result)

# Write a function add_numbers(a, b) that returns the sum of two numbers. Call it with add_numbers(3, 5).
def add_numbers(a, b):
    return a + b
result = add_numbers(3, 5)
print(result)

# Create a function multiply(x, y) that multiplies two numbers. Call it with positional arguments.
def multiply(X, Y):
    return X * Y
result = multiply(5, 2)
print(result)

# Define a function greet(name) that prints "Hello, <name>!". Call it with "Alice".
def greet(name):
    print(f"Hello {name}!")
greet("Alice")

# Write a function power(base, exponent) that returns base ** exponent. Call it with power(2, 3).
def function_power(base, exponent):
    return base ** exponent
result = function_power(2, 3)
print(result)

# Create a function area_rectangle(length, width) that returns the area. Call it with area_rectangle(10, 5).
def area_rectangle(length, width):
    return length * width
result = area_rectangle(10, 5)
print(result)

# Modify greet(name) to accept a keyword argument. Call it as greet(name="Bob").
def greet(name):
    print(name)
greet(name = "Bob")

# Write a function introduce(name, age) that prints "My name is <name> and I am <age> years old." Call it using keyword arguments.
def introduce(name, age):
    print(f"My name is {name} I am {age} years old")
introduce(name = "Haru", age = 20)

# Create a function calculate_price(item, price) and call it with keyword arguments.
def calculate_price(item, price):
    total = price
    print(f"Item {item} price total is {total}")
calculate_price(item = "Laptop", price = 60000)

# Write a function student_info(name, grade) and call it as student_info(grade="A", name="John").
def student_info(name, grade):
    print(f"grade {grade} and my name is {name}")
student_info(grade = "A", name = "John")

# Define book_details(title, author) and call it using keyword arguments.
def book_details(title, author):
    print(f"Book title is {title} and the author is {author}")
book_details(title = "Python", author = "van rossum")

# Write a function greet(name="Guest") that prints "Hello, <name>!". Call it without passing a name.
def greet (name = "Haru"):
    print(f"Hello, {name}!")
greet()

# Create a function discount(price, percent=10) that applies a discount. Call it with and without the percent.
def discount(price, percent=10):
    return price - (price * percent / 100)
print(discount(100))
print(discount(100, 20))

# Define welcome_message(message="Welcome to Python!"). Call it without arguments.
def welcome_message(message = "welcome to python!"):
    print(f"welcome_message, {message}")
welcome_message()

# Write a function circle_area(radius, pi=3.14) that calculates area. Call it with only radius.
def circle_area(radius, pi=3.14):
    return pi * radius * radius
result = circle_area(5)
print(result)

# Create print_date(day, month="March", year=2026) and call it with just day.
def print_date(day, month="March", year=2026):
    print(day, month, year)
print_date(19)

# Write order_food(item, quantity=1) and call it with order_food("Pizza").
def order_food(item, quantity=1):
    print(f"item {item}, quantity=1")
order_food("Pizza")

# Create travel(destination, days=7) and call it with travel("Paris", days=10).
def travel(destination, days=7):
    print(f"destination {destination}, days {days}")
travel("Paris", days=10)

# Define movie_ticket(movie, price=200, seat="Regular"). Call it with positional and keyword arguments.
def movie_ticket(movie, price=200, seat="Regular"):
   print(f"movie: {movie}")
   print(f"price: {price}")
   print(f"seat: {seat}")
movie_ticket("Hii Nanna") # positional arguments
movie_ticket(movie = "Kushi", price=300, seat="Premium") # Keyword arguments

# Write exam_score(student, subject="Math", score=100) and call it with mixed arguments.
def exam_score(student, subject="Math", score=100):
    print(f"student: {student}")
    print(f"subject: {subject}")
    print(f"score: {score}")
exam_score("Haru", score=90, subject="English")

# Create car_rental(car, days=5, insurance=True) and call it with both positional and keyword arguments.
def car_rental(car, days=5, insurance=True):
    print(f"car : {car}")
    print(f"days: {days}")
    print(f"insurance: {insurance}")
car_rental("Hyundai") # positional arguments
car_rental(car="Audi", days=10, insurance=True)

# Write a function sum_all(*args) that returns the sum of all numbers passed.
def sum_all(a, b):
    return a + b
result = sum_all(10, 20)
print(result)

# Create print_names(*args) that prints all names given.
def print_names(*args):
    for name in args:
        print(name)
result = print_names("Harika", "Haru", "Har")

# Define multiply_all(*args) that multiplies all numbers.
def multiply_all(a, b, c):
    return a * b * c
result = multiply_all(5, 5, 2)
print(result)

# Write max_number(*args) that returns the largest number.
def max_number(*args):
    return max(args)
result = max_number(10, 20, 30)
print(result)

# Create average(*args) that calculates the average of numbers.
def average(*args):
    return sum(args) / len(args)
result = average(5, 5, 8)
print(result)    

# Write a function print_info(**kwargs) that prints all key-value pairs.
def print_info(**kwargs):
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
print_info(name = "Haru", age = 20, city = "Nellore")

# Create student_profile(**kwargs) that prints student details.
def student_profile(**kwargs):
    for name, subject, marks in kwargs.items():
        print(name, subject, marks)
print_info(name = "Haru", subject = "English", marks = 90)

# Define car_details(**kwargs) that prints car attributes.
def car_details(**kwargs):
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
car_details(brand = "Hyundai", year = 2000, color = "White")

# Write employee_data(**kwargs) that prints employee info.
def employee_data(**kwargs):
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
employee_data(name = "Haru", salary = 60000, department = "IT" )

# Create settings(**kwargs) that prints configuration settings.
def settings(**kwargs):
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
settings(theme = "dark", volume = "High", language = "English")

# Write mixed_function(*args, **kwargs) that prints both.
def mixed_function(*args, **kwargs):
    print("positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
mixed_function( 10 , 20, 30 , name = "Haru", marks = 90, subject = "English") 

# Create register_user(*args, **kwargs) that prints positional and keyword arguments.
def register_user(*args, **kwargs):
    print("positional arguments:")
    for arg in args:
        print(arg)
    print("keyword arguments:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
register_user(1, "Haru", "Developer", username = "Haru", email = "Haru@000" )

# Define shopping_cart(*args, **kwargs) that prints items and details.
def shopping_cart(*args, **kwargs):
    print("positional arguments:")
    for arg in args:
        print(arg)
    print("keyword arguments:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
shopping_cart("milk", "bread", "sugar", delivery = "Home", total = 760)
    
# Write event_details(*args, **kwargs) that prints event info.
def event_details(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("keyword arguments:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
event_details("harika", "haru", "har", event = "wedding", date = 10-10-2026)

# Create log_data(*args, **kwargs) that prints logs.
def log_data(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("keyword arguments:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
log_data("Error started", "Retry attempt", level="ERROR", time="10:30 AM", user="admin")
    
# Write a function calculate_total(price, quantity=1, tax=5) that returns total cost.
def calculate_total(price, quantity=1, tax=5):
    total = price * quantity
    total += total * (tax / 100)
    return total
print(calculate_total(100))

# Create greet_people(*args, greeting="Hello") that greets multiple people.
def greet_people(*args, greeting="Hello"):
    for name in args:
     print(f"{greeting}, {name}!")
greet_people("Harika", "Haru", "Har")

# Define student_report(name, *args, **kwargs) that prints name, subjects, and extra info.
def student_report(name, *args, **kwargs):
    print(f"name: {name}")
    print("/nsub:")
    for subs in args:
        print(subs)
    print("/nExtra info:")
    for keys, values in kwargs.items():
     print(f"{keys} : {values}")
student_report(
          "Haru",
          "English", "Maths", "Science",
           age = 16,
           grade = "A"
)

# Write recipe(ingredient1, ingredient2, *args, **kwargs) that prints recipe details.
def recipe(ingredient1, ingredient2, *args, **kwargs):
    print("main ingredients:")
    print(ingredient1)
    print(ingredient2)
    
    print("/n extra items:")
    for item in args:
        print(item)
    for keys, values in kwargs.items():
     print(f"{keys} : {values}")
recipe(
    "flour", "Maida",
    "sugar", "milk", "butter", "eggs",
     name = "cake",
     time = "45 min"
)

# Create bank_account(name, balance=0, **kwargs) that prints account info.
def bank_account(name, balance=0, **kwargs):
    print(f"account holder: {name}")
    print(f"balance: {balance}")
    print("/n other details:")
    for keys, values in kwargs.items():
     print(f"{keys} : {values}")
bank_account(
    "Haru",
    5000,
    age = 16,
    accounttype = "savings"
)
            
# Write flight_booking(destination, *args, **kwargs) that prints booking details
def flight_booking(destination, *args, **kwargs):
    print(f"destination : {destination}")
    if args:
     print("services:")
    for item in args:
        print(item)
    for keys, values in kwargs.items():
     print(f"{keys} : {values}")
flight_booking( destination = "tirumala", services = "window seat", passenger = "Haru", class_type = "business")

# Create hotel_reservation(name, nights=1, **kwargs) that prints reservation info.
def hotel_reservation(name, nights=1, **kwargs):
    print(f"name : {name}")
    print(f"nights : {nights}")
    for keys, values in kwargs.items():
     print(f"{keys} : {values}")
hotel_reservation(name = "Haru", nights = 1, amount = 3000, age = 16)

# Define order_summary(item, quantity=1, *args, **kwargs) that prints order details.
def order_summary(item, quantity=1, *args, **kwargs):
    print(f"item : {item}")
    print(f"quantity : {quantity}")
    for item in args:
        print(args)
    for keys, values in kwargs.items():
     print(f"{keys} : {values}")
order_summary(item = "rice", quantity = 1, price = 1000, total = 1000)

# Write game_score(player, *args, **kwargs) that prints scores.
def game_score(player, *args, **kwargs):
    print(f"player :{player}")
    if args:
        print("scores:")
        for scores in args:
            print(scores)
        for keys, values in kwargs.items():
         print(f"{keys} : {values}")
game_score("name", 10, 20, 30, status = "winner", game = "cricket")

# Create conference_registration(name, *args, **kwargs) that prints registration details.
def conference_registration(name, *args, **kwargs):
    print(f"name : {name}")
    print("sessions:")
    for sessions in args:
        print(sessions)
    for keys, values in kwargs.items():
         print(f"{keys} : {values}")
conference_registration("Haru", "AI workshop", fee = 4000, city = "Hyderabad")

# Write calculator(operation, *args) that performs sum, multiply, etc.
def calculator(operation, *args):
    if operation == "sum":
        result = sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result = result * num
    else:
        result = "Invalid operation"
    print(f"result : {result}")
calculator("sum", 10, 20, 30)
calculator("multiply", 3, 6, 1)

# Create profile(name, age, *args, **kwargs) that prints full profile.
def profile(name, age, *args, **kwargs):
    print(f"name : {name}")
    print(f"age : {age}")
    print("password:")
    for password in args:
        print(password)
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
profile("Haru", 20, "Haru0", email = "H@123")

# Define task_manager(task, priority="Medium", *args, **kwargs) that prints task details.
def  task_manager(task, priority="Medium", *args, **kwargs):
    print(f"task : {task}")
    print(f"priority : {priority}")
    print("Additional notes:")
    for note in args:
        print(note)
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
task_manager("complete python project", "Medium", "submit before friday", name = "Haru", status = "inprogress")

# Write music_playlist(*args, **kwargs) that prints songs and playlist info.
def music_playlist(*args, **kwargs):
    print("songs:")
    for songs in args:
        print(songs)
    print("playlist info:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
music_playlist("Raanjhanaa", "Anuvanuvuu", "Om namo bhagavate vasudevaya", total_songs = 3, creator = "Haru")

# Create smart_home(device, *args, **kwargs) that prints device settings.
def smart_home(device, *args, **kwargs):
    print(f"device : {device}")
    print("commands:")
    for commands in args:
        print(commands)
    print("device settings:")
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
smart_home("smart light", "turn on", room = "living room", status = "active" )