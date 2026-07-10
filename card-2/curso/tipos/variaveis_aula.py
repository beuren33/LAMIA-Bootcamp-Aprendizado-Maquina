#print('Funcionou')
a=3
b=4.4

print(a+b)
# soma dentro do print e depois printa

texto = 'Sua Idade e: '
idade = 23

#print(texto + str(idade))

print(f'{texto}{idade}')
# f string facilita a maneira de printar variaveis

saudacao = 'bom dia'
print(3 * saudacao)

PI = 3.14
PI = 3.1415
# nomeclatura de Constante em Python, mas nao é nativo so convenção
raio =float(input('Informe o raio da circunferencia: '))
area = PI * pow(raio,2)

print(f'A area da circunferencia e {area} m2.')