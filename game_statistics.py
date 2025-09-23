from prettytable import PrettyTable

class GameStatistics:
    def __init__(self):
        self.switched = 0
        self.stayed = 0
        self.wins_switched = 0
        self.wins_stayed = 0

    def add_result(self, switched, won):
        if switched:
            self.switched += 1
            if won:
                self.wins_switched += 1
        else:
            self.stayed += 1
            if won:
                self.wins_stayed += 1

    def print_table(self):
        table = PrettyTable()
        table.field_names = ["Game results", "Rick switched", "Rick stayed"]
        table.add_row(["Rounds", self.switched, self.stayed])
        table.add_row(["Wins", self.wins_switched, self.wins_stayed])
        table.add_row([
            "P (estimate)",
            round(self.wins_switched / self.switched if self.switched else 0, 6),
            round(self.wins_stayed / self.stayed if self.stayed else 0, 6)
        ])
        print("\nGAME STATS")
        print(table)