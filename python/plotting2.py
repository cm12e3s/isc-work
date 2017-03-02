#exercise1
import matplotlib.pyplot as plt 
fig, ax1 = plt.subplots()
time = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]
ax1.plot(time, co2, "b--")
ax1.set_ylabel("CO2]")
ax2 = ax1.twinx()
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
ax2.plot(time, temp, "r*-")
ax2.set_ylabel("Temp (degc)")
plt.show()

#exercise2
plt.subplot(1, 2, 3)
x = range(0, 10, 1)
plt.plot (x)
plt.subplot(1, 3, 2)
y = range(10, 0, -1)
plt.plot(y)
plt.subplot(1, 3, 3)
z = [4] * 10
plt.plot(z)
plt.show
