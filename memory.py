"""
memory.py

Long Term Memory Module
Stores user information using SQLite.
"""

import sqlite3


class Memory:

    def __init__(self):

        self.connection = sqlite3.connect("history.db")

        self.cursor = self.connection.cursor()

        self.create_table()

    # ------------------------------------

    def create_table(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS memory(

            key TEXT PRIMARY KEY,

            value TEXT

        )

        """)

        self.connection.commit()

    # ------------------------------------

    def remember(self, key, value):

        key = key.lower().strip()

        value = value.strip()

        self.cursor.execute("""

        INSERT OR REPLACE INTO memory(key,value)

        VALUES(?,?)

        """, (key, value))

        self.connection.commit()

        return "Memory Saved."

    # ------------------------------------

    def recall(self, key):

        key = key.lower().strip()

        self.cursor.execute("""

        SELECT value

        FROM memory

        WHERE key=?

        """, (key,))

        result = self.cursor.fetchone()

        if result:

            return result[0]

        return "I don't remember that."

    # ------------------------------------

    def forget(self, key):

        key = key.lower().strip()

        self.cursor.execute("""

        DELETE FROM memory

        WHERE key=?

        """, (key,))

        self.connection.commit()

        return "Memory Deleted."

    # ------------------------------------

    def exists(self, key):

        key = key.lower().strip()

        self.cursor.execute("""

        SELECT *

        FROM memory

        WHERE key=?

        """, (key,))

        return self.cursor.fetchone() is not None

    # ------------------------------------

    def show_memory(self):

        self.cursor.execute("""

        SELECT *

        FROM memory

        """)

        rows = self.cursor.fetchall()

        if not rows:

            return "Memory Empty."

        output = ""

        for key, value in rows:

            output += f"{key} : {value}\n"

        return output

    # ------------------------------------

    def clear(self):

        self.cursor.execute("""

        DELETE FROM memory

        """)

        self.connection.commit()

        return "All Memory Cleared."

    # ------------------------------------

    def total(self):

        self.cursor.execute("""

        SELECT COUNT(*)

        FROM memory

        """)

        return self.cursor.fetchone()[0]

    # ------------------------------------

    def close(self):

        self.connection.close()


memory = Memory()


if __name__ == "__main__":

    while True:

        print("\n====== MEMORY ======")

        print("1. Remember")

        print("2. Recall")

        print("3. Forget")

        print("4. Show Memory")

        print("5. Total")

        print("6. Clear")

        print("7. Exit")

        choice = input("\nChoice : ")

        if choice == "1":

            key = input("Key : ")

            value = input("Value : ")

            print(memory.remember(key, value))

        elif choice == "2":

            key = input("Key : ")

            print(memory.recall(key))

        elif choice == "3":

            key = input("Key : ")

            print(memory.forget(key))

        elif choice == "4":

            print(memory.show_memory())

        elif choice == "5":

            print(memory.total())

        elif choice == "6":

            print(memory.clear())

        elif choice == "7":

            memory.close()

            break

        else:

            print("Invalid Choice")