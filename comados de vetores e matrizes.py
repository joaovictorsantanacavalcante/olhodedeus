# o comado para ordena os valores dentro do vetor em forma crecente utiliza o comando: nome do vetor.sort()

# e para odem contraria utiliza  comando: nome do vetor.sort(reverse=True) o (T) de true tem q ser (maiusculo)


# para criar uma lista vazia utiliza o camando list() ou nomedovetor[].

# para fazer com q a pessoa q digite o valor do indice, o valor do vetor voce ultiliza o seguinte comando: OBS NOME DO MEU VETOR e ((VET))
# vet=[]
# print('digite 5 valores')
# for cont in range(0,5):
#     vet.append(int(input('digite aqui')))
#     vet[cont]=vet[cont]%2
#
# print('dos valores digitados',vet.count(1),'sao impares')

# for cont in range(0,10): comando para fazer a retetiçao do lupin.
# nomevetor.append(int(input('digite o valor aqui'))) comando para o usuario atribuir os valores aos indices da lista

# nomevetor[cont]=nomevetor[cont]%2 comando q todos os valores dos indices ira ser dividido e o resto da conta ira ser o novo valor dos indices

# comandos de fatiamentos

# append,insert,extend,pop,del,+min,max,range,clear.

# para mostrar a lista ate um determinado valor basta indicar o nome da lista e indica do indice de começo ate o indece q deseja parar de mostrar ex:
#      0   1  2  3  4   5   6<- INDICE
# vet_2=[39, 5, 9, 1, 22, 46, 90]
#
# print(vet_2[3:])


#print ([numeroindice:]) comando para mostrar a partur de um indice ate o final

 # print(vet_2[::2])

 # para pula os indice comando print(vet_2[::dequantoemquanto])
idade=int(input('digite sua idade'))
if idade >=18 :
     print('voce e maior de idade!')
else:
     print('voce e menor de idade')