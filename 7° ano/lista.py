l1 = [1,2,3,4]
l2 = [3.8,4,3.2]
l3 = ["abacate", True, 13]
print(l1) #mostra a lista1
print(l2[0]) #mostra o primeiro elemento da lista2
print(len(l3)) #mostra o tamanho da lista3

print ("\n") #pula linha

nomes = ["Lucas", "Lívia", "Ana", "Manuella"]
for nome in nomes:
  print (nome)

print("\n") 

for nome in nomes:
  print (nome + " é legal")
  
print("\n")

for nome in nomes:
  if (nome!="Manuella"):
    print (nome + " é legal")
  else:
    print(nome + " não")

