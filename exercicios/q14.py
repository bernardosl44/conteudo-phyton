limite_peso = 50
multa_por_kg = 4

peso_peixe = float(input("informe o peso total: "))

excedente = peso_peixe - limite_peso
multa = excedente * multa_por_kg

if  peso_peixe > limite_peso:
    excedente = peso_peixe - limite_peso
    multa = excedente * multa_por_kg
    print("Houveram", excedente, "kg de peixe a mais do permitido")
    print("o valor da multa é R$", multa)
else:
    print("Nao foi maior do que o permitido")
