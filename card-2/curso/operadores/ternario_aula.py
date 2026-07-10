lockdown = False
grana = 130

status = 'Em casa' if lockdown or grana <=100 else 'Uhuuuu'
# if ternario comprime o if e else em uma linha
# status recebe 'em casa' se lockdown for true ou grana menor ou igual 100, se nao status recebe 'uhuuu'

print(status)