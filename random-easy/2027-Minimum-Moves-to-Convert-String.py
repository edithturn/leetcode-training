def minimumMoves(s):
    """
    Taking a windows of 03
    """
    moves = 0
    c = 0
    while c < len(s):
        if s[c] == 'X':
            c += 3
            moves +=1
            continue
        c += 1
    return moves
    
print(minimumMoves("XXX"))  # 1
print(minimumMoves("XXOX")) # 2
print(minimumMoves("OOOO")) # 0