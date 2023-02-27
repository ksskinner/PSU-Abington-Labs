import time

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def getList(file):
    studentsData = [] #creates a file
    with open(file) as f: #reads the file
        myline = f.readline()
        while myline:
            studentsData.append(myline.split()) #reads each line into a list
            myline = f.readline()
        f.close()

    for x in studentsData:  # converts the ID to an int
        x[0] = int(x[0])
    return studentsData #returns the data as a list of lists

def bubble(list):

    #of reach element in the list length - 1
    for x in range(len(list)-1):
        swapped = False

    #Secomd loop, minus
        for y in range(0,len(list)-1-x):
            #if list y is less than the number above it, swap them
            if list[y][0] > list[y+1][0]:
                temp = list[y]
                list[y] = list[y+1]
                list[y+1] = temp
                swapped = True
        #if no swap is made, return early
        if swapped == False:
            break
    #return sorted list
    return list



def selection(list):

    for slot in range(len(list)): #sqequentially searches each
        minPos = slot #sets the current position to the minimum
        for x in range(slot+1,len(list)):
            if list[x][0] < list[minPos][0]:
                minPos = x # #if it finds an item tht's smaller, record that position

        temp = list[slot] #swaps minimum with current
        list[slot] = list[minPos]
        list[minPos] = temp
    return list # return list

def insertion(list):
    for index in range(1,len(list)): #for each item in list
        pos = index
        current=list[index]
        while current[0] < list[pos-1][0] and pos > 0: #if it finds a smaller number
            list[pos] = list[pos-1] #shuffle the numbers upwards
            pos -= 1
        list[pos] = current #set the smaller number into place
    return list

def linear(list,target):

    for x in list: #search linearly through the list and return the item if found
        if x[0] == target:
            print("Target found")
            return x
    print("Target not found")

def binary(list,target):
    if len(list) == 1: # if there's only 1 item in the list
        if list[0][0] == target: #if the item is the target, return the target list
            print("Target Found")
            print(list[0])
        else:
            print("target not found") # else return not found
    else:
        if target==list[len(list)//2][0]: #if the target is the midpoint
            print("target Found")
            print(list[len(list)//2])
        else:
            if target <list[len(list)//2][0]:
                #if the target is less than midpoint, recursively run the left half
                binary(list[0:(len(list)//2)],target)
            else:
                # if the target is greater than midpoint, recursively run the right half
                binary(list[(len(list)//2):],target)


def merge(list):
    if len(list) > 1:
        mid = len(list)//2 #sets the midpoint
        left = list[0:mid] # Left half of the list
        right = list[mid:] # right half of the list

        merge(left) #recursiely runs left half
        merge(right) # recursively runs right half
        # Sets counters to track the items in each half
        i = 0 #left counter
        j = 0 # right counter
        k = 0 # index in the list
        while i < len(left) and j < len(right): #while there's items in both sides
            if left[i][0] < right[j][0]: #if left is smaller, add it to the list
                list[k] = left[i]
                i+=1
            else: # if right is smaller, add it to the list
                list[k] = right[j]
                j+=1
            k+=1
        while i< len(left): #if there are excess lefts, add them to the list
            list[k] = left[i]
            i+=1
            k+=1
        while j< len(right): #if there are excess rights, add them to the list
            list[k] = right[j]
            j += 1
            k +=1
    return list #return list


list1 = getList('Students.txt')
list2 = getList('Students.txt')
list3 = getList('Students.txt')
list4 = getList('Students.txt')
identicalList = getList('Single Student.txt')
print("unsorted data")
for x in list1:
    print(x)
print("-------------")
print("Identical Data")
for x in identicalList:
    print(x)
print("-------------")
print("Bubble sort")
start = time.perf_counter()*1000
sorted1 = bubble(list1)
print("Bubble Sort calculated in: " + str(time.perf_counter()*1000-start) + " ms")
for x in sorted1:
    print(x)
print("-----")
print("Bubble sort on sorted list")
start = time.perf_counter()*1000
sorted1 = bubble(sorted1)
print("Bubble Sort calculated in: " + str(time.perf_counter()*1000-start) + " ms")
for x in sorted1:
    print(x)
print("-----")
print("Bubble sort on identical list")
start = time.perf_counter()*1000
identicalList = bubble(identicalList)
print("Bubble Sort calculated in: " + str(time.perf_counter()*1000-start) + " ms")
for x in identicalList:
    print(x)
print("-----")
print("Selection")
start = time.perf_counter()*1000
print("Selection sort calculated in: " + str(time.perf_counter()*1000-start) + " ms")
sorted2 = selection(list2)
for x in sorted2:
    print(x)

print("-----")
print("Selection sort on sorted list")
start = time.perf_counter()*1000
print("Selection sort calculated in: " + str(time.perf_counter()*1000-start) + " ms")
sorted2 = selection(sorted2)
for x in sorted2:
    print(x)
print("-----")
print("Selection sort on identical list")
start = time.perf_counter()*1000
print("Selection sort calculated in: " + str(time.perf_counter()*1000-start) + " ms")
identical = selection(identicalList)
for x in identicalList:
    print(x)
print("-----")
print("Insertion")
start = time.perf_counter()*1000
print("Insertion sort calculated in: " + str(time.perf_counter()*1000-start) + " ms")
sorted3 = selection(list3)
for x in sorted3:
    print(x)
print("-----")
print("insertion sort on sorted list")
start = time.perf_counter()*1000
print("Insertion sort calculated in: " + str(time.perf_counter()*1000-start) + " ms")
sorted3 = selection(sorted3)
for x in sorted2:
    print(x)
print("-----")

print("Insertion sort on identical list")
start = time.perf_counter()*1000
print("Insertion sort calculated in: " + str(time.perf_counter()*1000-start))
identical = insertion(identicalList)
for x in identicalList:
    print(x)
print("-----")
print("merge")
start = time.perf_counter()*1000

sorted4 = merge(list4)
print("Merge sort calculated in: " + str(time.perf_counter()*1000-start) + " ms")
for x in sorted4:
    print(x)
print("-----")
print("merge sort on already sorted list")
start = time.perf_counter()*1000

sorted4 = merge(list4)
print("Merge sort calculated in: " + str(time.perf_counter()*1000-start) + " ms")
for x in sorted4:
    print(x)
print("-----")

print("merge sort on identical list")
start = time.perf_counter()*1000

identical = merge(identicalList)
print("Merge sort on identical list: " + str(time.perf_counter()*1000-start) + " ms")
for x in identical:
    print(x)
print("-----")

print("Linear search for index 1110666")
start = time.perf_counter()*1000
print(linear(list1,1110666))
print("Seaarch took: " + str(time.perf_counter()*1000-start) + " ms")

print("Binary search for index 1110666")
start = time.perf_counter()*1000
binary(list1,1110666)
print("Seaarch took: " + str(time.perf_counter()*1000-start) + " ms")



