# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 
# Example 1:
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 
# Constraints:
# 0 <= key, value <= 106
# At most 104 calls will be made to put, get, and remove.

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [[[], []] for i in range(self.size)]
        

    def put(self, key, value):
        """
        value will always be non-negative.
        """
        bucket, k = self._index(key)
        
        if k == -1:
            bucket[0].append(key)
            bucket[1].append(value)
        else:
            bucket[0][k] = key
            bucket[1][k] = value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket, k = self._index(key)
        if k == -1:
            return -1
        return bucket[1][k]
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket, k = self._index(key)
        if k == -1:
            pass
        else:
            bucket[0].pop(k)
            bucket[1].pop(k)
        
    def _hash(self, key):
        return key % self.size
    
    def _index(self, key):
        hash = self._hash(key)
        bucket  = self.buckets[hash]
        for v, k in enumerate(bucket[0]):
            if k == key:
                return bucket, v
        return bucket, -1

        

# Test Cases
#["MyHashMap","put","put","get","get","put","get","remove","get"]
#[[],         [1,1],[2,2], [1],  [3], [2,1], [2],  [2],    [2]]

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
print(obj.put(1,1))
print(obj.put(2,2))
param_1 = obj.get(1)
print(param_1)
param_2 = (obj.get(3))
print(param_2)
print(obj.put(2,1))
param_3 = obj.get(2)
print(param_3)
print(obj.remove(2))
param_4 = obj.get(2)
print(param_4)