def celsius_para_fahrenheit(celsius):
  """Converte a temperatura em Celsius para Fahrenheit. """
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# Aqui vai perguntar os graus em Celsius
temp_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Aqui converte e mostra o resultado em Fahrenheit
temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)
print(f"A temperatura em Fahrenheit é: {temp_fahrenheit:.2f}°F")
