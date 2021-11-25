class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.table = [None] * self.size

    def calculate_has_table(self, key):
        return key % self.size
        
    def add(self, key: int) -> None:
        value = self.calculate_has_table(key)
        if self.table[value] == None:
            self.table[value] = [key]
        else:
            self.table[value].append(key)
            

    def remove(self, key: int) -> None:
        value = self.calculate_has_table(key)
        if self.table[value] != None:
            while key in self.table[value]:
                self.table[value].remove(key)
            
        

    def contains(self, key: int) -> bool:
        value = self.calculate_has_table(key)
        
        if self.table[value] != None:
            return key in self.table[value]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)