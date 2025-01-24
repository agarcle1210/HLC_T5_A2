def comprobar():
    palabra=input("Introduce una palabra")
    caracteres=["@","#","$","%"]
    for i in palabra:
        if i in caracteres:
            print("La palabra contiene caracteres especiales")
            break
    else:
        print("La palabra no contiene caracteres especiales")

comprobar()