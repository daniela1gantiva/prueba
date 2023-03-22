#1 formatos de impresion
edad = 60
estatura = 1.6
print("La edad es: ", edad)
print('La estatura es:', estatura)
#1ra manera de uso de formato:
print('La estatura es:', estatura, "La edad es: ",
      edad)  #esto es texto concatenado con variables
#2da manera de uso de formato (la mas utilizada):
print(f'La estatura es: {estatura} y La edad es:  {edad}')
#3ra manera del uso del formato:
print('La estatura es: {} y La edad es:  {}'.format(estatura, edad))
print(' la edad mas la estatura es:', edad + estatura)
print(f' la edad mas la estatura es: {edad + estatura}')
print(' la edad mas la estatura es: {}'.format(edad + estatura))
suma= edad + estatura
print(f'la edad mas la estatura es:{suma}')
