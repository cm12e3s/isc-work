#exercise1
a = set([1 ,2, 3, 4, 5])
b = set([2, 4, 6, 8])
print a.union(b)
print a.intersection(b)

#exercise2
band = ["mel", "geri", "victoria", "mel", "emma"]
counts = { }
for member in band:
    if member not in counts:
        counts[member] = 1
    else:
        counts[member] += 1

for member in counts:
    print member, counts[member]

#exercise3

