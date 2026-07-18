"""
assistant.py
Main Brain of Nova AI
"""

import re

# Import Modules
from modules.calculator import calculator
from modules.datetime_module import datetime_module
from modules.notes import notes
from modules.knowledge import knowledge
from modules.jokes import jokes


class Assistant:

    def __init__(self):
        self.name = "Nova"

    def reply(self, user_input):

        text = user_input.lower().strip()

        # =========================
        # Greetings
        # =========================

        if text in ["hi", "hello", "hey", "hola"]:
            return "Hello! 👋 How can I help you today?"

        if text == "help":
            return self.help_menu()

        # =========================
        # Calculator
        # =========================

        math_pattern = r'^[0-9\+\-\*\/\(\)\.\^\s×÷]+$'

        if re.match(math_pattern, text):
            return str(calculator.calculate(text))

        if text.startswith(("sqrt", "factorial", "sin", "cos", "tan", "log")):
            return str(calculator.calculate(text))

        if "=" in text:
            return str(calculator.calculate(text))

        # =========================
        # Date & Time
        # =========================

        if text in ["time", "current time"]:
            return datetime_module.get_time()

        if text in ["date", "today"]:
            return datetime_module.get_date()

        if text == "day":
            return datetime_module.get_day()

        if text == "month":
            return datetime_module.get_month()

        if text == "year":
            return datetime_module.get_year()

        if text == "calendar":
            return datetime_module.get_calendar()

        # =========================
        # Notes
        # =========================

        if text.startswith("remember "):
            note = user_input[9:].strip()
            return notes.add_note(note)

        if text == "show notes":
            return notes.show_notes()

        if text.startswith("delete note"):

            try:
                note_id = int(text.split()[-1])
                return notes.delete_note(note_id)

            except:
                return "Please provide a valid note ID."

        if text.startswith("search note "):
            keyword = user_input[12:].strip()
            return notes.search_note(keyword)

        # =========================
        # Knowledge
        # =========================

        if text.startswith("who is "):

            topic = user_input[7:].strip()

            return knowledge.search(topic)

        if text.startswith("what is "):

            topic = user_input[8:].strip()

            return knowledge.search(topic)

        if text.startswith("tell me about "):

            topic = user_input[14:].strip()

            return knowledge.search(topic)

        if text.startswith("learn "):

            try:

                data = user_input[6:]

                topic, info = data.split(":", 1)

                return knowledge.learn(topic.strip(), info.strip())

            except:

                return "Format:\nlearn topic:information"

        if text == "topics":
            return knowledge.all_topics()

        # =========================
        # Jokes
        # =========================

        if "joke" in text:
            return jokes.random_joke()

        # =========================
        # Identity
        # =========================

        if text == "your name":
            return "My name is Nova."

        if text == "who created you":
            return "I was created by Hemant using Python."

        # =========================
        # Exit
        # =========================

        if text == "bye":
            return "Goodbye! 👋"

        # =========================
        # Default
        # =========================

        return (
            "I don't understand that yet.\n"
            "Type 'help' to see available commands."
        )

    def help_menu(self):

        return """
========= NOVA HELP =========

Greetings
----------
hi
hello

Calculator
----------
2+2
25*5
sqrt 81
factorial 5
sin 30
cos 60
tan 45
log 100

Date & Time
----------
time
date
day
month
year
calendar

Notes
----------
remember Buy milk
show notes
delete note 1
search note milk

Knowledge
----------
who is python
what is india
tell me about earth
topics
learn ai:Artificial Intelligence is...

Jokes
----------
tell me a joke

Other
----------
your name
who created you
help
exit

=============================
"""


if __name__ == "__main__":

    bot = Assistant()

    print("Nova AI Started!")

    while True:

        user = input("You : ")

        if user.lower() == "exit":
            break

        print("Nova :", bot.reply(user))