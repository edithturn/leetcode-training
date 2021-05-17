# def minDistance(word1, word2):
#     len_word1 = len(word1) - 1
#     len_word2 = len(word2) - 1
#     count = 0
#     id1 = 0
#     id2 = 0

#     while word1[id1] != word2[id2]:
#         print(id2)
#         id2 += 1
#         if (id1 >= len_word1) or (id2 >= len_word2):
#             break
#     #return id2
    
#     index = check_equal(id1, id2)
#     return index

# def no_equal(i1, i2):
#     id2 = i2
#     id1 = i1
#     while len(word2)
#     word1[i1] != word2[i2]:
#         id2 += 1
#     return True

# def check_equal(i1, i2):
#     id2 = i2
#     id1 = i1
#     bp = 0
#     while word1[i1] == word2[i2]:
#         if (i1 == len_word1) or  (i2 == len_word2):
#             break
#         id1 += 1
#         id2 += 1
#         bp += 1
#     return bp


# word1 = "leetcode"
# word2 = "etco"

# word11 = "sea"
# word22 = "eat"

# print("STEPS " + str(minDistance(word1, word2)))