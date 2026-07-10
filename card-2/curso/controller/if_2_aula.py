a = 'valor' #TRUE
a=0 #true
a = -0.00001 #false
a = ''#false
a = ' '#true
a = []#false
a={}#false

# vai printar false pois as chaves estao vazias
if a: # se a é True
    print('Existe!!!')
else:
    print('nao existe ou zero ou vazio')