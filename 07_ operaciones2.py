number = int(input('digite un numero: '))
# ****OPERACIONES RELACIONALES O DE COMPARACION****
print(number > 3)  # pregunta si el number es mayor que 3
print(number >= 3)  #pregunta si number es mayor o igual a 3
print(number < 3)  # si number es menor que tres
print(number <= 3)  # si number es igual a 3
print(number == 3)
print(number != 3)  # number es diferente a 3

#**** OPERACIONES LOGICAS****
print("operaciones logicas.")
# conjuncion (and &)
print("conjuncion")
print(False and True)
print(False and False & True)
print((number >= 3) and False)

#disyuncion (or, |)
print("disyuncion :")
print(False or True)
print(number <= 3 or number >= 10)
print(not (number <= 3 | number >= 10))

#negacion (not)
print("Negacion: ")
print(not (True))

# or exclusiva (^)
print('or exclusiva:')
print(False ^ False)
print(False ^ True)
print(True ^ False)
print(True ^ True)

# **** OPERACIONES DE PERTENENCIA ****
# in
print('operador in')
nombre = 'Daniela Gantiva'
print('z' in nombre )