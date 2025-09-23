import sys
from game import Game
from morty_loader import MortyLoader

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <num_boxes> <Morty class path>")
        print("Example: python main.py 3 morties.classic_morty.ClassicMorty")
        return

    try:
        num_boxes = int(sys.argv[1])
        if num_boxes < 3:
            raise ValueError
    except ValueError:
        print("Error: num_boxes must be an integer greater than 2")
        return

    morty_class_path = sys.argv[2]
    morty_instance = MortyLoader.load(morty_class_path, num_boxes)

    game = Game(num_boxes, morty_instance)
    game.play()

if __name__ == "__main__":
    main()