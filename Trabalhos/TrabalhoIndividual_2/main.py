"""
    @File.: Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select)
            Implementação utilizando a abordagem de divisão e conquista.
    @Author.: Pedro Carbonaro
    @Date.: 01/09/2025
"""

def max_min(arr, start, end):

    """
    Implementação do algoritmo MaxMin Select utilizando divisão e conquista.
    
    Args:
        arr: Lista de números a ser analisada
        start: Índice inicial do subproblema
        end: Índice final do subproblema
    
    Returns:
        Tupla contendo (maior_elemento, menor_elemento)
    """
    # Caso base: se temos apenas um elemento
    if start == end:
        return arr[start], arr[start]
    
    # Caso base: se temos dois elementos
    if end - start == 1:
        if arr[start] > arr[end]:
            return arr[start], arr[end]
        else:
            return arr[end], arr[start]
    
    # Dividir o problema em duas partes
    mid = (start + end) // 2
    
    # Resolver recursivamente para as duas metades
    max1, min1 = max_min(arr, start, mid)
    max2, min2 = max_min(arr, mid + 1, end)
    
    # Combinar resultados
    return max(max1, max2), min(min1, min2)


def find_max_min(arr):

    """
    Função auxiliar para chamar o algoritmo MaxMin Select.
    
    Args:
        arr: Lista de números a ser analisada
    
    Returns:
        Tupla contendo (maior_elemento, menor_elemento)
    """
    
    if not arr:
        raise ValueError("A lista não pode estar vazia")
    
    return max_min(arr, 0, len(arr) - 1)


# Exemplo de uso
if __name__ == "__main__":
    
    # Teste com uma lista pequena
    small_list = [5, 2, 9, 1, 7, 3, 8, 6, 4]
    print("Lista de entrada:", small_list)
    maximum, minimum = find_max_min(small_list)
    print(f"Maior elemento: {maximum}")
    print(f"Menor elemento: {minimum}")
    
    # Teste com uma lista maior (gerada aleatoriamente)
    import random
    large_list = [random.randint(1, 1000) for _ in range(100)]
    print("\nLista grande (100 elementos) gerada aleatoriamente")
    maximum, minimum = find_max_min(large_list)
    print(f"Maior elemento: {maximum}")
    print(f"Menor elemento: {minimum}")
    
    # Teste com uma lista ainda maior para demonstrar a eficiência
    very_large_list = [random.randint(1, 10000) for _ in range(10000)]
    print("\nLista muito grande (10000 elementos) gerada aleatoriamente")
    maximum, minimum = find_max_min(very_large_list)
    print(f"Maior elemento: {maximum}")
    print(f"Menor elemento: {minimum}")