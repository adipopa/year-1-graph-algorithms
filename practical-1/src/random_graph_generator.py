from double_dict_graph import DoubleDictGraph

import random


class RandomGraphGenerator:
    """ Class for generating a Graph given a number of vertices and edges. """
    @staticmethod
    def generate(graph: DoubleDictGraph, n, m):
        """ Precondition: m <= n*n, otherwise generate only n*n edges. """
        m = min(m, n*n)
        graph.init_dict(n)
        i = 0
        while i < m:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            c = random.randint(1, 100)
            try:
                graph.add_edge(x, y, c)
                i += 1
            except Exception:
                continue
