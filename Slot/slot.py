from curses.ascii import isdigit
import random

MAX_LINE = 10
MAX_BET = 1000
MIN_BET = 1

ROWS = 10
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value= {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        updated_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(updated_symbols)
            updated_symbols.remove(value)
            column.append(value)
        columns.append(column)    

    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = " ")
        print()


def check_win(columns, lines, bet, values):
    winnings = 0
    win_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            win_lines.append(line + 1)
    
    return winnings, win_lines

def deposit():
    while True:
        deposit_amount = input("How much money do you want to deposit into your account? $")

        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)

            if deposit_amount > 0:
                break

            else:
                print("Amount must be greater than 0.")

        else:
            print("Please enter a number. ")

    return deposit_amount

def num_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 - " + str(MAX_LINE) + ") ")

        if lines.isdigit():
            lines = int(lines)

            if (lines >= 1) and (lines <= MAX_LINE):
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number. ")

    return lines


def bet_num():
    while True:
        bet = input("What would you like to bet on each line? $")

        if bet.isdigit():
            bet = int(bet)

            if (bet >= MIN_BET) and (bet <= MAX_BET):
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}. ")
        else:
            print("Please enter a number. ")

    return bet

def game(balance):
    lines = num_lines()
    while True:
        bet = bet_num()
        bet_tot = bet * lines
        if balance < bet_tot:
             print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        
        else:
            break
    print(f"You are betting ${bet} on {lines} lines, so the total bet is ${bet_tot}.")

    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot(slots)
    winnings, win_lines = check_win(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines", *win_lines)

    return winnings - bet_tot

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("Press enter to spin or q to quit.")
        if spin == "q":
            break
        balance += game(balance)



main()