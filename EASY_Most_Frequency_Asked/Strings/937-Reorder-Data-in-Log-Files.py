# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:
# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:

# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.

# Example 1:
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

# Example 2:
# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


def reorderLogFiles(logs):
    """
    First Approach Force Brute using lambda

    ||======= Big O ======= ||
    - Time complexity : O(n)
    - Space complexity: O(1)​
    """
    final_d = []
    final_l = []

    for i in range(len(logs)):
        if logs[i][-1].isdigit():
            final_d.append(logs[i])
        else:
            final_l.append(logs[i].split())

    final_l.sort(key=lambda x :x[0])
    final_l.sort(key=lambda x :x[:1])

    for n in range(len(final_l)):
        final_l[n] = (" ".join(final_l[n]))
        final_d.insert(n, final_l[n])

    return final_d

# Test Cases

logs1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
logs3 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

print(reorderLogFiles(logs1))
print(reorderLogFiles(logs2))
print(reorderLogFiles(logs3))