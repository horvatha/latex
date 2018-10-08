x = [1, 2, 3, 4, 5]
y = [3, 5, 2, 7, -1]
plt.plot(x, y)
plt.plot(x, y, 'x')
plt.savefig('first.pdf')
plt.close()

x = np.linspace(0, np.pi, 777)
y = np.sin(x)
plt.plot(x, np.sin(x), 'r--', label='sin(x)')
plt.plot(x, np.sin(x)*np.cos(x), 'b:', label='sin(x)cos(x)')
plt.plot(x, np.sin(2*x), 'g-', label='sin(2x)')
plt.legend(loc='upper right')
plt.title('Trigonometry')
plt.xlabel('$\phi$ (radians)')
plt.ylabel('y')
plt.grid(True)
