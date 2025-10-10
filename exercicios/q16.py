import math

area_pintar = float(input("informe o tamanho da area a ser pintada em metros quadrados:" ))
litros_necessarios = area_pintar / 3
latas_comprar = math.ceil(litros_necessarios / 18)
preco_total = latas_comprar * 80
print(f"Serao necessarias {latas_comprar} latas de tinta.")
print(f"o preço total sera de R$ {preco_total:.2f}.")