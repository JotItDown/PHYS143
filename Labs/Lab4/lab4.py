import matplotlib.pyplot as plt
import math
from scipy.stats import linregress

y1 = [0.81, 1.46, 2.13, 2.64, 3.02, 3.33, 3.53, 3.74, 3.98, 4.22]
y = [math.log(((5)/(5-i))) for i in y1]
x = [4.4, 8.8, 13.2, 17.6, 22, 26.4, 30.8, 35.2, 39.6, 44]

fig, ax = plt.subplots()
ax.plot(x, y, color="#D33F49")

# Plot line of best fit
slope, intercept, r_value, p_value, std_err = linregress(x, y)
ax.plot(x, [slope * i + intercept for i in x], color="#0D5D56", linestyle='--')
ax.set_facecolor('#EBEBEB')
ax.set_axisbelow(True)
[ax.spines[side].set_visible(False) for side in ax.spines]
ax.grid()
ax.grid(which='major', color='white', linewidth=1.2)
ax.grid(which='minor', color='white', linewidth=0.6)
ax.minorticks_on()
ax.margins(0, 0)
ax.set_xlabel('Time (s)', fontweight ='bold')
ax.set_ylabel(r'ln($\dfrac{V}{V - V_C}$)', fontweight='bold')
ax.set_title("Time Constant ($\\tau$)", fontweight ='bold')
ax.legend(['Time Constant', 'Slope = {}'.format(slope.round(6))], loc='best')
print(slope, intercept, r_value, p_value, std_err)
# plt.show()
plt.savefig("PHYS143 Lab 4.png", format='png', dpi=2500, bbox_inches='tight')

