import random
import time

numlist = []
numDict = {}
for x in range(50000): # Runs 50,000 times
    tempNum = random.randint(1,10000) # creates a random number
    numlist.append(tempNum) # adds number to the list
    numDict[x]= tempNum # adds number to the dictionary at the index.

numToFind = random.randint(1,10000) #sets a value to find
numToDelete = random.randint(1,10000) #sets a value to delete
numToAdd = random.randint(1,10000) #sets a value to add
def find_in_list(ls,num):
    start=time.time()*1000 #sets the timer
    found = False
    for x in ls: #sequential search through the list to see if it's there.
        if num == x:
            print(str(num) + " found at index: "+ str(x)) #if it finds it, prints the index
            found = True
            break
    if not found:
        print("Number not found") # if the
    end = time.time()*1000
    print("Searching the list took: " + str(end-start) + " milliseconds")

def find_in_dict(dict,num):
    start=time.time()*1000 #starts time
    index = -1
    for x in dict.keys(): #searches the dictionary to see if it finds the value. if it does, it saves the index of the value
        if dict[x] == num:
            index = x
            break
    if index != -1: #if the value was found, delete that dictionary entry
        del dict[index]
        print(str(num) + " was found at index " + str(index)) #prints out the
    else:
        print("Number not found in list") #if the number is fond
    end = time.time() * 1000 #ends timer
    print("Searching dictionary took " + str(end-start) + " milliseconds")

def add_to_list(ls,num):
    start=time.time()*1000 #starts time
    ls.append(num) #appends the number to the end of the list
    end = time.time() * 1000
    print(str(num) + " has been added to the list.")
    print("Adding to list took" + str(end-start) + "milliseconds")

def del_from_list(ls,num):
    start=time.time_ns()#starts timer

    for x in ls: #if the number is in the list
        if x == num:
            print(str(num) + " has been deleted at index " + str(ls.index(num)))
            ls.remove(num) #removes it from the first instance
            break
    else:
        print(str(num)+ " is not in the list to delete") # else print that it's not in the list
    end = time.time_ns()
    print("Attempting to delete from list took " + str(end - start) + "milliseconds")

def del_from_dict(dict,num):
    start = time.time() * 1000 # starts timer
    index = -1
    for x in dict.keys(): #searches the dictionary to see if it finds the value. if it does, it saves the index of the value
        if dict[x] == num:
            index = x
            break
    if index != -1: #if the value was found, delete that dictionary entry
        del dict[index]
        print(str(num) + " was found at index " + str(index) + " and deleted")
    else:
        print("Number not found in list")
    end = time.time() * 1000 #ends timer
    print("Attempting to delete from dictionary took " + str(end-start) + " milliseconds")

def add_to_dict(dict,num):
    start = time.time() * 1000 #starts timer
    newKey = max(dict.keys())+1 #sets new key to the highest key + 1
    dict[newKey]=num #adds new intry to the new key, this prevents duplicate keys.
    print(str(num) + " added at key " + str(newKey))
    end = time.time() * 1000

    print("Adding to the dictionary took " + str(end-start) + " milliseconds")



print("Printing the list:")
start = time.time() * 1000

print(numlist)
end = time.time() * 1000
print("Printing the list took " + str(end-start) + " milliseconds")
print("----------")

print("Printing the dictionary:")
start = time.time() * 1000
print(numDict)
end = time.time() * 1000
print("Printing the dictionary took " + str(end-start) + " milliseconds")
print("----------")


find_in_list(numlist,numToFind)

print("----------")
find_in_dict(numDict,numToFind)
print("----------")


add_to_list(numlist,numToAdd)
print(numlist[-100:])
print("----------")

add_to_dict(numDict,numToAdd)
print(numDict)
print("----------")
del_from_list(numlist,numToDelete)
print("----------")
del_from_dict(numDict,numToDelete)
print("----------")
