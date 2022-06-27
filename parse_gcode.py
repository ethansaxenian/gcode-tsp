from tsp import Node, Point

# sets tool description and spindle speed
GCODE_START = "g21 g90 g91.1\nm6 t102\nm3 s18000\ng21 g90 g91.1\n"

# stops the spindle and ends the program
GCODE_END = "s0\nm5\nm30\n"


def parse_gcode_file(path: str):
    """
    Parses a G-code file and returns a list of nodes representing the segments that the bit moves through.
    """
    with open(path, 'r') as file:
        nodes = []
        node = None
        x, y = 0, 0
        id = 0
        for line in file:
            # 'g0' denotes the start and end of a new path
            if line.startswith("g0"):
                if "x" in line and "y" in line:
                    components = line.split(" ")
                    x = float(components[1][1:])
                    y = float(components[2][1:])
                    # create a new node as the start of a new segment
                    node = Node(id=id, start=Point(x, y), end=None, lines=[line])
                elif node is not None:
                    # add the node to the list of nodes when a segment ends
                    node.end = Point(x, y)
                    nodes.append(node)
                    node.lines.append(line)
                    node = None
                    id += 1
            # 'g1' denotes movement of the bit. These instructions are saved with the node.
            elif line.startswith("g1"):
                components = line.split(" ")
                # track the x and y coordinates of the bit so we know where the segment ends
                for c in components:
                    if c.startswith("x"):
                        x = float(c[1:])
                    elif c.startswith("y"):
                        y = float(c[1:])
                node.lines.append(line)

    return nodes


def get_lines_for_node(node: Node) -> list[str]:
    """
    Returns the lines that make up the segment that the node represents. The lines are reversed if necessary.
    """
    if not node.rev:
        return node.lines

    new_lines = [f"g0 x{node.end.x} y{node.end.y}\n"]
    for line in reversed(node.lines[1:-1]):
        new_lines.append(line)
    new_lines.append(node.lines[-1])

    return new_lines
