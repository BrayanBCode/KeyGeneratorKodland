import random 

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def DefaultKeyGen():
    password=""
    passlength = int(input("De que tamaño quiere su contraseña?: "))

    for i in range(passlength):
        password+=random.choice(elements)
    print(password)

def LeftKeyGen():
    password=""
    passlength = int(input("De que tamaño quiere su contraseña?: "))
    keyword = input("Ingrese la palabra a agregar: ")
    password_length = passlength - len(keyword)
    
    password+=keyword
    for i in range(password_length):
        password+=random.choice(elements)
    print("Contraseña:",password)

def MiddleKeyGen():
    password=""
    passlength = int(input("De que tamaño quiere su contraseña?: "))
    keyword = input("Ingrese la palabra a agregar: ")
    password_length = passlength - len(keyword)
    
    
    for i in range(password_length):
        password+=random.choice(elements)
        if(i == int((password_length/2) - 1)):
            password+=keyword
    print("Contraseña:",password)

def RightKeyGen():
    password=""
    passlength = int(input("De que tamaño quiere su contraseña?: "))
    keyword = input("Ingrese la palabra a agregar: ")
    password_length = passlength - len(keyword)
    
    for i in range(password_length):
        password+=random.choice(elements)
    password+=keyword
    print("Contraseña:",password)

def RandomKeyGen():
    password=""
    passlength = int(input("De que tamaño quiere su contraseña?: "))
    keyword = input("Ingrese la palabra a agregar: ")
    password_length = passlength - len(keyword)
    RadKey = random.randint(0, password_length)
    print(RadKey)
    for i in range(password_length):
        if(i == RadKey):
            password += keyword
        password+=random.choice(elements)
 
    print("Contraseña:",password)

def Menu():
    while(True):
        Menu = input("Le gustaria tener una palabra clave en su contraseña? S - Si / N - No : ").upper()
        if(Menu == "S"):
            print("Elija la posicion de la palabra clave \n 1 - Izquierda   2 - Derecha\n 3 - Medio       4 - Random")
            while(True):
                Menuselec = input()
                match Menuselec:
                    case "1":
                        LeftKeyGen()
                        break
                    case "2":
                        RightKeyGen()
                        break
                    case "3":
                        MiddleKeyGen()
                        break
                    case "4":
                        RandomKeyGen()
                        break
                    case _:
                        print("Caracter invalido - intente de nuevo")
                
            break
        elif (Menu == "N"):
            DefaultKeyGen()
            break
        else:
            print("Caracter invalido")

print("-- ! Bienvenido ! Soy un programa que genera contraseñas --") # Saludo normal 
Menu()
