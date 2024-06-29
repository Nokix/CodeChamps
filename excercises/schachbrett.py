"""Schachbrett ⭐⭐⭐
Wie viele verschiedene Zyklen, kann ein Springer auf einem 5x5 großen Spielfeld springen,
wenn er in der Ecke oben Links beginnt?

Bei einem 3x3 großen Feld sind es 4 verschieden Zyklen:

A1 -> C2 -> A3 -> B1 -> C3 -> A2 -> C1 -> B3
A1 -> C2
A1 -> B3 -> C1 -> A2 -> C3 -> B1 -> A3 -> C2
A1 -> B3

"""

class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Node({self.name})"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.name == other.name
        return False


class Graph:
    def __init__(self, node_relationship):
        self.node_relationship = node_relationship

    def get_neighbors(self, node):
        return self.node_relationship.get(node, [])

    def is_neighbor(self, node_a, node_b):
        neighbors_of_a = self.get_neighbors(node_a)
        return node_b in neighbors_of_a

    def find_cycles(self, start_node):
        def dfs(current_node, visited, path):
            visited.add(current_node)
            path.append(current_node)

            for neighbor in self.get_neighbors(current_node):
                if neighbor == start_node and len(path) > 1:
                    cycles.append(path.copy())
                elif neighbor not in visited:
                    dfs(neighbor, visited, path)

            path.pop()
            visited.remove(current_node)

        if isinstance(start_node, str):
            start_node = Node(start_node)
        cycles = []
        dfs(start_node, set(), [])
        return cycles


class ChessboardCreator:
    def __init__(self, figure, x_labels=3, y_labels=3):
        self.figure = figure
        self.x_labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZabzdefghijklmnopqrstuvwxyz"[:y_labels]
        self.y_labels = range(1, x_labels + 1)

    def create(self):
        nodes = [[Node(f"{x_label}{y_label}") for x_label in self.x_labels] for y_label in self.y_labels]

        graph = {}
        for x, row in enumerate(nodes):
            for y, node in enumerate(row):
                graph[node] = [nodes[x + x_diff][y + y_diff]
                               for x_diff, y_diff in self.figure.possible_fields(creator=self)
                               if 0 <= x_diff + x < len(self.x_labels) and 0 <= y_diff + y < len(self.y_labels)]

        return Graph(graph)


class Figure:
    def possible_fields(self, creator=None):
        return []


class Knight(Figure):
    def possible_fields(self, creator=None):
        return [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    def __str__(self):
        return "🐴"


if __name__ == '__main__':
    board = ChessboardCreator(Knight()).create()
    print(board)
    found_cycles = board.find_cycles("A1")
    for cycle in found_cycles:
        print(" -> ".join([str(node) for node in cycle]))

    print(len(found_cycles))
