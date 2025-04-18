import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

print(f"Python version: {sys.version}")
print(f"Matplotlib version: {matplotlib.__version__}")

# Create a simple plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y, label='sin(x)')
plt.title('Simple Matplotlib Test')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Try to show the plot with backend information
print(f"Matplotlib backend: {matplotlib.get_backend()}")
try:
    plt.show()
    print("Plot displayed successfully")
except Exception as e:
    print(f"Error displaying plot: {e}")

print("Test script completed") 