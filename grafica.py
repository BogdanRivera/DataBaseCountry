
import matplotlib.pyplot as plt


def grafics(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()
