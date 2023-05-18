#Função para buscar os candidatos e devolver uma lista com aqueles atendem aos critérios fornecidos pelo usuario.
def buscar_candidatos(resultados, nota_entrevista, nota_teorico, nota_pratica, nota_soft):
    candidatos = []
    for candidato, notas in resultados.items():
        nota_e, nota_t, nota_p, nota_s = [int(n[1]) for n in notas.split("_")]
        if nota_e >= nota_entrevista and nota_t >= nota_teorico and nota_p >= nota_pratica and nota_s >= nota_soft:
            candidatos.append(candidato)

    return candidatos

#Entrada das notas mínimas informadas pelo usuario
nota_entrevista = int(input("Digite a nota mínima (de 0 a 9) desejada na entrevista: "))
nota_teorico = int(input("Digite a nota mínima (de 0 a 9) desejada no teste teórico: "))
nota_pratica = int(input("Digite a nota mínima (de 0 a 9) desejada no teste prático: "))
nota_soft = int(input("Digite a nota mínima (de 0 a 9) desejada na avaliação de soft skills: "))

#Usuarios e notas disponiveis no codigo
resultados = {'Freddie Mercury': 'e8_t9_p8_s8',
         'Roger Waters': 'e8_t8_p7_s7',
         'Kurt Cobain': 'e5_t7_p6_s3',
         'Paul McCartney': 'e8_t7_p7_s8',
         'Klaus Meine': 'e8_t8_p9_s8'
}

#Função que checa os dados fornecidos pela função "busca_candidatos" e mostra o resultado
#Também faz a classificação por ordem alfabetica atraves do 'sorted' e retorna uma mensagem caso não encontre candidato.
candidatos_entrevistados = buscar_candidatos(resultados, nota_entrevista, nota_teorico, nota_pratica, nota_soft)
if len(candidatos_entrevistados) == 0:
    print('\n'+'=-'*36)
    print('\033[33m''\033[1m''Não foi possível encontrar candidatos com os parâmetros que você definiu.''\033[0m')
    print('=-'*36,'\n')

else:
    print("\033[1;36m"+"Excelente!"+"\033[0;0m",'Excelente! Encontrei os(as) seguintes candidatos(as):')
    candidatos_entrevistados = sorted(candidatos_entrevistados)
    for candidato in candidatos_entrevistados:
        nota = resultados[candidato]
        print('=-'*31)
        print("\033[32m{}: {}\033[0;0m \n".format(candidato,nota))

print('FIM=-=-=-=-=-=-=-=-=-=-FIM=-=-=-=-=-=-=-=-=-=-'*4)