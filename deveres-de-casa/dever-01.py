import random
import time

def insertion_sort(arr):
    """Implementação do algoritmo Insertion Sort O(n^2)."""
    # Percorre do segundo elemento até o final
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move os elementos do arr[0...i-1] que são maiores que a chave (key)
        # para uma posição à frente de sua posição atual
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Tamanhos das listas definidos no exercício
tamanhos_n = [1000, 5000, 10000, 20000, 50000]

print("Iniciando o comparativo de algoritmos de ordenação...")

for n in tamanhos_n:
    # 1. Gerar lista aleatória de tamanho n
    lista_original = [random.randint(0, 100000) for _ in range(n)]
    
    # Criamos cópias para garantir que ambos os métodos ordenem a mesma lista desordenada
    lista_para_insertion = lista_original.copy()
    lista_para_timsort = lista_original.copy()
    
    print(f"\n{'-'*30}")
    print(f"Tamanho da lista (n) = {n}")
    
    # 2. Medir o tempo do Insertion Sort O(n^2)
    inicio_insertion = time.time()
    insertion_sort(lista_para_insertion) # Ordena in-place (modifica a própria lista)
    fim_insertion = time.time()
    tempo_insertion = fim_insertion - inicio_insertion
    
    print(f"Tempo Insertion Sort: {tempo_insertion:.5f} segundos")
    
    # 3. Medir o tempo do Timsort O(n log n) usando a função nativa sorted()
    inicio_timsort = time.time()
    lista_ordenada_timsort = sorted(lista_para_timsort) # Retorna uma nova lista
    fim_timsort = time.time()
    tempo_timsort = fim_timsort - inicio_timsort
    
    print(f"Tempo Timsort (nativo): {tempo_timsort:.5f} segundos")