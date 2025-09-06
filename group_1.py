import itertools
from typing import List 
import numpy as np 
import matplotlib.pyplot as plt 
import math
import cmath
# Exemple for the N group

def cartesian_group(n:int, include_negatives:bool = False) -> list:
    myList = list(range(-n, n+1)) if include_negatives else list(range(n+1))
    return list(itertools.product(myList, repeat=2))



#equivalence relation 

def equivalence(n:int, a:int):
    return [a + k*n for k in range(-100, 100)]
        
def transposition(n:int): #1 ou 2
    if n == 1:
        return 2 
    elif n == 2:
        return 1 
    else:
        return 'Error'

class Zn: 
    def __init__(self, n:int): 
        self._n = n
        self.ensemble_de_classes_equivalences = []
    @property
    def n(self):
        return self._n
    def ensembles(self)->List[List[int]]:
        return self.ensemble_de_classes_equivalences
    @n.setter 
    def n(self, value:int):
        self._n = value
        
    def ensemble(self, a:int)->List:
        classe = equivalence(self._n, a)
        self.ensemble_de_classes_equivalences.append(classe)
        return classe

X = [1, 2, 3, 4, 5, 6]

E = [[1, 4], [2, 5], [3, 6]]

def partition_equivalence(partition, x:int, y:int):
    for element in partition:
        if x in element and y in element:
            return True
        else: 
            return False 
def definir_classe(partition, x):
    for element in partition:
        if x in element: 
            return element 
    return []
def definir_matrice(partition):
    # Find the maximum element in the partition to determine matrix size
    max_elem = max(max(sub) for sub in partition if len(sub) > 0)
    #print (max_elem)
    M = np.zeros((max_elem, max_elem))
    for sub in partition:
        if len(sub) >= 2:
            M[sub[0] - 1][sub[1] - 1] = 1
    return M

#chaque heure de la montre est en faite une classe modulo 12 et votre montre est une représentation de Z/12Z 

#représentation montre 

def horloge(heure:int):
    if heure <= 12:
        classe_equivalence_heure = equivalence(12, heure)
        return classe_equivalence_heure
    else: 
        return "Error"

def classe_equi(x:float):
    return [x+i for i in range(0, 20)]

def points_cercles(classe:List[float]):
    return [cmath.exp(2*cmath.pi*nombre*1j) for nombre in classe]



def __main__():
    z7 = Zn(7)
    z7.n = 7 
    
    
    # print(z7.ensemble(6))
    # print(z7.ensemble(-1))
    # print(definir_matrice(E))
    # print(horloge(1))
    ma_classe = classe_equi(1/7)
    print(ma_classe)
    data = points_cercles(ma_classe)
    x = [ele.real for ele in data]
    # extract imaginary part
    y = [ele.imag for ele in data]
   
    plt.scatter(x, y)
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.show()
    
    
    
    
    
if __name__ == "__main__":
    __main__()
    

