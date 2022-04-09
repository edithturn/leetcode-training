
def getDecimalValue(head):
    """
    Brute-Force: First get all values of the each node
    and concatenating into a string
    after converting it into an int, calculate the decimal
    by the sum of binary digits times their power of 2.

    Time O(n^2)
    Time O(1)
    """
    if head == None:
        return None        
    current = head
    num = ""
    while current:
        num += str(current.val)
        current = current.next
    
    num = int(num)
    index = 0
    res = 0
    while num > 0:
        if num%2 == 1:
            res += (2**index)
        index += 1
        num = num//10
    return num


def getDecimalValue(head):
    """"
    Binary to Decimal with Multiply by Two Algorithm
    Time: O(n)
    Space: O(1)
    """
    answer = 0
    if not head:
        return None
    while head:
        answer = answer*2 + head.val
        head = head.next
    return answer
