def fahrenheit_para_celsius(fahrenheit):
  """
  Converte uma temperatura de Fahrenheit para Celsius.

  Args:
    fahrenheit: A temperatura em graus Fahrenheit (float ou int).

  Returns:
    A temperatura convertida em graus Celsius (float).
  """
  celsius = (fahrenheit - 32) * 5/9
  return celsius

temperatura_f = float(input("Digite a temperatura em graus Fahrenheit: "))

temperatura_c = fahrenheit_para_celsius(temperatura_f)

print(f"A temperatura de {temperatura_f:.2f}°F é igual a {temperatura_c:.2f}°C.")