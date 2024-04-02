import matplotlib.pyplot as plt
import math
from scipy.stats import linregress

x = [8.214, 7.408, 6.879, 5.490, 5.196] # Frequency
y4 = [1.836, 1.576, 1.384, 0.884, 0.771] # Stopping Potential - Aperture 4 mm
y2 = [1.841, 1.678, 1.406, 0.912, 0.787] # Stopping Potential - Aperture 2 mm
y8 = [1.806, 1.572, 1.389, 0.880, 0.761] # Stopping Potential - Aperture 8 mm
fig, ax = plt.subplots()
ax.plot(x, y4, color="#D33F49")

# Plot line of best fit
slope, intercept, r_value, p_value, std_err = linregress(x, y4)
ax.plot(x, [slope * i + intercept for i in x], color="#0D5D56", linestyle='--')
ax.set_facecolor('#EBEBEB')
ax.set_axisbelow(True)
[ax.spines[side].set_visible(False) for side in ax.spines]
ax.grid()
ax.grid(which='major', color='white', linewidth=1.2)
ax.grid(which='minor', color='white', linewidth=0.6)
ax.minorticks_on()
ax.margins(0, 0)
ax.set_xlabel('Frequency (x $10^{14}$ Hz) ($\\lambda$)', fontweight ='bold')
ax.set_ylabel("Stopping Potential (V)", fontweight='bold')
ax.set_title("Stopping Potential vs Frequency", fontweight ='bold')
ax.legend(['Stopping Potential vs Frequency', 'Slope = h/e = {}'.format(slope.round(4))], loc='best')
print(slope, intercept, r_value, p_value, std_err)
# plt.show()
plt.savefig("PHYS143 Lab 9 - 1.png", format='png', dpi=2500, bbox_inches='tight')

# Clear the plot to make a new plot
plt.clf()
fig, ax = plt.subplots()
ax.plot(x, y2, color="#D33F49")

# Plot line of best fit
slope, intercept, r_value, p_value, std_err = linregress(x, y2)
ax.plot(x, [slope * i + intercept for i in x], color="#0D5D56", linestyle='--')
ax.set_facecolor('#EBEBEB')
ax.set_axisbelow(True)
[ax.spines[side].set_visible(False) for side in ax.spines]
ax.grid()
ax.grid(which='major', color='white', linewidth=1.2)
ax.grid(which='minor', color='white', linewidth=0.6)
ax.minorticks_on()
ax.margins(0, 0)
ax.set_xlabel('Frequency (x $10^{14}$ Hz) ($\\lambda$)', fontweight ='bold')
ax.set_ylabel("Stopping Potential (V)", fontweight='bold')
ax.set_title("Stopping Potential vs Frequency", fontweight ='bold')
ax.legend(['Stopping Potential vs Frequency', 'Slope = h/e = {}'.format(slope.round(4))], loc='best')
print(slope, intercept, r_value, p_value, std_err)
# plt.show()
plt.savefig("PHYS143 Lab 9 - 2.png", format='png', dpi=2500, bbox_inches='tight')

# Clear the plot to make a new plot
plt.clf()
fig, ax = plt.subplots()
ax.plot(x, y8, color="#D33F49")

# Plot line of best fit
slope, intercept, r_value, p_value, std_err = linregress(x, y8)
ax.plot(x, [slope * i + intercept for i in x], color="#0D5D56", linestyle='--')
ax.set_facecolor('#EBEBEB')
ax.set_axisbelow(True)
[ax.spines[side].set_visible(False) for side in ax.spines]
ax.grid()
ax.grid(which='major', color='white', linewidth=1.2)
ax.grid(which='minor', color='white', linewidth=0.6)
ax.minorticks_on()
ax.margins(0, 0)
ax.set_xlabel('Frequency (x $10^{14}$ Hz) ($\\lambda$)', fontweight ='bold')
ax.set_ylabel("Stopping Potential (V)", fontweight='bold')
ax.set_title("Stopping Potential vs Frequency", fontweight ='bold')
ax.legend(['Stopping Potential vs Frequency', 'Slope = h/e = {}'.format(slope.round(4))], loc='best')
print(slope, intercept, r_value, p_value, std_err)
# plt.show()
plt.savefig("PHYS143 Lab 9 - 3.png", format='png', dpi=2500, bbox_inches='tight')
