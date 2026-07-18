"""
files.py

File Management Module
Nova AI
"""

import os
import shutil
from pathlib import Path

try:
    from send2trash import send2trash
except ImportError:
    send2trash = None


class FileManager:

    # ------------------------------------
    # Create Folder
    # ------------------------------------

    def create_folder(self, folder_name):

        try:
            Path(folder_name).mkdir(parents=True, exist_ok=False)
            return f"Folder '{folder_name}' created."

        except FileExistsError:
            return "Folder already exists."

        except Exception as e:
            return f"Error: {e}"

    # ------------------------------------
    # Create File
    # ------------------------------------

    def create_file(self, file_name):

        try:

            Path(file_name).touch(exist_ok=False)

            return f"File '{file_name}' created."

        except FileExistsError:

            return "File already exists."

        except Exception as e:

            return f"Error: {e}"

    # ------------------------------------
    # Rename
    # ------------------------------------

    def rename(self, old_name, new_name):

        try:

            os.rename(old_name, new_name)

            return "Renamed successfully."

        except Exception as e:

            return f"Error: {e}"

    # ------------------------------------
    # Copy
    # ------------------------------------

    def copy(self, source, destination):

        try:

            shutil.copy2(source, destination)

            return "Copied successfully."

        except Exception as e:

            return f"Error: {e}"

    # ------------------------------------
    # Move
    # ------------------------------------

    def move(self, source, destination):

        try:

            shutil.move(source, destination)

            return "Moved successfully."

        except Exception as e:

            return f"Error: {e}"

    # ------------------------------------
    # Delete (Recycle Bin)
    # ------------------------------------

    def delete(self, path):

        if send2trash is None:
            return (
                "send2trash is not installed.\n"
                "Run: pip install send2trash"
            )

        try:

            send2trash(path)

            return "Moved to Recycle Bin."

        except Exception as e:

            return f"Error: {e}"

    # ------------------------------------
    # Exists
    # ------------------------------------

    def exists(self, path):

        return os.path.exists(path)

    # ------------------------------------
    # List Files
    # ------------------------------------

    def list_files(self, folder="."):

        try:

            files = os.listdir(folder)

            if not files:

                return "Folder is empty."

            return "\n".join(files)

        except Exception as e:

            return f"Error: {e}"

    # ------------------------------------
    # Search
    # ------------------------------------

    def search(self, folder, filename):

        results = []

        for root, dirs, files in os.walk(folder):

            for file in files:

                if filename.lower() in file.lower():

                    results.append(
                        os.path.join(root, file)
                    )

        if not results:

            return "No matching files found."

        return "\n".join(results)

    # ------------------------------------
    # File Size
    # ------------------------------------

    def size(self, file):

        try:

            size = os.path.getsize(file)

            return f"{size} bytes"

        except Exception as e:

            return f"Error: {e}"

    # ------------------------------------
    # Current Directory
    # ------------------------------------

    def current_directory(self):

        return os.getcwd()


files = FileManager()


if __name__ == "__main__":

    while True:

        print("\n========== FILE MANAGER ==========")

        print("1. Create Folder")
        print("2. Create File")
        print("3. Rename")
        print("4. Copy")
        print("5. Move")
        print("6. Delete")
        print("7. List Files")
        print("8. Search")
        print("9. File Size")
        print("10. Current Directory")
        print("11. Exit")

        choice = input("\nChoice : ")

        if choice == "1":

            name = input("Folder Name : ")

            print(files.create_folder(name))

        elif choice == "2":

            name = input("File Name : ")

            print(files.create_file(name))

        elif choice == "3":

            old = input("Old Name : ")

            new = input("New Name : ")

            print(files.rename(old, new))

        elif choice == "4":

            src = input("Source : ")

            dst = input("Destination : ")

            print(files.copy(src, dst))

        elif choice == "5":

            src = input("Source : ")

            dst = input("Destination : ")

            print(files.move(src, dst))

        elif choice == "6":

            path = input("Path : ")

            print(files.delete(path))

        elif choice == "7":

            folder = input("Folder (blank=current): ").strip()

            if folder == "":
                folder = "."

            print(files.list_files(folder))

        elif choice == "8":

            folder = input("Folder : ")

            filename = input("Search : ")

            print(files.search(folder, filename))

        elif choice == "9":

            file = input("File : ")

            print(files.size(file))

        elif choice == "10":

            print(files.current_directory())

        elif choice == "11":

            break

        else:

            print("Invalid Choice")