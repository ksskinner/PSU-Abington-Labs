class Stack:

    def __init__(self):
        self.items=[]
    def isEmpty(self): # returns true if empty or false if not
        if len(self.items) == 0:
            return True
        else:
            return False
    def peek(self):
        if len(self.items) == 0:
            pass
        else:
            return self.items[-1] # Returns last item
    def size(self): # returns number of items
        return len(self.items)
    def pop(self): # pops last item
        return self.items.pop()
    def push(self, item): # pushes item onto stack
        self.items.append(item)

class Queue:
    def __init__(self): #Creates a queue with two stacks
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self,num): # pushing item
        if self.s2.size()>0: # if the data is on stack 2
            self.moveto1() # move it to stack 1
        self.s1.push(num) # push item onto stack 1
    def pop(self): #popping item

        if self.s1.size()>0: # if item is on stack 1
            self.moveto2() # move it to stack 2
        if self.s2.size() != 0:
            return self.s2.pop() # pop item from stack 2
        else:
            print("Nothing to pop")
            return None
    def moveto2(self): # moving from stack 1 to 2
        for i in range(self.s1.size()): # for each item on 1
            self.s2.push(self.s1.pop()) # move it to 2

    def moveto1(self): # Moving from stack 2 to 1
        for i in range(self.s2.size()): # for each item on 2
            self.s1.push(self.s2.pop()) # move it to 1

def checkbalance(string):
    print("Initial string: " + string) #prints initial word
    stack = Stack()  #creates a stack
    matched = True # sets a matched

    for x in string: #reads string
        if x == "{" or x == "(" or x == "[":
            stack.push(x) # pushes left delimiter onto the stack
        elif x == "]" or x == ")" or x == "}": # Right delimiter
            if stack.size() == 0: # If nothing is on the stack, not balanced
                print("No match for: " + x)
                matched= False
                break
            current = stack.pop() # Put top of the stack in a variable

            if x == "}":
                if current != "{": # if { is not matched with }, return false and end
                    print(current + " does not match " + x)

                    matched = False
                    break
            elif x == ")":
                if current != "(":  # if ( is not matched with ), return false and end
                    print(current + " does not match " + x)

                    matched = False
                    break
            elif x == "]":
                if current != "[": # If [ is not matched with ] return false and end
                    print(current + " does not match " + x)
                    matched = False
                    break
            if matched== True: #if they match, print match
                print(current + " matches " + x)

    if stack.size() != 0: # If items are still in the stack after the string is processed
        print("No match for " + stack.pop())
        matched = False

    if matched: # if the items are balanced
        print("Delimiters are balanced")
    else: # if the string is not balanced
        print("Delimiters are not balanced")


q = Queue()
print(q.pop())
print("Pushing 4")
q.push(4)
print("Pushing 6")

q.push(6)
print("Pushing 8")

q.push(8)
print("Popping")
print(q.pop())
print("Popping")
print(q.pop())
print("Pushing 10")
q.push(10)
print("Popping")
print(q.pop())
print("Popping")
print(q.pop())


checkbalance("[{{[][]88}}]")
print("---------")
checkbalance("[]]]]")
print("---------")
checkbalance("[}")
print("---------")
checkbalance("[[this is a sentence]")