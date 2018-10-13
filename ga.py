import random
import copy
import functions as ft

quantidade_casas = 5
quantidade_caracteristicas = 5
tamanho_populacao = 30

caracteristicas = {}
caracteristicas["cor"] = ["amarela", "azul", "branca", "verde", "vermelha"]
caracteristicas["nacionalidade"] = ["alemão", "dinamarquês", "inglês", "norueguês", "sueco"]
caracteristicas["bebida"] = ["água", "café", "cerveja" ,"chá", "leite"]
caracteristicas["cigarro"] = ["blends", "bluemaster", "dunhill", "pall mall", "prince"]
caracteristicas["animal"] = ["cachorros", "cavalos", "gatos", "pássaros", "peixes"]


def show(result):
    print(result["cor"])
    print(result["nacionalidade"])
    print(result["bebida"])
    print(result["animal"])
    print(result["cigarro"])
def selecaoRoleta(populacao):
    fitness_by_individuo_in_populacao = [ft.fitnessByRules(individuo) for individuo in populacao]
    indice_maior1=0
    tam_populacao = len(fitness_by_individuo_in_populacao)
    for indice_fit in range(tam_populacao):
        if(fitness_by_individuo_in_populacao[indice_fit]>fitness_by_individuo_in_populacao[indice_maior1]):
            indice_maior1 = indice_fit
    fitness_by_individuo_in_populacao[indice_maior1] = 0
    indice_maior2=0
    for indice_fit in range(tam_populacao):
        if(fitness_by_individuo_in_populacao[indice_fit]>fitness_by_individuo_in_populacao[indice_maior2]):
            indice_maior2 = indice_fit
    return[indice_maior1, indice_maior2]

def selecaoTorneio(populacao, tam_amostra=4):
    random_indices = random.sample(range(0,tamanho_populacao), tam_amostra)
    fitness_by_individuo_in_populacao = [ft.fitnessByRules(individuo) for individuo in populacao]
    indice_pai = 0
    indice_mae = 1
    for i in range(tam_amostra):
        k = random_indices[i]
        if(fitness_by_individuo_in_populacao[k]>fitness_by_individuo_in_populacao[indice_pai]):
            indice_pai = k
    for i in range(tam_amostra):
        k = random_indices[i]
        if(fitness_by_individuo_in_populacao[k]>fitness_by_individuo_in_populacao[indice_mae]):
            if(indice_pai != k):
                indice_mae = k
    return [indice_pai, indice_mae]

def crossoverUniforme(individuoA, individuoB, taxa=0.3):#70% de chance haver o crossover em cada ponto
    pai = copy.deepcopy(individuoA)
    mae = copy.deepcopy(individuoB)
    for i in pai.keys():
        for j in range(5):
            if(random.random()>taxa):
                posic_caract_pai = ft.posicao(pai[i],mae[i][j])
                posic_caract_mae = ft.posicao(mae[i], pai[i][j])
                value = mae[i][j]
                mae[i][j] = pai[i][j]
                pai[i][j] = value
                pai[i][posic_caract_pai] = mae[i][j]
                mae[i][posic_caract_mae] = value
    return [pai, mae]

def crossoverPontual(individuoA, individuoB, taxa=0.3):#70% de chance haver o crossover em cada ponto
    pai = copy.deepcopy(individuoA)
    mae = copy.deepcopy(individuoB)
    tam = 1
    for key in pai.keys():
       tam = len(pai[key])
       break
    for i in pai.keys():
        #for j in range(5):
        j = random.randint(0,tam-1)
        if(random.random()>taxa):
            posic_caract_pai = ft.posicao(pai[i],mae[i][j])
            posic_caract_mae = ft.posicao(mae[i], pai[i][j])
            value = mae[i][j]
            mae[i][j] = pai[i][j]
            pai[i][j] = value
            pai[i][posic_caract_pai] = mae[i][j]
            mae[i][posic_caract_mae] = value
    return [pai, mae]

def mutacaoMudancaPontos(individuo, taxa=0.7):
    for i in individuo.keys():
        for j in range(5):
            if(random.random()>taxa):#30% de chance haver o crossover em cada ponto
                random_indice = random.randint(0, quantidade_casas-1)
                temp = individuo[i][j]
                individuo[i][j] = individuo[i][random_indice]
                individuo[i][random_indice] = temp

def ga(populacao_inicial, tipo_selecao=selecaoTorneio, tipo_crossover=crossoverUniforme, tipo_mutacao=mutacaoMudancaPontos, max_num_geracoes=300):
    populacao = populacao_inicial
    geracao = 0
    while(geracao<max_num_geracoes):
        u = [ft.fitnessByRules(ind) for ind in populacao]
        print(max(u))
        for i in range(tamanho_populacao):
            if (ft.fitnessByRules(populacao[i])>=15):
                result = populacao[i]
                show(result)
                return

        temp = []
        for i in range(int(tamanho_populacao/2)):
            [pai, mae] = tipo_selecao(populacao)
            [filho, filha]= tipo_crossover(populacao[pai], populacao[mae])

            tipo_mutacao(filho)
            tipo_mutacao(filha)
            temp.append(filho)
            temp.append(filha)

        nova_populacao = []
        for i in range(tamanho_populacao):
            nova_populacao.append(populacao[i])
            nova_populacao.append(temp[i])

        i = 0
        while(i < tamanho_populacao*2):
            j = i
            while(j < tamanho_populacao*2):
                #print(fitnessByRules(nova_populacao[i]))
                #print(fitnessByRules(nova_populacao[j]))
                if(ft.fitnessByRules(nova_populacao[i])<ft.fitnessByRules(nova_populacao[j])):

                    individuo_temp = copy.deepcopy(nova_populacao[i])
                    nova_populacao[i] = copy.deepcopy(nova_populacao[j])
                    nova_populacao[j] = copy.deepcopy(individuo_temp)
                j+=1
            i+=1
        populacao = []
        for i in range(tamanho_populacao):
            populacao.append(nova_populacao[i])
        geracao+=1
    show(populacao[0])
    print(ft.fitnessByRules(populacao[0]))

            #select melhores in temp and in population

#é um grupo de 10 matrizes de combinações aleatórias das características
populacao = []

for i in range(tamanho_populacao):
    #é um hash com uma combinação aleatória das características
    result = {}
    for caract in caracteristicas.keys():
        info = []
        result[caract] = []
        random_indices = random.sample(range(0,quantidade_casas), quantidade_casas)
        for indice in random_indices:
            info.append(caracteristicas[caract][indice])
        result[caract] = info
    populacao.append(result)

ga(populacao, selecaoRoleta, crossoverPontual, mutacaoMudancaPontos)


