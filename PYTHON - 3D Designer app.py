import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Designer3D:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_title("3D Designer")
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_zlabel('Z-axis')

    def add_cube(self, origin, size):
        x, y, z = origin
        dx, dy, dz = size
        xx = [x, x+dx, x+dx, x, x, x+dx, x+dx, x]
        yy = [y, y, y+dy, y+dy, y, y, y+dy, y+dy]
        zz = [z, z, z, z, z+dz, z+dz, z+dz, z+dz]
        verts = [
            [xx[0:4], yy[0:4], zz[0:4]],
            [xx[4:8], yy[4:8], zz[4:8]],
            [xx[0:2]+xx[6:8], yy[0:2]+yy[6:8], zz[0:2]+zz[6:8]],
            [xx[2:4]+xx[4:6], yy[2:4]+yy[4:6], zz[2:4]+zz[4:6]],
        ]
        for v in verts:
            self.ax.plot_surface(*v, alpha=0.5, color='blue')

    def add_sphere(self, center, radius):
        u, v = np.linspace(0, 2 * np.pi, 100), np.linspace(0, np.pi, 100)
        x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
        y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
        z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
        self.ax.plot_surface(x, y, z, color='green', alpha=0.6)

    def add_cylinder(self, base_center, radius, height):
        z = np.linspace(base_center[2], base_center[2] + height, 50)
        theta = np.linspace(0, 2 * np.pi, 50)
        theta_grid, z_grid = np.meshgrid(theta, z)
        x_grid = radius * np.cos(theta_grid) + base_center[0]
        y_grid = radius * np.sin(theta_grid) + base_center[1]
        self.ax.plot_surface(x_grid, y_grid, z_grid, color='red', alpha=0.6)

    def show(self):
        plt.show()

# Create a 3D designer instance
designer = Designer3D()

# Add shapes
designer.add_cube(origin=(0, 0, 0), size=(1, 1, 1))  # Cube at (0,0,0) with size 1x1x1
designer.add_sphere(center=(2, 2, 2), radius=1)      # Sphere at (2,2,2) with radius 1
designer.add_cylinder(base_center=(4, 4, 0), radius=1, height=2)  # Cylinder at (4,4,0) with radius 1 and height 2

# Show the design
designer.show()
