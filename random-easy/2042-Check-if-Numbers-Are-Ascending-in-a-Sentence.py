def areNumbersAscending(self, s: str) -> bool:
    _list = s.split()
    _max = float('-inf')
    for i in _list:
        if i.isdigit():
            tmp = int(i)
            if _max >= tmp:
                return False
            _max = tmp
    return True
            