#implementacion basica del metodo. No usar, no borrar hasta la entrega.

from math import *
def g(x):
#Function
    func=0.5*sqrt(10-x**3)

    return func

p0=0

tolerance=0.00001

n0=50

i=1

while i<=n0:

    p=g(p0)

    if abs(p-p0)<tolerance:

        print("El punto fijo es ",p," despues de ",i," iteraciones")

        break

    i=i+1

    p0=p

if i>n0:

    print("Not possible to obtain root")