import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from cube import Cube

# https://www.youtube.com/watch?v=ics0b1qupIc

def plot_cube(side1, side2, side3):
    cube = np.ones((side1, side2, side3), dtype = bool)
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.set_facecolor("Cyan")
    ax.voxels(cube, facecolor = "#E02050", edgecolors="k")
    ax.axis('on')
    #plt.plot()
    plt.show()
