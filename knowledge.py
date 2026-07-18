"""
knowledge.py
Offline Knowledge Module for Nova AI

Loads knowledge from data/knowledge.json
Supports:
- Search
- Learn
- Save
- Reload
- List all topics
"""

import json
import os


class Knowledge:

    def __init__(self):

        self.file_path = "data/knowledge.json"

        self.knowledge = {}

        self.load()

    # --------------------------
    # Load JSON
    # --------------------------

    def load(self):

        if not os.path.exists(self.file_path):

            self.knowledge = {}

            self.save()

            return

        try:

            with open(self.file_path, "r", encoding="utf-8") as file:

                self.knowledge = json.load(file)

        except:

            self.knowledge = {}

    # --------------------------
    # Save JSON
    # --------------------------

    def save(self):

        with open(self.file_path, "w", encoding="utf-8") as file:

            json.dump(
                self.knowledge,
                file,
                indent=4,
                ensure_ascii=False
            )

    # --------------------------
    # Search Topic
    # --------------------------

    def search(self, topic):

        topic = topic.lower().strip()

        if topic in self.knowledge:

            return self.knowledge[topic]

        return "I don't know anything about that."

    # --------------------------
    # Learn New Topic
    # --------------------------

    def learn(self, topic, information):

        topic = topic.lower().strip()

        information = information.strip()

        self.knowledge[topic] = information

        self.save()

        return f"I learned about '{topic}'."

    # --------------------------
    # Remove Topic
    # --------------------------

    def remove(self, topic):

        topic = topic.lower().strip()

        if topic not in self.knowledge:

            return "Topic not found."

        del self.knowledge[topic]

        self.save()

        return "Topic removed."

    # --------------------------
    # Topic Exists?
    # --------------------------

    def exists(self, topic):

        return topic.lower().strip() in self.knowledge

    # --------------------------
    # Total Topics
    # --------------------------

    def count(self):

        return len(self.knowledge)

    # --------------------------
    # List Topics
    # --------------------------

    def all_topics(self):

        if not self.knowledge:

            return "Knowledge base is empty."

        topics = sorted(self.knowledge.keys())

        return "\n".join(topics)

    # --------------------------
    # Reload File
    # --------------------------

    def reload(self):

        self.load()

        return "Knowledge reloaded."


knowledge = Knowledge()


# ---------------------------------------
# Testing
# ---------------------------------------

if __name__ == "__main__":

    while True:

        print("\n====== Knowledge Module ======")

        print("1. Search")

        print("2. Learn")

        print("3. Remove")

        print("4. Topics")

        print("5. Count")

        print("6. Reload")

        print("7. Exit")

        choice = input("\nChoice : ")

        if choice == "1":

            topic = input("Topic : ")

            print(knowledge.search(topic))

        elif choice == "2":

            topic = input("Topic : ")

            info = input("Information : ")

            print(knowledge.learn(topic, info))

        elif choice == "3":

            topic = input("Topic : ")

            print(knowledge.remove(topic))

        elif choice == "4":

            print()

            print(knowledge.all_topics())

        elif choice == "5":

            print("Total Topics :", knowledge.count())

        elif choice == "6":

            print(knowledge.reload())

        elif choice == "7":

            break

        else:

            print("Invalid Choice")