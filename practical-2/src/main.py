from directed_dict_graph import DirectedDictGraph
import re


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
            x, y = map(int, line.split())
            graph.add_edge(x, y)
        return graph
    except IOError as io_error:
        print(str(io_error))


def run():
    graph: DirectedDictGraph = read_input()

    print("Graph successfully loaded from graph.txt file.")

    while True:
        try:
            x, y = map(int, re.split(" |, |,", input("Give two vertices (x, y): ").strip()))

            shortest_path = graph.shortest_path(x, y)

            if shortest_path:
                path_length = len(shortest_path) - 1
                print("The shortest path between vertices " + str(x) + " and " + str(y) +
                      ", having a length of " + str(path_length) + ":")
                print(*shortest_path, sep=" -> ")
            else:
                print("No path found between vertices " + str(x) + " and " + str(y) + ".")

            should_continue = input("\nDo you wish to wish to find another path? [y/N]: ")
            if should_continue.strip().lower() != "y":
                break
        except ValueError:
            print("Invalid input, try again.")
        except Exception as e:
            print(str(e))


run()
