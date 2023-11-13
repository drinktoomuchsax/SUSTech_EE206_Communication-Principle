import pandas as pd
import os
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


def str_to_array(string):
    array = []
    # removing the first and last empty strings from the list
    string = string.split('\t')[1:-1]
    array = np.array([int(bit) for bit in string])
    return array


def calBER(a, b):
    if len(a) != len(b):
        raise ValueError("Arrays of unequal length")
    errorbits = sum(bit1 != bit2 for bit1, bit2 in zip(a, b))
    ber = errorbits / len(a)
    return ber


# list of file names
folder_path = 'lab7ProgramANDdata'

files = []

for i in range(24):
    file_name = str(i) + '.csv'
    files.append(file_name)


# initial ber
BERS = []

# loop over files
for i, file in enumerate(files):

    # read csv file into dataframe
    df = pd.read_csv(file)

    # initialize variables
    errorbits = 0
    size = len(df.columns)

    # turn the bits string into bits array
    # stupic asshole labview forget about the head row, i gotta manually add a head for every single file, fxxk!
    origin = str_to_array(df.iloc[0, 0])
    recover = str_to_array(df.iloc[1, 0])

    # compare origin and recover columns to calculate bit errors
    BER = calBER(origin, recover)
    BERS.append(BER)
    print(BERS)


# plot BER vs file index
# Create an x-axis array to match the length of BERS
x = np.arange(24)

# Smooth the curve
x_new = np.linspace(x.min(), x.max(), 300)
spline = make_interp_spline(x, BERS, k=3)
BERS_smooth = spline(x_new)

# Plot the graph
plt.plot(x_new, BERS_smooth)
# set plot parameters
plt.xlabel('E_b/N_0(dB)')
plt.ylabel('Bit Error Rate')
plt.title('BER vs E_b/N_0')
plt.plot(x_new, BERS_smooth, label="4-PSK")
plt.legend()
plt.show()
