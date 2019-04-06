from double_dict_graph import DoubleDictGraph


class Console:

    def __init__(self, graph: DoubleDictGraph = None):
        self.__graph = graph

        self.__options = {
            '1': self.ui_number_of_vertices,
            '2': self.ui_display_vertices_set,
            '3': self.ui_check_edge_existence,
            '4': self.ui_vertex_degrees,
            '5': self.ui_outbound_edges,
            '6': self.ui_inbound_edges,
            '7': self.ui_retrieve_modify_edge,
            '8': self.ui_modify_graph
        }

        self.__modify_graph_options = {
            '1': self.ui_add_edge,
            '2': self.ui_remove_edge,
            '3': self.ui_add_vertex,
            '4': self.ui_remove_vertex,
        }

    def ui_show_menu(self):
        print("The graph was read from the input file.")
        keep_alive = True
        while keep_alive:
            print("\nWhat do you wish to do next?")
            print("1. Get the number of vertices.")
            print("2. Display the set of vertices.")
            print("3. Check whether there exists an edge between two vertices.")
            print("4. Get the in degree and out degree of a vertex.")
            print("5. Display the set of outbound edges of a vertex.")
            print("6. Display the set of inbound edges of a vertex.")
            print("7. Retrieve or modify the cost of an edge.")
            print("8. Modify the graph.")
            print("0. Exit the application.")
            user_option = input("\nPlease select an option from 1-n or 0 to exit the app: ").strip().lower()
            if user_option in self.__options:
                try:
                    self.__options[user_option]()
                except ValueError as value_error:
                    print("Value ERROR: " + str(value_error))
                except Exception as exception:
                    print(str(exception))
            elif user_option == '0':
                keep_alive = False
            else:
                print("Invalid option!")

    def ui_number_of_vertices(self):
        print("There are " + str(self.__graph.no_of_vertices) + " vertices in the graph.")

    def ui_display_vertices_set(self):
        if self.__graph.no_of_vertices == 0:
            print("The set of vertices is empty.")
        for x in self.__graph.parse_x():
            print(str(x) + ":", end=" ")
            for y in self.__graph.parse_n_out(x):
                print(str(y) + "(" + str(self.__graph.get_cost(x, y)) + ")", end=" ")
            print()

    def ui_check_edge_existence(self):
        print("Give two vertex indexes to check whether there exists and edge between the two.")

        x = int(input("Vertex x: "))
        y = int(input("Vertex y: "))

        print("There " + ("exists an" if self.__graph.is_edge(x, y) else "is no") +
              " edge between vertex " + str(x) + " and " + str(y) + ".")

    def ui_vertex_degrees(self):
        print("Give a vertex index to check its in and out degrees.")

        x = int(input("Vertex x: "))

        print("The in degree of vertex " + str(x) + " is " + str(self.__graph.in_degree(x)) + ".")
        print("The out degree of vertex " + str(x) + " is " + str(self.__graph.out_degree(x)) + ".")

    def ui_outbound_edges(self):
        print("Give a vertex index to list its outbound edges.")

        x = int(input("Vertex x: "))

        if len(self.__graph.parse_n_out(x)) == 0:
            print("The set of outbound edges is empty.")
        for y in self.__graph.parse_n_out(x):
            print("(" + str(x) + ", " + str(y) + ")")

    def ui_inbound_edges(self):
        print("Give a vertex index to list its inbound edges.")

        y = int(input("Vertex y: "))

        if len(self.__graph.parse_n_in(y)) == 0:
            print("The set of inbound edges is empty.")
        for x in self.__graph.parse_n_in(y):
            print("(" + str(x) + ", " + str(y) + ")")

    def ui_retrieve_modify_edge(self):
        print("Give two vertex indexes to retrieve or modify the edge cost.")

        x = int(input("Vertex x: "))
        y = int(input("Vertex y: "))

        cost_of_edge = self.__graph.get_cost(x, y)
        print("The cost of this edge is: " + str(cost_of_edge))

        user_input = input("Do you wish to wish to modify this edge's cost value? [y/N]: ")
        if user_input.strip().lower() == "y":
            new_cost = int(input("New cost for this edge: "))
            self.__graph.set_cost(x, y, new_cost)

    def ui_modify_graph(self):
        keep_alive = True
        while keep_alive:
            print("\nWhat do you wish to do next?")
            print("1. Add an edge.")
            print("2. Remove an edge.")
            print("3. Add a vertex.")
            print("4. Remove a vertex.")
            print("0. Back.")
            user_option = input("\nPlease select an option from 1-4 or 0 to exit the app: ").strip().lower()
            if user_option in self.__options:
                try:
                    self.__modify_graph_options[user_option]()
                except ValueError as value_error:
                    print("Value ERROR: " + str(value_error))
                except Exception as exception:
                    print(str(exception))
            elif user_option == '0':
                keep_alive = False
            else:
                print("Invalid option!")

    def ui_add_edge(self):
        print("Give two vertex indexes and a cost to create a new edge.")

        x = int(input("Vertex x: "))
        y = int(input("Vertex y: "))
        c = int(input("Cost of this edge: "))

        self.__graph.add_edge(x, y, c)

    def ui_remove_edge(self):
        print("Give two vertex indexes to remove that edge.")

        x = int(input("Vertex x: "))
        y = int(input("Vertex y: "))

        self.__graph.remove_edge(x, y)

    def ui_add_vertex(self):
        print("Give an index to create a new vertex at that index.")

        x = int(input("Vertex x: "))

        self.__graph.add_vertex(x)

    def ui_remove_vertex(self):
        print("Give an index to remove the vertex from that index.")

        x = int(input("Vertex x: "))

        self.__graph.remove_vertex(x)
