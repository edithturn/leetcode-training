# loops
fam = [1.67, 1.68, 1.55, 1.55, 1.30]

for index, height in enumerate(fam):
    print("Index " + str(index) + " : " + str(height))


# Priting a range of numbers
for i in range(0,20, 2):
    print(i)

# Example from input in loops
#repeat = input("Type a number: ")
repeat = int('2')

for i in range(repeat):
    print(i)

# Is Statement inside a loop, continue,  break
#repeat = input("Insert number: ")
repeat = int(repeat)

for i in range(20):
    option = 8 # input("skip, print or exit")
    if option == "print":
        print(i)
    elif option == "skip":
        continue
    elif option == "exit":
        break
print("Goodbye!")

# Printing prices

present_price = []

for i in range(5):
    price = input("Insert price: ")
    price = float(price)
    present_price.append(price)

print(present_price)
