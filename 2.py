x = "tijera"
y = "piedra"
empate = x == y 
gana = "piedra"> "tijera" and "papel" > "piedra" and "tijera" > "papel"
pierde = "piedra" < "papel" and "papel" < "tijera" and "tijera" < "piedra"

if empate:
    print("Empate")
elif (x=="piedra" and y=="tijera") or (x=="papel" and y=="piedra") or (x=="tijera" and y=="papel"):
    print("Gana")
else:
    print("Pierde")
