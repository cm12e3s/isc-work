import matplotlib.pyplot as plt

plt.plot(range(10))
plt.show()

time = range(7)
co2 = [250, 265, 272, 360, 300, 320, 389]
plt.plot(time, co2)
plt.plot(time, co2, 'b--')
plt.title("Concentration of CO2 versus time")
plt.ylabel("[CO2]")
plt.xlabel("Time(decade)")
plt.show()

temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 2.2]
plt.plot(time, co2, 'b--', time, temp, 'r*-')
plt.show()
plt.savefig("co2_temp.pdf")


