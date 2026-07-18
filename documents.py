"""
documents.py

Document Reader Module
Nova AI
"""

import os
import pandas as pd
from PyPDF2 import PdfReader
from docx import Document


class Documents:

    # ---------------------------------------
    # Read PDF
    # ---------------------------------------

    def read_pdf(self, file):

        try:

            pdf = PdfReader(file)

            text = ""

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text + "\n"

            return text if text else "No text found."

        except Exception as e:

            return f"Error : {e}"

    # ---------------------------------------
    # Read DOCX
    # ---------------------------------------

    def read_docx(self, file):

        try:

            document = Document(file)

            text = ""

            for para in document.paragraphs:

                text += para.text + "\n"

            return text if text else "No text found."

        except Exception as e:

            return f"Error : {e}"

    # ---------------------------------------
    # Read TXT
    # ---------------------------------------

    def read_txt(self, file):

        try:

            with open(file, "r", encoding="utf-8") as f:

                return f.read()

        except Exception as e:

            return f"Error : {e}"

    # ---------------------------------------
    # Read CSV
    # ---------------------------------------

    def read_csv(self, file):

        try:

            data = pd.read_csv(file)

            return data.to_string(index=False)

        except Exception as e:

            return f"Error : {e}"

    # ---------------------------------------
    # Read Excel
    # ---------------------------------------

    def read_excel(self, file):

        try:

            data = pd.read_excel(file)

            return data.to_string(index=False)

        except Exception as e:

            return f"Error : {e}"

    # ---------------------------------------
    # File Information
    # ---------------------------------------

    def file_info(self, file):

        try:

            size = os.path.getsize(file)

            extension = os.path.splitext(file)[1]

            return f"""
File : {os.path.basename(file)}

Extension : {extension}

Size : {size} Bytes
"""

        except Exception as e:

            return f"Error : {e}"

    # ---------------------------------------
    # Count Words
    # ---------------------------------------

    def word_count(self, text):

        return len(text.split())

    # ---------------------------------------
    # Count Characters
    # ---------------------------------------

    def character_count(self, text):

        return len(text)


documents = Documents()


# ---------------------------------------
# Testing
# ---------------------------------------

if __name__ == "__main__":

    while True:

        print("\n========= DOCUMENTS =========")

        print("1. Read PDF")

        print("2. Read DOCX")

        print("3. Read TXT")

        print("4. Read CSV")

        print("5. Read Excel")

        print("6. File Info")

        print("7. Exit")

        choice = input("\nChoice : ")

        if choice == "1":

            file = input("PDF File : ")

            print(documents.read_pdf(file))

        elif choice == "2":

            file = input("DOCX File : ")

            print(documents.read_docx(file))

        elif choice == "3":

            file = input("TXT File : ")

            print(documents.read_txt(file))

        elif choice == "4":

            file = input("CSV File : ")

            print(documents.read_csv(file))

        elif choice == "5":

            file = input("Excel File : ")

            print(documents.read_excel(file))

        elif choice == "6":

            file = input("File : ")

            print(documents.file_info(file))

        elif choice == "7":

            break

        else:

            print("Invalid Choice")