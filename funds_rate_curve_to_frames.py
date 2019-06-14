import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d
from matplotlib.colors import LinearSegmentedColormap

# plot the funds rate curve
# find a way to make gif at different debt ceiling utilizations

# liquidation ratio
LR = 1.5
# debt ceiling utilization
DCU = 0.905
# debt ceiling rate offset
DCRO = 0.025
# volatility bias factor
VBF = 2



def fr_curve(x, y, lr, dcu, dcro, vbf):
	dcu_out = dcu_curve(dcu, dcro)
	return (1 / (100 * np.log(x - lr + 1))) + (vbf * y) + dcu_out

def dcu_curve(dcu, dcro):
	return pow((dcu - 0.5), 3) + dcro

x = np.linspace(LR+0.1, LR + 2, 70)
y = np.linspace(-0.02, 0.06, 50)

X, Y = np.meshgrid(x, y)
Z = fr_curve(X, Y, LR, DCU, DCRO, VBF)

cmap = plt.get_cmap('rainbow_r')
start = 0.2
stop = 1
colors = cmap(np.linspace(start, stop, cmap.N))
color_map = LinearSegmentedColormap.from_list('Upper Half', colors)
counter = 0
num_frames = 120
init_x_view = 35
final_x_view = 32
init_y_view = -55
final_y_view = -60
x_view = np.linspace(init_x_view, final_x_view, num_frames)
y_view = np.linspace(init_y_view, final_y_view, num_frames)
dc_util1 = np.linspace(0, 1, num_frames / 2)
dc_util2 = np.linspace(1, 0, num_frames / 2)
dc_util = np.concatenate((dc_util1, dc_util2))
for i in range(0, num_frames):
	Z = fr_curve(X, Y, LR, dc_util[i], DCRO, VBF)
	fig = plt.figure()
	ax = plt.axes(projection='3d')
	surf = ax.plot_surface(X, Y, Z,  cmap=color_map, vmin=-0.02, vmax=0.5, edgecolor='none', linewidth=0, antialiased=True)
	ax.set_xlabel('Collateralization Ratio (Liquidation={0})'.format(LR))
	ax.set_ylabel('Funds Rate')
	ax.set_zlabel('Stability Fee')
	ax.set_zlim([-0.1, 0.5])
	#plt.pcolor(X, Y, Z, cmap=color_map, vmin=-0.02, vmax=0.5)
	#ax.spines['bottom'].set_color('red')
	#ax.spines['top'].set_color('#11')
	ax.set_title('Variable SF per Collateral Ratio with Debt Ceiling Utilization: {0}\nVolatility Bias Factor={1}\nDebt Ceiling Rate Offset: {2}'.format(round(dc_util[i], 2), VBF, DCRO))
	#ax.text(x=45, y=-35, z=90, s="Debt Ceiling Utilization: {0}".format(round(dc_util[i], 2)))
	ax.view_init(x_view[i], y_view[i])
	fig.colorbar(surf, ax=ax, shrink=0.8, aspect=8)
	plt.savefig('out{0}'.format(i), dpi=160)











