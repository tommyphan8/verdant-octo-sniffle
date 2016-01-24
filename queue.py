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


def hotPotato(l, count):
    q = Queue()
    q.items = l
    num = 0
    while(q.size() != 1):
        temp = q.dequeue()
        if(num != count):
            q.enqueue(temp)
            num += 1
        else:
            num = 0
    return(q.dequeue())
print(hotPotato(["Bill","David","Susan","Jane","Kent"],4))

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))