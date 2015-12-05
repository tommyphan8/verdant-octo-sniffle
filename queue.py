class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def popAll(self):
        for x in range(A.size()):
            print(self.dequeue())


def hotPotato(nameList, num):
    q = Queue()
    
    for x in nameList:
        q.enqueue(x)
    
    temp = None
    while (q.size() > 0):
        for x in range(num):
            q.enqueue(q.dequeue())
        temp = q.dequeue()
    return temp

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))