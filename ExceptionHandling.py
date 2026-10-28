a = int(input("Enter a value:"))
b = int(input("Enter a value:"))
try:
  c = a/b
except ZeroDivisionError:
  print("cannot divide by zero") # zero division error
else:
  print("result=", c)
finally:
  print("problem ends")
  
# How to raise an Exception
try:
    age = -5

    if age < 0:
        raise ValueError("Invalid age")

except ValueError as e:
    print("Error:", e)
    

# User-defined Exception
class InvalidAgeError(Exception):
  pass
age = -5
try:
  if age < 0:
    raise  InvalidAgeError("Invalid age")
except InvalidAgeError as e:
  print("Error=", e)
  

# Multiple Exception Handling
try:
  a = 10
  b = 2
  lst = [10, 20, 30]
  print(a/b)
  print(lst[2])
except ZeroDivisionError:
  print("Cannot divide by zero")
except IndexError:
  print("Index out of range")
print("Rest of the program")