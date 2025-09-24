import sys
from game import Game
from morty_loader import MortyLoader

ALLOWED_MORTYS = [
    "morties.classic_morty.ClassicMorty",
    "morties.lazy_morty.LazyMorty"
]

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <num_boxes> <morty_class>")
        print(f"Allowed Mortys: {ALLOWED_MORTYS}")

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

    if morty_class_path not in ALLOWED_MORTYS:
        print(f"Error: Invalid Morty class. Choose one of {ALLOWED_MORTYS}")
        return

    # Load Morty instance
    morty_instance = MortyLoader.load(morty_class_path, num_boxes)
    if morty_instance is None:
        print(f"Error: Can't import module '{morty_class_path}'")
        return

    # Start game
    game = Game(num_boxes, morty_instance)

    while True:
        game.play_round()
        again = input("Play another round? (y=1/n=0)? ")
        if again != "1":
            break

    # Show final stats
    game.stats.display()

    MortyClass = MortyLoader.load(morty_class_path, num_boxes)
    game = Game(num_boxes, MortyClass)
    game.play()


if __name__ == "__main__":
    main()