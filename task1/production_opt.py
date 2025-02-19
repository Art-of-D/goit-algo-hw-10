from pulp import *

# Ініціалізація моделі
model = LpProblem("Maxproduction", LpMaximize)

# Визначення змінних
lemonade = LpVariable('lemonade', lowBound=0, cat='Integer')
fruit_juice = LpVariable('fruit_juice', lowBound=0, cat='Integer')

# Обмеження
model += 2 * lemonade + fruit_juice <= 100 # water
model += 1 * lemonade <= 50 # sugar
model += 1 * lemonade <= 30 # lemon acid
model += 2 * fruit_juice <= 40 # fruit mash

# Функція цілі (Максимізація прибутку)
model += fruit_juice + lemonade, "Production"

model.solve()


print("Виробляти продуктів lemonade:", lemonade.varValue)
print("Виробляти продуктів fruit_juice:", fruit_juice.varValue)