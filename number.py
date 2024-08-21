import math
import random
y = random.randint(1, 10)
print(y)
print(math.trunc(3.2))
# oct()
# hex()
# bin()
# int()
print(int("64", 8)) #octal
#bitwise operator
x = 1
x << 2 #left shift  
# decimal  {from decimal import Decimal}
# fraction {from fraction import Fraction}  


# Set
setone = {1, 2, 3, 4, 5}
print("union of set", setone | {6,7,8,9})
print("intersection of set", setone & {3, 5, 7, 4})
print(setone - {3, 9, 6})
