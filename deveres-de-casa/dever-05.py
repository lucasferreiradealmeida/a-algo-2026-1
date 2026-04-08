import math

# ==========================================
# EXERCÍCIO 1: FUNÇÃO RECURSIVA E FÓRMULA
# ==========================================
def f_recursiva(n):
    if n == 1:
        return 2
    else:
        return 2 * f_recursiva(n - 1) + n**2

def f_fechada(n):
    resultado = 13 * math.pow(2, n - 1) - n**2 - 4*n - 6
    return int(resultado)

# ==========================================
# EXERCÍCIO 2.1: MERGE SORT O(n log n)
# ==========================================
def merge_sort(lista):
    # Criamos uma cópia para não alterar a lista original no teste
    arr = lista.copy()
    
    def _merge_sort_recursivo(arr):
        if len(arr) > 1:
            meio = len(arr) // 2
            esq = arr[:meio]
            dir = arr[meio:]

            _merge_sort_recursivo(esq)
            _merge_sort_recursivo(dir)

            i = j = k = 0
            while i < len(esq) and j < len(dir):
                if esq[i] < dir[j]:
                    arr[k] = esq[i]
                    i += 1
                else:
                    arr[k] = dir[j]
                    j += 1
                k += 1

            while i < len(esq):
                arr[k] = esq[i]
                i += 1
                k += 1

            while j < len(dir):
                arr[k] = dir[j]
                j += 1
                k += 1
    
    _merge_sort_recursivo(arr)
    return arr

# ==========================================
# EXERCÍCIO 2.2: MULTIPLICAÇÃO DE MATRIZES O(n³)
# ==========================================
def multiplicar_matrizes(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# ==========================================
# ÁREA DE EXECUÇÃO (TESTES)
# ==========================================
if __name__ == "__main__":
    print("-" * 50)
    print(" 1. TESTE DA FUNÇÃO RECURSIVA")
    print("-" * 50)
    n_teste = 6
    print(f"Calculando F({n_teste})...")
    print(f" -> Via Recursão: F({n_teste}) = {f_recursiva(n_teste)}")
    print(f" -> Via Fórmula:  F({n_teste}) = {f_fechada(n_teste)}")
    
    print("\n" + "-" * 50)
    print(" 2. TESTE DO MERGE SORT")
    print("-" * 50)
    vetor_desordenado = [38, 27, 43, 3, 9, 82, 10]
    vetor_ordenado = merge_sort(vetor_desordenado)
    print(f"Lista Original: {vetor_desordenado}")
    print(f"Lista Ordenada: {vetor_ordenado}")

    print("\n" + "-" * 50)
    print(" 3. TESTE DA MULTIPLICAÇÃO DE MATRIZES")
    print("-" * 50)
    matriz_A = [[1, 2], [3, 4]]
    matriz_B = [[5, 6], [7, 8]]
    
    print("Matriz A:")
    for linha in matriz_A: print(f"  {linha}")
        
    print("Matriz B:")
    for linha in matriz_B: print(f"  {linha}")
        
    resultado_matriz = multiplicar_matrizes(matriz_A, matriz_B)
    print("Resultado (A x B):")
    for linha in resultado_matriz:
        print(f"  {linha}")
    print("-" * 50)