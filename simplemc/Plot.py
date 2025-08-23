from getdist import MCSamples, plots
import matplotlib.pyplot as plt
import numpy as np

# Load the chain data
data1 = np.loadtxt('/Users/anilkandel/Documents/SimpleMC/simplemc/chains/CPL_phy_DESI+PLK18+PantheonPlus_mcmc_1.txt')

weights1 = np.ones(data1.shape[0])

# Adjust this slice based on your actual parameter count
params1 = data1[:, 0:7]  # First 7 parameters

# Define parameter names and labels - FIXED: added missing param4
param_names = ['param1', 'param2', 'Om', 'Obh2', 'h', 'w0', 'wa']  # Changed to meaningful names
param_labels = ['Param1', 'Param2', r'\Omega_m', r'\Omega_b h^2', r'h', r'\omega_{0}', r'\omega_{a}']

# Create MCSamples object
samples1 = MCSamples(samples=params1, weights=weights1, names=param_names, labels=param_labels)

# Set up the plotter
g = plots.getSubplotPlotter(width_inch=6.0)
g.settings.figure_legend_frame = True
g.settings.alpha_filled_add = 0.6
g.settings.title_limit_fontsize = 9
g.settings.axes_labelsize = 12
g.settings.legend_fontsize = 12
g.settings.colorbar_axes_fontsize = 12

# ------------------- Full Triangle Plot -------------------
g.triangle_plot([samples1],
                ['Om', 'h', 'w0', 'wa'],  # Use the new parameter names
                filled=True,
                contour_colors=['orange'],
                legend_loc='upper right',
                legend_labels=[r'DESI+PLK18+PantheonPlus'])

# Export the full triangle plot
g.export("triangle_CPL.pdf")

# ------------------- 2D Plot for w0 and wa -------------------
g2d = plots.get_single_plotter(width_inch=6)
g2d.settings.figure_legend_frame = True
g2d.settings.alpha_filled_add = 0.7
g2d.settings.axes_labelsize = 10
g2d.settings.legend_fontsize = 10

# Create a 2D plot for w0 and wa
g2d.plot_2d(
    [samples1],
    param_pair=['w0', 'wa'],  # Use the new parameter names
    filled=True,
    colors=['orange'],
)

# Add vertical line at x = -1 and horizontal line at y = 0
plt.axvline(x=-1, color='gray', linestyle='--', linewidth=1.2)
plt.axhline(y=0, color='gray', linestyle='--', linewidth=1.2)

# Set the range for x-axis (w0) and y-axis (wa)
plt.xlim(-1.1, 0)
plt.ylim(-3, 1)

g2d.add_legend(legend_labels=[r'DESI+PLK18+PantheonPlus'], fontsize=9, legend_loc='upper right')

# Export the 2D plot for w0 and wa
g2d.export("w0_wa_2d_CPL.pdf")

# ------------------- Second 2D Plot with different settings -------------------
g2d1 = plots.get_single_plotter(width_inch=6)
g2d1.settings.figure_legend_frame = True
g2d1.settings.alpha_filled_add = 0.7
g2d1.settings.axes_labelsize = 13
g2d1.settings.legend_fontsize = 13

# Create another 2D plot for w0 and wa
g2d1.plot_2d(
    [samples1],
    param_pair=['w0', 'wa'],
    filled=True,
    colors=['orange'],
)

# Add vertical line at x = -1 and horizontal line at y = 0
plt.axvline(x=-1, color='gray', linestyle='--', linewidth=1.2)
plt.axhline(y=0, color='gray', linestyle='--', linewidth=1.2)

g2d1.add_legend(legend_labels=[r'DESI+PLK18+PantheonPlus'], fontsize=10, legend_loc='upper right')

# Export the second 2D plot
g2d1.export("w0_wa_2d_CPL_low_sn.pdf")
