with open("weather.csv","r") as reader:
    data = reader.read()
print data

with open("weather.csv", "r") as reader:
    line = reader.readline()
    while line:
        print line
        line = reader.readline()
print "It's over" 

with open("weather.csv", "r") as reader:
    header = reader.readline()
    rain = []
    for line in reader.readlines():
        r = line.strip().split(",")[-1]
        r = float(r)
        rain.append(r)
print rain

with open("myrain.txt", "w") as writer:
    for r in rain:
        writer.write(str(r) + "\n")

import struct

bin_data = struct.pack("bbbb", 123, 12, 45, 34)

with open("mybinary.txt", "wb") as bwriter:
        bwriter.write(bin_data)

with open("mybinary.txt", "rb") as breader:
    bin_data2 = breader.read()

data = struct.unpack("bbbb", bin_data2)
print data


   


