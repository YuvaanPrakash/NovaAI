"""
notes.py
Offline Notes Module using SQLite
"""

import sqlite3


class Notes:

    def __init__(self):

        self.connection = sqlite3.connect("history.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            note TEXT NOT NULL
        )
        """)

        self.connection.commit()

    def add_note(self, text):

        self.cursor.execute(
            "INSERT INTO notes(note) VALUES(?)",
            (text,)
        )

        self.connection.commit()

        return "✅ Note saved."

    def show_notes(self):

        self.cursor.execute(
            "SELECT * FROM notes"
        )

        notes = self.cursor.fetchall()

        if not notes:
            return "No notes found."

        output = []

        for note in notes:
            output.append(f"{note[0]}. {note[1]}")

        return "\n".join(output)

    def delete_note(self, note_id):

        self.cursor.execute(
            "DELETE FROM notes WHERE id=?",
            (note_id,)
        )

        self.connection.commit()

        return "🗑️ Note deleted."

    def search_note(self, keyword):

        self.cursor.execute(
            "SELECT * FROM notes WHERE note LIKE ?",
            (f"%{keyword}%",)
        )

        results = self.cursor.fetchall()

        if not results:
            return "No matching notes."

        output = []

        for note in results:
            output.append(f"{note[0]}. {note[1]}")

        return "\n".join(output)

    def close(self):
        self.connection.close()


notes = Notes()


if __name__ == "__main__":

    while True:

        print("\n------ Notes ------")
        print("1. Add Note")
        print("2. Show Notes")
        print("3. Delete Note")
        print("4. Search Note")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":

            note = input("Enter Note: ")
            print(notes.add_note(note))

        elif choice == "2":

            print(notes.show_notes())

        elif choice == "3":

            note_id = int(input("Note ID: "))
            print(notes.delete_note(note_id))

        elif choice == "4":

            keyword = input("Keyword: ")
            print(notes.search_note(keyword))

        elif choice == "5":

            notes.close()
            break

        else:

            print("Invalid Choice")