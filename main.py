"""
Nova AI
Main Entry Point
"""

from assistant import Assistant


def main():

    print("=" * 50)
    print("        NOVA AI ASSISTANT")
    print("=" * 50)
    print("Type 'help' to see commands.")
    print("Type 'exit' to quit.\n")

    nova = Assistant()

    while True:

        user_input = input("You : ").strip()

        if user_input == "":
            continue

        if user_input.lower() == "exit":
            print("\nNova : Goodbye! Have a great day.")
            break

        response = nova.reply(user_input)

        print(f"Nova : {response}\n")


if __name__ == "__main__":
    main()