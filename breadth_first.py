graph = {'1': ['2', '3'],
         '2': ['1', '3', '4', '5'],
         '3': ['1', '2', '5', '7', '8'],
         '4': ['2', '5'],
         '5': ['2', '3', '4', '6'],
         '6': ['5'],
         '7': ['3', '8'],
         '8': ['3', '7']
         }


class Node:

    def __init__(self, name, adjacent):
        self.name = name
        self.adjacent = adjacent
        self.discovered = 'undiscovered'
        self.distance = -1
        self.parent = None
        self.child = None

    def __repr__(self):
        return str('Node: {}'.format(self.name))

    def prev_node(self):
        return self.parent

    def next_node(self):
        return self.child


def bfs(graph, start):

    """Breadth first search implementation"""

    nodes = dict()
    tree = list()
    queue = list()

    for key, value in graph.items():
        if key not in start:
            i = Node(key, value)
            nodes[i.name] = i

    start_node = Node(start, graph[start])
    start_node.discovered = 'discovered'
    start_node.distance = 0
    nodes[start_node.name] = start_node

    queue.append(nodes[start_node.name])

    while queue:

        u = queue.pop(0)

        for adj in u.adjacent:
            if nodes[adj].discovered == 'undiscovered':
                u.child = adj
                nodes[adj].discovered = 'discovered'
                nodes[adj].distance = u.distance + 1
                nodes[adj].parent = u.name

                queue.append(nodes[adj])

        u.discovered = 'explored'
        tree.append(u)

    return tree
