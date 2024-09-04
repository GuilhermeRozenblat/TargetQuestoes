
def contaLetraA(palavra):
    x = 0
    for char in palavra:
        if char == 'a' or char == 'A':
            x += 1

    if x > 0:
        return f"A letra 'A' aparece {x} vez(es) na palavra."
    else:
        return "A letra 'A' não aparece na palavra."

entrada = input("Digite uma palavra: ")
resultado = contaLetraA(entrada)
print(resultado)