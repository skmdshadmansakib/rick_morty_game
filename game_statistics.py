class GameStatistics:
    def __init__(self):
        self.switched = {"wins": 0, "rounds": 0}
        self.stayed = {"wins": 0, "rounds": 0}

    def record_win(self, switch):
        if switch == 0:
            self.switched["wins"] += 1
            self.switched["rounds"] += 1
        else:
            self.stayed["wins"] += 1
            self.stayed["rounds"] += 1

    def record_loss(self, switch):
        if switch == 0:
            self.switched["rounds"] += 1
        else:
            self.stayed["rounds"] += 1

    def display(self):
        rounds_sw = self.switched["rounds"]
        rounds_st = self.stayed["rounds"]
        wins_sw = self.switched["wins"]
        wins_st = self.stayed["wins"]
        p_sw = wins_sw / rounds_sw if rounds_sw else 0
        p_st = wins_st / rounds_st if rounds_st else 0

        headers = ["Game results", "Rick switched", "Rick stayed"]
        rows = [
            ["Rounds", rounds_sw, rounds_st],
            ["Wins", wins_sw, wins_st],
            ["P(win)", f"{p_sw:.3f}", f"{p_st:.3f}"]
        ]

        # Calculate column widths (header vs row content)
        col_widths = []
        for i in range(len(headers)):
            max_len = max(len(str(headers[i])), *(len(str(row[i])) for row in rows))
            col_widths.append(max_len + 2)  # padding

        # Helper to draw horizontal lines
        def draw_line(left, mid, right):
            return left + mid.join("─" * w for w in col_widths) + right

        # Print table
        print("\n" + draw_line("┌", "┬", "┐"))

        # Header row
        header_row = "│" + "│".join(f"{h:^{w}}" for h, w in zip(headers, col_widths)) + "│"
        print(header_row)
        print(draw_line("├", "┼", "┤"))

        # Data rows
        for idx, row in enumerate(rows):
            row_line = "│" + "│".join(f"{str(cell):^{w}}" for cell, w in zip(row, col_widths)) + "│"
            print(row_line)
            if idx != len(rows) - 1:
                print(draw_line("├", "┼", "┤"))

        print(draw_line("└", "┴", "┘"))