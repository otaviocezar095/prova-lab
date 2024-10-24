def rlrelu(alpha, x):
  
  if alpha < 0 or alpha > 0.1:
    raise ValueError("O valor de alpha deve estar entre 0 e 0.1")

  return alpha * x if x < 0 else x
alpha = float(input('Informe alpha (0 <= alpha <= 0.1): '))
x = float(input('Informe x: '))
try:
  resultado = rlrelu(alpha, x)
  print(resultado)
except ValueError as e:
  print(e)