p = "palavra palavras"
print(p.upper()) #Transforma os caracteres em maiusculo
print(p.lower()) #Transforma os caracteres em minusculo
print(p.capitalize()) #Primeira letra fica maiuscula, e o resto minuscula

print(p.split()) #Separa p pelos espaços em uma lista 

pSeparado = p. split() 
print(pSeparado)
print(pSeparado[0]) #Printa a primeira palavra
print(pSeparado[1]) #Printa a segunda palavra

palavra = "za warado"
print(palavra) #mostra tudo
print(palavra[0]) #mostra a primeira letra
print(palavra[3]) #mostra a segunda letra
print(palavra[0:2]) #mostra tudo ate a terceira posicao
print(palavra[3:9]) #mostra da quarta ate a nona posicao
print(palavra[3:]) #mostra da quarta ate a ultima posicao
print(palavra[:3]) #mostra da primeira ate quarta posicao
print(palavra[::2]) #mostra do inicio ao fim de 2 em 2
print(palavra[1::2]) #mostra da segunda letra ate o fim de 2 em 2
print(palavra[::-1]) #mostra a palavra ao contrario
print(palavra[-1]) #mostra a ultima letra