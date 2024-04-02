import matplotlib.pyplot as plt
from scipy.stats import linregress

y = [9.52, 7.54, 6.99, 5.95]
x1 = [10, 15, 20, 25]
x = [1/i for i in x1]

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
ax.set_xlabel('1/Length (1/m)', fontweight ='bold')
ax.set_ylabel('Magnetic Flux Density (G)', fontweight ='bold')
ax.set_title("Magnetic Field Constant ($\mu_0$)", fontweight ='bold')
ax.legend(['Magnetic Flux Density', 'Slope = {}'.format(slope.round(4))], loc='best')
print(slope, intercept, r_value, p_value, std_err)
# plt.show()
plt.savefig("PHYS143 Lab 5.png", format='png', dpi=2500, bbox_inches='tight')

