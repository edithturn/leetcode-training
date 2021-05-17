def titleToNumber(columnTitle):
    """
    Using ACCII values to get the column number. Ascci number of A (Capital letter) is 65.
    We want to know the column number of A. 
    subtracting the  accii value of the giving number minus the asccii value of 'A' and adding ONE, we will get the column number.
    example: 65 - 'A' + 1 => 65 - 65 + 1 = 1
    Result: Column Number of A is 1 
    What happen if the columnTitle has more than one letter, in case of: "AB": We should calculate character by character, 
    first character (the result) will land beetween numbers from 1 to 26, 
    For the second character "B" is beetween the second section of 26 after 26, I mean I should add 26.
    """
    result = 0
    for char in columnTitle:
        firt_columnnumber = ord(char) - 65 + 1
        result = result*26 + firt_columnnumber
    return result

columnTitle = "A"
columnTitle1 = "Z"
columnTitle2 = "AB"
columnTitle3 = "ZY"
columnTitle4 = "FXSHRXW"

print(titleToNumber(columnTitle))
print(titleToNumber(columnTitle1))
print(titleToNumber(columnTitle2))
print(titleToNumber(columnTitle3))
print(titleToNumber(columnTitle4))