import math

# Tarefa 1: Implementação da função recursiva
def f_recursiva(n):
    # Caso base
    if n == 1:
        return 2
    # Chamada recursiva
    else:
        return 2 * f_recursiva(n - 1) + n**2

# Dica do slide 2: Cálculo usando a fórmula fechada
def f_fechada(n):
    # A fórmula matemática fechada resolvida para esta recorrência
    resultado = 13 * math.pow(2, n - 1) - n**2 - 4*n - 6
    return int(resultado)

# Tarefa 2: Solicitar ao usuário um valor de n
try:
    n = int(input("Digite um valor inteiro para n (n >= 1): "))
    
    if n < 1:
        print("Por favor, digite um valor maior ou igual a 1.")
    else:
        # Avisa o usuário se o número for muito grande para evitar travamentos
        if n > 30:
            print("Aviso: Como a complexidade é O(2^n), o cálculo recursivo pode demorar muito ou estourar o limite de recursão.")
            
        print("\n--- Resultados ---")
        resultado_rec = f_recursiva(n)
        print(f"Cálculo via recursão: F({n}) = {resultado_rec}")
        
        resultado_fec = f_fechada(n)
        print(f"Cálculo via fórmula fechada: F({n}) = {resultado_fec}")

except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro.")