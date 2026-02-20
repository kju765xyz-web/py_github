import matplotlib.pyplot as plt
import numpy as np

# Create a simple plot of a sine wave2
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid()
plt.show()
