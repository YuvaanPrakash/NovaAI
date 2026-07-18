"""
router.py
Routes the user's query to the correct module.
"""

from modules.calculator import calculator
from modules.datetime_module import datetime_module
from modules.notes import notes
from modules.knowledge import knowledge
from modules.jokes import jokes


class Router:

    def __init__(self):
        pass

    def route(self, query):

        text = query.lower().strip()

        # -----------------------
        # Calculator
        # -----------------------

        operators = ["+", "-", "*", "/", "%", "**"]

        if any(op in text for op in operators):
            return calculator.calculate(query)

        # -----------------------
        # Date & Time
        # -----------------------

        if text == "time":
            return datetime_module.get_time()

        if text == "date":
            return datetime_module.get_date()

        if text == "day":
            return datetime_module.get_day()

        if text == "month":
            return datetime_module.get_month()

        if text == "year":
            return datetime_module.get_year()

        if text == "calendar":
            return datetime_module.get_calendar()

        # -----------------------
        # Notes
        # -----------------------

        if text.startswith("remember "):

            note = query[9:].strip()

            return notes.add_note(note)

        if text == "show notes":
            return notes.show_notes()

        if text.startswith("delete note"):

            try:
                note_id = int(text.split()[-1])
                return notes.delete_note(note_id)

            except:
                return "Invalid Note ID"

        if text.startswith("search note"):

            keyword = query[12:].strip()

            return notes.search_note(keyword)

        # -----------------------
        # Knowledge
        # -----------------------

        if text.startswith("who is "):

            topic = query[7:]

            return knowledge.search(topic)

        if text.startswith("what is "):

            topic = query[8:]

            return knowledge.search(topic)

        if text.startswith("tell me about "):

            topic = query[14:]

            return knowledge.search(topic)

        if text.startswith("learn "):

            try:

                data = query[6:]

                topic, info = data.split(":", 1)

                return knowledge.learn(topic, info)

            except:
                return "Use:\nlearn topic:information"

        if text == "topics":
            return knowledge.all_topics()

        # -----------------------
        # Jokes
        # -----------------------

        if "joke" in text:
            return jokes.random_joke()

        # -----------------------
        # Greetings
        # -----------------------

        if text in ["hi", "hello", "hey"]:

            return "Hello 👋"

        if text == "help":

            return "Help menu coming soon."

        if text == "bye":

            return "Goodbye!"

        # -----------------------
        # Unknown
        # -----------------------

        return "Sorry, I don't understand."


router = Router()