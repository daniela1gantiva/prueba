# Condicional if
#if('prueba logica')
adivinar = 42
numero = int(input(' Sr usuario, digite un numero: '))
if (numero > adivinar):
  print('Bajele el volumen')
elif (numero < adivinar):
  print('subale el volumen')
else:
  print("VERDADERO")

# 2 anidado
if (numero >= adivinar):
  if (numero > adivinar):
    print('Coloque un numero menor.')
  else:
    print('Acertado!!!')
else:
  print('coloque un numero mayor')

#fin del if:
print('la instruccion "IF" termino.')
