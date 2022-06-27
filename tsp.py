from dataclasses import dataclass
from math import sqrt
from typing import Optional


@dataclass
class Point:
    x: float
    y: float

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __iter__(self):
        yield self.x
        yield self.y


@dataclass
class Node:
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
        return self.end if self.rev else self.start

    def get_end(self):
        return self.start if self.rev else self.end


def distance(p1: Point, p2: Point) -> float:
    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def tsp(nodes: list[Node]) -> list[Node]:
    curr = nodes[0]
    path = [curr]
    vis = {curr}

    while len(path) < len(nodes):
        dists = []

        for n in nodes:
            if n not in vis:
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
