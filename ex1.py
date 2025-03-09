def llegir_llista():
    l = []
    a = "a"
    while a != ".":
        a = input("Introdueix una paraula: ")
        if a !=".":
            l.append(a)
    return l

def lenp(l): 
    print(list(map(lambda l:len(l),l)))


#Programa principal
a=llegir_llista()
b=lenp(a)