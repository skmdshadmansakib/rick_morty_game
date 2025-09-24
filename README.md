# Rick & Morty Game 🎮
  
Rick tries to outsmart Morty in a probability-based guessing game.  

---

## 📹 Demo Video
(https://drive.google.com/file/d/1nGI0RXlpeDpUTRzOxZG2ohf5vZinXvUC/view?usp=drive_link)

---

## 🚀 Features
- Multiple Morty strategies (`ClassicMorty`, `LazyMorty`)
- Provably fair randomness (HMAC reveal)
- Rick can choose to **switch or stay** (Monty Hall problem inspired)
- Game statistics with clean **ASCII table output**
- Extendable — add new Morty strategies easily

---

## 🛠️ Installation & Usage

### 1. Clone the repo
bash
git clone https://github.com/skmdshadmansakib/rick_morty_game.git
cd rick_morty_game

### 2. Install requirements
pip install -r requirements.txt

### 3. Run the game
python main.py <num_boxes> <morty_class>

Example:
python main.py 3 morties.classic_morty.ClassicMorty


## **📌 Notes**

Works best with Python 3.10+

Designed for learning probability, randomness, and provably fair mechanisms

Inspired by the Monty Hall problem with a Rick & Morty twist

