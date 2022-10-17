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


def identificador_de_datas(lista_de_dados):
    datas = []
    for data in lista_de_dados:
        datas.append(data.split(",")[0])   
    return datas
        

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
    return -(maior_aumento), -(maior_diminuicao)


def media_das_mudancas(lista_de_dados,variacao):
    valores = identificador_de_valores(lista_de_dados)
    i = 0
    while i < len(valores) - 1:
        variacao.append(valores[i+1] - valores[i])
        i += 1
    return sum(variacao)/len(variacao)



variacao = []    
lista_de_dados = leitor_de_arquivos() #ok
meses = contador_de_meses(lista_de_dados) #ok
valor_liquido = calculador_de_valor_liquido(lista_de_dados) #ok
media = media_de_lucros_perdas(valor_liquido,meses) #ok
media_das_mudancas = media_das_mudancas(lista_de_dados,variacao) #ok
maior_aumento,maior_diminuicao = maior_aumento_menor_reducao(lista_de_dados) #ok
data = identificador_de_datas(lista_de_dados)

with open('financeiro_resultado.txt', 'w') as result:
    result.write('Analise financeira\n')
    result.write('-' * 28 + '\n')
    result.write(f'Total de meses: {meses}\n')
    result.write(f'Total: $ {valor_liquido}\n')
    result.write(f'Média: $ {media:.2f}\n')
    result.write(f'Variação da média: $ {media_das_mudancas:.2f}\n')
    result.write(f'Maior aumento nos lucros: {data[variacao.index(maior_aumento) + 1]} ($ {maior_aumento})\n')
    result.write(f'Maior redução nos lucros: {data[variacao.index(maior_diminuicao) + 1]} ($ {maior_diminuicao})\n')
