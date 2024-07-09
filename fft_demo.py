import numpy as np

# load data from csv file
data = np.loadtxt('data/NFO3163P1D230529N01T230BEV-44 001-000000A-000001.csv', delimiter=',')
print(f"{data.shape=}")

# apply fft to 3rd column
fft_result = np.fft.fft(data[:, 2])
print(f"{fft_result.shape=}")

# plot raw data and fft, on same figure, two subplots
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('TkAgg')  # or can use 'TkAgg', 'Qt5Agg', 'macosx'

fig, axs = plt.subplots(2)
axs[0].plot(data[:, 2])
axs[1].plot(np.abs(fft_result))
axs[1].set_ylim([0, 100])
plt.show()
