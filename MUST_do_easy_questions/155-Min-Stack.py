class MinStack:

    def __init__(self):
        """
        Using tow stacks: Add value to the stack anc omparing with other stack which stores the min value in the first stack.
        ||======= Big O ======= || 
        Time complexity : O(1)
        Space complexity: O(1)
        """
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minstack[-1]) if self.minstack else val
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()        

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minstack[-1]
     


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-3))
param_1 = obj.getMin()
print(param_1)
print(obj.pop())
param_2 = obj.top()
print(param_2)
param_3 = obj.getMin()
print(param_3)


#["MinStack","push","push","push","getMin","pop","top","getMin"]
#[[],[-2],[0],[-3],[],[],[],[]]

#Output
#[null,null,null,null,-3,null,0,-2]