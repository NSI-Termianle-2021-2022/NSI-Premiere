from math import *

l = [1, 2, 3, 4, 5]

l2 = l

l3 = [i - 6 for i in l]

l4 = [(i*3)+2 for i in l]

l5 = [(i*2)-2 for i in l]

l6 = [i**2 for i in l if i**2 > 15]

l7 = [for j in range(1, 399, 2) for i in l]

print(l, l2, l3, l4, l5, l6, l7)

