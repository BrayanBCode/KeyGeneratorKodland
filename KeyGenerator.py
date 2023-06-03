import random 

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
keywordLenght = 0; password=""; keyword = ""


print("Soy un programa que genera contraseñas") # Saludo normal 

while(True):
    try:
        pass_length = int(input("De cuantos caracteres quieres tu contraseña?: "))
        break
    except:
        print("Caracter invalido - intente de nuevo")
MenuLoop = True
while(MenuLoop):
    MenuSelec = input("Le gustaria agregar una palabra clave a la contraseña? S - Si / N - No: ").upper()
    if(MenuSelec == "S"):
        while(True):
            keyword = input("Ingrese la palabra clave: ")
            if(len(keyword) > pass_length):
                print("La palabra clave es muy grande - intente de nuevo")
            else:
                break
        
        ClaveGeneratorLoop = True
        while(ClaveGeneratorLoop):
            keywordbool = False
            PassSize = pass_length - len(keyword)
            password=""
            for i in range(PassSize):
                password+=random.choice(elements)
                if ((random.randint(0, PassSize) == random.randint(0, PassSize) and keywordbool == False)):
                    password+=keyword
                    keywordbool = True
            
            if keywordbool == True:
                ClaveGeneratorLoop = False
                MenuLoop = False
                break
            
    elif(MenuSelec == "N"):
        
        for i in range(pass_length):
            password+=random.choice(elements)

        break
    else:
        print("Caracter invalido - intente de nuevo")




print("Su contraseña generada es:", password)
if(keyword != ""):
    print("Su palabra clave fue:", keyword)


