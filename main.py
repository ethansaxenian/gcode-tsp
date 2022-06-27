import sys

from parse_gcode import GCODE_END, GCODE_START, get_lines_for_node, parse_gcode_file
from plot_nodes import plot_nodes
from tsp import tsp

if len(sys.argv) < 3:
    print("Usage: python3 main.py <input_file> <output_file>")
    sys.exit(1)

nodes = parse_gcode_file(sys.argv[1])
path = tsp(nodes)

with open(sys.argv[2], "w") as file:
    file.write(GCODE_START)
    for node in path:
        for line in get_lines_for_node(node):
            file.write(line)
    file.write(GCODE_END)

if len(sys.argv) == 4 and sys.argv[3] == "plot":
    plot_nodes(path)
