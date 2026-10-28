# Use map() to square each number in [2, 4, 6, 8].
nums = [2, 4, 6, 8]
square = list(map(lambda n:n * n, nums))
print(square)

# Convert an array of strings ["apple", "banana", "cherry"] into uppercase using map().
words =  ["apple", "banana", "cherry"]
upper = list(map(str.upper, words))
print(upper)

# Extract the id property from an array of objects: [{id:1,name:"A"}, {id:2,name:"B"}, {id:3,name:"C"}]
data =  [{"id":1,"name": "A"}, 
         {"id":2,"name":"B"},
         {"id":3,"name":"C"}]
names = list(map(lambda x:x["name"], data))
print(names)

# Add 5 to each element in [10, 20, 30] using map().
nums = [10, 20, 30]
element = list(map(lambda n:n + 5, nums))
print(element)

# Convert an array of numbers [1,2,3,4] into strings using map().
nums = [1,2,3,4]
str = list(map(str,nums))
print(str)

# Use map() to append "!" to each word in ["hi","hello","hey"].
data = ["hi","hello","hey"]
word = list(map(lambda x:x + "!", data))
print(word)

# Create a new array of lengths from ["dog","elephant","cat"].
words = ["dog","elephant","cat"]
length = list(map(len,words))
print(length)

# Use map() to transform [true,false,true] into ["YES","NO","YES"].
bool = [True,False,True] 
yes_no = list(map(lambda x : "yes" if x else "No", bool))
print(yes_no)

# Given [1,2,3], use map() to return [1,4,9].
num = [1,2,3]
result = list(map(lambda x:x * x, num))
print(result)

# Use map() to add a fullName property to each object in:[{first:"John",last:"Doe"}, {first:"Jane",last:"Smith"}]
data = [{"first":"John","last":"Doe"}, {"first":"Jane","last":"Smith"}]
object = list(map(lambda x:x ["first"] + " " + x["last"], data))
print(object)

# Use filter() to get even numbers from [1,2,3,4,5,6].
num =  [1,2,3,4,5,6]
even = list(filter(lambda x:x % 2 == 0, num))
print(even)

# Filter out words shorter than 4 letters from ["hi","hello","hey","world"].
data =  ["hi","hello","hey","world"]
words = list(filter(lambda x : len(x) >=4, data))
print(words)

# From [10,25,30,45], filter numbers greater than 20.
data = [10,25,30,45]
result = list(filter(lambda x : x > 20, data))
print(result)

# Filter out negative numbers from [5,-3,9,-1,0]
num = [5,-3,9,-1,0]
result = list(filter(lambda x : x < 0, num))
print(result)

# Use filter() to get names starting with "A" from ["Alice","Bob","Andrew","Charlie"].
data = ["Alice","Bob","Andrew","Charlie"]
result = list(filter(lambda x : x.startswith("A"), data))
print(result)

# From [100,200,300,400], filter numbers divisible by 200.
data = [100,200,300,400]
result = list(filter(lambda x : x % 200 == 0, data))
print(result)

# Use filter() to get objects with age > 18 from:[{name:"Tom",age:15},{name:"Jerry",age:20}]
data = [{"name":"Tom","age":15},{"name":"Jerry","age":20}]
result = list(filter(lambda x : x ["age"]> 18 , data))
print (result)

# Filter out duplicate values from [1,2,2,3,4,4,5] using filter().
num = [1,2,2,3,4,4,5]
result = list(filter(lambda x : num.count(x) == 1, num))
print(result)

# From ["red","blue","green","yellow"], filter colors containing "e".
colors = ["red","blue","green","yellow"]
result = list(filter(lambda x : "e" in x, colors))
print(result)

# Use reduce() to sum [1,2,3,4,5].
from functools import reduce
num = [1,2,3,4,5]
sum = reduce(lambda x,y : x+y, num)
print(sum)

# Find the maximum number in [10,25,30,5] using reduce().
from functools import reduce
num = [10,25,30,5]
max = reduce(lambda x,y : x if x > y else y, num)
print(max)

# Use reduce() to concatenate ["a","b","c"] into "abc".
from functools import reduce
data = ["a","b","c"]
result = reduce(lambda x,y : x+y , data)
print(result)

# Count occurrences of each element in [1,2,2,3,3,3] using reduce().
from functools import reduce
data =  [1,2,2,3,3,3]
result = reduce(lambda acc, x: {**acc, x: acc.get(x, 0) + 1}, data,{})
print(result)

# Use reduce() to flatten [[1,2],[3,4],[5]] into [1,2,3,4,5]
data = [[1,2],[3,4],[5]]
result = reduce(lambda acc,x: acc+x, data)
print(result)

# Calculate the product of [2,3,4] using reduce().
data = [2,3,4]
result = reduce(lambda x,y:x*y,data)
print(result)

# Use reduce() to find the longest word in ["cat","elephant","dog"].
data = ["cat","elephant","dog"]
result = reduce(lambda x,y : x if x > y else y, data)
print(result)

# Build an object mapping names to ages from:[{name:"Tom",age:15},{name:"Jerry",age:20}]
data = [{"name":"Tom","age":15},{"name":"Jerry","age":20}]
result = reduce(lambda acc, x: {**acc, x["name"]:x["age"]}, data,{})
print(result)

# Use reduce() to reverse ["a","b","c"] into "cba".
data = ["a","b","c"]
result = reduce(lambda acc, x: x + acc, data, "")
print(result)

# Calculate the average of [10,20,30,40] using reduce().
data = [10,20,30,40]
total = reduce(lambda x, y: x + y, data)
average = total / len(data)
print(average)