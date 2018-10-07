quantidade_casas = 5
quantidade_caracteristicas = 5
tamanho_populacao = 150

caracteristicas = {}
caracteristicas["cor"] = ["amarela", "azul", "branca", "verde", "vermelha"]
caracteristicas["nacionalidade"] = ["alemão", "dinamarquês", "inglês", "norueguês", "sueco"]
caracteristicas["bebida"] = ["água", "café", "cerveja" ,"chá", "leite"]
caracteristicas["cigarro"] = ["blends", "bluemaster", "dunhill", "pall mall", "prince"]
caracteristicas["animal"] = ["cachorros", "cavalos", "gatos", "pássaros", "peixes"]

import random
import copy

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

def posicao(arr, value):
    for i in range(len(arr)):
        if(arr[i]==value):
            return i

def fitnessByRules(individuo):
    m = individuo
    cont = 0
    if(m["nacionalidade"][0] == "norueguês"):
        cont +=1
    if(posicao(m["cor"], "vermelha") == posicao(m["nacionalidade"], "inglês")):
        cont +=1
    if(posicao(m["animal"], "cachorros") == posicao(m["nacionalidade"], "sueco")):
        cont +=1
    if(posicao(m["bebida"], "chá") == posicao(m["nacionalidade"], "dinamarquês") ):
        cont +=1
    if(posicao(m["cor"], "verde") == posicao(m["cor"], "branca") - 1):
        cont +=1
    if(posicao(m["cor"], "verde") == posicao(m["bebida"], "café")):
        cont +=1
    if(posicao(m["cigarro"], "pall mall") == posicao(m["animal"], "pássaros")):
        cont +=1
    if(posicao(m["cor"], "amarela") == posicao(m["cigarro"], "dunhill")):
        cont +=1
    if(posicao(m["bebida"], "leite") == 2):
        cont +=1
    if(posicao(m["cigarro"], "blends") == posicao(m["animal"], "gatos") +1 or posicao(m["cigarro"], "blends") == posicao(m["animal"], "gatos") -1):
        cont +=1
    if(posicao(m["animal"], "cavalos") == posicao(m["cigarro"], "dunhill") -1 or posicao(m["animal"], "cavalos") == posicao(m["cigarro"], "dunhill") +1):
        cont +=1
    if(posicao(m["cigarro"], "bluemaster") == posicao(m["bebida"], "cerveja")):
        cont +=1
    if(posicao(m["cigarro"], "prince") == posicao(m["nacionalidade"], "alemão") ):
        cont +=1
    if(posicao(m["nacionalidade"], "norueguês") == posicao(m["cor"], "azul") -1 or posicao(m["nacionalidade"], "norueguês") == posicao(m["cor"], "azul") +1):
        cont +=1
    if(posicao(m["cigarro"], "blends") == posicao(m["bebida"], "água") -1 or posicao(m["cigarro"], "blends") == posicao(m["bebida"], "água") +1):
        cont +=1
    return cont

def selecao(populacao):
    random_indices = random.sample(range(0,tamanho_populacao), 4)
    fitness_by_individuo_in_populacao = [fitnessByRules(individuo) for individuo in populacao]
    indice_pai = 0
    indice_mae = 1
    for i in range(4):
        k = random_indices[i]
        if(fitness_by_individuo_in_populacao[k]>fitness_by_individuo_in_populacao[indice_pai]):
            indice_pai = k
    for i in range(4):
        k = random_indices[i]
        if(fitness_by_individuo_in_populacao[k]>fitness_by_individuo_in_populacao[indice_mae]):
            if(indice_pai != k):
                indice_mae = k
    return [indice_pai, indice_mae]

def crossover(individuoA, individuoB):
    pai = copy.deepcopy(individuoA)
    mae = copy.deepcopy(individuoB)
    for i in pai.keys():
        for j in range(5):
            if(random.random()>0.3):#70% de chance haver o crossover em cada ponto
                posic_caract_pai = posicao(pai[i],mae[i][j])
                posic_caract_mae = posicao(mae[i], pai[i][j])
                value = mae[i][j]
                mae[i][j] = pai[i][j]
                pai[i][j] = value
                pai[i][posic_caract_pai] = mae[i][j]
                mae[i][posic_caract_mae] = value
    return [pai, mae]
def mutacao(individuo):
    for i in individuo.keys():
        for j in range(5):
            if(random.random()>0.7):#50% de chance haver o crossover em cada ponto
                random_indice = random.randint(0, quantidade_casas-1)
                temp = individuo[i][j]
                individuo[i][j] = individuo[i][random_indice]
                individuo[i][random_indice] = temp
fim = 0
while(1):
    u = [fitnessByRules(ind) for ind in populacao]
    print(max(u))
    for i in range(tamanho_populacao):
        if (fitnessByRules(populacao[i])>=12):
            result = populacao[i]
            print(result["cor"])
            print(result["nacionalidade"])
            print(result["bebida"])
            print(result["animal"])
            print(result["cigarro"])
            fim = 1
            break
    if(fim):
        break
    temp = []
    for i in range(int(tamanho_populacao/2)):
        [pai, mae] = selecao(populacao)
        [filho, filha]= crossover(populacao[pai], populacao[mae])

        mutacao(filho)
        mutacao(filha)
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
            if(fitnessByRules(nova_populacao[i])<fitnessByRules(nova_populacao[j])):

                individuo_temp = copy.deepcopy(nova_populacao[i])
                nova_populacao[i] = copy.deepcopy(nova_populacao[j])
                nova_populacao[j] = copy.deepcopy(individuo_temp)
            j+=1
        i+=1
    populacao = []
    for i in range(tamanho_populacao):
        populacao.append(nova_populacao[i])
        #select melhores in temp and in population




print(fitnessByRules(result))

