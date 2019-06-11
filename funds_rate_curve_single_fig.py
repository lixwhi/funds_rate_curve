import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# plot the funds rate curve
# find a way to make gif at different debt ceiling utilizations

# liquidation ratio
LR = 1.1
# debt ceiling utilization
DCU = 0.5
# debt ceiling rate offset
DCRO = 0.025
# volatility bias factor
VBF = 0.4



def fr_curve(x, y, lr, dcu, dcro, vbf):
	dcu_out = dcu_curve(dcu, dcro)
	return (1 / (100 * np.log(x - lr + 1))) + (vbf * y) + dcu_out

def dcu_curve(dcu, dcro):
	return pow((dcu - 0.5), 3) + dcro

x = np.linspace(LR+0.1, LR + 2, 70)
y = np.linspace(-0.05, 0.16, 50)

X, Y = np.meshgrid(x, y)
Z = fr_curve(X, Y, LR, DCU, DCRO, VBF)

# counter = 0
# num_frames = 100
# dc_util = np.linspace(0, 1, num_frames + 1)
# for i in range(0, num_frames):
#Z = fr_curve(X, Y, LR, dc_util[i], DCRO, VBF)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_xlabel('Collateralization Ratio (Liquidation={0})'.format(LR))
ax.set_ylabel('Funds Rate')
ax.set_zlabel('Stability Fee')
ax.set_zlim([-0.02, 0.2])
ax.set_title('Variable SF per Collateral Ratio\nDebt Ceiling Utilization: {0}\nVolatility Bias Factor={1}\nDebt Ceiling Rate Offset: {2}'.format(DCU, VBF, DCRO))
ax.view_init(35, -35)
#plt.savefig('out{0}'.format(i), dpi=80)
plt.show()










