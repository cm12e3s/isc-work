# exercise 1
a = [0, 1, 2]
b = a
print a, b
b[0] = "hello"
print a, b
a.append(3)
print a, b

# exercise 2
c = "can I change"
d = c
print c, d
d = "different"
print c, d

import copy

a =[0, 1, 2]
b = copy.deepcopy(a)
print a, b
b[0] = "hello"
print a, b
