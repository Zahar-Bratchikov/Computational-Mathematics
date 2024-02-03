import matplotlib.pyplot as plt

x = list(range(-10, 11))
y = [i ** 2 for i in x]
z = [i ** 3 for i in x]

plt.plot(x, y, x, z)
plt.show()
