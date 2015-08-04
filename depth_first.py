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
        self.child = list()
        self.count = 0

    def __repr__(self):
        return str('Node: {}'.format(self.name))

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < len(self.child):
            i = self.child[self.count]
            self.count += 1
            return i
        else:
            raise StopIteration

    def prev_node(self):
        return self.parent


def dfs(graph, start):

    """Implementation of depth-first search."""

    nodes = dict()
    stack = list()
    tree = list()

    for key, value in graph.items():
        if key not in start:
            i = Node(key, value)
            nodes[i.name] = i

    start_node = Node(start, graph[start])
    nodes[start_node.name] = start_node

    stack.append(nodes[start_node.name])

    while stack:

        v = stack.pop()

        if v.discovered == 'undiscovered':
            nodes[v.name].discovered = 'discovered'
            for adj in v.adjacent:
                v.child.append(adj)
                nodes[adj].parent = v.name
                stack.append(nodes[adj])
            tree.append(v)

    return tree
