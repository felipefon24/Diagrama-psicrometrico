from math import *

def Presion_vapor(T):
    if 0<=T<57:
        A1=23.7093
        B1=4111
        C1=237.7
        Ps=exp(A1-(B1/(C1+T)))
    elif 57<=T<135:
        A2=23.1863
        B2=3809.4
        C2=226.7
        Ps=exp(A2-(B2/(C2+T)))
    else:
        Ps="La temperatura esta fuera de los rangos de operacion"
    return Ps

def Temperatura_maxima(P):
    A1=23.7093
    B1=4111
    C1=237.7
    T=(B1/(A1-log(P)))
    if 0<=T<57:
        Tmax=T
    elif 57<=T<135:
        A2=23.186
        B2=3809.4
        C2=226.7
        Tmax=(B2/(A2-log(P)))
    else:
        Tmax="La temperatura quedo fuera de los rangos de operacion"
    return Tmax
print("hasta aqui llego el codigo")


