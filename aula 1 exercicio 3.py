#Exercício 3) Faça um algoritmo, em pseudocódigo, que leia a idade de uma pessoa
# expressa em dias e mostre-a expressa em anos, meses e dias.
# ( Considere que um mês tem 30 dias)
# variaveis
#   dias, numanos, nummeses, numdias: inteiros
#   dias = 0;
#   numanos = 0;
#   nummeses = 0;
#   numdias = 0;
#   escreva ("informe a idade expressa em dias: ")
#   leia (dias)
#   se (dias>=360) entao:
#       numanos = (dias/360)
#       dias = resto(dias/360)
#       se (dias >= 30) entao:
#       nummeses = (dias/30)
#       numdias = dias
#   senao:
#       numdias = dias
#   senao:
#       se (dias >= 30) entao:
#       nummese = (dias/30)
#       dias = resto(dias/30)
#       numdias = dias
#   senao:
#       numdias = dias;
#   escreva("anos: "; numanos; "meses: "; nummeses; "dias: "; numdias)
#fim
########################################################################################

dias = int(input("informe a idade da pessoa expressa em dias: "))
numanos = int(0);
nummeses = int(0);
numdias = int(0);
if (dias >= 360):
    numanos = (dias//360)
    dias = (dias % 360)

    if(dias >= 30):
        nummeses = (dias//30)
        dias = (dias % 30)
        numdias = dias
    else:
        numdias = dias
else:
    if(dias >=30):
        nummeses = (dias/30)
        dias = (dia % 30)
    else:
        numdias = dias;
print("a idade da pessoa é: ",numanos,",anos, ",nummeses,", meses e ",numdias," dias.")
