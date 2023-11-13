import matplotlib.pyplot as plt
import numpy as np
import random as ran

symbol_rate = 50  # kHz
step_size = 0.05
alphas = np.arange(0, 1.05, step_size)

roll_offs = [((-1 + alpha)+ran.random()*0.3)/2 for alpha in alphas]
bandwidths = [symbol_rate * (1 + roll_off) for roll_off in roll_offs]

plt.plot(alphas, bandwidths)
plt.xlabel('Alpha')
plt.ylabel('Bandwidth (kHz)')
plt.title('Relationship between alpha and bandwidth in 4QAM PSK modulation')
plt.show()
