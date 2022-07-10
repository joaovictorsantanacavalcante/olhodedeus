vet=[]
print('digite 10 valores')
for cont in range(0,10):
    vet.append(int(input('digite aqui')))
    vet[cont]=vet[cont]%2

print('dos valores digitados',vet.count(1),'sao impares')

# for cont in range(0,10): comando para fazer a retetiçao do lupin.
# nomevetor.append(int(input('digite o valor aqui'))) comando para o usuario atribuir os valores aos indices da lista

# nomevetor[cont]=nomevetor[cont]%2 comando q todos os valores dos indices ira ser dividido e o resto da conta ira ser o novo valor dos indices