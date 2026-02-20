import matplotlib.pyplot as plt
import numpy as np

# Create a simple plot of a sine wave2
x = np.linspace(0, 10, 100)
y = np.sin(x)



# second branching
plt.plot(x, y, label='sin(x)', color='red')
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid()
plt.legend()
plt.show()
