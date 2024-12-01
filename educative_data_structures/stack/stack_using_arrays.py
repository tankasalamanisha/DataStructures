class StackImplimentation:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.st = [None]*self.capacity
    def push(self,ele):
        if self.top == self.capacity-1:
            print("Stack Overflow")
            return
        self.top += 1
        self.st[self.top] = ele
        self.print_stack()
    def top_element(self)->int:
        if self.top == -1:
            print("Empty Stack")
        else:
            return self.st[self.top]
    def pop(self)->int:
        if self.top == -1:
            print("Stack Underflow")
        else:
            top_ele = self.st[self.top]
            self.top -= 1
            return top_ele
    def size(self):
        return self.top+1
    def print_stack(self):
        print(self.st)

if __name__== "__main__":
    my_stack = StackImplimentation(capacity=5)
    my_stack.top_element()
    my_stack.push(8)
    my_stack.push(5)
    my_stack.push(14)
    my_stack.push(6)
    my_stack.print_stack()
    my_stack.top_element()
    my_stack.size()
    my_stack.pop()
    my_stack.top_element()
    my_stack.size()
    my_stack.print_stack()