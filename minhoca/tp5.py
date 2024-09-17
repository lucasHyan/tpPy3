def soma_dos_digitos():
    string_numerica = input("Digite uma string numérica: ")

    if string_numerica.isdigit():
        soma = sum(int(digito) for digito in string_numerica)
        print(f"A soma dos dígitos é: {soma}")
    else:
        print("Erro: A string contém caracteres não numéricos.")


soma_dos_digitos()
