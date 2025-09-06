from abc import ABC, abstractmethod

class groupe(ABC):
    pass
class groupe_Z(groupe): 
    def __init__(self, element_neutre:int, loi:str):
        #attributs privés
        self._element_neutre = element_neutre
        self._loi = loi 
        self._elements = [self._element_neutre]
    @property 
    def element_neutre(self):
        return f"L'element neutre est {self._element_neutre}"
    @property
    def loi(self):
        return f"la loi est {self._loi}"
    @property 
    def elements(self):
        return self._elements
    
    def element_a_rajouter(self, element):
        if type(element) == int:
            self._elements.append(element)
        if type(element) == list: 
            self._elements += element 
        
    def homomorphisme(self, k:int):
        resultats = []
        for element in self._elements:
            resultats.append(k*element)
        return resultats
    def symetrie(self): 
        for element in self._elements: 
            if -element not in self._elements:
                self._elements.append(-element)


class generateur_a_Z(groupe_Z):
    def __init__(self, a:int, groupe):
        self._a = a
        self._groupe = groupe 
        self._elements = []
    
    @property
    def a(self):
        return self._a
    
    @property
    def elements(self):
        return self._elements
    
    def generate(self, a, n): 
        for i in range(-n, n+1): 
            self._elements.append(i*a)
            
        
    
    
            
        
    
    




def main(): 
    print("Ici on fait des essais: ")
    groupe_additif = groupe_Z(0, "additive")
    print(groupe_additif.element_neutre)
    print(groupe_additif.loi)
    groupe_additif.element_a_rajouter(1)
    groupe_additif.element_a_rajouter([k for k in range(3, 100)])
    groupe_additif.symetrie()
    print(groupe_additif.elements)



if __name__ == "__main__":
    main()