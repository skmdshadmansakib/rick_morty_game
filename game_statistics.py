from tabulate import tabulate

class GameStatistics:
    def __init__(self):
        self.switched_rounds = 0
        self.stayed_rounds = 0
        self.switched_wins = 0
        self.stayed_wins = 0

    def add_result(self, switched: bool, won: bool):
        if switched:
            self.switched_rounds += 1
            if won: self.switched_wins += 1
        else:
            self.stayed_rounds += 1
            if won: self.stayed_wins += 1

    def print_stats(self):
        def estimate(wins, rounds):
            return wins/rounds if rounds else 0

        table = [
            ["Rounds", self.switched_rounds, self.stayed_rounds],
            ["Wins", self.switched_wins, self.stayed_wins],
            ["P (estimate)", f"{estimate(self.switched_wins, self.switched_rounds):.3f}", f"{estimate(self.stayed_wins, self.stayed_rounds):.3f}"],
        ]
        print("\nGAME STATS")
        print(tabulate(table, headers=["Game results", "Rick switched", "Rick stayed"], tablefmt="fancy_grid"))