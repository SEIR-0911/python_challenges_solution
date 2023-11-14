
# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June?
# - How many Minutes are in the month of August?

# Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year?
# In days, in weeks, in cups of coffee?


# ---------------------------------
import math


def minToSec(min):
    return min*60


def hourToSec(hours):
    return minToSec(hours*60)


def dayToSec(days):
    return (hourToSec(days*24))


def monthToHours(month):
    print("We don't care about leap years here.")

    if month == "february":
        days = 28
    elif month == "april" or month == "june" or month == "September" or month == "November":
        days = 30
    else:
        days = 31

    hours = days*24

    print(
        f"There are {days} days in {month}. Therefore there are {hours} hours.")
    return hours


def monthToMin(month):

    hours = monthToHours(month)
    print(f'And {hours*60} minutes.')
    return hours*60


print("Question 1:")
print(minToSec(3))
print(hourToSec(4))
print(dayToSec(10))
print(monthToHours('june'))
print(monthToMin('august'))

print(f'There are {dayToSec(365)/60} minutes in a year.')
# ---------------------------------


#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
def mid(string):
    has_middle = len(string) % 2

    if has_middle:
        middle_idx = int((len(string) - 1) / 2)
        return string[middle_idx]
    else:
        return ""


print("Question 2:")
print(mid("even"))
print(mid("odd"))
# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
def hide_credit(num):
    num_str = str(num)
    temp = ''.join([('*') for i in num_str[:-4]])
    output = temp + num_str[-4:]

    return output


print("Question 3:")
print(hide_credit(1234567894445))
# ---------------------------------


# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```

statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


# ---------------------------------
def online_count(dict):
    online_count = 0
    for key in dict:
        if dict[key] == "online":
            online_count += 1

    return online_count


print("Question 4:")
print(online_count(statuses))
# ---------------------------------


#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
def discount(price, percent):
    return price - (price*(percent/100))


print("Question 5:")
print(discount(100, 20))
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------


def pythagoras(adj, opp):
    hypo = math.sqrt((adj**2)+(opp**2))
    return hypo


print("Question 6:")
print(pythagoras(3, 4))
# ---------------------------------


#  7) Fibonacci Sequence
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
def fib(num1, num2, steps):
    sequence = [num1, num2]
    for i in range(0, steps):
        sequence.append(sequence[-2]+sequence[-1])

    return sequence[2:]


print("Question 7:")
print(fib(0, 1, 9))
# ---------------------------------
