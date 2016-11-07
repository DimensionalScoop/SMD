import numpy as np

possible_throws = 0
sum_is_9 = 0
sum_greater_than_9 = 0

for red in range(1, 7):
    for blue in range(1, 7):
        possible_throws += 1
        if red + blue == 9:
            sum_is_9 += 1
        if red + blue > 9:
            sum_greater_than_9 += 1

assert possible_throws == 36
print("a)", sum_is_9)
print("b)", sum_greater_than_9 + sum_is_9)
