caracteristicas = {}
caracteristicas["cor"] = ["amarela", "azul", "branca", "verde", "vermelha"]
caracteristicas["nacionalidade"] = ["alemão", "dinamarquês", "inglês", "norueguês", "sueco"]
caracteristicas["bebida"] = ["água", "café", "cerveja" ,"chá", "leite"]
caracteristicas["cigarro"] = ["blends", "bluemaster", "dunhill", "pall mall", "prince"]
caracteristicas["animal"] = ["cachorros", "cavalos", "gatos", "pássaros", "peixes"]



from itertools import permutations
#
# caracteres = [0, 1, 2]
# permsList = []
# genComb = permutations(caracteres, 3) # aqui e onde tens de especificar o numero de chars que cada combinacao tenha
# for subset in genComb:
#     print(subset) # tuple retornado com uma combinacao por loop
#     permsList.append(subset)
# #print(permsList)
#

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


m= {}
def insert(m, key, combinacoes, elementos):
    for i in range(5):
        m[key].append(elementos[combinacoes[i]])

permList1 = []
genComb1 = permutations([0, 1, 2, 3, 4], 5)
for subset in genComb1:
     permList1.append(subset)



tam = 120
resolvido = 0
for c1 in range(tam):
    m["cor"] = []
    insert(m, "cor", permList1[c1], caracteristicas["cor"])
    for c2 in range(tam):
        m["nacionalidade"] = []
        insert(m, "nacionalidade", permList1[c2], caracteristicas["nacionalidade"])
        for c3 in range(tam):
            m["bebida"] = []
            insert(m, "bebida", permList1[c3], caracteristicas["bebida"])
            for c4 in range(tam):
                m["cigarro"] = []
                insert(m, "cigarro", permList1[c4], caracteristicas["cigarro"])
                for c5 in range(tam):
                    m["animal"] = []
                    insert(m, "animal", permList1[c5], caracteristicas["animal"])
                    #print(fitnessByRules(m))
                    if(fitnessByRules(m)>=15):
                        print(m)
                        print(fitnessByRules(m))
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


