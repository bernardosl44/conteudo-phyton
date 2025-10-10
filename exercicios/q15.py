
valor_por_hora = float(input("Digite o valor que você ganha por hora: "))


horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))


salario_bruto = valor_por_hora * horas_trabalhadas


desconto_ir = salario_bruto * 0.11    # 11% para o Imposto de Renda
desconto_inss = salario_bruto * 0.08  # 8% para o INSS
desconto_sindicato = salario_bruto * 0.05 # 5% para o sindicato

salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato

print("-" * 30) # Linha divisória aleatoria pra dividir
print(f"a. Salário Bruto: R$ {salario_bruto:.2f}")
print(f"b. Desconto do INSS: R$ {desconto_inss:.2f}")
print(f"c. Desconto do Sindicato: R$ {desconto_sindicato:.2f}")
print(f"d. Salário Líquido: R$ {salario_liquido:.2f}")
print("-" * 30)
