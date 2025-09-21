class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def push_left(self, value):
        new_node = Node(value)
        if self.front is None:  
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def push_right(self, value):
        new_node = Node(value)
        if self.rear is None:  
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def pop_left(self):
        if self.front is None:
            print("The deque is empty")
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is not None:
            self.front.prev = None
        else:
            self.rear = None
        return value

    def pop_right(self):
        if self.rear is None:
            print("The deque is empty")
            return None
        value = self.rear.value
        self.rear = self.rear.prev
        if self.rear is not None:
            self.rear.next = None
        else:
            self.front = None
        return value

    def print_deque(self):
        current = self.front
        if current is None:
            print("The deque is empty")
            return
        while current is not None:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")


deque = Deque()
deque.push_left(10)
deque.push_right(20)
deque.push_left(5)
deque.push_right(30)
deque.print_deque()   
print("Pop left:", deque.pop_left())
print("Pop right:", deque.pop_right())
deque.print_deque()   
