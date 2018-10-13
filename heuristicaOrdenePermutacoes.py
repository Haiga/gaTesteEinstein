from copy import deepcopy
from itertools import permutations
import functions as ft

caracteristicas = {}
caracteristicas["cor"] = ["amarela", "azul", "vermelha", "verde", "branca"]
caracteristicas["nacionalidade"] = ["norueguês", "dinamarquês", "inglês", "alemão", "sueco"]
caracteristicas["bebida"] = ["água", "café", "leite" ,"chá", "cerveja"]
caracteristicas["cigarro"] = ["dunhill", "bluemaster", "blends", "pall mall", "prince"]
caracteristicas["animal"] = ["cavalos", "gatos", "cachorros", "pássaros", "peixes"]

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

def insert(m, key, combinacoes, elementos):
    for i in range(5):
        m[key].append(elementos[combinacoes[i]])

def ordene(permList, key):
    teste = zerarSolucao()
    values = []
    total_perm = len(permList)
    for indice_perm in range(total_perm):
        insert(teste, key, permList[indice_perm], caracteristicas[key])
        values.append(ft.fitnessByRules(teste))
        teste = zerarSolucao()

    for i in range(total_perm):
        for j in range(i, total_perm):
            if(values[i]<values[j]):
                temp = values[i]
                values[i] = values[j]
                values[j] = temp
                temp_perm = deepcopy(permList[i])
                permList[i] = deepcopy(permList[j])
                permList[j] = deepcopy(temp_perm)

permList1 = []
permList2 = []
permList3 = []
permList4 = []
permList5 = []
genComb1 = permutations([0, 1, 2, 3, 4], 5)
for subset in genComb1:
     permList1.append(subset)
     permList2.append(subset)
     permList3.append(subset)
     permList4.append(subset)
     permList5.append(subset)

ordene(permList1,'cor')
ordene(permList2, 'nacionalidade')
ordene(permList3, 'bebida')
ordene(permList4, 'cigarro')
ordene(permList5, 'animal')

tam = len(permList1)
resolvido = 0
m={}
for c1 in range(tam):
    m["cor"] = []
    insert(m, "cor", permList1[c1], caracteristicas["cor"])
    for c2 in range(tam):
        m["nacionalidade"] = []
        insert(m, "nacionalidade", permList2[c2], caracteristicas["nacionalidade"])
        for c3 in range(tam):
            m["bebida"] = []
            insert(m, "bebida", permList3[c3], caracteristicas["bebida"])
            for c4 in range(tam):
                m["cigarro"] = []
                insert(m, "cigarro", permList4[c4], caracteristicas["cigarro"])
                for c5 in range(tam):
                    m["animal"] = []
                    insert(m, "animal", permList5[c5], caracteristicas["animal"])
                    #print(ft.fitnessByRules(m))
                    if(ft.fitnessByRules(m)>=15):
                        for key in m:
                            print(m[key])
                        #print(m)
                        print(ft.fitnessByRules(m))
                        resolvido = 1
                        break
                if(resolvido):
                    break
            if (resolvido):
                break
        if(resolvido):
            break
    if(resolvido):
        break
