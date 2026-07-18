"""
jokes.py
Offline Jokes Module for Nova AI
"""

import random


class Jokes:

    def __init__(self):

        self.jokes = [

            "Why do programmers prefer dark mode? Because light attracts bugs.",

            "Why did the Python developer go broke? Because he kept using up all his cache.",

            "Debugging is like being a detective in a crime movie where you are also the criminal.",

            "There are only 10 types of people in the world: those who understand binary and those who don't.",

            "Why don't programmers like nature? It has too many bugs.",

            "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'",

            "I would tell you a UDP joke, but you might not get it.",

            "Why was the computer cold? It forgot to close its Windows.",

            "My computer beat me at chess... but it was no match for me at kickboxing.",

            "Why did the laptop visit the doctor? It caught a virus.",

            "Why was the JavaScript developer sad? Because he didn't Node how to Express himself.",

            "I changed my password to 'incorrect'. Now whenever I forget it, my computer says 'Your password is incorrect.'",

            "Artificial Intelligence won't replace humans... unless humans keep forgetting to save their work.",

            "Why did the robot get promoted? Because it had outstanding processing skills.",

            "Never trust an atom. They make up everything."

        ]

    def random_joke(self):
        return random.choice(self.jokes)

    def joke_count(self):
        return len(self.jokes)

    def add_joke(self, joke):

        joke = joke.strip()

        if joke == "":
            return "Joke cannot be empty."

        self.jokes.append(joke)

        return "New joke added."

    def all_jokes(self):

        output = ""

        for i, joke in enumerate(self.jokes, start=1):
            output += f"{i}. {joke}\n\n"

        return output.strip()


jokes = Jokes()


if __name__ == "__main__":

    while True:

        print("\n===== Joke Center =====")
        print("1. Random Joke")
        print("2. Show All Jokes")
        print("3. Add Joke")
        print("4. Joke Count")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            print("\n😂", jokes.random_joke())

        elif choice == "2":
            print("\n")
            print(jokes.all_jokes())

        elif choice == "3":
            joke = input("Enter joke: ")
            print(jokes.add_joke(joke))

        elif choice == "4":
            print(f"\nTotal jokes: {jokes.joke_count()}")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")