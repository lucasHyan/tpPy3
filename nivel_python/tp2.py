transacoes = [
    "1,ProdutoA,2,10.00",
    "2,ProdutoB,1,20.00",
    "3,ProdutoA,1,10.00",
    "4,ProdutoC,5,5.00"
]

def calcular_vendas(transacoes):
    vendas = {}
    for transacao in transacoes:
        id_produto, nome_produto, quantidade, valor_unitario = transacao.split(',')
        quantidade = int(quantidade)
        valor_unitario = float(valor_unitario)
        valor_total = quantidade * valor_unitario
        
        if nome_produto in vendas:
            vendas[nome_produto] += valor_total
        else:
            vendas[nome_produto] = valor_total
    
    return vendas

def produtos_principais(transacoes):
    quantidades = {}
    receitas = {}
    
    for transacao in transacoes:
        id_produto, nome_produto, quantidade, valor_unitario = transacao.split(',')
        quantidade = int(quantidade)
        valor_unitario = float(valor_unitario)
        valor_total = quantidade * valor_unitario
        
        if nome_produto in quantidades:
            quantidades[nome_produto] += quantidade
        else:
            quantidades[nome_produto] = quantidade
        
        if nome_produto in receitas:
            receitas[nome_produto] += valor_total
        else:
            receitas[nome_produto] = valor_total
    
    produto_mais_vendido = max(quantidades, key=quantidades.get)
    produto_maior_receita = max(receitas, key=receitas.get)
    
    return produto_mais_vendido, produto_maior_receita

def calcular_vendas_convertidas(transacoes, fator_conversao):
    total_receitas = 0

    for transacao in transacoes:
        id_produto, nome_produto, quantidade, valor_unitario = transacao.split(',')
        quantidade = int(quantidade)
        valor_unitario = float(valor_unitario)
        valor_total = quantidade * valor_unitario
        total_receitas += valor_total
    
    total_receitas_convertidas = total_receitas * fator_conversao
    
    print(f"Total de vendas convertidas: {total_receitas_convertidas:.2f}")

print(calcular_vendas(transacoes))
print(produtos_principais(transacoes))
calcular_vendas_convertidas(transacoes, 5)

