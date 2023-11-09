import networkx as nx
import matplotlib.pyplot as plt
import tree_scores as ts

# Esta función visualizará el árbol
def visualize_tree(node):
    G = nx.DiGraph()

    def add_nodes_and_edges(graph, current_node, parent=None):
        graph.add_node(str(current_node.board) + f"\nScore: {current_node.score}")
        if parent is not None:
            graph.add_edge(str(parent.board) + f"\nScore: {parent.score}", str(current_node.board) + f"\nScore: {current_node.score}")
        for child in current_node.children:
            add_nodes_and_edges(graph, child, current_node)

    add_nodes_and_edges(G, node)
    pos = nx.spring_layout(G)
    labels = {node: node for node in G.nodes()}

    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=1000, node_color='lightblue', font_size=8, font_color='black')
    plt.title('Árbol de Puntajes')
    plt.show()

if __name__ == '__main__':
    # Crear un objeto Node para representar el tablero inicial
    initial_board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    tree_root = ts.Node(initial_board, 0)  # Proporciona el tablero inicial y una puntuación inicial

    # Genera el árbol de búsqueda (ajusta la profundidad según tus necesidades)
    ts.generate_tree(tree_root, depth=3, current_player='X')  # Proporciona el jugador actual

    # Asigna las puntuaciones
    ts.assign_scores(tree_root, current_player='X')  # Proporciona el jugador actual

    # Visualiza el árbol de puntajes
    visualize_tree(tree_root)



