primera_lista = ['Manzana','Banano'] 
print(primera_lista)
nombres = ["Cesar", "luisa","octavio"]
print(nombres)

lista1 = [2,4,89,1000,3.14]
print(lista1)
lista2 = ['a',123,'A',3.1416,'palabra',True,1000]
print(lista2)
# tamaño de una lista (len):
print("tamaño de lista:")
print(len(lista1))
print(len(lista2))
#tipo de dato lista:
print('tipo de dato lista:')
print(type(lista1))
print(type(lista2))
#otra lista.
print("Funcion list():")
num = [1,2,3,4,5]
print(num)
num2 = list((1,2,3,4,5))
print(num2)
print("Index list:")
print(num[0])
print(num [0:3])
print(num[-1::-1])
print("uso de funcion IN:")
print(3 in num)
print(10 in num)
num1 = num
print(num)
print(num2)
print(num1 is num)
print(num2 is num)