from provably_fair import ProvablyFair
from game_statistics import GameStatistics

class Game:
    def __init__(self, num_boxes, morty):
        self.num_boxes = num_boxes
        self.morty = morty
        self.stats = GameStatistics()

    def get_valid_input(self, prompt, min_val, max_val):
        while True:
            try:
                n = int(input(prompt))
                if min_val <= n < max_val:
                    return n
                else:
                    print(f"Error: number must be between {min_val} and {max_val-1}")
            except ValueError:
                print("Error: invalid input")

    def play_round(self):
        print(f"Morty: Oh geez, Rick, I'm gonna hide your portal gun in one of the {self.num_boxes} boxes!")
        pf = ProvablyFair(self.num_boxes)
        print(f"Morty: HMAC1={pf.get_hmac()}")
        rick_value = self.get_valid_input("Rick, enter your number: ", 0, self.num_boxes)
        morty_value, key = pf.reveal()
        print(f"Morty's number is {morty_value}, KEY={key.hex()}, final={(morty_value + rick_value) % self.num_boxes}")
        guess = self.get_valid_input("What's your guess: ", 0, self.num_boxes)
        remaining_boxes = [i for i in range(self.num_boxes) if i != guess]
        print(f"Morty: Available boxes: {remaining_boxes}")
        switch = self.get_valid_input("Rick, switch (0) or stay (1)? ", 0, 2)
        final_box = (morty_value + rick_value) % self.num_boxes
        won = (guess == final_box) if switch else (guess != final_box)
        print(f"Morty: The portal gun is in box {final_box}")
        print(f"Morty: {'You won!' if won else 'You lost!'}")
        self.stats.add_result(switched=(switch == 0), won=won)
        return self.get_valid_input("Morty: Play another round? (y=1/n=0)? ", 0, 2) == 1

    def play(self):
        while True:
            if not self.play_round():
                break
        self.stats.print_stats()
        print("Morty: Okay… uh, bye!")