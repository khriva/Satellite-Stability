import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
from matplotlib.animation import FFMpegWriter
import matplotlib
from Integrator import getStatements, Statements
from matplotlib.patches import FancyArrowPatch
from Quaternions import get_ssk_to_iso
Const = 3.986 * (10 ** 14)
x=1*7*(10**6)
y = 0
z = 0
Vx = 0
Vy=(Const/x)**(1/2) - 2000
Vz=0
wz=0.001
wx=0.0001
wy=0.0001
xy=0
qw=1
qx=0
qy=0
qz=0
initial_state = np.array([x, y, z, Vx, Vy, Vz, wx, wy, wz,qw, qx, qy, qz])

Statements = getStatements(initial_state)




satellite_x= Statements[:,0]
satellite_y=Statements[:,1]
x_axis_vectors = []
y_axis_vectors = []
for i in Statements:
    vec = get_ssk_to_iso(i)
    x_axis_vectors.append([vec[0],vec[1]])
    y_axis_vectors.append([vec[3],vec[4]])






fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-8000, 8000)
ax.set_ylim(-8000,8000)
ax.set_aspect('equal')

# Параметры орбиты
orbit_radius = 7000  # Радиус орбиты
satellite_radius = 0.1  # Размер спутника (точки)

# Создаем орбиту (статика)
circle = plt.Circle((0, 0), orbit_radius, fill=False,
                    color='blue', linestyle='-', alpha=0.5)
ax.add_patch(circle)

# Земля в центре
earth = plt.Circle((0, 0), 6400, color='green', alpha=0.7)
ax.add_patch(earth)
satellite_point, = ax.plot([], [], 'ro', markersize=10, label='Спутник')
# Стрелки осей спутника (изначально пустые)
# X-ось спутника (красная)
sat_x_arrow = FancyArrowPatch((0, 0), (0, 0),
                             arrowstyle='->',
                             color='red',
                             linewidth=2,
                             mutation_scale=15)

# Y-ось спутника (зеленая)
sat_y_arrow = FancyArrowPatch((0, 0), (0, 0),
                             arrowstyle='->',
                             color='green',
                             linewidth=2,
                             mutation_scale=15)

# Z-ось (направление на Землю/от Земли) - синяя
sat_z_arrow = FancyArrowPatch((0, 0), (0, 0),
                             arrowstyle='->',
                             color='blue',
                             linewidth=2,
                             mutation_scale=15)
ax.add_patch(sat_x_arrow)
ax.add_patch(sat_y_arrow)
ax.add_patch(sat_z_arrow)


def init():
    satellite_point.set_data([], [])
    sat_x_arrow.set_positions((0, 0), (0, 0))
    sat_y_arrow.set_positions((0, 0), (0, 0))
    sat_z_arrow.set_positions((0, 0), (0, 0))
    return satellite_point, sat_x_arrow, sat_y_arrow, sat_z_arrow
