# estrutura do enquantono pytho
# while <condiçao>:

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
#
#
# dim=input().split
# numero_linha, numero_coluna=int(dim[0]). int(dim[0])
# matriz=[]
# for l in range(numero_linha):
#     linha=[]
#     for c in range(numero_coluna):
#         linha.append(int(input('digite o numero de linhas')))
#         matriz.append(linha)
#
# print(matriz)
#
matriz=[[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]]
cont=mai=scol=0
for l in range(0, 3):
    for c in range(0,10):
        matriz[l][c] = int(input(f'digite um valor para [{l}, {c}]: '))
        cont+=matriz[l][c]


for l in range(0, 3):
    for c in range(0, 10):
        print(f'[{matriz[l][c]}]')
        print(f'{cont}')





#
#
# vetor1=[]
# vetor2=[]
# resul=[]
#
# for x in range(0,10):
#     vetor1.append(int(input('digite')))
#
#
# for i in range (0, 10):
#     vetor2.append(int(input('digite aqui')))
#
# for a in range(0, 10):
#     resul.append(vetor1*vetor2)
#
#     print(resul)
#
# vw=[]
# v1=[]
# vr=[]
# for x in range(0,6):
#     v1.append(int(input('digite')))
# for e in range(0,6):
#      vw.append(int(input('a')))
# for a in range(0, 10):
#     vr=vw[x]*v1[e]
#
# print(vr)
