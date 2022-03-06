from random import randint


def detect_if_any_collision(birthdays: list):
    for i in range(len(birthdays)):
        for j in range(len(birthdays)):
            if i != j and birthdays[i] == birthdays[j]:
                return True
    return False


def probability_of_at_least_one_collision(people: int, simulation_count: int):
    if people <= 1:
        return 0

    collisions = 0
    for i in range(simulation_count):
        peoples_birthdays = []
        for i in range(people):
            peoples_birthdays.append(randint(1, 365))
        if detect_if_any_collision(peoples_birthdays):
            collisions += 1

    probability = collisions / simulation_count

    return probability


for i in range(1, 51):
    simulation_count = 10000
    formated = "{:.3f}".format(
        probability_of_at_least_one_collision(i, simulation_count))
    print(f"{i}: {formated}")
