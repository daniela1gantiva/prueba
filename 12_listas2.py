num = [99, 34, 25, 56, 72]
print(num)
num[1] = 88
print(num)
#num= [99,88,25,56,72]
# funcion INSERT.
num.insert(1, 77)
print(num)
# FUNCION APPEND:
num.append(100)
print(num)
# num = [99,77,88,25,56,72,100]
num2 = [9, 8, 7]
print(num)
# FUNCION EXTEND:
num.extend(num2)
print(num)
#FUNCION REMOVE:
num.remove(100)
print(num)
#num = [99,77,88,25,56,72,9,8,7]
# FUNCION POP:
num.pop(2)
print(num)
#[99,77,25,56,72,9,8,7]
# FUNCION DEL
del num[0]
print(num)
#[77,25,56,72,9,8,7]
# FUNCION CLEAR:
num2.clear()
print(num2)