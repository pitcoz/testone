# encoding : utf-8
import matplotlib.pyplot as plt
import pandas as pd
import numpy as ny
import tools

# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.plot([0,1,3, 5], [0, 1, 10, 33], linewidth=5, linestyle='--', color='y', label='--')
# x = range(0, 20)
x = ny.linspace(0,2,20)
y = ny.linspace(0,3,10)
# x = range(9)
# y = [((-1)**i) for i in x]

# y = [i**n for i in x]
# y = [ny.sin(i) for i in x]
# fig, axed = plt.figure(figsize=[800, 800])
# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)

fig, (axs) = plt.subplots(2, 2, sharex='all', sharey='all')

axs[0, 0].plot(y, y**2, label='quadratic', linestyle='solid')
axs[0, 0].legend()
axs[0, 1].plot(x, x**3, label='3times', linestyle=':')
axs[1, 0].plot(x, x, label='line', linestyle='--')
axs[1, 0].plot(y, y**2, label='quadratic', linestyle='solid')
axs[1, 1].plot(y, y**2, label='quadratic', linestyle='solid')
axs[1, 1].plot(x, x**3, label='3times', linestyle=':')
axs[1, 1].plot(x, x, label='line', linestyle='--')
plt.legend()
plt.show()
