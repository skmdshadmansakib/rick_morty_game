import sys
from game import Game
from morty_loader import MortyLoader

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <num_boxes> <Morty class path>")
        return

    try:
        num_boxes = int(sys.argv[1])
    except ValueError:
        print("Error: num_boxes must be an integer")
        return

    morty_class_path = sys.argv[2]

    MortyClass = MortyLoader.load(morty_class_path, num_boxes)
    game = Game(num_boxes, MortyClass)
    game.play()

if __name__ == "__main__":
    main()