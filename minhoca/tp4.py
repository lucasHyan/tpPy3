frase = input("Digite uma frase: ")

num_caracteres = len(frase)
num_palavras = len(frase.split())
num_espacos = frase.count(' ')

print(f"Número de caracteres: {num_caracteres}")
print(f"Número de palavras: {num_palavras}")
print(f"Número de espaços em branco: {num_espacos}")