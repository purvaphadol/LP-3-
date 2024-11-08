# -*- coding: utf-8 -*-
"""pract4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JthLvlGYau3okuva-GsvwoJrGN2Fn5ae

## Gradient Descent Algorithm

#### find the local minima of the function y=(x+3)² starting from the point x=2
"""

current_x = 2
rate = 0.01 # Learning rate
precision = 0.000001  # This tells us when to stop the algorithm
delta_x = 1
max_iterations = 10000 # Maximum number of iterations
iteration_counter = 0

# dy/dx of eqn = 2*(x+3)
def slope(x):
    return 2*(x+3)

def value_y(x):
    return (x+3)**2
y = []
x = []
y.append(value_y(current_x))
x.append(current_x)

while delta_x > precision and iteration_counter < max_iterations:
    previous_x = current_x
    current_x = previous_x - rate * slope(previous_x)
    y.append(value_y(current_x))
    x.append(current_x)
    delta_x = abs(previous_x - current_x)
    iteration_counter += 1

print(f"Local Minima occurs at: {current_x}")

import matplotlib.pyplot as plt

plt.scatter(x,y)
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.title('y=(x+3)^2')
plt.show()

"""Implement Gradient Descent Algorithm to find the local minima of a function.
For example, find the local minima of the function y=(x+3)² starting from the point x=2
"""

