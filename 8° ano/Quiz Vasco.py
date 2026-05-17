print("Você acha que conhece o Clube de Regatas Vasco da Gama? Vamos começar!")
nome = input("Qual é o seu nome?")
p = 0

p1 = input("\nQuando o Vasco foi fundado? \nA.1890 B.1898 C.1988 D.1900")
if (p1 == "B"):
  p = p + 1
  print("Acertou!")
else:
  print("Você errou! O vasco foi fundado em 1898.")

p2 = input("\nQuantos titulos internacionais o vasco tem? \nA.4 B.6 C.2 D.5")
if (p2 == "A"):
  p = p + 1
  print("Acertou!")
else:
  print("Você errou! O vasco tem 4 titulos internacionais.")

p3 = input("\nQuantos titulos nacionais o vasco tem? \nA.6 B.5 C.3 D.4")
if (p3 == "A"):
  p = p + 1
  print("Acertou!")
else:
  print("Você errou! O vasco tem 6 titulos nacionais.")

p4 = input("\nQual é o maior artilheiro do vasco? \nA.Roberto Dinamite B.Romário C.Ademir D.Pinga")
if (p4 == "A"):
  p = p + 1
  print("Acertou!")
else:
  print("Você errou! O Roberto Dinamite é o maior artilheiro do vasco.")

p5 = input("\nQual o período que o Vasco usou umbro?\nA.2002-2006 e 2014-2016 B.2003-2006 e 2014-2017")
if (p5 == "B"):
  p = p + 1
  print("Acertou!")
else:
  print("Você errou! O vasco usou umbro em dois periodos, 2003-2006 e 2014-2017")

p6 = input("\nQual o titulo que o vasco conquistou no seu centenário?\nA.mercosul B.taça rio - são paulo C.libertadores D.brasileiro")
if (p6 == "C"):
  p = p + 1
  print("Acertou!")
else:
  print("Você errou! No seu centenário o vasco conquistou uma libertadores!")

p7 = input("\nQual a marca de cerveja patrocina o vasco?\nA.skol B.ambev C.devassa D.brahma")
if (p7 == "B"):
  p = p + 1
  print("Acertou!")
else:
  print("Você errou! O vasco é patrocinado pela ambev!")

p8 = input("\nQual foi o primeiro mascote do vasco?\nA.vasco da gama B.baleia C.don corvo D.almirante")
if (p8 == "C"):
  p = p + 1
  print("Acertou!")
else:
  print("Você errou! O primeiro mascote do vasco foi o don corvo!")

p9 = input("\nEm que ano o Vasco foi campeão da Libertadores?\nA.1952 B.1998 C.1997 D.2000")
if (p9 == "B"):
  p = p + 1
  print("Acertou!")
else:
  print("Você errou! O vasco ganhou a libertadores em 1998!")

p10 = input("\nQuem fez o gol histórico no Monumental dando a classificação para a final da libertadores 1998?\nA.Juninho Pernanbucano B.Donizete C.Juninho Paulista D.Pedrinho")
if (p10 == "A"):
  p = p + 1
  print("Acertou!")
else:
  print("Você errou! Quem fez o gol histórico no Monumental dando a classificação para a final da libertadores 1998 foi o Juninho Monumental!")

print("\nParabéns", nome, ", você acertou",p,"/ 10 perguntas!")
ranking = open("ranking.txt","a")
ranking.write(nome + " " + "pontuação =" + str(p) + "\n")
ranking.close()

