def calculaFib(entrada):
    fib = [0, 1]
    while fib[-1] < entrada:
        fib.append(fib[-1] + fib[-2])
    return fib

def confere(entrada,fib):
    for i in fib:
        if i == entrada:
            return f"O número {entrada} pertence à sequência de fibonacci."
    return f"O número {entrada} não pertence à sequência de fibonacci."

def imprime(lista):
    print("Sequência de fibonacci:", end=" ")
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()

entrada = int(input("Digite um número: "))
fib = calculaFib(entrada)
resultado = confere(entrada, fib)
imprime(fib)
print(resultado)
