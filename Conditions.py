"""
Python Practice Assignment
Topics: if, if-else, elif, nested if, match-case
"""
import dis
from encodings.punycode import insertion_unsort

# Q1. Read a number. Print Positive, Negative, or Zero.

number = float(input("Enter a number: "))
if number > 0:
    print(number,"is positive")
elif number == 0:
    print(number,"is zero")
else:
    print(number,"is negative")

# Q2. Read a number. Print Even or Odd.

number = float(input("Enter a Number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Q3. Read your age. Print Eligible to Vote or Not Eligible.

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote!")

# Q4. Read two numbers. Print the bigger number.

number1 = float(input("Enter the 1st number: "))
number2 = float(input("Enter the 2nd number: "))

if number1 > number2:
    print(number1, "is bigger then ", number2)
else:
    print(number2, "is bigger then ", number1)

# We can also use max() global function here
print(max(number1, number2))

# Q5. Read three numbers. Print the smallest number.

number1 = float(input("Enter the 1st number : "))
number2 = float(input("Enter the 2nd number : "))
number3 = float(input("Enter the 3rd number : "))

if number1 < number2 and number1 < number3:
    print(number1, "is the smallest number")
elif number2 < number1 and number2 < number3:
    print(number2," is the smallest number")
elif number3 < number1 and number3 < number2:
    print(number3," is the smallest number")
else:
    print("Invalid numbers")

# We can also do it using min() GLobal function
print(min(number1, number2, number3))

# Q6. Read a year and check if it is leap or not.

year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Q7. Read a month number (1-12). Print the month name using match-case.

month = int(input("Enter a month number: "))
match month:
    case 1:
        print('January')
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid month number")

# Q8. Ask the user to enter two numbers. If both numbers are exactly the same,
# print "They are equal". Otherwise, print "They are different".

number1 = float(input("Enter the 1st number: "))
number2 = float(input("Enter the 2nd number: "))

if number1 == number2:
    print("They are equal")
else:
    print("They are different")

# Q9. Read a traffic signal (Red, Yellow, Green).
# Print the correct action using match-case.

signal = input("Enter the traffic signal: ")

match signal:
    case "Red":
        print("Wait, Signal is Red")
    case "Yellow":
        print("Ready, Signal is Yellow")
    case "Green":
        print("Go, Signal is Green")
    case _:
        print("Please enter a valid signal format")

# Q10. Make a simple calculator. Read two numbers and an operator (+, -, *, /).

number1 = float(input("Enter the first number: "))
operator = input("Enter a operator: ")
number2 = float(input("Enter the second number: "))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
elif operator == "%":
    print(number1 % number2)
else:
    print("Please enter a valid operator")

# Or we can also do it using match case

match operator:
    case "+":
        print(number1 + number2)
    case "-":
        print(number1 - number2)
    case "*":
        print(number1 * number2)
    case "/":
        print(number1 / number2)
    case "%":
        print(number1 % number2)
    case _:
        print("Please enter a valid operator")
#

# Q11. Ask the student to enter their test percentage. Use elif to find their letter grade:
# • 90% or above → Grade A
# • 75% to 89% → Grade B
# • 50% to 74% → Grade C
# • Below 50% → Grade F

percentage = float(input("Enter your test percentage:"))

if percentage >= 90:
    print("Grade A")
elif 75 <= percentage <= 89:
    print("Grade B")
elif 50 <= percentage <= 74:
    print("Grade C")
else:
    print("Grade F")

# Q12. Temperature Guide Ask the user to enter today's temperature in Celsius.
# • If it is above 30 degrees, print "It is hot".
# • If it is between 15 and 30 degrees (inclusive), print "It is pleasant".
# • If it is below 15 degrees, print "It is cold".

temperature = float(input("Enter the Temp in Celsius: "))

if temperature > 30:
    print("It is hot ")
elif 15 <= temperature <= 30:
    print("It is pleasant")
elif temperature < 15:
    print("It is cold")
else:
    print("Enter a valid temp ")

# Q13. Ask the user to pick a food item by typing a letter: 'P' for Pizza,
# 'B' for Burger, or 'S' for Sandwich. Use match-case to display the price:
# • Pizza → $10
# • Burger → $6
# • Sandwich → $4
# • Any other letter → "Item not available"

item = input("Enter the item letter: ")

match item:
    case "P":
        print("Pizza → $10")
    case "B":
        print("Burger → $6")
    case "S":
        print("Sandwich → $4")
    case _:
        print("Please enter a valid letter. Hint P, B, S")

# Q14. Ask the user how much money they spent at a toy store.
# • If they spent more than $100, give them a $20 discount and print the final
# price.
# • If they spent more than $50 but less than $100, give them a $5 discount and
# print the final price.
# • Otherwise, print the original price with no discount.

spent_money = float(input("Enter the amount you spent on toy store: "))

if spent_money > 100:
    discount = spent_money - 20
    print("THe final price after discount is:",discount)
elif spent_money > 50 and spent_money <= 100:
    discount = spent_money - 5
    print("The final Price after discount is: ", discount)
else:
    print(spent_money,"No discount")

# Q15. Ask the user for their age. If they are 12 years old or older, ask them if they are a
# student ("yes" or "no").
# • If they are a student, the ticket costs $8.
# • If they are not a student, the ticket costs $12.
# • If they are under 12 years old, the ticket is free.

age = int(input("Enter your age: "))

if age >= 12:
    student = input("Enter you are student or not: yes or no: ")
    if student == "yes":
        print("Ticked cost will be $8")
    elif student == "no":
        print("Ticked cost will be $12")
elif age < 12:
    print("Ticked is free")


# Q16. Ask the applicant for two things: their age and their years of experience.(solve it using
# nested if )
# • If they are 21 or older, check their experience:
# o If they have 3 or more years of experience, print "You are hired!".
# o Otherwise, print "You need more experience".
# • If they are under 21, print "You are too young for this job

age = int(input("Enter your age: "))

if age >= 21:
    years_of_exp = int(input("Enter years of ep: "))
    if years_of_exp >= 3:
        print("You are hired")
    else:
        print("You need more experience")
else:
    print("You are too young for this job")

# Q17. ATM: Read account balance and withdrawal amount. Check if money can be
# withdrawn.

account_balance = float(input("Enter your account balance: "))
amount_withdraw = float(input("Enter the amount you want to withdraw: "))

if account_balance >= amount_withdraw:
    print("You can withdraw ")
else:
    print("You can not withdraw ")

# OR we can also use this logic too
if account_balance - amount_withdraw >= 0:
    print("You can withdraw")
else:
    print("You can not withdraw ")

"""
 Q18. Bank Loan: Read age, monthly income, and job status.Decide if the loan is approved
"""

age = int(input("Enter your age: "))
monthly_income = float(input("Enter your monthly income: "))
job_status = input("Enter your job status: yes or no : ")

if age >= 18 and monthly_income >= 50000 and job_status == "yes":
    print("Your loan is approved ")
else:
    print("You can not apply for this loan ")

# OR we can also do it using nested if
if age >= 18:
    if job_status == "yes":
        if monthly_income >= 50000:
            print("Your loan is approved ")
        else:
            print("Your monthly income is too low ")
    else:
        print("You need a job for this loan ")
else:
    print("You can not apply for this loan ")


"""
Q19. Store a secret number (like 7) inside a variable. Ask the user to guess the number.
If they guess it right, print "Correct guess!".
 If their guess is too high, print "Too high, try again!".
If their guess is too low, print "Too low, try again!
"""

secret_number = 7
user_guess = int(input("Enter your guess number: "))

if user_guess == secret_number:
    print("Correct guess! ")
elif user_guess > secret_number:
    print("Too high, try again! ")
else:
    print("Too low, try again! ")

""" 
Q20. Ask the user for the distance (in km).
 Less than 5km: $5 fee.
 5km to 15km: $10 fee.
 More than 15km: $15 fee
"""

distance = int(input("Enter the distance in KM :"))

if distance < 5:
    print("Fee is $5")
elif distance >= 5 and distance < 15:
    print("Fee is $10")
else:
    print("Fee is $15")










