class Solution:
    def toLowerCase(self, s: str) -> str:
        _len = len(s)
        for i in s:
            s += i.lower()
        return s[_len: len(s)]
        