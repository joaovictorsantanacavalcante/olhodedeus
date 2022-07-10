vetor1=[]
vetor2=[]
vetor3=[]

for x in range(10):
    vetor1.append(x)


for i in range(10):
    if(vetor1[i]%2!=0):
        vetor2.append(vetor1[i])
    else:
        vetor3.append(vetor1[i])
print('vetor1 :', vetor1)
print('vetor2 impares', vetor2)
print('vetor3 pares:',vetor3)
