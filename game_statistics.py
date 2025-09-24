from prettytable import PrettyTable

class GameStatistics:
    def __init__(self):
        self.rounds_switched = 0
        self.rounds_stayed = 0
        self.wins_switched = 0
        self.wins_stayed = 0

    def record(self, switched, won):
        if switched:
            self.rounds_switched += 1
            if won:
                self.wins_switched += 1
        else:
            self.rounds_stayed += 1
            if won:
                self.wins_stayed += 1

    def show(self):
        table = PrettyTable()
        table.field_names = ["Game results", "Rick switched", "Rick stayed"]
        table.add_row(["Rounds", self.rounds_switched, self.rounds_stayed])
        table.add_row(["Wins", self.wins_switched, self.wins_stayed])
        est_switched = self.wins_switched / self.rounds_switched if self.rounds_switched else 0
        est_stayed = self.wins_stayed / self.rounds_stayed if self.rounds_stayed else 0
        table.add_row(["P (estimate)", f"{est_switched:.3f}", f"{est_stayed:.3f}"])
        print("\n=== GAME STATS ===")
        print(table)