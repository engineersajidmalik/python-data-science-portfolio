### Part A

## Basic Indexing

# Question 1
word = 'Artificial'
# Firs Character  # Last character # Second Character# Third Character
print("The Fist Char is:",word[0])
print("The Second Char is:",word[1])
print("The Third Char is:",word[2])
print("The Last Char is:",word[9])

# Question 2
country = "Pakistan"
# Print P a n
print(country[0], country[1], country[7], sep="\n")

#Question 3
numbers = [15, 28, 34, 49, 56, 78]
# Print First, Fourth and Last Element
print(numbers[0], numbers[3], numbers[5], sep="\n")

# Question 4
fruits = ["Apple","Banana","Orange","Mango","Peach"]
# Print  Banana, Mango, and Peach using indexing only
print(fruits[1], fruits[3], fruits[4], sep="\n")

### Part B – Negative Indexing

# Question 5
language = "Programming"
# Print Last , second last, fifth last char
print(language[-11], language[-10], language[-7])

# Question 6
colors = ["Red","Green","Blue","Black","White"]
# Print  White, Black, and Green using negative indexing only
print(colors[4], colors[3], colors[1])

# Question 7
marks = [78,85,91,66,74,88,95]
# Print  last, third last, and fifth last mark
print(marks[6], marks[4], marks[2])

# Question 8
sentence = "Python is amazing"
# Print Using negative indexing, print: g n p
print(sentence[-1], sentence[-2], sentence[-12], sentence[-17])

### Part C – Basic Slicing

# Question 9
numbers = [10,20,30,40,50,60,70,80]
# Print the first four and last four numbers using slicing.
print("The First 4 numbers are:",numbers[0:4:])
print("The Last 4 numbers are:",numbers[4:])

#Question 10
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Print the first 10 letters and the last 10 letters.
print("The fist 10 char are:", alphabet[:10:])
print("The last 10 char are:", alphabet[16::])

# Question 11
cities = ["Lahore","Karachi","Islamabad","Peshawar","Quetta","Multan"]
# Print the first three cities and the last two cities using slicing.
print("The First 3 cities are:", cities[:3:])
print("The Last 2 cities are:", cities[4::])

### Part D – Step Slicing
# Question 12
numbers = [1,2,3,4,5,6,7,8,9,10]
# Print every second number and every third number
print("Every 2nd number is:", numbers[0::2])
print("Every 3rd number is:", numbers[0::3])

# Question 13
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Print every second and every third letter
print("Every 2nd letter is:", text[0::2])
print("Every 3rd letter is:", text[0::3])

# Question 14
values = [5,10,15,20,25,30,35,40,45,50]
# Print elements at even indices and odd indices.
print("Even indices elements are:", values[0::2])
print("Odd indices elements are:", values[1::2])

# Question 15
word = "COMPUTERSCIENCE"
# Print every second character starting from index 1.
print(word[1::2])

### Part E – Advanced Indexing and Slicing
# Question 16
word = "PYTHON"
# Reverse the string using slicing
print("The reversed string is:", word[::-1])

# Question 17
numbers = [5,10,15,20,25,30,35]
# Reverse the list using slicing.
print("Reversed numbers is:", numbers[::-1])

# Question 18
message = "Python Programming Language"
# Print Python
print("Python =",message[:6:])
# Print Programming
print("Programming =", message[7:19:])
# Print Language
print("Language =", message[19::])
# Print nohtyP
# (At negative indexing we must need to give me -1 value at step position beacuse it shows the direction that we have to move from Right to left
print("nohtyP =", message[-22::-1])
# The last 8 characters
print("The last 8 char =",message[19::])
# Print Every second character from the entire string
print("Every 2nd char from entire string =", message[0::2])

# Question 19
data = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#  Print the first 10 characters.
print(data[0:10:])
#  Print the alphabets only.
print(data[10::])
#  Print every second character.
print(data[0::2])
#  Print the string in reverse.
print(data[-1::-1])
#  Print characters from index 5 to 20.
print(data[5:21:])
#  Print every third character from index 3 to the end.
print(data[3::3])
#  Print the last 10 characters.
print(data[-1:-11:-1])
# Print everything except the first and last character.
print(data[1:34:])

