# Solicita a quantidade de horas trabalhadas
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

# Solicita o valor da hora ao usuário
valor_hora = float(input("Digite o valor da hora trabalhada: "))

# Calcula o salário bruto multiplicando as horas pelo valor da hora
salario_bruto = horas_trabalhadas * valor_hora

# Exibe o salário bruto
print(f"O salário bruto é: R$ {salario_bruto:.2f}")