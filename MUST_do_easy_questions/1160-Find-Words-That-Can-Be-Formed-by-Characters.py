
def countCharacters(words, chars):
    """
    Iterate across the words, and then iterate each character per word,
    if the amount of character that appear in the word is grather than the amount of  the character in chars, it means that they are not equal.
    If flag is one it means quantities of appears of a character in both word and chars is the same, we need to add in to the answer.
    Big O:
    Time: O(n*m), where n is the lengh of words and m is the lengh of chars
    Space: O(1)
    """
    
    ans = 0
    
    for word in words:
        flag = 1
        for char in word:
            if word.count(char) > chars.count(char):
                flag = 0
                break
        if flag == 1:
            ans += len(word)
    return ans

words1 = ["cat","bt","hat","tree"]
chars1 = "atach" # 6

print(countCharacters(words1, chars1)) # 6


words2 = ["hello","world","leetcode"]
chars2 = "welldonehoneyr"

print(countCharacters(words2, chars2)) # 10
