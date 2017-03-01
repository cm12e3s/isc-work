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
    if word.find ("i") > -1 or word.find("I") > -1:
        print "I found 'i' in: '{}'".format(word)


