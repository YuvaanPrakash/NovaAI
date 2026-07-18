"""
config.py

Global configuration file for Nova AI
Edit values here instead of changing them throughout the project.
"""

# =====================================================
# Assistant Information
# =====================================================

ASSISTANT_NAME = "Nova"

VERSION = "1.0.0"

DEVELOPER = "Hemant"

DESCRIPTION = "Offline AI Assistant built in Python"


# =====================================================
# Database
# =====================================================

DATABASE_NAME = "history.db"


# =====================================================
# Data Files
# =====================================================

KNOWLEDGE_FILE = "data/knowledge.json"

NOTES_FILE = "data/notes.json"

RESPONSES_FILE = "data/responses.json"


# =====================================================
# User Interface
# =====================================================

WELCOME_MESSAGE = f"""
======================================
        Welcome to {ASSISTANT_NAME}
======================================

Type 'help' for commands.
Type 'exit' to quit.

"""

GOODBYE_MESSAGE = "Goodbye! Have a great day."


# =====================================================
# Commands
# =====================================================

EXIT_COMMAND = "exit"

HELP_COMMAND = "help"


# =====================================================
# Default Responses
# =====================================================

UNKNOWN_COMMAND = (
    "Sorry, I don't understand that yet."
)

ERROR_MESSAGE = (
    "Something went wrong."
)


# =====================================================
# Greeting Messages
# =====================================================

GREETINGS = [

    "Hello!",

    "Hi there!",

    "Welcome back!",

    "Hey!",

    "Nice to see you."

]


# =====================================================
# Supported Operators
# =====================================================

OPERATORS = [

    "+",

    "-",

    "*",

    "/",

    "%",

    "**"

]


# =====================================================
# Date Commands
# =====================================================

DATE_COMMANDS = [

    "time",

    "date",

    "day",

    "month",

    "year",

    "calendar"

]


# =====================================================
# Notes Commands
# =====================================================

NOTE_COMMANDS = [

    "remember",

    "show notes",

    "delete note",

    "search note"

]


# =====================================================
# Knowledge Commands
# =====================================================

KNOWLEDGE_COMMANDS = [

    "who is",

    "what is",

    "tell me about",

    "learn",

    "topics"

]


# =====================================================
# Joke Commands
# =====================================================

JOKE_COMMANDS = [

    "joke"

]