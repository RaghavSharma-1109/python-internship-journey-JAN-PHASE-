class Queue:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 =[]
    def enqueue(self,x):
        self.stack1.append(x)
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return "Queue Empty"
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return "Queue Empty"
        
        return self.stack2[-1]
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
    
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())

q.enqueue(4)

print(q.peek())