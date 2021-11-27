
def maxDistToClosest(seats):
    """
    Grouping by zero and looking the distance bettween two occupied seats.
    Update the previos seat to update in case we find a maxium lenghs of zeros together.

    Big O:
    Time: O(n), since we are iterating the array once
    Space: O(n), not using extra space
    """
    prev_seat = None
    distance = float('-INF')
    
    for index in range(len(seats)):
        if seats[index] == 1:
            if prev_seat == None:
                distance = index
            else:
                distance = max(distance, (index - prev_seat) // 2)
            prev_seat = index
    distance = max(distance, len(seats) - 1 - prev_seat)
    return distance
        
        
# Test Cases
seats1 = [1,0,0,0,1,0,1]
seats2 = [1,0,0,0]
seats3 = [0,1]


print(maxDistToClosest(seats1)) # 2
print(maxDistToClosest(seats2)) # 3
print(maxDistToClosest(seats3)) # 1