def adivinar():
    import random
    numero = random.randint(1, 50)
    while True:
        num = int(input("adivina el número: "))
        if num == numero:
            print("¡Adivinaste!")
            break
        elif num < numero:
            print("El número es mayor")
        else:
            print("El número es menor")

adivinar()