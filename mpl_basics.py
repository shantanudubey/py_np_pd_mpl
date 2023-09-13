import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

print("matplotlib version :", mpl.__version__)


# Plotting a Simple Graph
xvalues = np.linspace(0,2,100)
yvalues = np.linspace(0,2,100)
plt.plot(xvalues, yvalues)
plt.title("Simple Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
