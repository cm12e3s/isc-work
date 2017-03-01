t = (1,)
print t[-1]

l = range(100, 201)
l.append(201)
print l[-1]
tup = tuple(l)
print tup[0], tup[-1]

mylist = [23, "hi", 2.4e-10]
for (count, item) in enumerate(mylist):
    print count, item

(first, middle, last) = mylist
print first, middle, last
(first, middle, last) = (last, middle, first)
print first, middle, last

