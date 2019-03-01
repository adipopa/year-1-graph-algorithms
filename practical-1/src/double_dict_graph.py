import numpy as np


class DoubleDictGraph:

    def __init__(self, n):
        """ Creates a graph with n vertices (numbered from 0 to n-1) """
        self.__dictIn = {}
        self.__dictOut = {}
        self.__dictCost = {}

        for i in range(n):
            self.__dictIn[i] = []
            self.__dictOut[i] = []

    def parse_x(self):
        """ Returns an iterable containing all the vertices """
        x = np.array(self.__dictOut.keys())
        return np.copy(x)

    def parse_n_out(self, x):
        """ Returns an iterable containing the outbound neighbours of x """
        n_out = np.array(self.__dictOut[x])
        return np.copy(n_out)

    def parse_n_in(self, x):
        """ Returns an iterable containing the inbound neighbours of x """
        n_in = np.array(self.__dictIn[x])
        return np.copy(n_in)

    def is_edge(self, x, y):
        """ Returns True if there exists an edge from x to y, False otherwise """
        return y in self.__dictOut[x]

    def add_edge(self, x, y, c):
        """ Adds an edge from vertex x to y with a cost of c
        Precondition: there is no edge from x to y """
        if x not in self.parse_x:
            raise Exception("The vertex " + str(x) + " doesn't exist in this graph.")
        if y not in self.parse_x:
            raise Exception("The vertex " + str(y) + " doesn't exist in this graph.")
        if self.is_edge(x, y):
            raise Exception("There already exists an edge from vertex " + str(x) + " to " + str(y) + ".")
        self.__dictOut[x] = y
        self.__dictIn[y] = x
        self.__dictCost[(x, y)] = c
