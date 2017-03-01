s = "I love to write python"
for i in s:
    print i

print s[4]
print s[-1]
print len(s)
print s[0] + "\n", s[0][0][0]

split_s = s.split()
print split_s
for word in split_s:
    if word.find ("i") > -1:
        print "I found 'i' in: '{}'".format(word)
    elif word.find ("I") > -1:
        print "I found 'I' in: '{}'".format(word)
    else:
        print "Letters 'i' and 'I' not found in '{}'".format(word)

something = "Completely different"
print dir(something)
print something.count("t")
print something.find ("plete")
print something.split("e")
thing2 = something.replace("Different", "Silly") # this will not work, strings are immutable so can't be changed.
print thing2
something[0] = "B"
print something








