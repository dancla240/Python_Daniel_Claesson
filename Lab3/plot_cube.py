import matplotlib.pyplot as plt
import numpy as np


# Used this video as inspiration: https://www.youtube.com/watch?v=ics0b1qupIc

def plot_cube(side1, side2, side3):
    cube = np.ones((side1, side2, side3), dtype=bool)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    ax.voxels(cube, facecolors="#E02050", edgecolors="k")
    ax.axis('on')

    plt.show()