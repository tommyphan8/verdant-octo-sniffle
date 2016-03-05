class HashTable:
    def __init__(self):
        self.size = 11
        self.key = [None] * self.size
        self.value = [None] * self.size

    def put(self, key, val):
        hashValue = self.hashFunction(key)

        if self.key[hashValue] == None:
            self.key[hashValue] = key
            self.value[hashValue] = val
        elif self.key[hashValue] == key:
            self.value[hashValue] = val
        else:
            rehashValue = self.rehash(hashValue)
            found = False
            while(not found and rehashValue != hashValue):
                if self.key[rehashValue] == None:
                    self.key[rehashValue] = key
                    self.value[rehashValue] = val
                    found = True
                elif self.key[rehashValue] == key:
                    self.value[rehashValue] = val
                    found = True
                else:
                   rehashValue = self.rehash(rehashValue)    
    def get(self, key):
        hashValue = self.hashFunction(key)
        if self.key[hashValue] == None:
            return None
        elif self.key[hashValue] == key:
            return self.value[hashValue] 
        else:
            rehashValue = self.rehash(hashValue)
            while rehashValue != hashValue:
                if self.key[rehashValue] == key:
                    return self.value[rehashValue]
                else:
                    rehashValue = self.rehash(rehashValue)

    def hashFunction(self, key):
        return key % self.size

    def rehash(self, pos):
        return (pos+1) % self.size

    #overloading methods
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self, key, val):
        self.put(key,val)

temp = HashTable()

H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"

H[20] ='chicken'
H[17]='tiger'
H[20]='duck'



print(H.key)
print(H.value)
print(H[55])
