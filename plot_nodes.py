import matplotlib.pyplot as plt

from tsp import Node


def plot_nodes(nodes: list[Node], label_nodes: bool = False):
    start = nodes[0].get_end()
    end = nodes[1].get_start()

    for i in range(len(nodes[1:])):
        if i > 0:
            xs, ys = tuple(start)
            xe, ye = tuple(end)
            plt.scatter(xs, ys, color="blue", marker=".")
            plt.scatter(xe, ye, color="red", marker=".")
            plt.plot([xs, xe], [ys, ye], color="black")

        start = nodes[i].get_end()
        end = nodes[i+1].get_start()

    for i, node in enumerate(nodes):
        xs, ys = tuple(node.start)
        xe, ye = tuple(node.end)
        if label_nodes:
            plt.annotate(f"{node.id}s", (xs, ys))
            plt.annotate(f"{node.id}e", (xe, ye))
        plt.plot([xs, xe], [ys, ye], ":", color="gray")

    plt.show()
    plt.close()
