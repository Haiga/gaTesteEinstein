def posicao(arr, value):
    for i in range(len(arr)):
        if(arr[i]==value):
            return i
    return -1

def fitnessByRules(individuo):
    m = individuo
    cont = 0
    if(m["nacionalidade"][0] == "norueguês"):
        cont +=1
    if(posicao(m["cor"], "vermelha") == posicao(m["nacionalidade"], "inglês")):
        if(posicao(m["cor"], "vermelha")!=-1 and posicao(m["nacionalidade"], "inglês") != -1):
            cont +=1
    if(posicao(m["animal"], "cachorros") == posicao(m["nacionalidade"], "sueco")):
        if(posicao(m["animal"], "cachorros") !=-1 and posicao(m["nacionalidade"], "sueco") !=-1):
            cont +=1
    if(posicao(m["bebida"], "chá") == posicao(m["nacionalidade"], "dinamarquês")):
        if(posicao(m["bebida"], "chá") !=-1 and posicao(m["nacionalidade"], "dinamarquês") !=-1):
            cont +=1
    if(posicao(m["cor"], "verde") == posicao(m["cor"], "branca") - 1):
        if(posicao(m["cor"], "verde") !=-1 and posicao(m["cor"], "branca")!=-1):
            cont +=1
    if(posicao(m["cor"], "verde") == posicao(m["bebida"], "café")):
        if(posicao(m["cor"], "verde") !=-1 and posicao(m["bebida"], "café")!=-1):
            cont +=1
    if(posicao(m["cigarro"], "pall mall") == posicao(m["animal"], "pássaros")):
        if(posicao(m["cigarro"], "pall mall") != -1 and posicao(m["animal"], "pássaros")!=-1):
            cont +=1
    if(posicao(m["cor"], "amarela") == posicao(m["cigarro"], "dunhill")):
        if(posicao(m["cor"], "amarela") !=-1  and posicao(m["cigarro"], "dunhill") !=-1):
            cont +=1
    if(posicao(m["bebida"], "leite") == 2):
        cont +=1
    if(posicao(m["cigarro"], "blends") == posicao(m["animal"], "gatos") +1 or posicao(m["cigarro"], "blends") == posicao(m["animal"], "gatos") -1):
        if(posicao(m["cigarro"], "blends") !=-1 and posicao(m["animal"], "gatos") !=-1):
            cont +=1
    if(posicao(m["animal"], "cavalos") == posicao(m["cigarro"], "dunhill") -1 or posicao(m["animal"], "cavalos") == posicao(m["cigarro"], "dunhill") +1):
        if(posicao(m["animal"], "cavalos") !=-1 and posicao(m["cigarro"], "dunhill") !=-1):
            cont +=1
    if(posicao(m["cigarro"], "bluemaster") == posicao(m["bebida"], "cerveja")):
        if(posicao(m["cigarro"], "bluemaster") !=-1 and posicao(m["bebida"], "cerveja")!=-1):
            cont +=1
    if(posicao(m["cigarro"], "prince") == posicao(m["nacionalidade"], "alemão")):
        if(posicao(m["cigarro"], "prince") !=-1 and posicao(m["nacionalidade"], "alemão")!=-1):
            cont +=1
    if(posicao(m["nacionalidade"], "norueguês") == posicao(m["cor"], "azul") -1 or posicao(m["nacionalidade"], "norueguês") == posicao(m["cor"], "azul") +1):
        if(posicao(m["nacionalidade"], "norueguês")!=-1 and posicao(m["cor"], "azul") !=-1):
            cont +=1
    if(posicao(m["cigarro"], "blends") == posicao(m["bebida"], "água") -1 or posicao(m["cigarro"], "blends") == posicao(m["bebida"], "água") +1):
        if(posicao(m["cigarro"], "blends") != -1 and posicao(m["bebida"], "água") !=-1):
            cont +=1
    return cont



def isValid(individuo):
    m = individuo
    cont = 0
    if(m["nacionalidade"][0] == "norueguês") or (posicao(m["nacionalidade"], "norueguês") == -1):
        cont +=1
    if(posicao(m["cor"], "vermelha") == posicao(m["nacionalidade"], "inglês")) \
            or (posicao(m["cor"], "vermelha")==-1) \
            or (posicao(m["nacionalidade"], "inglês") ==-1):
            cont +=1
    if(posicao(m["animal"], "cachorros") == posicao(m["nacionalidade"], "sueco")) \
            or (posicao(m["animal"], "cachorros") ==-1) \
            or (posicao(m["nacionalidade"], "sueco") ==-1):
            cont +=1
    if(posicao(m["bebida"], "chá") == posicao(m["nacionalidade"], "dinamarquês")) \
            or(posicao(m["bebida"], "chá") ==-1) \
            or (posicao(m["nacionalidade"], "dinamarquês") ==-1):
            cont +=1
    if(posicao(m["cor"], "verde") == posicao(m["cor"], "branca") - 1) \
            or (posicao(m["cor"], "verde") ==-1) \
            or (posicao(m["cor"], "branca")==-1):
            cont +=1
    if(posicao(m["cor"], "verde") == posicao(m["bebida"], "café")) \
            or (posicao(m["cor"], "verde") ==-1) \
            or (posicao(m["bebida"], "café")==-1):
            cont +=1
    if(posicao(m["cigarro"], "pall mall") == posicao(m["animal"], "pássaros")) \
            or (posicao(m["cigarro"], "pall mall") == -1) \
            or (posicao(m["animal"], "pássaros")==-1):
            cont +=1
    if(posicao(m["cor"], "amarela") == posicao(m["cigarro"], "dunhill")) \
            or (posicao(m["cor"], "amarela") ==-1) \
            or (posicao(m["cigarro"], "dunhill") ==-1):
            cont +=1
    if(posicao(m["bebida"], "leite") == 2) or (posicao(m["bebida"], "leite") == -1):
        cont +=1
    if(posicao(m["cigarro"], "blends") == posicao(m["animal"], "gatos") +1 or posicao(m["cigarro"], "blends") == posicao(m["animal"], "gatos") -1) \
            or (posicao(m["cigarro"], "blends") ==-1) \
            or (posicao(m["animal"], "gatos") ==-1):
            cont +=1
    if(posicao(m["animal"], "cavalos") == posicao(m["cigarro"], "dunhill") -1 or posicao(m["animal"], "cavalos") == posicao(m["cigarro"], "dunhill") +1) \
            or (posicao(m["animal"], "cavalos") ==-1) \
            or (posicao(m["cigarro"], "dunhill") ==-1):
            cont +=1
    if(posicao(m["cigarro"], "bluemaster") == posicao(m["bebida"], "cerveja")) \
            or (posicao(m["cigarro"], "bluemaster") ==-1) \
            or (posicao(m["bebida"], "cerveja")==-1):
            cont +=1
    if(posicao(m["cigarro"], "prince") == posicao(m["nacionalidade"], "alemão")) \
            or (posicao(m["cigarro"], "prince") ==-1) \
            or (posicao(m["nacionalidade"], "alemão")==-1):
            cont +=1
    if(posicao(m["nacionalidade"], "norueguês") == posicao(m["cor"], "azul") -1 or posicao(m["nacionalidade"], "norueguês") == posicao(m["cor"], "azul") +1) \
            or (posicao(m["nacionalidade"], "norueguês")==-1) \
            or (posicao(m["cor"], "azul") ==-1):
            cont +=1
    if(posicao(m["cigarro"], "blends") == posicao(m["bebida"], "água") -1 or posicao(m["cigarro"], "blends") == posicao(m["bebida"], "água") +1) \
            or (posicao(m["cigarro"], "blends") == -1) \
            or (posicao(m["bebida"], "água") ==-1):
            cont +=1
    return cont == 15


