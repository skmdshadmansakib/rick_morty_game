# Rick & Morty Provably Fair Game

This is a Python implementation of a provably fair game inspired by Rick & Morty. The game demonstrates HMAC-based fairness and modular design with “Morty plugins.”

---

## Project Overview

- The user (Rick) tries to guess which box contains the portal gun.
- Morty hides the portal gun in one of the boxes and uses HMACs to prove the numbers are fair.
- The game supports multiple Morty implementations: 
  - **ClassicMorty** – uses random selection for remaining boxes.
  - **LazyMorty** – removes boxes with the lowest index, no random numbers.
- Game statistics (switch/stay probabilities) are calculated and displayed in a formatted ASCII table.

---

## Features / Rules Compliance

✅ **Separate classes/files** for modular design:  
- `key_manager.py` – handles cryptographic key generation.  
- `provably_fair.py` – implements HMAC-based provably fair number generation.  
- `game_statistics.py` – accumulates game stats and calculates probabilities.  
- `cli_parser.py` – parses command-line arguments.  
- `morty_loader.py` – dynamically loads Morty classes.  
- `morties/classic_morty.py` – ClassicMorty plugin.  
- `morties/lazy_morty.py` – LazyMorty plugin.  
- `main.py` – entry point.  
- `game.py` – contains the main game loop.  

✅ **HMAC fairness** – the key and message (Morty number) are used to generate HMAC before Rick makes a selection.  

✅ **Command-line validation** – incorrect usage handled:  
- No arguments → shows usage example.  
- Only one argument → shows usage.  
- Non-existent Morty class → shows import error.  

✅ **Statistics and probabilities** – calculated per Morty behavior (switch/stay).  

✅ **ASCII table output** – game statistics displayed nicely using `tabulate`.

---

## Requirements

- Python 3.10+
- `tabulate` library

`bash
pip install -r requirements.txt

## **Usage**
python main.py <num_boxes> <Morty class path>
Example:
python main.py 3 morties.classic_morty.ClassicMorty
python main.py 3 morties.lazy_morty.LazyMorty
Testing Incorrect Parameters
python main.py                  # no arguments
python main.py 1                # only one argument
python main.py 3 morties.fake_morty.FakeMorty  # non-existent class

## **Gameplay**
1. Morty hides the portal gun in one of the boxes and displays HMAC1.

2. Rick enters a number (0-indexed).

3. Morty generates fair random number and displays HMAC2.

4. Rick enters a guess for the remaining boxes.

5. Rick can switch or stay with his choice.

6. Morty reveals the portal gun and the secret key(s).

7. Game statistics table is updated.

## **Video Demonstration**
[https://streamable.com/e/sh9m5h](https://streamable.com/s5vxy6)

## **GitHub Repository**
https://github.com/skmdshadmansakib/rick_morty_game

## **Notes**
• The numbers in the prompts are 0-indexed ([0, num_boxes)) by default.

• Statistics are estimated based on switching/staying behavior.

• HMAC verification ensures the computer cannot cheat.
