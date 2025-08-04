import numpy as np
from numpy import linalg
from numpy.linalg import solve, det
#import PySimpleGUI as sg

#define a minimum tolerance to avoid errors
epsilon = float(1e-9)
tooSmall = 1

#check for the tolerance in order to avoid margin errors
def tolerance(determinant):
    if np.abs(determinant) < epsilon:
        return 0
    else:
        return determinant
    
#solve system using Gauss-Jordan method
def GaussJordanMethod(C):
    for j in range(len(C)):
        input("Enter to continue the process: ")
        if C[j,j] == 0:
            count = sum(1 for value in C[j, :] if value != 0)  # Count non zeros in the j-th row
            if count <= 2:
                if C[j, len(C)] == 0:
                    print("\n\n Infinite solutions found. Final matrix is:")
                    print(C)
                    return
                elif C[j, len(C)] != 0:
                    print("\n\n No solutions found. Final matrix is:")
                    print(C)
                    return
        elif C[j,j] != 1 and C[j,j] != 0:

            while np.abs(C[j,j]) < tooSmall:
                print("Too small: computation may lead to inconsistencies. Matrix multiplied by 10.")
                C = C*10
            print()

            print(f'\n Modifying elements in COLUMN: {j+1}\n')
            print(f"Operation made: Row{j+1}/{C[j,j]}")
            C[j,:] = C[j,:] / C[j,j]
            print(C)
        else:
            print("\n Row", j+1, "was not modifed.\n")
        
        for i in range(len(C)):
            if i != j and C[j,j] != 0:
                print(f"\n Modifying elements in ROW {i+1}\n")
                print(f"Operation made: Row{i+1} - ({C[i,j]/C[j,j]}) Row{j+1}")
                C[i,:] = C[i,:] -C[i,j] * C[j,:] 
                
                print(C)
    return
    
#input number of variables in the system
def inputVarNumber():
    access = False
    while not access:
        try:
            varNumber = int(input("How many variables does the system have? "))
            access = True
        except Exception as e:
            print("Exception: number must be integer; try again. \n")
    return varNumber

#introduce the matrix's coefficients and the vector of results
def inputSystem():   
    n = int(np.abs(inputVarNumber()))

    #coeficient matrix of n size
    A = np.zeros((n,n))
    # indepentent term vector of n elements
    B = np.zeros(n)

    print()
    print("Insert coefficients for A[n,n]x matrix and b[n] vector: \n")
    for i in range(n):
        print(f"coefficients in the {i+1} equation: ")
        for j in range(n):
            go = False
            while not go:
                try:    
                    A[i,j] = float(input(f"A[{i+1}, {j+1}] = "))
                    go = True
                except Exception as e:
                    print("Input must be a number; try again.")

    print()
    print("Insert coefficients for b[n] vector: \n")
    for i in range(n):
        go = False
        while not go:
            try:    
                B[i] = float(input(f"b[{i+1}] = "))
                go = True
            except Exception as e:
                print("Input must be a number; try again.")

    C = np.concatenate((A, B.reshape(-1, 1)), axis=1)

    return A,B,C

#function to solve the system
def solveSystem():
    # Ax = b
    A,B,C = inputSystem()

    print("\n Original matrix")
    print(C)

    determinant = tolerance(det(A))
    print("\n Determinant is: ", determinant)

    if (determinant != 0):
        try:
            print("Solution using numpy: ")
            print(np.linalg.solve(A,B))
            print()
        except Exception as e:
            print("Solution couldn't be computed using numpy. \n")
            print("Using Gauss-Jordan method. \n")
            GaussJordanMethod(C)
    else:
        print("Using Gauss-Jordan method. \n")
        GaussJordanMethod(C)

    return

def Heading():
    print("\n CODE FOR SOLVING LINEAR EQUATION SYSTEMS")
    print(" @author: Juan Pablo Estañol Solís - 174856")
    print("          Carlos Estañol Solís - 177173 \n")
    print("\n This program solves Linear Equations Systems")

#function to compute the matrices or exit
def options():
    ans = input("\n\n Solve a new linear equations system? [Y/n] ")
    print()

    if ans == 'Y' or ans == "y":
        solveSystem()
        return True
    else:
        print("\n Ending program...")
        return False

#main code
def main():
    Heading()
    ans = True
    while ans:
        ans = options()
    return

main()