def data_para_texto(data_str):
    dias = {
        '01': 'Primeiro', '02': 'Dois', '03': 'Três', '04': 'Quatro', '05': 'Cinco', 
        '06': 'Seis', '07': 'Sete', '08': 'Oito', '09': 'Nove', '10': 'Dez', 
        '11': 'Onze', '12': 'Doze', '13': 'Treze', '14': 'Catorze', '15': 'Quinze', 
        '16': 'Dezesseis', '17': 'Dezessete', '18': 'Dezoito', '19': 'Dezenove', '20': 'Vinte', 
        '21': 'Vinte e um', '22': 'Vinte e dois', '23': 'Vinte e três', '24': 'Vinte e quatro', '25': 'Vinte e cinco', 
        '26': 'Vinte e seis', '27': 'Vinte e sete', '28': 'Vinte e oito', '29': 'Vinte e nove', '30': 'Trinta', 
        '31': 'Trinta e um'
    }
    
    meses = {
        '01': 'janeiro', '02': 'fevereiro', '03': 'março', '04': 'abril', '05': 'maio', 
        '06': 'junho', '07': 'julho', '08': 'agosto', '09': 'setembro', '10': 'outubro', 
        '11': 'novembro', '12': 'dezembro'
    }
    
    dia, mes, ano = data_str.split('/')
    
    dia_texto = dias[dia]
    mes_texto = meses[mes]
    
    return f"{dia_texto} de {mes_texto} de {ano}"

print(data_para_texto("26/11/2024"))
print(data_para_texto("23/11/2010"))
print(data_para_texto("31/12/193"))
print(data_para_texto("01/01/2000"))

# Não consegui um jeito de fazer a conversão do ano, consegui quase utilizando GPT mas decidi não usar.