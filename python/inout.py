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

