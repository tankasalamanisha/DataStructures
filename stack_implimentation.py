# Abstract data-type : data- type whose behaviour is defined based
# on the data attributes and the methods associated with it.
class Stack():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def push(self,ele):
        return self.items.append(ele)
    def size(self):
        return len(self.items)


if __name__=="__main__":
    s= Stack()
    s.push("Manisha")
    s.push("Mukunda")
    print(s.peek())