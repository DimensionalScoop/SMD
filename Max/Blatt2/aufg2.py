print("Loading imports...")
import pandas as pd
import smd
import os
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
matplotlib.style.use('ggplot')


# import random numbers generated beforehand with aufg2_init.py
if not os.path.isfile("data/lin_con.csv"):
    print("Generating data...")
    import aufg2_init

print("Loading data...")
data_a = pd.DataFrame.from_csv("data/lin_con.csv")
data_b = pd.DataFrame.from_csv("data/trandom.csv")
data_c = pd.DataFrame.from_csv("data/lin_con_big.csv")

# b)


def histogram_plot(random_data, filename):
    smd.set_plot_size(smd.din_A4_portrait)
    random_data.hist(bins=50)
    plt.savefig(filename, dpi=300)

smd.add_process(lambda: histogram_plot(data_a, "fig/2a.pdf"))


# c)
def scatter_plot(random_data, filename):
    """Generates scatter plot from 1D array by using triplets of successive floats as x,y,z coordinates."""
    assert len(random_data) >= 3

    x = random_data[0::3]
    y = random_data[1::3]
    z = random_data[2::3]
    # cut arrays to same lenght
    min_lenght = min(len(x), len(y), len(z))
    x = x[:min_lenght - 1]
    y = y[:min_lenght - 1]
    z = z[:min_lenght - 1]

    fig = plt.figure(figsize=smd.din_A4_landscape)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, z, 'r+', zdir='y', zs=1.5)
    ax.plot(y, z, 'g+', zdir='x', zs=-0.5)
    ax.plot(x, y, 'k+', zdir='z', zs=-0.5)
    ax.scatter(x, y, z, s=5, lw=0)
    ax.set_xlim([-0.5, 1.5])
    ax.set_ylim([-0.5, 1.5])
    ax.set_zlim([-0.5, 1.5])
    fig.savefig(filename, dpi=300)


smd.add_process(lambda: scatter_plot(data_a["Anfangswert 2786"], "fig/2c.pdf"))


# e)
smd.add_process(lambda: histogram_plot(data_b, "fig/2e-1.pdf"))
smd.add_process(lambda: scatter_plot(data_b["Anfangswert 0"], "fig/2e-2.pdf"))


# f)
smd.add_process(lambda: print("# of generated 0.5s:\n", data_c[data_c == 0.5].count().value_counts()))

print("Running plots...")
smd.run_all()
print("Finished plots.")
