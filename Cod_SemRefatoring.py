# sem refatoring
print("menu")
print("1 - soma")
print("2 - subtrair")
print("3 - multiplicar")
print("4 - dividir")
escolha = int(input("digite uma opção: "))
if escolha == 1:
    numero1_Soma = float(input("Digite um numero: "))
    numero2_Soma = float(input("Digite outro numero: "))
    resultado_soma = numero1_Soma + numero2_Soma
    print(f"o resulta do da soma é: {resultado_soma}")

elif escolha == 2:
    numero1_Subtrair = float(input("Digite um numero: "))
    numero2_Subtrair = float(input("Digite outro numero: "))
    resultado_Subtrair = numero1_Subtrair - numero2_Subtrair
    print(f"o resulta do da soma é: {resultado_Subtrair}")

elif escolha == 3:
    numero1_Multiplicar = float(input("Digite um numero: "))
    numero2_Multiplicar = float(input("Digite outro numero: "))
    resultado_Multiplicar = numero1_Multiplicar * numero2_Multiplicar
    print(f"o resulta do da soma é: {resultado_Multiplicar}")

elif escolha == 4:
    numero1_Dividir = float(input("Digite um numero: "))
    numero2_Dividir = float(input("Digite outro numero: "))
    resultado_Dividir = numero1_Dividir / numero2_Dividir
    print(f"o resulta do da soma é: {resultado_Dividir}")
