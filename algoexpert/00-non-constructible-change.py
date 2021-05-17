def nonConstructibleChange(coins):
    # Write your code here.
    _sum = 0
    new_a = []
    if min(coins) == max(coins):
        _max = len(coins) + 1
        flag = 0
    else:
        _max = max(coins)
        flag = 1
    print(f"Max {_max}")
    print(f"coins {coins}")
    for i in range(len(coins) - flag):
        j = i + 1
        for j in coins:
            _sum = coins[i] + coins[j]
            new_a.append(_sum)
            print(_sum)
        new_a.append(coins[i])

    result = 0
    new_a.sort()
    print(f"New A {new_a}")
    for i in new_a:
        print(i)
        if i + 1 not in new_a:
            #print(i)
            result = i + 1
            break
    return result


coins1 = [1, 1, 1, 1, 1]
print(f"Resulf {nonConstructibleChange(coins1)}")

coins3 = [5, 7, 1, 1, 2, 3, 22]
print(f"Resulf {nonConstructibleChange(coins3)}")

#coins2 = [1, 2 , 5]
#print(f"Resulf {nonConstructibleChange(coins2)}")


#coins4 = [6, 4, 5, 1, 1, 8, 9]
#print(f"Resulf {nonConstructibleChange(coins4)}")

#coins5 =   [6, 4, 5, 1, 1, 8, 9]
#print(f"Resulf {nonConstructibleChange(coins5)}")