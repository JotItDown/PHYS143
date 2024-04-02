import math
import matplotlib.pyplot as plt
from scipy.stats import linregress

y1 = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
y = [math.log(1- (i / 5)) for i in y1]
# x = [6.171, 4.5, 3.9, 3.0, 2.436, 2.488, 2.540, 1.6]
# x = [6.171, 4.5, 3.9, 3.0, 2.936, 2.540, 2.488, 1.6]
x = [6.171, 4.4, 3.4, 2.8, 2, 1.6, 1.1, 0.6]

fig, ax = plt.subplots()
ax.plot(x, y, color="#451F55")

# Plot line of best fit
slope, intercept, r_value, p_value, std_err = linregress(x, y)
ax.plot(x, [slope * i + intercept for i in x], color="#92AA83", linestyle='--')
ax.set_facecolor('#EBEBEB')
ax.set_axisbelow(True)
[ax.spines[side].set_visible(False) for side in ax.spines]
ax.grid()
ax.grid(which='major', color='white', linewidth=1.2)
ax.grid(which='minor', color='white', linewidth=0.6)
ax.minorticks_on()
ax.margins(0, 0)
ax.set_xlabel('Time (s)', fontweight ='bold')
ax.set_ylabel('Voltage (V)', fontweight ='bold')
ax.set_title("Voltage Across Capacitor $V_c$", fontweight ='bold')
ax.legend(['Voltage', 'Trendline'], loc='best')
print(slope, intercept, r_value, p_value, std_err)
# plt.show()
plt.savefig("PHYS143 Lab 3-2.png", format='png', dpi=2500, bbox_inches='tight')

