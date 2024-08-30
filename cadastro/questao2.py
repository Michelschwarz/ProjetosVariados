def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n
def main():
    try:
        numero = int(input("Digite um número para verificar se ele pertence a sequencia"))
        if is_fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
