import random

class GuessingGame:
    def __init__(self, lower_bound=1, upper_bound=100):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.target_number = random.randint(lower_bound, upper_bound)
        self.guess_count = 0

    def guess(self, number):
        self.guess_count += 1
        if number < self.target_number:
            return "Too low!"
        elif number > self.target_number:
            return "Too high!"
        else:
            return f"Congratulations! You've guessed the number in {self.guess_count} tries."

def execute():
    game = GuessingGame()
    print(f"Welcome to the Guessing Game! Try to guess the number between {game.lower_bound} and {game.upper_bound}.")
    
    while True:
        try:
            user_input = int(input("Enter your guess: "))
            result = game.guess(user_input)
            print(result)
            if "Congratulations" in result:
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    execute()