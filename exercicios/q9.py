def celsius_para_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

temp_celsius = float(input("Digite a temperatura em graus Celsius: "))

temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)
print(f"A temperatura em Fahrenheit é: {temp_fahrenheit:.2f}°F")
