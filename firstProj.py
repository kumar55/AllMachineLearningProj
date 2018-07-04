import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 5 x 2 matrix of randome numbers
x = np.linspace(2, 20, 10).reshape(5,2)

noise = np.random.uniform(-1.5, 1.5, 10)
