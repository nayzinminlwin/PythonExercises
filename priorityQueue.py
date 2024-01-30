from pqueue import pQueue

p =pQueue()

p.enqueue("HELLO",1)
p.enqueue("H",2)
p.enqueue("E",5)
p.enqueue("L",3)
p.enqueue("O",3)
p.enqueue("Sample",9)

print(p.size()) #7
print(p.dequeue()) #Sample
print(p.dequeue()) #E
print(p.size()) #4
print("---------------------")
print(p.dequeue()) #L
print(p.dequeue()) #O
print(p.dequeue()) #H
print(p.size()) #1