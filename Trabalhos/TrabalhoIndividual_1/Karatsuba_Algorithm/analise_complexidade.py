"""
    @File.: Análise de complexidade do algoritmo de Karatsuba para multiplicação eficiente.
    @Author.: Pedro Carbonaro
    @Date.: 2023-10-05
"""

"""
Análise detalhada da complexidade do algoritmo de Karatsuba.
Este arquivo contém ferramentas para analisar e visualizar a complexidade do algoritmo.
"""

import time
import math
import random
from main import karatsuba, multiplicacao_tradicional


def gerar_numero_aleatorio(digitos):
    """
    Gera um número aleatório com o número especificado de dígitos.
    
    Args:
        digitos (int): Número de dígitos desejado
    
    Returns:
        int: Número aleatório com o número especificado de dígitos
    """
    if digitos == 1:
        return random.randint(1, 9)
    
    # Gera um número com 'digitos' dígitos
    min_val = 10 ** (digitos - 1)
    max_val = 10 ** digitos - 1
    return random.randint(min_val, max_val)


def medir_tempo_multiplas_execucoes(func, x, y, num_execucoes=5):
    """
    Mede o tempo médio de execução de uma função ao longo de múltiplas execuções.
    
    Args:
        func: Função a ser medida
        x (int): Primeiro número
        y (int): Segundo número
        num_execucoes (int): Número de execuções para média
    
    Returns:
        float: Tempo médio de execução
    """
    tempos = []
    
    for _ in range(num_execucoes):
        start_time = time.perf_counter()
        func(x, y)
        end_time = time.perf_counter()
        tempos.append(end_time - start_time)
    
    return sum(tempos) / len(tempos)


def analise_complexidade_experimental():
    """
    Realiza análise experimental da complexidade temporal.
    """
    print("=== Análise Experimental da Complexidade ===\n")
    
    # Tamanhos de teste (número de dígitos)
    tamanhos = [10, 50, 100, 200, 500, 1000]
    
    print(f"{'Dígitos':<10} {'Karatsuba (s)':<15} {'Tradicional (s)':<18} {'Speedup':<10} {'Razão Teórica':<15}")
    print("-" * 75)
    
    resultados_karatsuba = []
    resultados_tradicional = []
    
    for digitos in tamanhos:
        # Gera números de teste
        x = gerar_numero_aleatorio(digitos)
        y = gerar_numero_aleatorio(digitos)
        
        # Mede tempo do Karatsuba
        tempo_k = medir_tempo_multiplas_execucoes(karatsuba, x, y)
        resultados_karatsuba.append(tempo_k)
        
        # Mede tempo da multiplicação tradicional (apenas para números menores)
        if digitos <= 500:  # Evita tempos muito longos
            tempo_t = medir_tempo_multiplas_execucoes(multiplicacao_tradicional, x, y)
            resultados_tradicional.append(tempo_t)
            speedup = tempo_t / tempo_k if tempo_k > 0 else float('inf')
        else:
            tempo_t = "N/A"
            speedup = "N/A"
        
        # Calcula razão teórica (n^2 / n^1.585)
        razao_teorica = (digitos ** 2) / (digitos ** 1.585) if digitos > 1 else 1
        
        print(f"{digitos:<10} {tempo_k:<15.6f} {str(tempo_t):<18} {str(speedup):<10} {razao_teorica:<15.2f}")
    
    return resultados_karatsuba, resultados_tradicional


def calcular_complexidade_teorica(n):
    """
    Calcula as complexidades teóricas para um dado tamanho n.
    
    Args:
        n (int): Tamanho da entrada (número de dígitos)
    
    Returns:
        dict: Dicionário com as complexidades calculadas
    """

    return {
        'karatsuba': n ** math.log2(3),  # n^log2(3) ≈ n^1.585
        'tradicional': n ** 2,           # n^2
        'linear': n,                     # n
        'logaritmica': math.log2(n)      # log(n)
    }


def demonstrar_crescimento_complexidade():
    """
    Demonstra como as complexidades crescem com o tamanho da entrada.
    """
    print("\n=== Crescimento Teórico das Complexidades ===\n")
    
    tamanhos = [10, 100, 1000, 10000, 100000]
    
    print(f"{'n':<8} {'O(log n)':<12} {'O(n)':<12} {'O(n^1.585)':<15} {'O(n^2)':<15}")
    print("-" * 65)
    
    for n in tamanhos:
        complexidades = calcular_complexidade_teorica(n)
        print(f"{n:<8} {complexidades['logaritmica']:<12.2f} {complexidades['linear']:<12} "
              f"{complexidades['karatsuba']:<15.0f} {complexidades['tradicional']:<15}")


def analise_casos_especiais():
    """
    Analisa casos especiais do algoritmo de Karatsuba.
    """
    print("\n=== Análise de Casos Especiais ===\n")
    
    # Caso 1: Números de tamanhos muito diferentes
    print("1. Números de tamanhos diferentes:")
    x1, y1 = 12345678901234567890, 123
    tempo1 = medir_tempo_multiplas_execucoes(karatsuba, x1, y1)
    print(f"   {x1} * {y1}")
    print(f"   Tempo: {tempo1:.6f}s")
    
    # Caso 2: Números com muitos zeros
    print("\n2. Números com padrões específicos:")
    x2, y2 = 1000000000, 2000000000
    tempo2 = medir_tempo_multiplas_execucoes(karatsuba, x2, y2)
    print(f"   {x2} * {y2}")
    print(f"   Tempo: {tempo2:.6f}s")
    
    # Caso 3: Potências de 10
    print("\n3. Potências de 10:")
    x3, y3 = 10**15, 10**15
    tempo3 = medir_tempo_multiplas_execucoes(karatsuba, x3, y3)
    print(f"   {x3} * {y3}")
    print(f"   Tempo: {tempo3:.6f}s")


def main():
    """
    Executa todas as análises de complexidade.
    """
    print("ANÁLISE DETALHADA DA COMPLEXIDADE DO ALGORITMO DE KARATSUBA")
    print("=" * 60)
    
    # Análise experimental
    analise_complexidade_experimental()
    
    # Demonstração do crescimento teórico
    demonstrar_crescimento_complexidade()
    
    # Análise de casos especiais
    analise_casos_especiais()
    
    print("\n=== Conclusões ===")
    print("1. O algoritmo de Karatsuba demonstra complexidade O(n^1.585)")
    print("2. Para números grandes, oferece vantagem significativa sobre O(n^2)")
    print("3. O overhead de recursão pode afetar números pequenos")
    print("4. A complexidade espacial O(log n) é aceitável para a maioria dos casos")

if __name__ == "__main__":
    main()