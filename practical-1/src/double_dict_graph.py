from copy import deepcopy


class DoubleDictGraph:

    def __init__(self):
        """ Creates a graph with n vertices (indexed from 0 to n-1). """
        self.__dictOut = {}
        self.__dictIn = {}
        self.__dictCost = {}

    def init_dict(self, n):
        """ Initialize the graph's outbound and inbound sets, given a number of vertices. """
        for i in range(n):
            self.__dictOut[i] = []
            self.__dictIn[i] = []

    def parse_x(self):
        """ Returns an iterable containing all the vertices. """
        return deepcopy(list(self.__dictOut.keys()))

    def parse_n_out(self, x):
        """ Returns an iterable containing the outbound neighbours of x. """
        if not self.is_vertex(x):
            raise Exception("The vertex " + str(x) + " doesn't exist in this graph.")
        return deepcopy(self.__dictOut[x])

    def parse_n_in(self, x):
        """ Returns an iterable containing the inbound neighbours of x. """
        if not self.is_vertex(x):
            raise Exception("The vertex " + str(x) + " doesn't exist in this graph.")
        return deepcopy(self.__dictIn[x])

    def is_vertex(self, x):
        """ Returns True if the vertex x exists in the graph and False otherwise. """
        return x in self.__dictOut.keys()

    def is_edge(self, x, y):
        """ Returns True if there exists an edge from x to y, False otherwise.
        Precondition: x and y are vertices in the graph. """
        if not self.is_vertex(x):
            raise Exception("The vertex " + str(x) + " doesn't exist in this graph.")
        if not self.is_vertex(y):
            raise Exception("The vertex " + str(y) + " doesn't exist in this graph.")
        return y in self.__dictOut[x]

    def add_edge(self, x, y, c):
        """ Adds an edge from vertex x to y with a cost of c.
        Precondition: there is no edge from x to y. """
        if self.is_edge(x, y):
            raise Exception("There already exists an edge from vertex " + str(x) + " to " + str(y) + ".")
        self.__dictOut[x].append(y)
        self.__dictIn[y].append(x)
        self.__dictCost[(x, y)] = c

    def remove_edge(self, x, y):
        """ Removes the edge from vertex x to y along with its assigned cost.
        Precondition: there exists an edge from x to y. """
        if not self.is_edge(x, y):
            raise Exception("There's no edge between vertex " + str(x) + " and " + str(y) + ".")
        self.__dictOut[x].remove(y)
        self.__dictIn[y].remove(x)
        del self.__dictCost[(x, y)]

    def add_vertex(self, x):
        """ Adds the vertex x to the dict of vertices.
        Precondition: x is not already an vertex of the graph. """
        if self.is_vertex(x):
            raise Exception("This vertex already exists.")
        self.__dictOut[x] = []
        self.__dictIn[x] = []

    def remove_vertex(self, x):
        """ Removes the vertex x from the dict of vertices.
        Precondition: x is a vertex in the graph. """
        if not self.is_vertex(x):
            raise Exception("This vertex doesn't exist.")
        for y in self.__dictOut[x]:
            self.__dictIn[y].remove(x)
            del self.__dictCost[(x, y)]
        del self.__dictOut[x]
        for y in self.__dictIn[x]:
            self.__dictOut[y].remove(x)
            del self.__dictCost[(y, x)]
        del self.__dictIn[x]

    def copy_graph(self):
        """ Returns a deep copy of the current graph (instance of DoubleDictGraph). """
        return deepcopy(self)

    def in_degree(self, x):
        """ Returns a integer representing the in degree of a given vertex x.
        Precondition: x is a vertex in the graph. """
        if not self.is_vertex(x):
            raise Exception("The vertex " + str(x) + " doesn't exist in this graph.")
        return len(self.__dictIn[x])

    def out_degree(self, x):
        """ Returns a integer representing the out degree of a given vertex x.
        Precondition: x is a vertex in the graph. """
        if not self.is_vertex(x):
            raise Exception("The vertex " + str(x) + " doesn't exist in this graph.")
        return len(self.__dictOut[x])

    def get_cost(self, x, y):
        """ Returns a integer representing the cost associated to the edge from x to y.
        Precondition: there exists an edge from x to y. """
        if not self.is_edge(x, y):
            raise Exception("There is no edge from vertex " + str(x) + " to " + str(y) + ".")
        return self.__dictCost[(x, y)]

    def set_cost(self, x, y, new_cost):
        """ Updates the cost of the edge from x to y with the value of new_cost.
        Precondition: there exists an edge from x to y. """
        if not self.is_edge(x, y):
            raise Exception("There is no edge from vertex " + str(x) + " to " + str(y) + ".")
        self.__dictCost[(x, y)] = new_cost

    @property
    def no_of_vertices(self):
        """ Returns a integer representing the number of vertices in the graph. """
        return len(self.__dictOut.keys())
