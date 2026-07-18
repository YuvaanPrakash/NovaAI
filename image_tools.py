"""
image_tools.py

Image Processing Module
Nova AI
"""

from PIL import Image
import cv2
import os


class ImageTools:

    def __init__(self):

        self.reader = easyocr.Reader(['en'], gpu=False)

    # -----------------------------------
    # Image Information
    # -----------------------------------

    def info(self, image_path):

        try:

            img = Image.open(image_path)

            return f"""
Image Information
-----------------
File : {os.path.basename(image_path)}
Format : {img.format}
Width : {img.width}
Height : {img.height}
Mode : {img.mode}
"""

        except Exception as e:

            return f"Error: {e}"

    # -----------------------------------
    # Resize Image
    # -----------------------------------

    def resize(self, image_path, width, height, output):

        try:

            img = Image.open(image_path)

            img = img.resize((width, height))

            img.save(output)

            return f"Saved as {output}"

        except Exception as e:

            return f"Error: {e}"

    # -----------------------------------
    # Convert Image Format
    # -----------------------------------

    def convert(self, image_path, output):

        try:

            img = Image.open(image_path)

            img.save(output)

            return f"Converted to {output}"

        except Exception as e:

            return f"Error: {e}"

    # -----------------------------------
    # Rotate Image
    # -----------------------------------

    def rotate(self, image_path, angle, output):

        try:

            img = Image.open(image_path)

            img = img.rotate(angle, expand=True)

            img.save(output)

            return "Rotation Complete."

        except Exception as e:

            return f"Error: {e}"

    # -----------------------------------
    # Grayscale
    # -----------------------------------

    def grayscale(self, image_path, output):

        try:

            img = Image.open(image_path)

            img = img.convert("L")

            img.save(output)

            return "Grayscale Image Saved."

        except Exception as e:

            return f"Error: {e}"

    # -----------------------------------
    # Read Text (OCR)
    # -----------------------------------

    def read_text(self, image_path):

        try:

            result = self.reader.readtext(image_path)

            if not result:

                return "No text found."

            text = ""

            for item in result:

                text += item[1] + "\n"

            return text

        except Exception as e:

            return f"Error: {e}"

    # -----------------------------------
    # Face Detection
    # -----------------------------------

    def detect_faces(self, image_path):

        try:

            cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades +
                "haarcascade_frontalface_default.xml"
            )

            image = cv2.imread(image_path)

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faces = cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5
            )

            return f"Faces Detected : {len(faces)}"

        except Exception as e:

            return f"Error: {e}"


image_tools = ImageTools()


if __name__ == "__main__":

    while True:

        print("\n======= IMAGE TOOLS =======")

        print("1. Image Info")
        print("2. Resize")
        print("3. Convert")
        print("4. Rotate")
        print("5. Grayscale")
        print("6. OCR")
        print("7. Detect Faces")
        print("8. Exit")

        choice = input("\nChoice : ")

        if choice == "1":

            path = input("Image : ")

            print(image_tools.info(path))

        elif choice == "2":

            path = input("Image : ")

            w = int(input("Width : "))

            h = int(input("Height : "))

            out = input("Output : ")

            print(image_tools.resize(path, w, h, out))

        elif choice == "3":

            path = input("Image : ")

            out = input("Output : ")

            print(image_tools.convert(path, out))

        elif choice == "4":

            path = input("Image : ")

            angle = float(input("Angle : "))

            out = input("Output : ")

            print(image_tools.rotate(path, angle, out))

        elif choice == "5":

            path = input("Image : ")

            out = input("Output : ")

            print(image_tools.grayscale(path, out))

        elif choice == "6":

            path = input("Image : ")

            print(image_tools.read_text(path))

        elif choice == "7":

            path = input("Image : ")

            print(image_tools.detect_faces(path))

        elif choice == "8":

            break

        else:

            print("Invalid Choice")