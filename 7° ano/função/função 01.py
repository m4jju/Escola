def POI (numero):         #mostra se o numero é par ou impar (0-10)
  return numero %2==0
for i in range (11):
  print (POI (i),i )
  
print ("--------------------")

def PPOOII (numero2):      #mostra se o numero é par (true) ou impar (5)
  return numero2 %2==0
print (PPOOII(5))

print ("--------------------")
print ("questão 01")

#1- mostra os lados em um dado de seis faces
for a in range (1,7):
  print (a)
  
print ("--------------------")
print ("questão 02")

#2-Possiveis combinações com dois dados de seis lados
for b in range (1,7):
  for c in range (1,7):
    print ("(",b,",",c,")")
 
print ("--------------------")
print ("questão 03")

#3- conbinações de tres dados de quatro lados
for d in range (1,5):
  for e in range (1,5):
    for f in range (1,5):
      print (d,e,f)
      print ("_____")
