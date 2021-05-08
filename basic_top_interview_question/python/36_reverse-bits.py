def reverseBits(self, n: int) -> int:
    res = 0
    power = 31
    while n:
        # if n == 1 then operate with 1, it n == 0the noperate with 0 | moving bit to left and add it to the res
        res = res + ((n & 1) << power)        
        # Updating n with the new with in the right position
        n = n >> 1
        # Decrease power in the previos value: 2^31 2^30...2^2 2^1 2^0
        power -= 1
        print(power)
    return res
