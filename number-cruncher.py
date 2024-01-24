import random
import time

# ANSI escape codes for colorization
RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'

def generate_numbers():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    equation = f"{num1} {operator} {num2}"
    answer = eval(equation)
    return equation, answer

def colorize_text(text, color):
    return f"{color}{text}{RESET}"

def play_game():
    score = 0
    while True:
        equation, correct_answer = generate_numbers()
        colorized_equation = colorize_text(f"Calculate: {equation}", CYAN)
        print(colorized_equation)

        start_time = time.time()
        user_answer = input("Your answer: ")

        try:
            user_answer = float(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            break

        elapsed_time = time.time() - start_time

        if user_answer == correct_answer and elapsed_time <= 20:
            score += 1
            print(f"Correct! Your current score: {score}")
        elif elapsed_time > 20:
            print("Time's up! Game over.")
            break
        else:
            print(f"Wrong answer! The correct answer is {correct_answer}. Game over. Your final score: {score}")
            break

if __name__ == "__main__":
    print("Welcome to the Number Cruncher Game!")
    print("You have 20 seconds per round. Enter your answers quickly and correctly.")
    print("Type 'exit' to end the game.\n")

    play_game()
