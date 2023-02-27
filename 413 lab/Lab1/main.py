import random
import time
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def gcd(a,b): #
    if b == 0: # A % B is 0, then A is divisible by B. THus return A
        return a
    else:
        return gcd(b,a%b)
        #otherwise, recursively call gcd with b and a modulus b.

numlist = []
numlist2 = []

for i in range(1000): #creating a list of 1000 items
    numlist.append(random.randint(1,10000))


for i in range(10000): # creating a list of 10,000 items
    numlist2.append(random.randint(1,10000))

def find_max(ls):
    max = ls[0] #sets the maximum to the first element
    for x in ls: # checks each item in the list
        if x > max: # if the current x is larger than max, replace max
            max = x
    return max # returns the maax

def find_min(ls):
    min = ls[0] #set min variable to
    for x in ls: #searches each item linearly

        if x < min: #if the current x is less than min, set min to x
            min = x
    return min # return min

# Press the green button in the gutter to run the script.


def divide_max(ls):
    if len(ls) == 1: #if the lenght of the list is only 1 item, return it
        return ls[0]
    elif len(ls) == 2: #if the length of the list is 2 items, return the max
        return max(ls[0],ls[1])
    else: #otherwise, call the function recursively to get the max for the
        # first and second halves of the list
        return max(divide_max(ls[0:int(len(ls)/2)]),divide_max(ls[int(len(ls)/2):]))


def divide_min(ls):

    if len(ls) == 1: #if the length of the list is 1, return the only digit
        return ls[0]
    elif len(ls) == 2: #if there are two items, return the minimum of the two
        return min(ls[0],ls[1])
    else:
        # otherwise, call the function recursively to get the min for the
        # first and second halves of the list
        return min(divide_min(ls[0:int(len(ls)/2)]),divide_min(ls[int(len(ls)/2):]))


print("Enter the first number: ")
num1 = input()
print("Enter the second number: ")
num2 = input()
print("The GCD of " + str(num1) + " and " + str(num2) + " is " + str(gcd(int(num1),int(num2))))

print("----------")
start = time.time_ns()
print("The linear search max of list 1 is: " + str(find_max(numlist)))
print("This took: " + str(time.time_ns()-start) + " nanoseconds")
print("----------")
start = time.time_ns()
print("The linear search max of list 2 is: " + str(find_max(numlist2)))
print("This took: " + str(time.time_ns()-start) + " nanoseconds")
print("----------")
start = time.time_ns()
print("The linear search min of list 1 is: " + str(find_min(numlist)))
print("This took: " + str(time.time_ns()-start) + " nanoseconds")
print("----------")
start = time.time_ns()
print("The linear search min of list 2 is: " + str(find_min(numlist2)))
end = time.time_ns()
print("This took: " + str(end-start) + " nanoseconds")
print("----------")

print("--------")
start2 = time.time_ns()
print("By divide and conquer, the max of list 1 is " + str(divide_max(numlist)))
print("This took: " + str(time.time_ns()-start2) + " nanoseconds")
print("--------")
start2 = time.time_ns()
print("By divide and conquer, the max of list 2 is " + str(divide_max(numlist2)))
end = time.time_ns()
print("This took: " + str(end-start2) + " nanoseconds")
print("--------")
start2 = time.time_ns()
print("By divide and conquer, the min of list 1 is " + str(divide_min(numlist)))
end = time.time_ns()
print("This took: " + str(end-start2) + " nanoseconds")
print("--------")
start2 = time.time_ns()
print("By divide and conquer, the min of list 1 is " + str(divide_min(numlist2)))
end = time.time_ns()
print("This took: " + str(end-start2) + " nanoseconds")