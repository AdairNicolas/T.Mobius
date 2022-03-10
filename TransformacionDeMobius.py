
from gettext import find


print("Bienvenido al programa sobre las transformacxiones de Mobius\n")

z1=input("Ingresa el primer numero complejo: ")
z2=input("Ingresa el segundo numero complejo: ")
z3=input("Ingresa el tercer numero complejo: ")
z4=input("Ingresa el cuarto numero complejo: ")

circunferencia = input("Ingrese la ecuación de la circunferencia :")

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
    
valoresc(circunferencia)    