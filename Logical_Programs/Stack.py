class Stack:
    def __init__(self,lst):
        self.lst=lst
    def push(self,value):
        self.lst.append(value)
        return self.lst
    def pop(self):
        try:
            lst=self.lst
            return lst.pop()
        except(IndexError):
            return ("It is a empty stack so couldn't pop")
    def peek(self):
        try:
            length=len(self.lst)
            return self.lst[length-1]
        except(IndexError):
            return ("It is a empty stack so couldn't peek")
    def is_empty(self):
        if len(self.lst)==0:
            return ("Empty stack")
    
non_empty=Stack([1,2,3,4,2,3])
empty=Stack([])
lst=[non_empty,empty]
for i in lst:
    print(i.pop())
    print(i.push(10))
    print(i.peek())
    i.is_empty()
    print()

