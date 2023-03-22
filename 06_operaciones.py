# ****OPERACIONES ARITMETICAS****
# suma +, resta -, multi *, div /,div entera //, jerarquia: (),**,*/, +-
#residuo o modulo %, potencia **
number = int(input('digite un numero: '))
'''print(f' la suma con  2 es: {number + 2}')
print(f' la resta con  2 es: {number - 2}')
print(f' la multiplicacion con  2 es: {number * 2}')
print(f' divicion con  2 es: {number / 2}')
print(f' divicion ENTERA con  2 es: {number // 2}')
print(f' el residuo con  2 es: {number % 2}')
print(f' la potencia con  2 es: {number ** 2}')'''

# OPERACIONES de asignacion
contador = 1
print(f'antes de += {contador}')
contador += 1  #contador= contador + 1 (+= operador. asignacion incremental)
print(f'antes de += es: {contador}')
contador = 9
contador -= 1  #contador = contador -  (-= oper, asignacion decremental)

number += 1
print(f'operador incremental += resultado es: {number}')
number -= 1
print(f'al usar el operador decremental -= el resultado es: {number}')
number *= 2
print(f'al usar el operador decremental *= el resultado es: {number}')
number /= 2
print(f'al usar el operador decremental /= el resultado es: {number}')
number //= 2
print(f'al usar el operador decremental //= el resultado es: {number}')
number %= 3
print(f'al usar el operador decremental %= el resultado es: {number}')
number **= 2
print(f'al usar el operador decremental **= el resultado es: {number}')
