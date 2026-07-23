# Aritimetricos
print(5 + 3)  # soma
print(5- 3)  # subtração
print(5 *3)  # multiplicação
print(6/3)  # divisão

print(6%2)
print(5%2)
# % e resto da divisão, exemplo: 6%2 = 0, 5%2 = 1

# Atribuição
result = 5
result += 2  # result = result + 2
result -= 1  # result = result - 1
result *= 3  # result = result * 3
result /= 2  # result = result / 2
print(result)

#logicos
x =6

print(not True) # Output = False
print(-7) 
print(-x)
print(+1)
w= 12
#w++
# nao existe incremento e decremento em python
print(w)

# Relacionais
a = 3
y=8

print(a>y)
# se a é maior que y output = False
print(a>=y)
# se a é maior ou igual que y output = False
print(a<y)
# se a é menor que y output = True
print(a<=y)
# se a é menor ou igual que y output = True
print(a==y)
# se a é igual a y output = False
print(a!=y)
# se a é diferente de y output = True

print('3'!=3)
# comparação entre string e inteiro

# Logicos
e = True
f=False
u= True

print(e and f and  u)
# no and todas tem que ser verdadeiras
# output = False 
print(e or f or u)
# no or se qualquer uma é True ja é valido
# output = True
print(e != f)
# se e é diferente de f
print(not e)
#negação de e

print(e and not f and u)
# outpu e True pois esta negando f que é False

# Ternario
var = 'Esta chovendo'
x = 'Tem Guarda Chuva'

status = 'Ficar em Casa' if var == 'Esta chovendo' or x == 'Nao tem guarda chuva' else 'Pode sair'
# se var for igual a Esta chovendo ou x for igual a Nao tem guarda chuva então status = Ficar em Casa se nao status = Pode sair

print(status)