class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
        #insert(0,item) mean inserting every incoming item into 0 index
        #so the previous item at 0 will move to index 1.
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

q=Queue()
q.enqueue(12)
q.enqueue('dog')
q.enqueue(True)

for x in range(q.size()):
    print("index :",q.items.index(q.items[x]),"Value:",q.items[x])

print(q.size())
print(q.dequeue())