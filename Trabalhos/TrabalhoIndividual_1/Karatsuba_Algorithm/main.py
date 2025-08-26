"""
    @File.: Implementação do algoritmo de Karatsuba para multiplicação eficiente.
    @Author.: Pedro Carbonaro
    @Date.: 2023-10-05
"""

def karatsuba(x, y):
    
    """    
    O algoritmo divide dois números em partes menores e usa a fórmula:
    x * y = (a * 10^n + b) * (c * 10^n + d)
          = a*c * 10^(2n) + (a*d + b*c) * 10^n + b*d
          = a*c * 10^(2n) + ((a+b)*(c+d) - a*c - b*d) * 10^n + b*d
    
    Args:
        x (int): Primeiro número inteiro
        y (int): Segundo número inteiro
    
    Returns:
        int: Produto de x e y
    """
    # Caso base: se algum dos números for pequeno, usa multiplicação tradicional
    if x < 10 or y < 10:
        return x * y
    
    # Determina o número de dígitos do maior número
    n = max(len(str(x)), len(str(y)))
    
    # Calcula a metade do número de dígitos (arredonda para cima se ímpar)
    m = n // 2
    
    # Divide x em duas partes: a (parte alta) e b (parte baixa)
    a = x // (10 ** m)  # Parte alta de x
    b = x % (10 ** m)   # Parte baixa de x
    
    # Divide y em duas partes: c (parte alta) e d (parte baixa)
    c = y // (10 ** m)  # Parte alta de y
    d = y % (10 ** m)   # Parte baixa de y
    
    # Três multiplicações recursivas (ao invés de quatro)
    ac = karatsuba(a, c)           # a * c
    bd = karatsuba(b, d)           # b * d
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd  # (a+b)*(c+d) - ac - bd = ad + bc
    
    # Combina os resultados usando a fórmula de Karatsuba
    result = ac * (10 ** (2 * m)) + ad_plus_bc * (10 ** m) + bd
    
    return result


def multiplicacao_tradicional(x, y):
    """
    Multiplicação tradicional para comparação de desempenho.
    
    Args:
        x (int): Primeiro número inteiro
        y (int): Segundo número inteiro
    
    Returns:
        int: Produto de x e y
    """

    return x * y


def medir_tempo_execucao(func, x, y):
    """
    Mede o tempo de execução de uma função de multiplicação.
    
    Args:
        func: Função a ser medida
        x (int): Primeiro número
        y (int): Segundo número
    
    Returns:
        tuple: (resultado, tempo_em_segundos)
    """
    import time
    
    start_time = time.time()
    resultado = func(x, y)
    end_time = time.time()
    
    return resultado, end_time - start_time


def main():
    """
    Função principal que demonstra o uso do algoritmo de Karatsuba.
    """
    print("=== Algoritmo de Karatsuba ===\n")
    
    # Casos de teste
    casos_teste = [
        (12, 34),
        (1234, 5678),
        (123456, 789012),
        (12345678901234567890, 98765432109876543210)
    ]
    
    print("Comparação entre Karatsuba e Multiplicação Tradicional:\n")
    print(f"{'Números':<40} {'Karatsuba':<15} {'Tradicional':<15} {'Tempo K':<12} {'Tempo T':<12}")
    print("-" * 100)
    
    for x, y in casos_teste:
        # Executa Karatsuba
        resultado_k, tempo_k = medir_tempo_execucao(karatsuba, x, y)
        
        # Executa multiplicação tradicional
        resultado_t, tempo_t = medir_tempo_execucao(multiplicacao_tradicional, x, y)
        
        # Verifica se os resultados são iguais
        assert resultado_k == resultado_t, f"Erro: resultados diferentes para {x} * {y}"
        
        print(f"{str(x) + ' * ' + str(y):<40} {resultado_k:<15} {resultado_t:<15} {tempo_k:<12.6f} {tempo_t:<12.6f}")
    
    print("\n=== Demonstração passo a passo ===")
    x, y = 1234, 5678
    print(f"\nCalculando {x} * {y} com Karatsuba:")
    print(f"Resultado: {karatsuba(x, y)}")
    print(f"Verificação: {x * y}")

if __name__ == "__main__":
    main()