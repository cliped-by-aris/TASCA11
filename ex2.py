from functools import reduce

def Passar_a_Numero():
    l=[3,4,1,5]
    a=reduce(lambda a,b: str(a) + str(b),l)
    print(a)

#Programa principal

b= Passar_a_Numero()