from cli_parser import CLIParser
from morty_loader import MortyLoader
from game import Game

def main():
    num_boxes, morty_class_path = CLIParser.parse_args()
    morty = MortyLoader.load(morty_class_path, num_boxes)
    game = Game(num_boxes, morty)
    game.play()

if __name__ == "__main__":
    main()