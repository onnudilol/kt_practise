from collections import defaultdict

vertices = {'a': {'b': 7, 'c': 9, 'f': 14},
            'b': {'c': 10, 'd': 15},
            'c': {'d': 11, 'f': 2},
            'd': {'e': 6},
            'e': {'f': 9}}

# Creating defaultdict from vertices with an empty dictionary as the default.
# Prevents key errors when adding end point nodes.

graph = defaultdict(lambda: defaultdict(dict))

for key, value in vertices.items():
    graph[key] = value


class PQDijkstra:
    """
    A hastily implemented priority queue for use with dijkstra().
    """
    # TODO: Maybe make this a subclass of queue.PriorityQueue

    def __init__(self):
        self.queue = list()

    def __repr__(self):
        return '<PQDijkstra {}>'.format(self.queue)

    def __str__(self):
        return self.queue

    def __iter__(self):
        return iter(self.queue)

    def __getitem__(self, item):
        return self.queue[item]

    def is_empty(self):
        return len(self.queue) == 0

    def add(self, item):
        self.queue.append(item)

    def remove(self, item):
        for x in self.queue:
            if x.name == item:
                self.queue.remove(x)

    def get_min(self):
            self.queue.sort(key=lambda x: x.distance)
            return self.queue.pop(0)


class Node:
    def __init__(self, name, child):
        self.name = name
        self.children_weights = child
        self.children = list(child.keys())
        self.parent = None
        self.distance = float('inf')

    def __repr__(self):
        return '<Node {}>'.format(self.name)

    def get_parent(self):
        return str(self.parent)

    def get_closest(self):
        return min(self.children_weights)


def dijkstra(graph, start, end):
    """
    Greedy algorithm that returns the shortest path from start to end.  Uses PQDijkstra to implement the priority queue
    version of the algorithm.
    """
    path = list()
    nodes = PQDijkstra()
    vertices = list()

    # TODO: simplify the setup

    for x, y in graph.items():
        vertices.append(x)
        vertices += list(y.keys())

    vertices_unique = set(vertices)

    for vertex in vertices_unique:
        i = Node(vertex, graph[vertex])
        nodes.add(i)

    for node in nodes:
        if node.name == start:
            node.distance = 0

    while not nodes.is_empty():

        node = nodes.get_min()

        path.append(node)

        for child in node.children:
            alt = node.distance + node.children_weights[child]
            for x in nodes:
                if x.name == child:
                    if alt < x.distance:
                        x.distance = alt
                        x.parent = node.name

    shortest_path = list()
    shortest_path = [x for x in path if x.name == end]

    while shortest_path[0].parent is not None:
        for x in path:
            if x.name == shortest_path[0].parent:
                shortest_path.insert(0, x)

    return shortest_path
