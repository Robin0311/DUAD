class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None  

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("The stack is empty")
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def print_stack(self):
        current = self.top
        if current is None:
            print("The stack is empty")
            return
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print_stack()      
print("Pop:", stack.pop())
stack.print_stack()      
