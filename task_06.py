#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Жадібні алгоритми та динамічне програмування
Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.
Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.
Розробіть функцію greedy_algo жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.
Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.
"""


def greedy_algo(items, budget):
    """Greedy knapSack algorithm"""
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    total_calories = 0
    total_cost = 0
    selected_items = []

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return total_calories, total_cost, selected_items


def dynamic_programming(items, budget):
    """0/1 knapSack algorithm"""
    item_list = [(info["cost"], info["calories"], name) for name, info in items.items()]
    n = len(item_list)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    keep = [[False] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost, calories, _ = item_list[i - 1]
        for w in range(budget + 1):
            if cost <= w and dp[i - 1][w - cost] + calories > dp[i - 1][w]:
                dp[i][w] = dp[i - 1][w - cost] + calories
                keep[i][w] = True
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    total_cost = 0
    w = budget
    for i in range(n, 0, -1):
        if keep[i][w]:
            selected_items.append(item_list[i - 1][2])
            total_cost += item_list[i - 1][0]
            w -= item_list[i - 1][0]

    return dp[n][budget], total_cost, selected_items


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }
    budget = 100

    # Test greedy
    greedy_calories, greedy_cost, greedy_items = greedy_algo(items, budget)
    print(
        f"Greedy: {greedy_calories} calories, Spent: {greedy_cost} UAH, Items: {greedy_items}"
    )

    # Test dp
    dp_calories, dp_cost, dp_items = dynamic_programming(items, budget)
    print(f"Dynamic: {dp_calories} calories, Spent: {dp_cost} UAH, Items: {dp_items}")
