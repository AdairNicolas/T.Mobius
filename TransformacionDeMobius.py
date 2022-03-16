from gettext import find
from turtle import color
import matplotlib.pyplot as plt
import numpy as np


def numcomp(z1):

    z1p = z1.find("+")
    z1n = z1.find("-")

    if z1p != -1:
        aa = z1[0:z1p]
        a = float(aa)
        bb = z1[(z1p+1):len(z1)-1]
        b = float(bb)
        return a, b
    elif z1n != -1:
        aa = z1[0:z1n]
        a = float(aa)
        bb = z1[(z1n):len(z1)-1]
        b = float(bb)
        return a, b
    else:
        print("Z no es correcto, por favor revise sus datos")


def suma(a, b, a2, b2):
    sumr = a+a2
    sumi = b+b2
    sum = (str(sumr) + "+"+str(sumi)+"i")
    return sum


def resta(a, b, a2, b2):
    resr = a-a2
    resi = b-b2
    res = (str(resr)+"+"+str(resi)+"i")
    return res


def multiplicacion(a, b, a2, b2):
    mulr = (a*a2)-(b*b2)
    muli = (a*b2)+(b*a2)
    mul = (str(mulr)+"+"+str(muli)+"i")
    return mul


def division(a, b, a2, b2):
    divr = ((a*a2)-(b*(-b2)))/((a2*a2)+(b2*b2))
    divi = ((a*(-b2))+(b*a2))/((a2*a2)+(b2*b2))
    div = (str(divr)+"+"+str(divi)+"i")
    return div


def valoresc(cir, r1, i1, r2, i2, r3, i3, r4, i4):
    tip = cir[0:1]
    if(tip == "("):
        hlim = cir.find("x")
        hfin = cir.find(")")
        hp = cir[hlim+1:hfin]
        klim = cir.find("y", hfin)
        kfin = cir.find(")", klim)
        kp = cir[klim+1:kfin]
        rlim = cir.find("=", kfin)
        rp = cir[rlim+1:]
        h = -1*float(hp)
        k = -1*float(kp)
        rpp = float(rp)
        r = pow(rpp, 0.5)
        print("h: ", h)
        print("k: ", k)
        print("r: ", r)

        return h, k, r
    elif(tip != "("):
        lima = cir.find("(")
        AS = cir[0:lima]
        limfa = cir.find(")", lima)
        limb = cir.find("x", limfa)
        BS = cir[limfa+1:limb]
        limc = cir.find("y", limb)
        CS = cir[limb+1:limc]
        limd = cir.find("=", limc)
        DS = cir[limc+1:limd]
        A = float(AS)
        BP = float(BS)
        CP = float(CS)
        DP = float(DS)
        if (A == 0):
            print("\n----La función insertada es una recta----")
            x = np.arange(-8, 8)
            y = (-BP*x-DP)/CP

            plt.plot(x, y)
            plt.title("Funcion original", fontsize=15)
            plt.grid(True)
            plt.axhline(0, color='green', lw=2)
            plt.axvline(0, color='green', lw=2)
            plt.xlabel('Real')
            plt.ylabel('Imaginario')
            plt.show()

            p1r, p1i = 0, -DP/CP #interseca con el el eje y
            p2r, p2i = -DP/BP, 0 #intersecta con el eje x
            p3r, p3i = (p1r+p2r)/2, (p1i+p2i)/2 #punto entre las intersecciones
            print(f"\nIntersección en el eje y: pt1({p1r},{p1i})")
            print(f"Intersección en el eje x: pt2({p2r},{p2i})")
            print(f"Punto medio entre los anteriores puntos: pt3({p3r},{p3i})")

            res1 = mobius(p1r, p1i, p2r, p2i, p3r, p3i, 0, 0,
                          0, r1, i1, r2, i2, r3, i3, r4, i4)
            res2 = mobius(p2r, p2i, p1r, p1i, p3r, p3i, 0, 0,
                          0, r1, i1, r2, i2, r3, i3, r4, i4)
            res3 = mobius(p3r, p3i, p2r, p2i, p1r, p1i, 0, 0,
                          0, r1, i1, r2, i2, r3, i3, r4, i4)

            print(f"\nPunto pt1 transformado: {res1}")
            print(f"Punto pt2 transformado: {res2}")
            print(f"Punto pt3 transformado: {res3}")

            rr1, ri1 = numcomp(res1)
            rr2, ri2 = numcomp(res2)
            rr3, ri3 = numcomp(res3)

            hnn, knn, rnn = sistemadeecuaciones(rr1, ri1, rr2, ri2, rr3, ri3)

            graficar(hnn, knn, rnn, rr1, ri1, rr2,
                     ri2, rr3, ri3, 'Función Transformada:')

            exit()

        B = BP/A
        C = CP/A
        D = DP/A
        h = -B/2
        k = -C/2
        r = (1/2)*(pow(((B*B)+(C*C)-(4*D)), 0.5))
        print(A)
        print(B)
        print(C)
        print(D)
        print(r)
        print(h)
        print(k)
        return h, k, r


def obtenerpuntos(h, k, r):
    x1 = h+r
    y1 = k
    x2 = h-r
    y2 = k
    x3 = h
    y3 = k+r
    return x1, y1, x2, y2, x3, y3


def mobius(x, y, x2, y2, x3, y3, h, k, r, r1, i1, r2, i2, r3, i3, r4, i4):

    #ad - bc != 0

    ad = multiplicacion(r1, i1, r4, i4)
    adR, adI = numcomp(ad)

    bc = multiplicacion(r2, i2, r3, i3)
    bcR, bcI = numcomp(bc)

    bandera = resta(adR, adI, bcR, bcI)
    banderaR, banderaI = numcomp(bandera)

    if (banderaR == 0.0 and banderaI == 0.0):
        print("\nLa función ingresada NO es transformacion de mobius pues ad - bc = 0!!!")
        print("Por lo que solo se transforma a un punto...")
        graficar(h, k, r, x, y, x2, y2, x3, y3, 'Función Original')
        graficapunto(1, 0, 'Función Transformada')
        exit()
    else:
        mul = multiplicacion(x, y, r1, i1)
        azr, azi = numcomp(mul)
        mul2 = multiplicacion(x, y, r3, i3)
        czr, czi = numcomp(mul2)
        sum = suma(azr, azi, r2, i2)
        numeradorr, numeradori = numcomp(sum)
        sum2 = suma(czr, czi, r4, i4)
        denominadorr, denominadori = numcomp(sum2)
        res = division(numeradorr, numeradori, denominadorr, denominadori)
        return res


def sistemadeecuaciones(p1r, p1i, p2r, p2i, p3r, p3i):
    A1 = (2*p2r)-(2*p1r)
    B1 = (2*p2i)-(2*p1i)
    C1 = (pow(p2r, 2)+pow(p2i, 2))-(pow(p1r, 2)+pow(p1i, 2))
    A2 = (2*p3r)-(2*p1r)
    B2 = (2*p3i)-(2*p1i)
    C2 = (pow(p3r, 2)+pow(p3i, 2))-(pow(p1r, 2)+pow(p1i, 2))

    hn = ((C1*B2) - (C2*B1))/((A1*B2)-(A2*B1))
    kn = ((C1*A2) - (C2*A1))/((B1*A2)-(B2*A1))
    rn = pow(pow(p1r-hn, 2) + pow(p1i-kn, 2), 0.5)
    return hn, kn, rn


def resolverSistema(p1r, p1i, p2r, p2i, p3r, p3i):
    # ax+bx=c
    # dx+ex=f
    a = (2*p2r)-(2*p1r)
    b = (2*p2i)-(2*p1i)
    c = (pow(p2r, 2)+pow(p2i, 2))-(pow(p1r, 2)+pow(p1i, 2))

    d = (2*p3r)-(2*p1r)
    e = (2*p3i)-(2*p1i)
    f = (pow(p3r, 2)+pow(p3i, 2))-(pow(p1r, 2)+pow(p1i, 2))

    A = np.array([[a, b], [d, e]])
    B = np.array([c, f])

    x = np.linalg.pinv(A).dot(B)
    radio = pow(pow(p1r - x[0], 2) + pow(p1i - x[1], 2), 0.5)

    print("\nCentro de la transformación: ", x)
    print("Radio de la transformación: ", radio)

    return x, radio


def graficar(h, k, r, x1, y1, x2, y2, x3, y3, tit):
    fig, axes = plt.subplots()
    draw_circle = plt.Circle((h, k), r, fill=False)

    xmin = h-r
    xmax = h+r
    ymin = k-r
    ymax = k+r

    plt.title(tit)
    plt.axis([xmin-(r/10), xmax+(r/10), ymin-(r/10), ymax+(r/10)])

    plt.scatter(h, k, color="red")
    plt.scatter(x1, y1, color="blue")
    plt.scatter(x2, y2, color="blue")
    plt.scatter(x3, y3, color="blue")

    axes.set_aspect(1)
    axes.add_artist(draw_circle)

    plt.axhline(0, color='green', lw=2)
    plt.axvline(0, color='green', lw=2)

    plt.grid()
    plt.show()


def graficapunto(a, b, tit):
    plt.title(tit)
    plt.axis([(a-20), (a+20), (b-20), (b+20)])
    plt.plot(a, b, 'ro')
    plt.grid(True)
    plt.axhline(0, color='green', lw=2)
    plt.axvline(0, color='green', lw=2)
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.show()


print("-----BIENVENDIO A LA CALCULADORA DE TRANSFORMACION DE MOBIUS-----\n")

z1 = input("Por favor, ingresa el primer numero complejo: ")
z2 = input("Ingresa el segundo numero complejo: ")
z3 = input("Ingresa el tercer numero complejo: ")
z4 = input("Ingresa el cuarto numero complejo: ")

circunferencia = input("Ingrese su ecuación de la circunferencia:")

r1, i1 = numcomp(z1)
r2, i2 = numcomp(z2)
r3, i3 = numcomp(z3)
r4, i4 = numcomp(z4)

h, k, r = valoresc(circunferencia, r1, i1, r2, i2, r3, i3, r4, i4)

print("\nUsted ingreso: \n")
print(f"(x + {h})^2 + (y + {k})^2 = {r}^2")

x1, y1, x2, y2, x3, y3 = obtenerpuntos(h, k, r)

p1 = mobius(x1, y1, x2, y2, x3, y3, h, k, r, r1, i1, r2, i2, r3, i3, r4, i4)
p2 = mobius(x2, y2, x1, y1, x3, y3, h, k, r, r1, i1, r2, i2, r3, i3, r4, i4)
p3 = mobius(x3, y3, x1, y1, x2, y2, h, k, r, r1, i1, r2, i2, r3, i3, r4, i4)
p1r, p1i = numcomp(p1)
p2r, p2i = numcomp(p2)
p3r, p3i = numcomp(p3)

centro, r2 = resolverSistema(p1r, p1i, p2r, p2i, p3r, p3i)

print("\nLa nueva ecuación de la transformacion es:\n ")
print(f"(x + {centro[0]})^2 + (y + {centro[1]})^2 = {r2}^2")

graficar(h, k, r, x1, y1, x2, y2, x3, y3, 'Función Original')
graficar(centro[0], centro[1], r2, p1r, p1i,
         p2r, p2i, p3r, p3i, 'Función Transformada')
