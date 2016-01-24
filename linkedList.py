class Node:
    def __init__(self,initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

class linkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        if self.head == None:
            temp.setNext(self.last)
            self.head = temp
            self.last = temp
        else:
            temp.setNext(self.head)
            self.head = temp 
       
    def size(self):
        count = 0
        current = self.head
        while(current != None):
            count += 1
            current = current.getNext()
        return count 

    def search(self,item):
        found = False
        current = self.head
        while (current != None):
            if current.getData() == item:
                return True
            else:
                current = current.getNext()
        return False 

    def remove(self, item):
        delete = False
        if self.head == None:
            print('Cannot delete from empty list')
        else:
            if(self.head.getData() == item):
                if self.head == self.last:
                    self.head = None
                    self.last = None
                else:
                    self.head = self.head.getNext()
                delete = True
            else:
                prev = self.head
                current = prev.getNext()
                while(current != None and not delete):
                    if current.getData() == item:
                        prev.setNext(current.getNext())
                        if current.getNext() == None:
                            self.last = prev
                        delete = True
                    else:
                        prev = current
                        current = prev.getNext()

        if(delete):
            print('Deleted successfully!')
        else:
            print('Unsuccessful')

    def append(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.last = temp
        else:
            temp.setNext(self.last.getNext())
            self.last.setNext(temp)
            self.last = temp




    def print(self):
        temp = ''
        current = self.head
        while(current != None):
            temp += str(current.getData()) + " "
            current = current.getNext()
        print(temp)

class orderedList(linkedList):
    def __init__(self):
        linkedList.__init__(self)

    def index(self, item):
        current = self.head
        index = 0
        while(current != None):

            if current.getData() == item:

                return index
            else:
                index += 1
                current = current.getNext()
    
    # def pop(self, pos = None):
    #     item = None
    #     if self.head == self.last:
    #         self.head = None
    #         self.last = None
    #     else:
    #         pop = False
    #         prev = self.head
    #         current = prev.getNext()
    #         while(current != None and not pop):
    #             if current == self.last:
    #                 item = current.getData()
    #                 prev.setNext(current.getNext())
    #                 self.last = prev
    #                 pop = True
    #             else:
    #                 prev = current
    #                 current = current.getNext()
    #     return item
    
    def pop(self, pos):
        index = 1
        item = None
        if (pos == 0):
            item = self.head
            if(self.head == self.last):
                self.head = None
                self.last = None
            else:
                self.head = self.head.getNext()
        else:
            pop = False
            prev = self.head
            current = prev.getNext()
            while(current != None and not pop):
                if index == pos:
                    item = current.getData()
                    prev.setNext(current.getNext());
                    self.last = prev
                    pop = True
                    print('!')
                else:
                    prev = current
                    current = current.getNext()
                    index += 1

        return item

    def search(self,item):
        found = False
        current = self.head
        while (current != None):
            if current.getData() == item:
                return True
            elif ccurrent.getData() > item:
                return False
            else:
                current = current.getNext()
        return False 

    #o(n) insert
    def insert(self,item):
        try:
            temp = Node(item)
            if self.head == None:
                self.head = temp
                self.last = temp
            elif item <= self.head.getData():
                temp.setNext(self.head)
                self.head = temp
            else:
                prev = self.head
                current = prev.getNext()
                insert = False
                while (current != None and not insert):
                    if item > prev.getData() and current == None:
                        temp.setNext(current)
                        prev.setNext(temp)
                        self.last = temp
                        insert = True
                    elif item > prev.getData() and item <= current.getData():                
                        temp.setNext(current)
                        prev.setNext(temp)
                        insert = True
                    elif item > current.getData() and current.getNext() == None:
                        temp.setNext(current.getNext())
                        current.setNext(temp)
                        self.last = temp
                        insert = True
                    else:
                        prev = current
                        current = current.getNext()
        except:
            print(item, "is not a valid number")









mylist = orderedList()
# mylist.add(31)
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)

# print(mylist.size())
# mylist.print()
# print(mylist.search(93))
# print(mylist.search(100))

# mylist.add(100)
# mylist.print()
# print(mylist.search(100))
# print(mylist.size())

# mylist.remove(54)
# mylist.print()
# print(mylist.size())
# mylist.remove(93)
# mylist.print()
# print(mylist.size())
# print(mylist.search(93))
# print(mylist.head.getData())
# print(mylist.last.getData())
# print("appending")

# mylist.print()
# mylist.append('4')
# print(mylist.search('4'))
# mylist.print()
# mylist.append(5)
# print("pop")
# mylist.print()
# mylist.pop(1)

# mylist.print()
# mylist.pop(1)

# mylist.print()
# mylist.pop(2)
mylist.insert(6)
mylist.print()
mylist.insert(5)
mylist.print()
mylist.insert(6)
mylist.print()
mylist.insert(3)
mylist.print()
mylist.insert(7)
mylist.print()
mylist.insert(2)
mylist.print()
mylist.insert(0)
mylist.print()
mylist.insert('s')
