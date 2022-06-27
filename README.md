# gcode-tsp

This repo attempts to optimize the path taken by a CNC drill bit by using a greedy algorithm to solve the Traveling Salesman problem. 
The goal is to minimize the distance the bit travels in the air.

The command line program parses a G-code file given as input and outputs a new G-code file encoding a more efficient path.

#### Usage:
```shell
python3 main.py <input_file> <output_file>
```

An optional fourth parameter `plot` may be added which will additionally display a plot of the machine's path for visualization purposes. 
`matplotlib` is required to view the plot. Run `pip3 install matplotlib` to install.
