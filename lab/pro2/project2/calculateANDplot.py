import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


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