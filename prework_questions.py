#Question 1: 
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    """function prints a greeting message"""
    print('hello_'+user_name)

#Question 2: 
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    """function prints all odd numbers from 1 to 100"""
    number = 1
    while number <= 100:
        if number % 2 == 1:
            print(number, end=" ")
        number += 1

#Puestion 3: 
# Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    """function returns the largest number from a list of intergers or floats"""
    max = a_list[0]
    for number in a_list:
        if max < number:
            max = number
    return max

#Question 4: 
# Write a function to return if the given year is a leap year. The return should be boolean Type (true/false).
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    """functions returns if given year is a leap year"""
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#Question 5: 
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    """function checks if numbers in list are consecutive by testing if each new entery is 1 greater than the last, except for the first entery"""
    first = True
    for number in a_list:
        if first == True:
            prev_number = number
            first = False
            continue
        elif number == prev_number + 1:
            prev_number = number
        else:
            return False
    return True