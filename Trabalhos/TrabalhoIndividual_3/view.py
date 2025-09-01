"""
Visualização de grafos e Caminho Hamiltoniano usando NetworkX e Matplotlib.
Autor: Pedro Carbonaro
"""

import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List, Optional

def draw_graph_with_hamiltonian(graph: Dict[int, List[int]], path: Optional[List[int]], directed: bool = False, title: str = "Grafo"):
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    for v, vizinhos in graph.items():
        for u in vizinhos:
            G.add_edge(v, u)
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(7,5))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos)
    if path and len(path) > 1:
        h_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=h_edges, edge_color='red', width=3)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange')
        plt.title(f"{title}\nCaminho Hamiltoniano: {path}\n(Feche o gráfico para ir para o próximo)")
    else:
        plt.title(f"{title}\nNão existe Caminho Hamiltoniano\n(Feche o gráfico para ir para o próximo)")
    print(f"[VISUALIZAÇÃO] {title} - Feche o gráfico para ir para o próximo.")
    plt.show()

if __name__ == "__main__":
    from main import hamiltonian_path
    exemplos = [
        {
            'nome': 'Grafo Não Orientado 1',
            'grafo': {
                0: [1,2],
                1: [0,2,3],
                2: [0,1,3],
                3: [1,2]
            },
            'directed': False
        },
        {
            'nome': 'Digrafo 2',
            'grafo': {
                0: [1],
                1: [2],
                2: [3],
                3: []
            },
            'directed': True
        },
        {
            'nome': 'Grafo Não Orientado 3',
            'grafo': {
                0: [1,2],
                1: [0,2],
                2: [0,1,3],
                3: [2]
            },
            'directed': False
        },
        {
            'nome': 'Digrafo 4',
            'grafo': {
                0: [1,2],
                1: [3],
                2: [3],
                3: []
            },
            'directed': True
        },
        {
            'nome': 'Grafo Não Orientado 5',
            'grafo': {
                0: [1],
                1: [0,2,3],
                2: [1,3],
                3: [1,2]
            },
            'directed': False
        }
    ]
    for idx, exemplo in enumerate(exemplos, 1):
        grafo = exemplo['grafo']
        n = len(grafo)
        caminho = hamiltonian_path(grafo, n)
        print(f"\n[VISUALIZAÇÃO] Exemplo {idx}: {exemplo['nome']} - Feche o gráfico para ir para o próximo.")
        draw_graph_with_hamiltonian(grafo, caminho, directed=exemplo['directed'], title=f"Exemplo {idx}: {exemplo['nome']}")
