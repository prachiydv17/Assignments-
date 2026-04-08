class Stack:
    def __init__(self):
        self.items = [10,20,30,40]

    def push(self, item):
        self.items.append(item)
        print(item, "pushed into stack")

    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty")
        else:
            self.items.pop()
            print( "popped from stack")

    def peek(self):
        if len(self.items) == 0:
            print("Stack is empty")
        else:
            print("Top element is:", self.items[-1])


s = Stack()

s.push(10)
s.push(9)

s.peek()
s.pop()
s.peek()