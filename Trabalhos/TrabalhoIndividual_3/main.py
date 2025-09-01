"""
Algoritmo para encontrar Caminho Hamiltoniano em grafos orientados e não orientados.
Autor: Pedro Carbonaro
Data: 2025-09-01
"""

from typing import List, Dict, Optional

def hamiltonian_path(graph: Dict[int, List[int]], n: int) -> Optional[List[int]]:
	"""
	Tenta encontrar um caminho Hamiltoniano usando backtracking.
	graph: dicionário de adjacência {vértice: [vizinhos]}
	n: número de vértices
	Retorna uma lista com o caminho, ou None se não existe.
	"""
	path = []
	visited = set()

	def backtrack(v):
		path.append(v)
		visited.add(v)
		if len(path) == n:
			return True
		for u in graph.get(v, []):
			if u not in visited:
				if backtrack(u):
					return True
		path.pop()
		visited.remove(v)
		return False

	for start in graph:
		path.clear()
		visited.clear()
		if backtrack(start):
			return path.copy()
	return None

if __name__ == "__main__":
	
	exemplos = [
		{
			'nome': 'Grafo Não Orientado 1',
			'grafo': {
				0: [1,2],
				1: [0,2,3],
				2: [0,1,3],
				3: [1,2]
			},
			'orientado': False
		},
		{
			'nome': 'Digrafo 2',
			'grafo': {
				0: [1],
				1: [2],
				2: [3],
				3: []
			},
			'orientado': True
		},
		{
			'nome': 'Grafo Não Orientado 3',
			'grafo': {
				0: [1,2],
				1: [0,2],
				2: [0,1,3],
				3: [2]
			},
			'orientado': False
		},
		{
			'nome': 'Digrafo 4',
			'grafo': {
				0: [1,2],
				1: [3],
				2: [3],
				3: []
			},
			'orientado': True
		},
		{
			'nome': 'Grafo Não Orientado 5',
			'grafo': {
				0: [1],
				1: [0,2,3],
				2: [1,3],
				3: [1,2]
			},
			'orientado': False
		}
	]

	for idx, exemplo in enumerate(exemplos, 1):
		grafo = exemplo['grafo']
		n = len(grafo)
		print(f"\n--- Exemplo {idx}: {exemplo['nome']} ---")
		print(f"Vértices: {list(grafo.keys())}")
		arestas = []
		for v, vizinhos in grafo.items():
			for u in vizinhos:
				if exemplo['orientado'] or (u,v) not in arestas:
					arestas.append((v,u))
		print(f"Arestas: {arestas}")
		caminho = hamiltonian_path(grafo, n)
		if caminho:
			print(f"Caminho Hamiltoniano encontrado: {caminho}")
		else:
			print("Não existe Caminho Hamiltoniano neste grafo.")