# Enter your code here. Read input from STDIN. Print output to STDOUT

class Queue:
    def __init__(self):
        self.stack1 = []

    def enqueue(self, x):
       self.stack1.append(x)

    def dequeue(self):
        stack2 = self.stack1[1:]
        self.stack1.clear()
        self.stack1 = stack2[::]

    def peek(self):
        print(self.stack1[0])


q = Queue()

for _ in range(int(input())):
    o = list(map(int, input().split()))
    if o[0] == 1:
        q.enqueue(o[1])
    if o[0] == 2:
        q.dequeue()
    if o[0] == 3:
        q.peek()