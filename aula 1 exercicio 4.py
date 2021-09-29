#Exercício 4) Faça um algoritmo, em pseudocódigo, que leia o tempo de duração
# de um evento em uma fábrica expressa em segundos e mostre-o expresso em dias,
# horas, minutos e segundos.

# variaveis
#   dias, horas, minutos, segundos: inteiros
#
#dias = 0;
#horas = 0;
#minutos = 0;
#segundos = 0;
#   escreva ("informe o tempo de duracao em segundos: ")
#   leia (segundos)
#   se (dias >= 86400) então:
#   tempo = (tempo//86400 >= 1)
#   dias = resto(dias/86400)
#   se (horas >= 3600) então:
#       tempo = (horas/3600)
#       tempo = resto(tempo/3600)
#       se(tempo >= 60):
#            minutos = (tempo/60)
#           tempo = resto(tempo/60)
#           segundos = tempo
#      senao:
#           segundos = tempo;
#   senao:
#       se (tempo >= 60):
#         minutos = (tempo/60)
#         tempo = resto(tempo/60)
#         segundos = tempo
#
#       senao:
#           segundos = tempo;
#   escreva(""a quantidade é: ",dias," dias, ",horas," horas, ",minutos," minutos e ",segundos," segundos)
#fim

############################################################################
tempo = 0;
dias = 0;
horas = 0;
minutos = 0;
segundos = 0;
tempo = int(input("informe o tempo de duracao em segundos: "))
if(tempo//86400 >= 1):
    dias = (tempo % 86400)
    if(tempo >= 3600):
        horas = (tempo//3600)
        tempo = (tempo % 3600)
        if(tempo >= 60):
            minutos = (tempo//60)
            tempo = (tempo % 60)
            segundos = tempo
        else:
            segundos = tempo;
    else:
        if(tempo >= 60):
          minutos = (tempo//60)
          tempo = (tempo % 60)
          segundos = tempo
        else:
            segundos = tempo
print("a quantidade é: ",dias," dias, ",horas," horas, ",minutos," minutos e ",segundos," segundos.")