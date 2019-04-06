from directed_dict_graph import DirectedDictGraph


def read_input():
    file = open("graph.txt")
    try:
        graph: DirectedDictGraph = DirectedDictGraph()
        line = file.readline().strip()
        if len(line) == 0:
            return graph
        n, m = map(int, line.split())
        graph.init_dict(n)
        for i in range(m):
            line = file.readline().strip()
            x, y, c = map(int, line.split())
            graph.add_edge(x, y, c)
        return graph
    except IOError as io_error:
        print(str(io_error))


def run():
    graph: DirectedDictGraph = read_input()




run()
