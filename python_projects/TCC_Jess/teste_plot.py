import matplotlib.pyplot as plt
from matplotlib.ticker import LogFormatter
import numpy as np

fig, axes = plt.subplots(4, figsize=(12, 24))

dt = 0.01
t = np.arange(dt, 20.0, dt)

# first plot doesn't use a formatter
axes[0].semilogx(t, np.exp(-t / 5.0))
axes[0].set_xlim([0, 25])
axes[0].grid()

xlims = [[0, 25], [0.2, 8], [0.6, 0.9]]

for ax, xlim in zip(axes[1:], xlims):
    ax.semilogx(t, np.exp(-t / 5.0))
    formatter = LogFormatter(labelOnlyBase=False,
                             minor_thresholds=(2, 0.4))

    ax.get_xaxis().set_minor_formatter(formatter)
    ax.set_xlim(xlim)
    ax.grid()

plt.show()