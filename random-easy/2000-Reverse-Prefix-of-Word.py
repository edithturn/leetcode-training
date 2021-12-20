class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stop = 0
        _reversed = []
        if ch in word:
            for i in word:
                _reversed.append(i)
                stop += 1
                if ch == i:
                    break
            _reversed.reverse()
            word = ''.join(_reversed) + word[stop:]
        return word
        