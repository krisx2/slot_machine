from random import choice

max_lines = 3
min_bet = 1
max_bet = 100

ROWS = 3
COLUMNS = 3

REWARDS = {
    "A": 3,
    "B": 4,
    "C": 15,
    "D": 4,
}
multipliers = {
    "A": 10,
    "B": 5,
    "C": 2,
    "D": 5,
}


def check_winning_lines(slots: list, lines_bet_on, bet, values):
    winnings = 0
    lines_won = []
    for i, winning_combination in enumerate(slots):
        if i + 1 > lines_bet_on:
            break
        first_reward = winning_combination[0]
        if winning_combination.count(first_reward) == len(winning_combination):
            winnings += values[first_reward] * bet
            lines_won.append(i + 1)

    return winnings, lines_won


def print_slots(rows):
    for each_column in rows:
        print(*each_column, sep=" | ")


def spin(rows, cols, rewards):
    all_rewards = []

    for reward, reward_count in rewards.items():
        for _ in range(reward_count):
            all_rewards.append(reward)

    slots = []
    for _ in range(cols):

        current_column = []
        current_choices = all_rewards.copy()

        for _ in range(rows):
            chosen_value = choice(current_choices)
            current_column.append(chosen_value)
            current_choices.remove(chosen_value)

        slots.append(current_column)

    return slots


def deposit():
    while True:
        deposit_amount = input("Enter your deposit amount: ")

        if not deposit_amount.isdigit():
            print("Please enter a number.\n")

        elif int(deposit_amount) == 0:
            print("Deposit must be more than 0.\n")

        else:
            return int(deposit_amount)


def bet_on_each_line():
    while True:
        bet_amount = input("What would you like to bet on each line?: ")

        if not bet_amount.isdigit():
            print("Please enter a number.\n")

        elif not min_bet <= int(bet_amount) <= max_bet:
            print(f"Bet must be between{min_bet} - {max_bet}.\n")

        else:
            return int(bet_amount)


def lines_to_bet_on():
    while True:
        lines_amount = input(f"Bet on lines (1 - {max_lines}): ")

        if not lines_amount.isdigit():
            print("Please enter a number.\n")

        elif not 1 <= int(lines_amount) <= max_lines:
            print("Enter a valid number of lines.\n")

        else:
            return int(lines_amount)


def retry_game(current_balance):
    lines = lines_to_bet_on()
    while True:
        bets = bet_on_each_line()
        total_bet = lines * bets
        if total_bet <= current_balance:
            break
        print(f"You dont have enough... Your current balance is ${current_balance}")

    print(f"Your total bet is ${total_bet} --> You bet on {lines} lines with {bets}")

    spinning_the_machine = spin(ROWS, COLUMNS, REWARDS)
    won_amount, won_lines = check_winning_lines(spinning_the_machine, lines, bets, multipliers)
    print_slots(spinning_the_machine)
    print(f"You won ${won_amount}")
    print(f"Lines won on:", *won_lines)
    return won_amount - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        quit_checker = input("Press Enter to play (type q to quit): ")
        if quit_checker == "q":
            break
        else:
            balance += retry_game(balance)

    print(f"You left with ${balance}")


main()
