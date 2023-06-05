import random 

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def RequestLength ():
    while(True):
        try:
            length = int(input("De que tamaño quiere su contraseña?: "))
            return length
        except:
            print("Valor invalido - intente de nuevo")

def RequestKeyword():
    while(True):
        try:
            keyword = input("Ingrese la palabra a agregar: ")
            return keyword
        except:
            print("Valor invalido - intente de nuevo")

def MiddleKeyGen(keyword, passlength, PassMiddle = ""):
    password_length = passlength - len(keyword)
    
    for i in range(password_length):
        PassMiddle+=random.choice(elements)
        if(i == int((password_length/2) - 1)):
            PassMiddle+=keyword
    return PassMiddle

def RandomKeyGen(keyword, passlength, PassRandom = ""):
    password_length = passlength - len(keyword)
    RandKey = random.randint(0, password_length)

    for i in range(password_length):
        if(i == RandKey):
            PassRandom += keyword
        PassRandom+=random.choice(elements)
    return PassRandom

def DefaultKeyGen(keyword, passlength, PassDeafult = ""):
    if(keyword is None):
        keyword = ""
    
    password_length = passlength - len(keyword)

    for i in range(password_length):
        PassDeafult+=random.choice(elements)
    print(len(PassDeafult))
    return PassDeafult


PassRandom = ""; PassDeafult = ""; PassDir = ""
def Menu():
    while(True):
        Menu = input("Le gustaria tener una palabra clave en su contraseña? S - Si / N - No : ").upper()
        if(Menu == "S" or Menu == "SI"):
            print("Elija la posicion de la palabra clave \n 1 - Izquierda   2 - Derecha\n 3 - Medio       4 - Random")
            while(True): # PassRandom = ""; PassDeafult = ""; PassDir = ""
                Menuselec = input()
                match Menuselec:
                    case "1":
                        keyword = RequestKeyword()
                        print(DefaultKeyGen(keyword, RequestLength(),PassDeafult = keyword))
                        break
                    case "2":
                        keyword = RequestKeyword()                     
                        print(DefaultKeyGen(keyword, RequestLength()) + keyword)
                        break
                    case "3":
                        print(MiddleKeyGen(RequestKeyword(), RequestLength()))
                        break
                    case "4":
                        print(RandomKeyGen(RequestKeyword(), RequestLength()))
                        break
                    case _:
                        print("Caracter invalido - intente de nuevo")
                
            break
        elif (Menu == "N" or Menu == "NO"):
            print(DefaultKeyGen(None, RequestLength()))
            break
        else:
            print("Caracter invalido")
            
print("-- ! Bienvenido ! Soy un programa que genera contraseñas --") # Saludo normal
Menu()
