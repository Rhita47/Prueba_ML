import random
import random

# Function to simulate Monty Hall problem
def monty_hall_simulation_correct(trials=10000, switch=True):
    win_count = 0
    for _ in range(trials):
        doors = [0, 0, 0]
        car_position = random.randint(0, 2)
        doors[car_position] = 1

        contestant_choice = random.randint(0, 2)
        remaining_doors = [i for i in range(3) if i != contestant_choice and doors[i] == 0]
        monty_opens = random.choice(remaining_doors)

        if switch:
            remaining_choice = [i for i in range(3) if i != contestant_choice and i != monty_opens][0]
            contestant_choice = remaining_choice

        if doors[contestant_choice] == 1:
            win_count += 1

    return win_count

trials = 10000

wins_with_switch = monty_hall_simulation_correct(trials, switch=True)
wins_without_switch = monty_hall_simulation_correct(trials, switch=False)

percent_with_switch = (wins_with_switch / trials) * 100
percent_without_switch = (wins_without_switch / trials) * 100

print(f"Percentage of wins if switched: {percent_with_switch}%")
print(f"Percentage of wins if not switched: {percent_without_switch}%")
