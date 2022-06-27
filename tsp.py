from dataclasses import dataclass
from math import sqrt
from typing import Optional


@dataclass
class Point:
    """
    Encodes a point in 2D space.
    """
    x: float
    y: float

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __iter__(self):
        yield self.x
        yield self.y


@dataclass
class Node:
    """
    A 'Node' represents a segment of the path that the CNC bit takes while in the air.

    id: the ID of the node
    lines: the lines of G-code that make up the path
    start: the start point of the path
    end: the end point of the path
    rev: whether the path is reversed (note that this will eventually reverse the list of lines)
    """
    id: int
    lines: list[str]
    start: Point
    end: Optional[Point]
    rev = False

    def __repr__(self):
        return str(self.id)

    def __hash__(self):
        return hash(((self.start.x, self.start.y), (self.end.x, self.end.y)))

    def get_start(self):
        """
        Returns the start point of the path and takes into account whether the path is reversed.
        """
        return self.end if self.rev else self.start

    def get_end(self):
        """
        Returns the end point of the path and takes into account whether the path is reversed.
        """
        return self.start if self.rev else self.end


def distance(p1: Point, p2: Point) -> float:
    """
    Returns the Euclidean distance between two points.
    """
    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def tsp(nodes: list[Node]) -> list[Node]:
    """
    Solves the Traveling Salesman problem using a greedy algorithm.

    :param nodes: A list of nodes encoding an unoptimized path.
    :return: A list of nodes encoding a more optimal path.
    """
    curr = nodes[0]
    path = [curr]
    vis = {curr}

    while len(path) < len(nodes):
        dists = []

        for n in nodes:
            if n not in vis:
                # calculate the distance from the current node both the start and end points of each other node
                dist_to_start = distance(curr.get_end(), n.start)
                dist_to_end = distance(curr.get_end(), n.end)
                if dist_to_end < dist_to_start:
                    dists.append((n, dist_to_end, True))
                else:
                    dists.append((n, dist_to_start, False))

        node, dist, needs_rev = min(dists, key=lambda x: x[1])
        node.rev = needs_rev

        path.append(node)
        vis.add(node)
        curr = node

    return path
