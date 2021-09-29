#Exercício 1- Faça um algoritmo que leia a nota das três provas de um aluno e calcule a média ponderada das notas de três provas que é dada pela fórmula:
#Média= (P1 + P2 + 2.0* P3)/4.0
#
# Variaveis
#   p1, p2, p3, media : real
# Inicio
#   Escreva ("informe a primeira nota")
#   leia (p1)
#   Escreva ("informe a segunda nota")
#   leia (p2)
#   Escreva ("informe a terceira nota")
#   leia (p3)
#   media = (P1 + P2 + 2*P3)/4
#   escreva (media)
#Fim
####################################################################################

p1 = float(input("Informe a primeira nota: "))
p2 = float(input("Informe a segunda nota: "))
p3 = float(input("Informe a terceira nota: "))
media = (p1+p2+2*p3)/4
print(media)