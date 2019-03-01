from double_dict_graph import DoubleDictGraph


def run():
    file = open("graph_input.txt")
    try:
        line = file.readline().strip()
        n, m = map(int, line.split())
        graph = DoubleDictGraph(n)
        for i in range(m):
            line = file.readline().strip()
            x, y, c = map(int, line.split())
            graph.add_edge(x, y, c)
    except IOError as io_error:
        print(str(io_error))


run()
