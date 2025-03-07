from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        return f"Soc un {self.especie} de {self.edat} anys."

class Cavall(Animal):
    def xerrar(self):
        return "Hiiiii"
    
    def mourem(self):
        return "Trotant"

class Dofi(Animal):
    def xerrar(self):
        return "Cliii Cliii"
    
    def mourem(self):
        return "Nedant"

class Abella(Animal):
    def xerrar(self):
        return "Bzzz Bzzz"
    
    def mourem(self):
        return "Volant"
    
    def picar(self):
        return "Picada llançada!"

class Huma(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom
    
    def xerrar(self):
        return "Hola!"
    
    def mourem(self):
        return "Caminant"

class Fiet(Huma):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares = pares
    
    def nompares(self):
        return f"Els meus pares són: {', '.join(self.pares)}"

class Centaure(Cavall, Huma):
    def __init__(self, especie, edat, nom):
        Huma.__init__(self, especie, edat, nom)
    
    def xerrar(self):
        return "Soc un centaure i puc parlar!"
    
    def mourem(self):
        return "Galopant i caminant"

class Xou:
    def xerrar(self):
        return "Xou fa un so especial!"
    
    def mourem(self):
        return "Xou es mou d'una manera única"
    
    def quisoc(self):
        return "Soc un Xou!"

animals = [
    Cavall("Cavall", 5),
    Dofi("Dofi", 8),
    Abella("Abella", 1),
    Huma("Huma", 30, "Alex"),
    Fiet("Huma", 5, "Pep", ["Alex", "Susan"]),
    Centaure("Centaure", 100, "Quiron"),
    Xou()
]

for animal in animals:
    print(animal.quisoc())
    print(animal.xerrar())
    print(animal.mourem())
    if isinstance(animal, Abella):
        print(animal.picar())
    if isinstance(animal, Fiet):
        print(animal.nompares())
    print()