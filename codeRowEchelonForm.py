"Carlos Gabriel Estañol Solís"
"177173"
# -*- coding: utf-8 -*-

import numpy as np
import sys


print("\n CODIGO PARA ENCONTRAR SOLUCIONES A ECUACIONES LINEALES")
print(" @author: Carlos Gabriel Estañol Solís - 177173 \n")


# Ax = b
#coeficient matrix
A = np.array([[1.,-.4,-.6],[-.6,.9,-.2],[-.4,-.5,.8]])
# indepentent term vector
B = np.array([0,0,0]) # 1x3

#Bcolumn = np.array([[i],[j],[k]]) #3x1
#C = np.concatenate((A,Bcolumn), axis=1)

C = np.concatenate((A, B.reshape(-1, 1)), axis=1)

try:
    print("Solution using numpy: ")
    print(np.linalg.solve(A,B))
    print()
except Exception as e:
    print("Can't solve using numpy. \n")

print("Original matrix")
print(C)

for j in range(len(C)):
    print(f'\nModificando los elementos de la COLUMNA: {j+1}\n')
    if (C[j,j] == 0):
        print("Infinite solutions found. Final matrix is: ")
        print(C)
        sys.exit()
    elif C[j,j] != 1:
        print(f"Operación realizada: Row{j+1}/{C[j,j]}")
        C[j,:] = C[j,:] / C[j,j]
        print(C)
    else:
        print("\n La fila", j+1, "no fue modificada.\n")
    
    for i in range(len(C)):
        if i != j:
            print(f"\nModificando los elementos de la FILA {i+1}\n")
            print(f"Operación realizada: Row{i+1} - ({C[i,j]/C[j,j]}) Row{j}")
            C[i,:] = C[i,:] -C[i,j] * C[j,:] 
            
            print(C)
