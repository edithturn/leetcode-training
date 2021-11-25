import heapq

class KthLargest:
    """
    Using heap to order the numbers in an array, each time the len of the array exceeds k, we need to remove the lower numbers in the array.

    Big O:
    Time: O(N⋅log(N) + M⋅log(k)), where  O(N⋅log(N) is for the constructor for convert nums in a heap and removing from heap until len equal to k.
    M⋅log(k)) is for add(), adding and removing elements from the heap.
    Space: O(N), where N is the size of the array.
    """
    def __init__(self, k, nums):
        """
        Initializing the heap, lower number in index zero. Removing all lower numbers until len of heap is k.
        With this we can take the first index as the kth  largest.
        """
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)
        
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)            

    def add(self, val: int) -> int:
        """
        Each number added into the heap, is located in its order, adding a nuew number means the len of the hep exceeds the K, so we need to remove a the lower number.
        With this we will just remain k elements into the array and is easier return the kth largest number.
        """
        heapq.heappush(self.minheap, val)
        
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
            

# Your KthLargest object will be instantiated and called as such:
#["KthLargest", "add", "add", "add", "add", "add"]
#[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))  # return 4
print(obj.add(5))  # return 5
print(obj.add(10)) # return 5
print(obj.add(9))  # return 8
print(obj.add(4))  # return 8
