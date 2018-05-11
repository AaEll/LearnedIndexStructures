import numpy as np
import matplotlib as mpl
import pandas as pd
from numpy import genfromtxt
mpl.use('agg')
import matplotlib.pyplot as plt



data_to_plot = []
for x in range(4,20):
    csv = genfromtxt("Data/Data/outputLinfinity{0}.csv".format(x))
    data_to_plot.append(csv)
fig = plt.figure(1, figsize=(9, 6))
print(data_to_plot)
# Create an axes instance
ax = fig.add_subplot(111)
ax.set_yscale('log')
# Create the boxplot
bp = ax.boxplot(data_to_plot, positions=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])

# Save the figure
fig.savefig('fig1.png', bbox_inches='tight')
