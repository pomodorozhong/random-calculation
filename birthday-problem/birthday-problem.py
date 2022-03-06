from math import factorial


def probability_of_no_any_collision(people: int):
    if people <= 1:
        return 1
    probability = 1
    for i in range(1, people):
        probability_ith = 1 - i/365
        probability *= probability_ith
    return probability


def probability_of_at_least_one_collision(people: int):
    return 1 - probability_of_no_any_collision(people)


for i in range(1, 51):
    formated = "{:.3f}".format(probability_of_at_least_one_collision(i))
    print(f"{i}: {formated}")
