def getDecimalValueI(head):
    """
    Time O(2^2)
    Time O(1)
    """
    if head == None:
        return None        
    current = head
    string = ""
    while current:
        string += str(current.val)
        current = current.next
    
    answer = 0
    index = 0
    for i in range(len(string)-1,-1,-1):
        answer += (2**index) * int(string[i])
        index += 1
    return answer
    
def getDecimalValuII(head):
    """"
    Time: O(n)
    Space: O(1)
    """
    answer = 0
    if head == None:
        return None
    while head:
        answer = 2*answer + head.val
        head = head.next
    return answer
