def leitor_de_arquivos():
    lista_de_dados = []
    with open("dados_financeiros.txt") as dados:
        lista_de_dados = dados.readlines()
        del(lista_de_dados[0])
    return lista_de_dados


def identificador_de_valores(lista_de_dados):
    valores = []
    for valor in lista_de_dados:
        valores.append(int(valor.split(",")[1]))   
    return valores

            
def organizador_de_texto(lista_de_dados,meses,valor_liquido,media_das_mudancas,maior_aumento,maior_diminuicao):
    
    
    
    mensagem = f"""
    Analise financeira
    ----------------------------
    Total de meses: {meses}
    Total: $ {valor_liquido:.2f}
    Média: $ {media:.2f}
    Variação da média: $ {media_das_mudancas:.2fs}
    Maior aumento nos lucros: fevereiro de 2012 ($ {maior_aumento:.2f})
    Maior redução nos lucros: setembro de 2013 ($ {maior_diminuicao:.2f})
    """
    print(mensagem)
    return mensagem
        

def contador_de_meses(lista_de_dados):
    numero_total_de_meses = 0
    meses = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec"
    for linha in lista_de_dados:
        if linha.split("-")[0] in meses: numero_total_de_meses += 1
    return numero_total_de_meses



def calculador_de_valor_liquido(lista_de_dados):
    valor_liquido = 0
    for valor in lista_de_dados:
        valor_liquido += int(valor.split(",")[1])   
    return valor_liquido 


def media_de_lucros_perdas(valor_liquido,meses):
    return valor_liquido / meses


def maior_aumento_menor_reducao(lista_de_dados,):
    valores = identificador_de_valores(lista_de_dados)
    maior_aumento = valores[0] - valores[1]
    maior_diminuicao = valores[0] - valores[1]
    valor_anterior = valores[0]
    for valor in valores:
        if valor_anterior - valor < maior_aumento:
            maior_aumento = valor_anterior - valor
        elif valor_anterior - valor > maior_diminuicao:
            maior_diminuicao = valor_anterior - valor
        valor_anterior = valor
    return maior_aumento, maior_diminuicao


def media_das_mudancas(lista_de_dados):
    media_das_mudancas = 0
    valores = identificador_de_valores(lista_de_dados)
    valor_anterior = valores[0]
    for valor in valores:
        media_das_mudancas += valor_anterior - valor
    media_das_mudancas = media_das_mudancas/ (len(valores)) 
    return media_das_mudancas



    
lista_de_dados = leitor_de_arquivos()
meses = contador_de_meses(lista_de_dados)
valor_liquido = calculador_de_valor_liquido(lista_de_dados)
media = media_de_lucros_perdas(valor_liquido,meses)
media_das_mudancas = media_das_mudancas(lista_de_dados)
maior_aumento,maior_diminuicao = maior_aumento_menor_reducao(lista_de_dados)
media_das_mudancas(lista_de_dados)


"""
O número total de meses incluídos no conjunto de dados ok
O valor total líquido de "Lucros / Perdas" durante todo o período ok
A média dos "Lucros / Perdas" durante todo o período ok
A média das mudanças em "Lucros / Perdas" durante todo o período
O maior aumento nos lucros (data e valor) durante todo o período ok
A maior redução nas perdas (data e valor) ao longo de todo o período ok
"""
"""
Analise financeira
----------------------------
Total de meses: 86
Total: $ 38382578
Média: $ 446309,04
Variação da média: $ -2315,12
Maior aumento nos lucros: fevereiro de 2012 ($ 1926159)
Maior redução nos lucros: setembro de 2013 ($ -2196167)
"""