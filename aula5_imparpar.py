numero = float(input("Digite um número inteiro aleatório: "))

resto = numero % 2

print(resto)
if resto == 1:
    print("O valor",numero,"é impar.")
else:
    print("O valor",numero,"é par.")
