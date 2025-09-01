# Caminho Hamiltoniano em Grafos

## Descrição do Projeto
Este projeto implementa um algoritmo em Python para encontrar um Caminho Hamiltoniano em grafos orientados ou não orientados. Um Caminho Hamiltoniano é um caminho que visita cada vértice do grafo exatamente uma vez. O algoritmo utiliza uma abordagem de backtracking para explorar todas as possibilidades de caminhos.

### Lógica do Algoritmo (linha a linha)
- O grafo é representado como um dicionário de adjacência `{vértice: [vizinhos]}`.
- A função `hamiltonian_path(graph, n)` tenta encontrar um caminho Hamiltoniano:
  - Para cada vértice de início, executa o backtracking.
  - O backtracking adiciona o vértice ao caminho e marca como visitado.
  - Se o caminho tem todos os vértices, retorna o caminho.
  - Para cada vizinho não visitado, chama recursivamente.
  - Se não encontrar, desfaz a escolha (backtrack).
- O programa inclui exemplos de uso para grafos orientados e não orientados.

## Como Executar o Projeto
1. Certifique-se de ter o Python 3 instalado.
2. No terminal, navegue até a pasta do projeto:
   ```bash
   cd TrabalhoIndividual_3
   ```

3. Execute o arquivo principal:
  ```bash
  python main.py
  ```
4. O programa exibirá se existe ou não um Caminho Hamiltoniano nos exemplos fornecidos.

### Requisitos
- Python 3.8 ou superior
- Sistema Linux/WSL recomendado

### Passo a passo para rodar o projeto
1. Certifique-se de ter o Python 3 instalado:
  ```bash
  python3 --version
  ```
2. Instale os pacotes necessários para ambiente virtual:
  ```bash
  sudo apt update
  sudo apt install python3-full python3-venv
  ```
3. Crie e ative o ambiente virtual:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
4. Instale as dependências do projeto:
  ```bash
  pip install networkx matplotlib
  ```
5. Execute o arquivo principal:
  ```bash
  python main.py
  ```
6. Para visualizar os grafos e Caminhos Hamiltonianos:
  ```bash
  python view.py
  ```
  > **Atenção:** Feche cada janela de gráfico para visualizar o próximo exemplo. O log no console também avisa quando um novo grafo será exibido.

## Visualização do Grafo e Caminho Hamiltoniano

Para visualizar os grafos e destacar o Caminho Hamiltoniano, instale as bibliotecas necessárias:

```bash
pip install networkx matplotlib
```

Depois, execute o arquivo de visualização:

```bash
python view.py
```

O grafo será desenhado, mostrando todos os vértices e arestas, e o Caminho Hamiltoniano (se encontrado) será destacado em vermelho.

### Exemplo de visualização

![Exemplo de visualização do grafo](exemplo_grafo.png)

O código em `view.py` permite visualizar todos os exemplos de grafos do projeto.

## Relatório Técnico

### Classes de Complexidade: P, NP, NP-Completo, NP-Difícil
- O problema do Caminho Hamiltoniano pertence à classe **NP-Completo**.
- Justificativa:
  - Está em NP: dado um caminho, é possível verificar em tempo polinomial se ele é Hamiltoniano.
  - É NP-Completo: pode ser reduzido ao Problema do Caixeiro Viajante (TSP), que também é NP-Completo.
  - O TSP é uma generalização do Caminho Hamiltoniano, pois busca o ciclo Hamiltoniano de menor custo.
  - Não há algoritmo conhecido de tempo polinomial para o problema em grafos gerais.

### Complexidade Assintótica de Tempo
- O algoritmo de backtracking tem complexidade **O(n!)** no pior caso, onde n é o número de vértices.
- Determinação:
  - Para cada vértice inicial, explora todas as permutações possíveis dos vértices.
  - A cada passo, pode escolher entre os vértices não visitados, levando a n! possibilidades.
  - Método: contagem de operações e análise combinatória.

### Aplicação do Teorema Mestre
- O Teorema Mestre não se aplica diretamente ao algoritmo de Caminho Hamiltoniano.
- Justificativa:
  - O Teorema Mestre é usado para recorrências do tipo T(n) = aT(n/b) + f(n), comuns em algoritmos de divisão e conquista.
  - O algoritmo de backtracking não possui essa estrutura de recorrência, pois o número de subproblemas não é fixo e depende das escolhas.

### Análise dos Casos de Complexidade
- **Pior caso:** O grafo é denso e não possui Caminho Hamiltoniano. O algoritmo explora todas as possibilidades, levando a O(n!) operações.
- **Melhor caso:** O caminho Hamiltoniano é encontrado logo nas primeiras tentativas, especialmente em grafos com estrutura linear ou ciclo.
- **Caso médio:** Depende da estrutura do grafo; em geral, a complexidade permanece exponencial, mas pode ser menor se o grafo for favorável.
- **Impacto:** O desempenho do algoritmo é altamente sensível à estrutura do grafo. Para grafos pequenos, é viável; para grandes, torna-se impraticável.

---

### Referências
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms.
- https://en.wikipedia.org/wiki/Hamiltonian_path
- https://en.wikipedia.org/wiki/NP-completeness

---

Projeto desenvolvido para a disciplina Fundamentos de Projeto e Análise de Algoritmos - FPAA.
