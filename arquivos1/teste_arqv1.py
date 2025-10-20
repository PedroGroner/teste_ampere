def fibonacci(n):

  sequencia = [0, 1]
  # Continua gerando os próximos números até atingir a quantidade desejada
  while len(sequencia) < n:
    proximo_valor = sequencia[-1] + sequencia[-2]
    sequencia.append(proximo_valor)
  return sequencia[:n]

