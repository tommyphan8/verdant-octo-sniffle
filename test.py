class List():
    def __init__(self):
        self.items = []

    def add(self,item):
        self.items.append(item)

    def remove(self,item):
        self.items.remove(item)

    def search(self,item):

        for x in range(len(items)):
            if self.items[x] == item:
                return True
        return False

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        for x in range(len(self.items)):
            if self.items[x] == item:
                return x

    def insert(self, pos, item):
        self.items.insert(pos, item)

    def pop(self):
        return self.items.pop()

    def pop(self,pos):
        return self.items.pop(pos)