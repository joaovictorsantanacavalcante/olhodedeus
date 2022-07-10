vpri=[]
v2=[]
v3=[]
print('digite 10 valores')

for x in range(0,10):
    vpri.append(int(input('digite aqui')))

for x in range(0, 10):
    if (vpri[x]%2!=1):
        v2.append(vpri[x])
    else:
        v3.append(vpri[x])
print('vetor dos valores digitados:',vpri)
print('vetor de numeros impares:',v2)
print('vetor par:', v3)





# segunda logica: fazer com que a pessoa digite os valorres, ultilizar o % para indetifica os pares e inpares depois ultilizar o comando para separa somente os zeros e uns cada vetor iria



