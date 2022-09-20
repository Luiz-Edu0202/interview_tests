def leitor_de_arquivos():
    lista_de_dados = []
    with open("dados_financeiros.txt") as dados:
        lista_de_dados = dados.readlines()
        del(lista_de_dados[0])
    return lista_de_dados


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


def media_das_mudancas(media,lista_de_dados):
    media_das_mudancas = 0
    for valor in lista_de_dados:
        mes = int(valor.split(",")[1])   
        media_das_mudancas += mes - media
    return media_das_mudancas


def maior_aumento_menor_reducao(lista_de_dados):
    return max(lista_de_dados), min(lista_de_dados)


lista_de_dados = leitor_de_arquivos()
meses = contador_de_meses(lista_de_dados)
valor_liquido = calculador_de_valor_liquido(lista_de_dados)
media = media_de_lucros_perdas(valor_liquido,meses)
media_das_mudancas = media_das_mudancas(media,lista_de_dados)
print(maior_aumento_menor_reducao(lista_de_dados))