letras = 0
consoantes = 0
vogais = 0
vv= ['A','E','I','O','U','a','e','i','o','u']
palavra = 'ForaAbacate' 
for l in palavra: 
 print(l, end = ' ')  #separa as letras 
 letras+=1
 if l in vv:
  vogais+=1
 else:
  consoantes+=1
print('\nletras =',letras,'\nvogais=', vogais,'\nconsoantes =', consoantes)
