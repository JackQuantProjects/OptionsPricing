from Data import buildSurface
import numpy as np
import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from scipy.interpolate import RBFInterpolator

SMOOTH = True


x, y, z = buildSurface()

# Create regular grid
T_grid = np.linspace(x.min(), x.max(), 50)
K_grid = np.linspace(y.min(), y.max(), 50)

T_mesh, K_mesh = np.meshgrid(T_grid, K_grid)

# Interpolate IV onto grid

if SMOOTH:

    T_scaled = (x - x.mean()) / x.std()
    K_scaled = (y - y.mean()) / y.std()

    points = np.column_stack((T_scaled, K_scaled))

    rbf = RBFInterpolator(
        points,
        z,
        smoothing=0.1
    )

    T_mesh_scaled = (T_mesh - x.mean()) / x.std()
    K_mesh_scaled = (K_mesh - y.mean()) / y.std()

    grid_points = np.column_stack((
        T_mesh_scaled.ravel(),
        K_mesh_scaled.ravel()
    ))

    IV_mesh = rbf(grid_points).reshape(T_mesh.shape)

else:

    IV_mesh = griddata(
        (x, y),
        z,
        (T_mesh, K_mesh),
        method="linear"
    )

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")

surface = ax.plot_surface(
    T_mesh * 365,
    K_mesh,
    IV_mesh * 100,
    cmap="gnuplot2",
    edgecolor="none",
    antialiased=True
)

ax.set_xlabel("Days to Maturity", labelpad=10)
ax.set_ylabel("Strike", labelpad=10)
ax.set_zlabel("Implied Volatility (%)", labelpad=10)

ax.set_title(
    "Implied Volatility Surface",
    pad=20
)

cbar = fig.colorbar(
    surface,
    ax=ax,
    shrink=0.6,
    pad=0.1
)

cbar.set_label("Implied Volatility (%)")

ax.view_init(
    elev=25,
    azim=-130
)

plt.tight_layout()
plt.show()
