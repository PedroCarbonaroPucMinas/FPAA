# Projeto Algoritmo de Karatsuba

O Algoritmo de Karatsuba é um projeto desenvolvido para demonstrar uma implementação eficiente de multiplicação de números inteiros grandes. Este projeto implementa o algoritmo de Karatsuba, que reduz a complexidade temporal da multiplicação de O(n²) para O(n^log₂3) ≈ O(n^1.585), onde n é o número de dígitos.

## Estrutura do Projeto

O projeto contém os seguintes arquivos:

### `main.py`
Arquivo principal contendo:
- Implementação do algoritmo de Karatsuba
- Função de multiplicação tradicional para comparação
- Medição de tempo de execução
- Casos de teste demonstrativos

### `analise_complexidade.py`
Arquivo auxiliar para análise detalhada contendo:
- Análise experimental da complexidade temporal
- Geração de números aleatórios para teste
- Comparação entre diferentes tamanhos de entrada
- Análise de casos especiais
- Demonstração do crescimento teórico das complexidades

### `grafo_fluxo_karatsuba.drawio`
Arquivo de diagrama draw.io contendo:
- **Grafo de fluxo de controle redesenhado** com layout profissional
- **Design simétrico e organizado** com cores hierárquicas
- **Numeração clara dos nós** (1-8) para fácil referência
- **Análise de complexidade ciclomática** visual integrada
- **Caminhos independentes identificados** com destaque
- **Legenda completa e organizada** com exemplos visuais
- **Informações técnicas** do algoritmo incluídas

### `INSTRUCOES_DIAGRAMA.md`
Guia detalhado sobre como visualizar e usar o arquivo draw.io, incluindo troubleshooting.

### `README.md`
Documentação completa do projeto com explicações técnicas e relatório de análise.

## Algoritmo de Karatsuba

O algoritmo de Karatsuba, desenvolvido por Anatoly Karatsuba em 1960, é um algoritmo de divisão e conquista que permite multiplicar dois números inteiros de n dígitos com uma complexidade menor que o algoritmo tradicional de multiplicação.

### Princípio do Algoritmo

O algoritmo baseia-se na decomposição de dois números em partes menores e utiliza apenas três multiplicações recursivas ao invés de quatro, como seria necessário no método tradicional.

Para dois números x e y com n dígitos:
- x = a × 10^m + b
- y = c × 10^m + d

Onde m = n/2, a fórmula tradicional seria:
x × y = ac × 10^(2m) + (ad + bc) × 10^m + bd

O insight de Karatsuba é calcular ad + bc usando:
ad + bc = (a + b)(c + d) - ac - bd

Isso reduz o número de multiplicações de 4 para 3: ac, bd, e (a+b)(c+d).

## Explicação da Implementação

### Estrutura do Código

O arquivo `main.py` contém a implementação completa do algoritmo com as seguintes funções:

#### 1. `karatsuba(x, y)`
Função principal que implementa o algoritmo:

```python
def karatsuba(x, y):
    # Caso base: números pequenos usam multiplicação tradicional
    if x < 10 or y < 10:
        return x * y
    
    # Calcula o número de dígitos e a metade
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    # Divide os números em partes alta e baixa
    a = x // (10 ** m)  # Parte alta de x
    b = x % (10 ** m)   # Parte baixa de x
    c = y // (10 ** m)  # Parte alta de y
    d = y % (10 ** m)   # Parte baixa de y
    
    # Três multiplicações recursivas
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    
    # Combina os resultados
    return ac * (10 ** (2 * m)) + ad_plus_bc * (10 ** m) + bd
```

**Explicação linha a linha:**

1. **Caso base (linhas 2-3)**: Se algum número tem menos de 10 (um dígito), usa multiplicação direta.
2. **Cálculo de dígitos (linhas 5-6)**: Determina o tamanho dos números e calcula a metade.
3. **Divisão dos números (linhas 8-11)**: Separa cada número em parte alta e baixa.
4. **Três multiplicações (linhas 13-15)**: Realiza as multiplicações recursivas necessárias.
5. **Combinação (linha 17)**: Aplica a fórmula de Karatsuba para obter o resultado final.

#### 2. `multiplicacao_tradicional(x, y)`
Função de comparação que usa o operador de multiplicação padrão do Python.

#### 3. `medir_tempo_execucao(func, x, y)`
Função auxiliar para medir o tempo de execução das operações.

#### 4. `main()`
Função principal que demonstra o uso do algoritmo com casos de teste.

## Como Executar o Projeto

### Pré-requisitos
- Python 3.6 ou superior
- Sistema operacional: Windows, macOS ou Linux

### Instruções de Execução

#### Passo 1: Navegue até o diretório do projeto
```bash
cd "c:\Users\Carbonaro\Desktop\Projetos\Faculdade\FPAA\TrabalhoIndividual_1"
```

#### Passo 2: Execute o script principal
```bash
python main.py
```

### Ambiente Virtual (Recomendado)

Para isolar as dependências do projeto:

#### Criar e ativar ambiente virtual:
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar no Windows
.venv\Scripts\activate

# Ativar no macOS/Linux
source .venv/bin/activate
```

#### Executar o projeto:
```bash
python main.py
```

#### Para análise detalhada de complexidade:
```bash
python analise_complexidade.py
```

#### Para visualizar o grafo de fluxo:
1. Abra o arquivo `grafo_fluxo_karatsuba.drawio` no [draw.io](https://app.diagrams.net/)
2. Ou use a extensão Draw.io Integration no VS Code
3. O diagrama mostra o grafo de fluxo completo com análise ciclomática

### Saída Esperada

O programa exibirá uma comparação entre o algoritmo de Karatsuba e a multiplicação tradicional:

```
=== Algoritmo de Karatsuba ===

Comparação entre Karatsuba e Multiplicação Tradicional:

Números                                  Karatsuba       Tradicional     Tempo K      Tempo T     
----------------------------------------------------------------------------------------------------
12 * 34                                  408             408             0.000001     0.000000
1234 * 5678                              7006652         7006652         0.000015     0.000001
123456 * 789012                          97408265472     97408265472     0.000089     0.000002
12345678901234567890 * 98765432109876543210  1219326311370217952237463801111263526900  0.001234     0.000003

=== Demonstração passo a passo ===

Calculando 1234 * 5678 com Karatsuba:
Resultado: 7006652
Verificação: 7006652
```

## Relatório Técnico

### Análise da Complexidade Ciclomática

#### Grafo de Fluxo de Controle

O algoritmo de Karatsuba possui a seguinte estrutura de controle:

**Nós do Grafo:**
1. Entrada da função
2. Verificação do caso base (if x < 10 or y < 10)
3. Cálculo de n e m
4. Divisão dos números (a, b, c, d)
5. Primeira chamada recursiva (ac)
6. Segunda chamada recursiva (bd)
7. Terceira chamada recursiva (ad_plus_bc)
8. Cálculo do resultado final
9. Retorno do resultado

**Arestas do Grafo:**
- Entrada → Verificação caso base
- Verificação caso base → Retorno direto (caso verdadeiro)
- Verificação caso base → Cálculo n,m (caso falso)
- Cálculo n,m → Divisão números
- Divisão números → Primeira recursão
- Primeira recursão → Segunda recursão
- Segunda recursão → Terceira recursão
- Terceira recursão → Cálculo resultado
- Cálculo resultado → Retorno

#### Grafo de Fluxo de Controle

O arquivo `grafo_fluxo_karatsuba.drawio` contém a representação visual completa do grafo de fluxo, incluindo:

**Nós do Grafo (n = 10):**
1. **Entrada** - `karatsuba(x, y)` (elipse roxa)
2. **Decisão** - `if x < 10 or y < 10` (losango amarelo)
3. **Caso Base** - `return x * y` (retângulo verde)
4. **Cálculo n,m** - Determinar tamanhos (retângulo azul)
5. **Divisão** - Separar números em partes (retângulo azul)
6. **Recursão 1** - `ac = karatsuba(a, c)` (retângulo vermelho)
7. **Recursão 2** - `bd = karatsuba(b, d)` (retângulo vermelho)
8. **Recursão 3** - `karatsuba(a+b, c+d)` (retângulo vermelho)
9. **Cálculo Final** - Combinar resultados (retângulo azul)
10. **Saída** - `return result` (elipse roxa)

**Arestas do Grafo (e = 10):**
- e1: Entrada → Verificação caso base
- e2: Verificação → Caso base (TRUE)
- e3: Caso base → Saída
- e4: Verificação → Cálculo n,m (FALSE)
- e5: Cálculo n,m → Divisão números
- e6: Divisão → Recursão 1
- e7: Recursão 1 → Recursão 2
- e8: Recursão 2 → Recursão 3
- e9: Recursão 3 → Cálculo final
- e10: Cálculo final → Saída

**Caminhos Independentes:**
1. **Caminho 1 (Caso Base)**: 1 → 2 → 3 → 10
2. **Caminho 2 (Caso Recursivo)**: 1 → 2 → 4 → 5 → 6 → 7 → 8 → 9 → 10

**Cálculo da Complexidade Ciclomática:**
- e (arestas) = 9
- n (nós) = 9
- p (componentes conexos) = 1

**m = e - n + 2p = 9 - 9 + 2(1) = 2**

A complexidade ciclomática é **2**, indicando baixa complexidade estrutural e facilidade de teste.

### Análise da Complexidade Assintótica

#### Complexidade Temporal

**Melhor Caso: O(n^log₂3)**
- Ocorre quando os números têm tamanhos similares e são divididos equilibradamente
- A recorrência é T(n) = 3T(n/2) + O(n)
- Pelo Teorema Mestre: T(n) = O(n^log₂3) ≈ O(n^1.585)

**Caso Médio: O(n^log₂3)**
- Similar ao melhor caso, pois a divisão é sempre pela metade
- Mantém a mesma complexidade assintótica

**Pior Caso: O(n^log₂3)**
- Mesmo quando um número é significativamente menor que o outro
- A complexidade não degrada devido à estrutura do algoritmo

#### Complexidade Espacial

**Melhor/Médio/Pior Caso: O(log n)**
- Devido à pilha de recursão que pode ir até log n níveis de profundidade
- Cada chamada recursiva usa espaço constante para variáveis locais

#### Comparação com Multiplicação Tradicional

| Aspecto | Karatsuba | Tradicional |
|---------|-----------|-------------|
| Temporal | O(n^1.585) | O(n²) |
| Espacial | O(log n) | O(1) |
| Prático | Melhor para n > 1000 | Melhor para n pequeno |

### Análise de Desempenho

O algoritmo de Karatsuba oferece vantagens significativas para números grandes:

1. **Números pequenos (< 1000 dígitos)**: A multiplicação tradicional pode ser mais rápida devido ao overhead da recursão.

2. **Números médios (1000-10000 dígitos)**: Karatsuba começa a mostrar vantagens claras.

3. **Números grandes (> 10000 dígitos)**: Karatsuba é significativamente mais eficiente.

### Implementações Otimizadas

Para uso em produção, algumas otimizações são recomendadas:

1. **Threshold adaptativo**: Usar multiplicação tradicional para números menores que um limiar otimizado.
2. **Balanceamento**: Equilibrar tamanhos quando os números têm comprimentos muito diferentes.
3. **Representação numérica**: Usar bases maiores (ex: base 10^9) para reduzir operações.

## Vantagens e Desvantagens

### Vantagens
- Complexidade assintótica superior para números grandes
- Algoritmo elegante e matematicamente interessante
- Base para algoritmos mais avançados (ex: FFT)

### Desvantagens
- Overhead de recursão para números pequenos
- Uso adicional de memória (pilha de recursão)
- Implementação mais complexa que multiplicação tradicional

## Versão do Python

Este projeto foi desenvolvido e testado na versão **3.13.0** do Python, mas é compatível com versões 3.6 ou superiores.

## Referências

- Karatsuba, A. and Ofman, Yu. (1962). "Multiplication of Many-Digital Numbers by Automatic Computers"
- Knuth, Donald E. "The Art of Computer Programming, Volume 2: Seminumerical Algorithms"
- Cormen, Thomas H., et al. "Introduction to Algorithms"

## Licença

Este projeto está licenciado sob a Licença MIT.