import array


class Vector:
    def __init__(self):
        self.a = array.array('i') # Creates a vector of Integers
        self.maxLength = 2 #sets the maximum lenght to 2

    def length(self): # Returns the legnth of the array
        return len(self.a)

    def contains(self,item):
        if item in self.a: #If the object is in the array, return true
            return True
        else:
            return False # #otherwise, return false

    def getitem(self,index):
        if index <= (self.length() -1): #if index is in range, return item
            return self.a[index]
        else:
            print("Object not found")

    def setitem(self,index,item):

        if index <= self.length(): #if the index is in the range
            print(str(item) + " is set at index " + str(index))
            self.a[index] = item #set the item at that range.
        else:
            print("This index does not exist")

    def append(self,item):
        if self.length() < self.maxLength: #if the array is not full
            self.a.append(item) #add the item
        else:
            print("No room in the array to add new values.")
            # Otherwise, print full

    def insert(self,ndx, item):
        if self.length() < self.maxLength:
        # CHeck to see if the array is full
            if ndx <= self.length(): #if the index is within the new range
                self.a.insert(ndx,item)
            else:
                print("Index out of range")
        else:
            print("No room in the array to add new values.")

    def indexOf(self,item):  #returns the value if found
        if self.contains(item):
            return self.a.index(item)
        else:
            print("Not in list") #prints if item is not in the array

    def remove(self,index):
        if index<self.length(): #If the index is in the list
            self.a.pop(index) #pop it
        else:
            print("No element of that index exists")

    def extend(self,vectorB): #adds a second vecotr to the current

        self.a.extend(vectorB.a) #adds the second vector's values to the first
        self.maxLength = (max(self.maxLength,vectorB.maxLength))*2
        #sets the vector max siee to double the length

    def subVector(self,start,end):
        if start < self.length() and end < self.length():
            #Cchecks that the start and end are inside the bounds
            if start>end and end >0:
                #checks that the start is smaller than the end
                print("Last index must be larger than the first index")

            else:
                tempVector = Vector() #creates a new vector
                tempVector.a.extend(self.a[start:end+1])
                #sets new vector's array to the splice of the old
                tempVector.maxLength=self.maxLength

                #sets max lengtht to the old array's
                return tempVector
        else: #else, the indexes are out of bounds
            print("Indexes out of bounds")

print("Creating vector")
A = Vector()
print("Printing vector")
print(A.a)
print("-------")
print("Initial Vector")
print(A.a)
print("Appending 1")
A.append(1)
print("Appending 2")
A.append(2)
print("Printing array")
print(A.a)
print("-------")
print("Printing Length")
print(A.length())
print("-------")
print("Array contains 1")
print(A.contains(1))
print("Array contains 5")
print(A.contains(5))

print("-------")
print("The item at Index 1 is: " + str(A.getitem(1)))
print("The item at Index -1 is: " + str(A.getitem(-2)))

print("--------")
print("Initial array")
print(A.a)
print("Changing index 1 to 10")
A.setitem(1,10)
print(A.a)
print("-----")

print("Initial array")
print(A.a)
print("Removing Index 0")
A.remove(0)
print("Removing Index 10")
A.remove(10)

print("Final array")
print(A.a)
print("-----")

print("Initial array")
print(A.a)
print("Inserting 5 at Index 0")
A.insert(0,5)
print("Inserting 20 at Index 4")
A.insert(4,5)

print("Final array")
print(A.a)
print("-----")

print("The index of 10 is " + str(A.indexOf(10)))
print("The index of 40")
A.indexOf(40)
print("-----")
print("Creating Vector B with 30 and 40")
B = Vector()
B.append(30)
B.append(40)
print("Printing B")
print(B.a)
print("Extending A by B")
A.extend(B)
print(A.a)
print("-----")

print("Initial array")
print(A.a)
print("Creating a subvector from index 0-2")
C = A.subVector(0,2)
print(C.a)
