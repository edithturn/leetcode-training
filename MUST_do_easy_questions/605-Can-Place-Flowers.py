
def canPlaceFlowers(flowerbed, n):
    """
    Adding zeros in the head and in the tail. Checkig three the current, the previous and the next number, if they are zero is where we should put a plant.
    ||======= Big O ======= ||
    Time complexity : O(n), where n is the lenght of flowerbed.
    Space complexity: O(1)
    """
    new_flowerbed = [0] + flowerbed + [0]
    
    for i in range(len(flowerbed)):
        if new_flowerbed[i] == 0 and new_flowerbed[i + 1] == 0 and new_flowerbed[i + 2]  == 0:
            new_flowerbed[i + 1] = 1
            n -= 1
        if n <= 0:
            return True
    return False


# Test Cases
print(canPlaceFlowers([1,0,0,0,1], 1)) # True
print(canPlaceFlowers([1,0,0,0,1], 2)) # False
print(canPlaceFlowers([0], 1)) # True
print(canPlaceFlowers([0], 2)) # False
