import re

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)  
    if len(cpf) != 11:
        return "CPF inválido. Deve conter 11 dígitos."
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf_formatado

def validar_email(email):
    email = email.lower()
    padrao = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    if not re.match(padrao, email):
        return "E-mail inválido."
    return email

def validar_telefone(telefone):
    telefone = re.sub(r'\D', '', telefone)  
    if len(telefone) != 11:
        return "Telefone inválido. Deve conter 11 dígitos."
    telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    telefone_inteiro = int(telefone)
    return telefone_inteiro, telefone_formatado


cpf = input("Digite o CPF: ")
email = input("Digite o e-mail: ")
telefone = input("Digite o telefone: ")

cpf_validado = validar_cpf(cpf)
email_validado = validar_email(email)
telefone_validado = validar_telefone(telefone)

print(f"CPF: {cpf_validado}")
print(f"E-mail: {email_validado}")
if isinstance(telefone_validado, tuple):
    print(f"Telefone (inteiro): {telefone_validado[0]}")
    print(f"Telefone (formatado): {telefone_validado[1]}")
else:
    print(telefone_validado)