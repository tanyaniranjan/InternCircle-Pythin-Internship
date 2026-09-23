import random
from collections import Counter


def number_guessing_game():
    print("\n===== Number Guessing Game =====")
    print("I have selected a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")


def word_counter():
    print("\n===== Word Counter =====")

    filename = input("Enter the text file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.lower().split()
        word_frequency = Counter(words)

        print("\nTotal words:", len(words))
        print("\nWord Frequency:")

        for word, count in word_frequency.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found. Please check the file name.")


def main():
    while True:
        print("\n===== Number Guessing Game & Word Counter =====")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
