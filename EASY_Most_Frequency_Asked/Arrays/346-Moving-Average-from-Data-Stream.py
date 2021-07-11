# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.
 

# Example 1:
# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
 

# Constraints:
# 1 <= size <= 1000
# -105 <= val <= 105
# At most 104 calls will be made to next.


import collections


class MovingAverageI:

    def __init__(self, size):
        """
        First Approach Brute Force using deque

        ||======= Big O ======= ||
        - Time complexity : O(n) 
        - Space complexity: O(1)
        """
        self.queue = collections.deque(maxlen=size)

    def next(self, val):   
        queue = self.queue
        queue.append(val)
        return round(float(sum(queue)/len(queue)),2) 



class MovingAverageII:
    """
    First Approach Brute Force using deque

    ||======= Big O ======= ||
    - Time complexity : O(1) 
    - Space complexity: O(1)
    """
    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.size = size
        self.sum = 0

    def next(self, val):   
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()
        self.queue.append(val)
        self.sum += val
        return round(float(self.sum/len(self.queue)),2)


# Your MovingAverage object will be instantiated and called as such:

# input: ["MovingAverage","next","next","next","next"]
# input: [[3],[1],[10],[3],[5]]
# output: [null,1.00000,5.50000,4.66667,6.00000]

print("Approach Brute Force using deque ")
obj = MovingAverageI(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))

print("  ")
print("Approach Slide Window")
obj1 = MovingAverageII(3)
print(obj1.next(1))
print(obj1.next(10))
print(obj1.next(3))
print(obj1.next(5))