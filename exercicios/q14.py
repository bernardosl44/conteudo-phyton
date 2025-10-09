# Aqui vai definir o limite de peso e o valor da multa por quilo excedente
LIMITE_PESO = 50  # kg
VALOR_MULTA_POR_QUILO = 4.00  # Reais

# 1. Ler o peso dos peixes
try:
    peso = float(input("Digite o peso dos peixes em quilos: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número para o peso.")
    exit()

# 2. Calcular o excesso e a multa
excesso = 0
multa = 0.0

if peso > LIMITE_PESO:
    # Calcula a quantidade de quilos excedentes
    excesso = peso - LIMITE_PESO
    # Calcula o valor total da multa
    multa = excesso * VALOR_MULTA_POR_QUILO

# 3. Imprimir os resultados com mensagens adequadas
print("\n--- Relatório de Pescador ---")
print(f"Peso de peixes capturado: {peso:.2f} kg")

if excesso > 0:
    print(f"Regulamento de pesca excedido!")
    print(f"Quantidade de quilos excedente: {excesso:.2f} kg")
    print(f"Valor da multa: R$ {multa:.2f}")
