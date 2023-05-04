# refatoring
import Funcoes
import os

os.system("cls")
print("menu")
print("1 - soma")
print("2 - subtrair")
print("3 - multiplicar")
print("4 - dividir")
escolha = int(input("digite uma opção: "))

if escolha == 1:
    Funcoes.somar_dois_numeros()

elif escolha == 2:
    Funcoes.subtrair_dois_numeros()

elif escolha == 3:
    Funcoes.multiplicar_dois_numeros()

elif escolha == 4:
    Funcoes.dividir_dois_numeros()
