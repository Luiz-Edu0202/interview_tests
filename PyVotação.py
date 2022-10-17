def contador_de_votos(votos,candidato):
    contagem = 0
    for voto in votos:
        if voto == candidato:
            contagem += 1
    return contagem
 
 
def vencedor(candidatos,votos_do_vencedor):
    for candidato,votos in candidatos.items():
        if votos == votos_do_vencedor:
            return candidato
         

eleitor = []
municipio = []
votos = []


with open('dados_elecao.txt', 'r') as dados:
    for linha in dados:
        eleitor.append(linha.split(',')[0])
        municipio.append(linha.split(',')[1])
        votos.append(linha.split(',')[2].strip())
    eleitor.remove(eleitor[0])
    municipio.remove(municipio[0])
    votos.remove(votos[0])

dicionario_eleicao = {}
total_votos = len(eleitor) #ok
candidatos = list(set(votos)) #ok
votos_do_vencedor = contador_de_votos(votos,candidatos[0])
    
with open('resultado.txt','w') as result:
    result.write('Resultados eleitorais\n')
    result.write('-' * 28 + '\n')
    result.write(f'Total de votos: {total_votos}\n')
    result.write('-' * 28 + '\n')
    for candidato in candidatos:
        votos_no_candidato = contador_de_votos(votos,candidato)
        result.write(f'{candidato}: {votos_no_candidato * 100/ total_votos:.1f}% ({votos_no_candidato}) \n')
        dicionario_eleicao[candidato] = votos_no_candidato
        if votos_do_vencedor < votos_no_candidato:
            votos_do_vencedor = votos_no_candidato
    result.write('-' * 28 + '\n')
    vencedor = vencedor(dicionario_eleicao,votos_do_vencedor)
    result.write(f'Vencedor: {vencedor}')
    