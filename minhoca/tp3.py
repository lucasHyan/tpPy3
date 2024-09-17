import string

def palavra_mais_longa(texto):
    texto_sem_pontuacao = texto.translate(str.maketrans('', '', string.punctuation))
    palavras = texto_sem_pontuacao.split()
    palavra_mais_longa = max(palavras, key=len)
    
    return palavra_mais_longa

texto_exemplo = "O rato roeu a roupa do rei de roma."
print("A palavra mais longa é:", palavra_mais_longa(texto_exemplo))