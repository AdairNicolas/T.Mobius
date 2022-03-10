
from gettext import find

def numcomp(z1):

    z1p = z1.find("+")
    z1n = z1.find("-",1)

    if z1p!=-1:
        aa=z1[0:z1p]
        a=float(aa)
        bb=z1[(z1p+1):len(z1)-1]
        b=float(bb)
        return a,b
    elif z1n != -1:
        aa=z1[0:z1n]
        a=float(aa)
        bb=z1[(z1n):len(z1)-1]
        b=float(bb)
        return a,b
    else:
        print("z1 es invalido")

def suma(a,b,a2,b2):
    sumr= a+a2
    sumi= b+b2
    sum=(str(sumr) +"+"+str(sumi)+"i")
    return sum

def resta(a,b,a2,b2):
    resr = a-a2
    resi = b-b2
    res = (str(resr)+"+"+str(resi)+"i")
    return res

def multiplicacion(a,b,a2,b2):
    mulr= (a*a2)-(b*b2)
    muli= (a*b2)+(b*a2)
    mul = (str(mulr)+"+"+str(muli)+"i")
    return mul

def division(a,b,a2,b2):
    divr = ((a*a2)-(b*(-b2)))/((a2*a2)+(b2*b2))
    divi = ((a*(-b2))+(b*a2))/((a2*a2)+(b2*b2))
    div =  (str(divr)+"+"+str(divi)+"i")
    return div    


def valoresc (cir):
    tip = cir[0:1]
    if(tip == "("):
        return cir
    elif(tip!="("):
        lima = cir.find("(")
        AS = cir[0:lima]
        limfa = cir.find(")",lima)
        limb = cir.find("x",limfa)
        BS = cir[limfa+1:limb]
        limc = cir.find("y",limb)
        CS = cir[limb+1:limc]
        limd = cir.find("=",limc)
        DS = cir[limc+1:limd]
        A = float(AS)
        BP = float(BS)
        CP = float(CS)
        DP = float(DS)
        B = BP/A
        C = CP/A
        D = DP/A
        h = -B/2
        k = -C/2
        r = (1/2)*(pow(((B*B)+(C*C)-(4*D)),0.5 ) )
        print(A)
        print(B)
        print(C)
        print(D)
        print(r)
        print(h)
        print(k)
        return h,k,r

def obtenerpuntos(h,k,r):
    x1 = h+r
    y1 = k
    x2 = h-r
    y2 = k
    x3 = h
    y3 = k+r
    return x1,y1,x2,y2,x3,y3

def mobius(x,y,r1,i1,r2,i2,r3,i3,r4,i4):
    mul = multiplicacion(x,y,r1,i1)
    azr,azi = numcomp(mul)
    mul2 = multiplicacion(x,y,r3,i3)
    czr,czi = numcomp(mul2)
    sum = suma(azr,azi,r2,i2)
    numeradorr,numeradori = numcomp(sum)
    sum2 = suma(czr,czi,r4,i4)
    denominadorr,denominadori = numcomp(sum2)
    res = division(numeradorr,numeradori,denominadorr,denominadori)
    return res




print("Bienvenido al programa sobre las transformacxiones de Mobius\n")

z1=input("Ingresa el primer numero complejo: ")
z2=input("Ingresa el segundo numero complejo: ")
z3=input("Ingresa el tercer numero complejo: ")
z4=input("Ingresa el cuarto numero complejo: ")

circunferencia = input("Ingrese la ecuación de la circunferencia :")

r1,i1 = numcomp(z1)
r2,i2 = numcomp(z2)
r3,i3 = numcomp(z3)
r4,i4 = numcomp(z4)

h,k,r =valoresc(circunferencia)    

x1,y1,x2,y2,x3,y3 = obtenerpuntos(h,k,r)

p1 = mobius(x1,y1,r1,i1,r2,i2,r3,i3,r4,i4)
p2 = mobius(x1,y1,r1,i1,r2,i2,r3,i3,r4,i4)
p3 = mobius(x1,y1,r1,i1,r2,i2,r3,i3,r4,i4)
p1r,p1i = numcomp(p1)
p2r,p2i = numcomp(p2)
p3r,p3i = numcomp(p3)
    
