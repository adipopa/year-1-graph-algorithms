from double_dict_graph import DoubleDictGraph

from random_graph_generator import RandomGraphGenerator

from console import Console


def read_input():
    file = open("graph1k.txt")
    try:
        graph: DoubleDictGraph = DoubleDictGraph()
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


def test_copy_graph(graph: DoubleDictGraph):
    copied_graph: DoubleDictGraph = graph.copy_graph()

    graph.add_edge(1, 41, 7)
    graph.remove_edge(1, 268)
    graph.remove_edge(1, 581)
    graph.remove_vertex(2)

    assert copied_graph.is_edge(1, 41) == False
    assert copied_graph.is_edge(1, 268) == True
    assert copied_graph.is_edge(1, 581) == True
    assert copied_graph.is_vertex(2) == True


def run():
    #graph: DoubleDictGraph = read_input()

    graph: DoubleDictGraph = DoubleDictGraph()

    random_graph_generator: RandomGraphGenerator = RandomGraphGenerator()
    random_graph_generator.generate(graph, 10, 1000)

    #test_copy_graph(graph)

    console: Console = Console(graph)
    console.ui_show_menu()


run()
