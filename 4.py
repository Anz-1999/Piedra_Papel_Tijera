import random
# x = input("piedra, papel o tijera:")
# y = random.choice(["piedra","papel","tijera"])

def info():
    if x == y :
        print("Empate")
        return True
    elif (x=="piedra" and y=="tijera") or (x=="papel" and y=="piedra") or (x=="tijera" and y=="papel"):
        print("Gana")
        return False
    else:
        print("Pierde")
        return False

empate = True
while empate:
    x = input("piedra, papel o tijera:")
    y = random.choice(["piedra","papel","tijera"])
    print("Sistema: ",y)
    empate=info()