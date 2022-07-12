# vetor1=[]
# vetor2=[]
# vr=[]
#
# print('digite os valores das listas')
# for i in range(0,10):
#     vetor1.append(int(input('digite:')))
#
# print(vetor1)
#
# print('digite os valores da segunda lista')
# for x in range(0,10):
#     vetor2.append(int(input('digite aqui:')))
#
#
#
#
# print(vr)
# print(vetor1)
# print(vetor2)


vetor1=[]
vetor2=[]
vetor3=[]
print('digite o valor do primeiro vetor')
for x in range(0,10):
    vetor1.append(int(input('digite:')))
print('digite o valor do segundo vetor')
for x in range(0, 10):
    vetor2.append(int(input('digite:')))
    vetor3.append(vetor1[x]*vetor2[x])
print(vetor1)
print(vetor2)
print(vetor3)