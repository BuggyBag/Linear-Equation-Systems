#### @ author: Carlos Estañol
#### @ ID: 177173
#### @ Bisection method

import numpy as np

def my_bisection(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        print("The scalars a and b do not bound a root")
        return
        #raise Exception("The scalars a and b do not bound a root")
        

    m = (a + b) / 2

    if np.abs(f(m)) < tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, tol)



#### Exercise 1
print("\n Exercise 1 \n")

f = lambda x: x - 2**(-x)
root = my_bisection(f, 0, 1, 0.00001)

print("The solution to the equation is equal to ", root)


#### Exercise 2
print("\n Exercise 2 \n")

f = lambda x: np.exp(x) - x**2 + 3*x + 2
root = my_bisection(f, -1, 0, 0.00001)

print("The solution to the equation is equal to ", root)


#### Exercise 3
print("\n Exercise 3 \n")

f = lambda x: 2*x*np.cos(2*x) - (x+1)**2
root = my_bisection(f, -3, -2, 0.00001)
root1 = my_bisection(f, -1, 0, 0.00001)

print("The solution to the equation is equal to ", root)
print("The solution to the equation is equal to ", root1)


#### Exercise 4
print("\n Exercise 4 \n")

f = lambda x: x*np.cos(x) - 2*x**2 + 3*x - 1
root = my_bisection(f, 0.2, 0.3, 0.00001)
root1 = my_bisection(f, 1.2, 1.3, 0.00001)

print("The solution to the equation is equal to ", root)
print("The solution to the equation is equal to ", root1)