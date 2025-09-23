from provably_fair import ProvablyFair
from game_statistics import GameStatistics

class Game:
    def __init__(self, num_boxes, morty_instance):
        self.num_boxes = num_boxes
        self.morty = morty_instance
        self.stats = GameStatistics()

    def get_valid_input(self, prompt, min_val, max_val):
        while True:
            try:
                value = int(input(prompt))
                if value < min_val or value >= max_val:
                    print(f"Error: number must be between {min_val} and {max_val-1}")
                    continue
                return value
            except ValueError:
                print("Error: please enter a valid integer.")

    def play(self):
        while True:
            print(f"Morty: Oh geez, Rick, I'm gonna hide your portal gun in one of the {self.num_boxes} boxes!")
            fair = ProvablyFair(self.num_boxes)
            print(f"Morty: HMAC1={fair.get_hmac()}")

            rick_value = self.get_valid_input("Rick, enter your number: ", 0, self.num_boxes)
            morty_value, key = fair.reveal()
            final_value = (morty_value + rick_value) % self.num_boxes

            print(f"Morty's number is {morty_value}, KEY={key.hex()}, final={final_value}")
            guess = self.get_valid_input("What's your guess: ", 0, self.num_boxes)

            available_boxes = self.morty.remove_boxes(final_value, guess)
            print(f"Morty: Available boxes: {available_boxes}")

            switch = self.get_valid_input("Rick, switch (0) or stay (1)? ", 0, 2)
            won = final_value == guess if switch else final_value != guess
            self.stats.add_result(switched=(switch==0), won=won)

            print(f"Morty: {'You won!' if won else 'You lost!'}")

            cont = input("Morty: Play another round? (y/Y or n/N)? ").lower()
            if cont != 'y':
                break

        self.stats.print_table()
        print("Morty: Okay… uh, bye!")