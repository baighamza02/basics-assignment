class HashTable:
    
    def __init__(self, size):
        self.size = size
        self.table = [[[None,None]]] * size

    def makeHash(self, key):
        key = ''.join(str(ord(char)) for char in key)#converting individual char to its ascii and then joining with rest of the string
        return int(key)%self.size
    
    def insert(self, key, value):
        index = self.makeHash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
            else:
                self.table[index].append([key,value])
    
    def get(self, key):
        index = self.makeHash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def remove(self, key):
        index = self.makeHash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return
        return None
    

myHashTable = HashTable(20)
myHashTable.insert('key1',1)
myHashTable.insert('key2',233)
myHashTable.insert('key3',3)

print(myHashTable.get('key1'))
print(myHashTable.get('key2'))
print(myHashTable.get('key3'))

myHashTable.remove('key1')
print(myHashTable.get('key1'))
