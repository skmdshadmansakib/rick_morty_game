import sys

class CLIParser:
    @staticmethod
    def parse_args():
        if len(sys.argv) != 3:
            print("Usage: python main.py <num_boxes> <Morty class path>")
            print("Example: python main.py 3 morties.classic_morty.ClassicMorty")
            sys.exit(1)

        try:
            num_boxes = int(sys.argv[1])
            if num_boxes < 2:
                raise ValueError
        except ValueError:
            print("Error: <num_boxes> must be an integer >= 2")
            sys.exit(1)

        morty_class_path = sys.argv[2]
        return num_boxes, morty_class_path