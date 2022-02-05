def countGoodSubstrings(self, s: str) -> int:
    count = 0
    for i in range(0, len(s) - 2):
        if len(set(s[i: i + 3])) == 3:
            count += 1
    return count
    

print(countGoodSubstrings("xyzzaz"))  # 1
print(countGoodSubstrings("aababcabc")) # 4