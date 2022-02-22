def flipAndInvertImage(image):
    """
    Using Two Pointers, iterate each row in the list, fo reach row make a swap of elements and invert the number.
    Big O:
    Time O(n*n/2) -> O(n*m)
    Space: O(1) , not extra space is used
    """
    for img in image:
        left = 0
        right = len(img) - 1
        while left <= right:
            img[left], img[right] = abs(img[right]-1), abs(img[left]-1)
            left += 1
            right -= 1
            
    return image


print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))                    # [[1,0,0],[0,1,0],[1,1,1]]
print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))    # [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]