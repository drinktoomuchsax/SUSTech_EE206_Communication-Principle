import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Example data
file_index = np.arange(24)
BERS = np.random.rand(24)

# Smooth the curve
x_new = np.linspace(file_index.min(), file_index.max(), 300)
spline = make_interp_spline(file_index, BERS, k=3)
BERS_smooth = spline(x_new)

# Plot the graph
plt.plot(x_new, BERS_smooth)
plt.xlabel('File Index')
plt.ylabel('BER')
plt.title('Smooth BER vs. File Index Curve')
plt.show()
