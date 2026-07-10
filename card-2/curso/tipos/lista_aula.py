nums = [1,2,3]
#cris uma lisya
print(type(nums))

nums.append(3)
#adiciona o 3 a lista nums, atraves do append
nums.append(4)
nums.append(500)
print(len(nums))
# printa a quantidade de numeros da lista

nums[3] = 100
# adiciona ao lugar de indice 3 na lista o numero 100
nums.insert(0,-200)
# adiciona o -200 no indice 0 da lista

print(nums[6])
# printa o numero da lista no indice 6
print(nums[-1])
# printa o ultimo item da lista
print(nums[-2])
#printa o penultimo item da lista

print(nums)