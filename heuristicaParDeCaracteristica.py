from copy import deepcopy
import functions as ft
from itertools import permutations

def posicao(arr, value):
    for i in range(len(arr)):
        if(arr[i]==value):
            return i
    return -1

def insert(m , key1, key2, value1, value2, inicial=0):
    listx = []
    cont1 = inicial
    while(cont1<5):
        listx.append(cont1)
        cont1+=1
    cont1 = 0
    while(cont1<inicial):
        listx.append(cont1)
        cont1+=1

    for i in listx:
        if m[key1][i] == "" and m[key2][i] == "":
            m[key1][i] = value1
            m[key2][i] = value2
            return 1
    return -1

def call_insert(individuo, i, inicial=0):
    if i==0:
        return insert(individuo, "cor", "nacionalidade", "vermelha", "inglês", inicial)
    elif i==1:
        return insert(individuo, "cor", "bebida", "verde", "café", inicial)
    elif i==2:
        return insert(individuo, "bebida", "nacionalidade", "chá", "dinamarquês", inicial)
    elif i==3:
        return insert(individuo, "cigarro", "animal", "pall mall", "pássaros", inicial)
    elif i==4:
        return insert(individuo, "cor", "cigarro", "amarela", "dunhill", inicial)
    elif i==5:
        return insert(individuo, "cigarro", "bebida", "bluemaster", "cerveja", inicial)
    elif i==6:
        return insert(individuo, "cigarro", "nacionalidade", "prince", "alemão", inicial)
    elif i==7:
        return insert(individuo, "animal", "nacionalidade", "cachorros", "sueco", inicial)

def complete(m, key, combinacoes, elementos):
    cont = 0
    for i in range(5):
        if(m[key][i]==""):
            m[key][i] = elementos[combinacoes[cont]]
            cont +=1

def zerarSolucao():
    individuo = {}

    individuo["cor"] = ["", "", "", "", ""]
    individuo["nacionalidade"] = ["", "", "", "", ""]
    individuo["bebida"] = ["", "", "", "", ""]
    individuo["cigarro"] = ["", "", "", "", ""]
    individuo["animal"] = ["", "", "", "", ""]

    individuo["nacionalidade"][0] = "norueguês"
    individuo["bebida"][2] = "leite"
    return individuo

faltantes = {}
faltantes["cor"] = ["azul", "branca"]
faltantes["nacionalidade"] = []
faltantes["bebida"] = ["água"]
faltantes["cigarro"] = ["blends"]
faltantes["animal"] = ["cavalos", "gatos", "peixes"]

permList = []
genComb = permutations([0, 1, 2, 3, 4, 5, 6, 7], 8)
for subset in genComb:
     permList.append(subset)

permList1 = []
genComb1 = permutations([0, 1], 2)
for subset in genComb1:
    permList1.append(subset)
permList2 = [[]]
permList3 = [[0]]
permList4 = [[0]]
permList5 = []
genComb5 = permutations([0, 1, 2], 3)
for subset in genComb5:
    permList5.append(subset)


total_combinacoes = len(permList)
for combinacao in range(total_combinacoes):
    for inicial in range(5):
        solucao = zerarSolucao()
        flag = 1
        for i in range(8):

            permutacao = permList[combinacao]
            if call_insert(solucao, permutacao[i], inicial) == -1:
                solucao = zerarSolucao()
                flag = 0
                break
        if(flag):
            solucao_corrente = deepcopy(solucao)
            flag_final = 0
            for i1 in range(len(permList1)):
                for i2 in range(len(permList2)):
                    for i3 in range(len(permList3)):
                        for i4 in range(len(permList4)):
                            for i5 in range(len(permList5)):

                                complete(solucao_corrente, "cor", permList1[i1], faltantes["cor"])
                                complete(solucao_corrente, "nacionalidade", permList2[i2], faltantes["nacionalidade"])
                                complete(solucao_corrente, "bebida", permList3[i3], faltantes["bebida"])
                                complete(solucao_corrente, "cigarro", permList4[i4], faltantes["cigarro"])
                                complete(solucao_corrente, "animal", permList5[i5], faltantes["animal"])


                                if(ft.fitnessByRules(solucao_corrente)==15):
                                    for i in solucao_corrente:
                                        print(solucao_corrente[i])
                                    print(ft.fitnessByRules(solucao_corrente))
                                    #print(solucao_corrente)
                                    flag_final = 1
                                    break

                                solucao_corrente = deepcopy(solucao)
                            if(flag_final):
                                break
                        if(flag_final):
                            break
                    if(flag_final):
                        break
                if(flag_final):
                    break
        if(flag_final):
            break
    if(flag_final):
        break
