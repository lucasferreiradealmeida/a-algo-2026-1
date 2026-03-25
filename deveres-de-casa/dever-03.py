def eh_palindromo(arr):
    # Caso Base: Um array vazio ou com apenas 1 elemento é sempre um palíndromo
    if len(arr) <= 1:
        return True
    
    # Passo Recursivo: Verifica se o primeiro e o último elemento são iguais
    if arr[0] == arr[-1]:
        # Se forem iguais, chama a função novamente para o "meio" do array
        # arr[1:-1] cria uma fatia ignorando o primeiro e o último item
        return eh_palindromo(arr[1:-1])
    else:
        # Se forem diferentes, já sabemos que não é palíndromo
        return False

# Testando com os exemplos do slide
array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

print(f"array1 = {array1} -> É palíndromo? {eh_palindromo(array1)}")
print(f"array2 = {array2} -> É palíndromo? {eh_palindromo(array2)}")
print(f"array3 = {array3} -> É palíndromo? {eh_palindromo(array3)}")
print(f"array4 = {array4} -> É palíndromo? {eh_palindromo(array4)}")