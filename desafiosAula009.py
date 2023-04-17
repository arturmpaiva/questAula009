# D E S A F I O S

# 1 ler o nome completo de alguém, mostrar o nome com todas maiusculas, minusculas, quantas letras no nome, sem espaços, quantas letras tem o primeiro nome
# 2 ler um número de 0 a 9999 e mostrar na tela cada um dos números separados/ ex: unidade: 4, dezena: 1, centena: 4, milhar: 5
# 3 ler o nome da cidade e mostrar se começa ou não com a palavra "Santo"
# 4 ler o nome da pessoa e mostrar se tem "Silva"
# 5 ler uma frase e mostrar quantas vezes tem a letra 'a', em que posição aparece pela primeira vez, e pela última
# 6 ler o nome completo de alguém e mostrar o primeiro e o último nome separadamente+

# 1.
nome = input("Digite seu nome completo ").strip()
print("Seu nome maiúsculo é ", nome.upper())
print("Seu nome minúsculo é ", nome.lower())
letras = len(nome) - nome.count(" ")
print("Seu nome tem ", letras, "letras")
separa = nome.split()
print("Seu primeiro nome tem ", len(separa[0]), "letras")

# 2.
num = input("Digite um número de 0 a 9999: ")
if len(num) == 4:
    print("Unidade: ", num[3])
    print("Dezena:  ", num[2])
    print("Centena: ", num[1])
    print("Milhar:  ", num[0])
elif len(num) == 3:
    print("Unidade: ", num[2])
    print("Dezena:  ", num[1])
    print("Centena: ", num[0])
elif len(num) == 2:
    print("Unidade: ", num[1])
    print("Dezena:  ", num[0])
elif len(num) == 1:
    print("Unidade: ", num)
else:
    print("ERROR: NÚMERO INVÁLIDO")

# 3.
cidade = input("Digite o nome de uma cidade: ").capitalize()
separa2 = cidade.split()
print("Santo" in separa2[0])

# 4.
nome2 = input("Digite seu nome: ").title()
print("Silva" in nome2)

# 5.
frase = input("Digite uma frase: ").lower().strip()
print("A letra 'a' aparece {} vezes".format(frase.count("a")))
print("A letra 'a' aparece pela primeira vez na posição {}".format(frase.find("a")))
print("A letra 'a' aparece pela última vez na posição {}".format(frase.rfind("a")))



# 6.
nome3 = input("Digite seu nome completo: ")
separa3 = nome3.split()
print("O seu primeiro nome é {}".format(separa3[0]))
print("O seu último nome é {}".format(separa3[-1]))