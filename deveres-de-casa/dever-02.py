import time
import sys

# Aumenta o limite de recursões permitidas pelo Python para suportar n=1000
sys.setrecursionlimit(2000)

def fatorial(n):
    """
    Calcula o fatorial de n de forma recursiva.
    """
    # Caso base: O fatorial de 0 ou 1 é sempre 1.
    # Isso impede que a função chame a si mesma infinitamente.
    if n == 0 or n == 1:
        return 1
    
    # Passo recursivo: Multiplica o número atual pelo fatorial do seu antecessor.
    else:
        return n * fatorial(n - 1)

# Valores de entrada (n) exigidos pelo exercício
valores_n = [10, 100, 500, 1000]

print("Medição de Tempo de Execução:")
print("-" * 40)

# Laço para testar cada valor de n e medir o tempo
for n in valores_n:
    # Captura o tempo exato antes da execução
    inicio = time.perf_counter() 
    
    # Executa o cálculo do fatorial
    resultado = fatorial(n) 
    
    # Captura o tempo exato após a execução
    fim = time.perf_counter() 
    
    # Calcula a diferença para obter o tempo total de execução
    tempo_execucao = fim - inicio
    
    print(f"n = {n:<5} | Tempo de execução: {tempo_execucao:.8f} segundos")


"""
Análise de Complexidade Assintótica
Complexidade de Tempo: O(n)

Explicação do Raciocínio:
A complexidade assintótica de tempo deste algoritmo é linear, representada por O(n).

Para entender o motivo, precisamos observar quantas vezes a função principal é executada. Quando chamamos fatorial(n), a função realiza uma operação de multiplicação em tempo constante O(1) 
e então faz uma nova chamada a si mesma passando n - 1. Esse processo se repete até que n chegue a 1 ou 0 (o caso base).

Portanto, para um número n, o algoritmo fará exatamente n chamadas recursivas. Como cada chamada custa um tempo constante O(1), 
o tempo total de execução cresce de forma diretamente proporcional ao tamanho da entrada n. Se você dobrar o valor de n, o número de operações (e o tempo de execução) 
também dobrará aproximadamente.

(Atenção: Na prática da linguagem Python, 
multiplicações de números gigantescos, como o resultado de 1000!, podem ter um leve custo adicional de 
processamento interno da linguagem, mas matematicamente a estrutura recursiva do algoritmo continua sendo de ordem linear O(n)).
"""