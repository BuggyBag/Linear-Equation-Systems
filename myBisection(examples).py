#### @ author: Carlos Estañol
#### @ ID: 177173
#### @ Bisection method (examples)

import numpy as np

def my_bisection(f, a, b, tol):
    if np.sign(f(a))==np.sign(f(b)):
        print("The scalars a and b do not bound a root")
        return
        #raise Exception("The scalars a and b do not bound a root")
  
    m=(a+b)/2

    if np.abs(f(m))<tol:
        return m
    elif np.sign(f(a))==np.sign(f(m)):
        return my_bisection(f, m, b, tol)
    elif np.sign(f(b))==np.sign(f(m)):
        return my_bisection(f, a, m, tol)



#------------Example 1 --------------#
    
print("\n Example #1 \n")

f = lambda x: x**2 - 2

root = my_bisection(f, 0, 2, 0.1)
print("The solution to the equation is ", root)

root1 = my_bisection(f, 0, 2, 0.1)
print("The solution to the equation is ", root1)

print("f(root) = ", f(root))
print("f(root1) = ", f(root1))

#---------Example 2-----------------#

print("\n Example #2 \n")

f = lambda x: x*3 + 4*x*2 - 10

root = my_bisection(f, 1, 2, 10**(-4))
print("The solution to the equation is ", root)


#-----------Example 3-------------#

print("\n Example #3 \n")

f = lambda x: np.sqrt(x) - np.cos(x)

root = my_bisection (f, 0, 1, 10**(-3))
print("The solution to the equation is ", root)