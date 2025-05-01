#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Використання методу Монте-Карло
Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.
Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.
На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.
"""

import numpy as np

# Number of rolls
num_rolls = 100_000

# Simulate rolling two dice
dice1 = np.random.randint(1, 7, num_rolls)
dice2 = np.random.randint(1, 7, num_rolls)

# Calculate the sums of the two dice
sums = dice1 + dice2
sum_counts = {i: 0 for i in range(2, 13)}
for s in sums:
    sum_counts[s] += 1

# Calculate probabilities
probabilities = {key: count / num_rolls for key, count in sum_counts.items()}

# Print the probability table
print("Сума  | Імовірність")
print("-------------------")
for sum_value in range(2, 13):
    print(f"{sum_value}     | {probabilities[sum_value] * 100:.2f}%")
