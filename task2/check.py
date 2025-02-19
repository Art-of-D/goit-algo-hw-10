import scipy.integrate as spi
from graphic import f, a, b

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

def print_result(result=result, error=error):
  print("scipy.quad -> ", result, error)
