#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії
Написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
"""

import turtle


def draw_square(t, length):
    for _ in range(4):
        t.forward(length)
        t.right(90)


def draw_branch(t, length, depth):
    if depth == 0:
        return

    # Draw the current square
    draw_square(t, length)

    # Move to the top right corner
    t.forward(length)
    t.right(45)

    # Draw the right branch
    draw_branch(t, length / 2, depth - 1)

    # Move back to the top left corner
    t.left(90)
    draw_branch(t, length / 2, depth - 1)

    # Move back to the original position
    t.right(45)
    t.backward(length)


def draw_fractal_tree(depth, length=100):
    t = turtle.Turtle()
    t.speed(0)
    t.color("green")

    # Start drawing
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    draw_branch(t, length, depth)
    turtle.done()


# Test user input for recursion depth
try:
    depth = int(input("Enter the recursion depth: "))
    if depth < 0:
        print("Please enter a positive integer.")
    elif depth > 6:
        print("Depth too high. Using 5 instead.")
        depth = 6

    draw_fractal_tree(depth)

except ValueError:
    print("Invalid input. Please enter a positive integer.")
