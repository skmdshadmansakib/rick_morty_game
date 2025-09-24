from game_statistics import GameStatistics

class Game:
    def __init__(self, num_boxes, morty_instance):
        self.num_boxes = num_boxes
        self.morty = morty_instance  # Already an instance!
        self.stats = GameStatistics()

    def play_round(self):
        print("\n=== New Round ===")
        # Generate Morty's choice with HMAC
        hmac_value = self.morty.generate_hmac()
        print(f"Morty: HMAC1={hmac_value}")

        # Rick chooses a number
        while True:
            try:
                rick_choice = int(input(f"Rick, enter your number (0–{self.num_boxes-1}): "))
                if 0 <= rick_choice < self.num_boxes:
                    break
                else:
                    print(f"Error: number must be between 0 and {self.num_boxes-1}")
            except ValueError:
                print("Error: must enter an integer")

        # Morty finalizes number
        final_number, key = self.morty.finalize_number()
        print(f"Morty's number revealed after choice, KEY={key}, final={final_number}")

        # Rick guesses
        while True:
            try:
                guess = int(input(f"What's your guess (0–{self.num_boxes-1}): "))
                if 0 <= guess < self.num_boxes:
                    break
                else:
                    print(f"Error: number must be between 0 and {self.num_boxes-1}")
            except ValueError:
                print("Error: must enter an integer")

        # Rick switches or stays
        while True:
            try:
                switch = int(input("Rick, switch (0) or stay (1)? "))
                if switch in [0, 1]:
                    break
                else:
                    print("Error: enter 0 for switch, 1 for stay")
            except ValueError:
                print("Error: must enter 0 or 1")

        # Check result
        if (switch == 0 and guess != final_number) or (switch == 1 and guess == final_number):
            print("Rick found the portal gun! 🎉")
            self.stats.record_win(switch)
        else:
            print("Rick failed! Morty tricked him. 😢")
            self.stats.record_loss(switch)