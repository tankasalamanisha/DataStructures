class Stack():
    def __init__(self):
        """Function to initialise an empty stack as soon as the object is created"""
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items

if __name__ == "__main__":
    stack_1 = Stack()
    print(f"Stack is empty:{stack_1.is_empty()}")
    stack_1.push("A")
    print(stack_1.get_stack())
    stack_1.push("B")
    stack_1.push("C")
    print(stack_1.get_stack())
    stack_1.pop()
    print(stack_1.get_stack())
    print(stack_1.peek())


