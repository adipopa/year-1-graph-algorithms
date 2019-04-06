from copy import deepcopy


class DirectedDictGraph:

    def __init__(self):
        """ Creates a graph with n vertices (indexed from 0 to n-1). """
        self.__dictIn = {}

    def init_dict(self, n):
        """ Initialize the graph's outbound and inbound sets, given a number of vertices. """
        for i in range(n):
            self.__dictIn[i] = []

    def parse_x(self):
        """ Returns an iterable containing all the vertices. """
        return deepcopy(list(self.__dictIn.keys()))

    def parse_n_in(self, x):
        """ Returns an iterable containing the inbound neighbours of x. """
        if not self.is_vertex(x):
            raise Exception("The vertex " + str(x) + " doesn't exist in this graph.")
        return deepcopy(self.__dictIn[x])

    def is_vertex(self, x):
        """ Returns True if the vertex x exists in the graph and False otherwise. """
        return x in self.__dictIn.keys()

    def is_edge(self, x, y):
        """ Returns True if there exists an edge from x to y, False otherwise.
        Precondition: x and y are vertices in the graph. """
        if not self.is_vertex(x):
            raise Exception("The vertex " + str(x) + " doesn't exist in this graph.")
        if not self.is_vertex(y):
            raise Exception("The vertex " + str(y) + " doesn't exist in this graph.")
        return y in self.__dictIn[x]

    def add_edge(self, x, y):
        """ Adds an edge from vertex x to y with a cost of c.
        Precondition: there is no edge from x to y. """
        if self.is_edge(x, y):
            raise Exception("There already exists an edge from vertex " + str(x) + " to " + str(y) + ".")
        self.__dictIn[y].append(x)

    def shortest_path(self, src, dest):
        """ Returns the lowest length path between vertices src and dest (if they exist), using a
        backward breadth-first search from the ending vertex. """
        if not self.is_vertex(src):
            raise Exception("The vertex " + str(src) + " doesn't exist in this graph.")
        if not self.is_vertex(dest):
            raise Exception("The vertex " + str(dest) + " doesn't exist in this graph.")
        queue = list()
        queue.append([dest])
        while queue:
            path = queue.pop(0)
            node = path[0]
            if node == src:
                return path
            for adj in self.__dictIn[node]:
                new_path = list(path)
                new_path.insert(0, adj)
                queue.append(new_path)
