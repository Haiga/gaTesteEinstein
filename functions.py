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
