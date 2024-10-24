def calcular_imc(peso, altura):
  imc = peso / (altura ** 2)

  if imc < 17:
    return "Muito abaixo do peso"
  elif 17 <= imc < 18.5:
    return "Abaixo do peso"
  elif 18.5 <= imc < 25:
    return "Peso Normal"
  elif 25 <= imc < 30:
    return "Sobrepeso"
  elif 30 <= imc < 35:
    return "Obesidade Grau I"
  elif 35 <= imc < 40:
    return "Obesidade Grau II"
  else:
    return "Obesidade Grau III"

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = calcular_imc(peso, altura)
classificacao = imc
print(f"Seu IMC é: {imc:}")
print(f"Classificação: {classificacao}")