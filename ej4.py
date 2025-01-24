def comprobar():
    default="1234"
    intentos=0
    while intentos<3:
        usuario=input("Introduce la contraseña: ")
        if usuario==default:
            print("contraseña correcta")
            break
        else:
            print("contraseña incorrecta")
            intentos+=1

comprobar()