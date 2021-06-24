# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

# Example 1:
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

# Example 2:
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

# Example 3:
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.

def isAlienSorted(words, order):
    order_dic = {}

    for index, value in enumerate(order):
        order_dic[value] = index
    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            if j >= len(words[i + 1]):
                return False
            if words[i][j] != words[i + 1][j]:
                if order_dic[words[i][j]] > order_dic[words[i + 1][j]]:
                    return False
                break
    return True


# Test Cases
words1 = ["hello","leetcode"] # True
order1 = "hlabcdefgijkmnopqrstuvwxyz"

words2 = ["word","world","row"] # False
order2 = "worldabcefghijkmnpqstuvxyz"

words3 = ["apple","app"]  # False
order3 = "abcdefghijklmnopqrstuvwxyz"

words4 = ["apap","app"] # True
order4 = "abcdefghijklmnopqrstuvwxyz"

words5 = ["kuvp","q"] # True
order5 = "ngxlkthsjuoqcpavbfdermiywz"

print(isAlienSorted(words1, order1))
print(isAlienSorted(words2, order2))
print(isAlienSorted(words3, order3))
print(isAlienSorted(words4, order4))
print(isAlienSorted(words5, order5))