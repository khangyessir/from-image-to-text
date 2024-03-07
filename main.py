from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget
from PIL import Image
from pytesseract import pytesseract
import enum
import sys

class OS(enum.Enum):
    Mac = 0
    Windows = 1

class ImageReader:
    def __init__(self, os: OS):
        if os == OS.Mac:
            print('Running on Mac\n')
        if os == OS.Windows:
            windows_path = r'D:\pyproject\tesseract.exe'
            pytesseract.tesseract_cmd = windows_path
            print('Running on : WINDOWS\n')

    def extract_text(self, image: str, lang: str) -> str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang)
        return extracted_text

class FileDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png)", options=options)
        if fileName:
            ir = ImageReader(OS.Windows)  # Adjust this according to your OS
            text = ir.extract_text(fileName, lang='eng')  # Change 'eng' to the desired language
            print(text)
            sys.exit(0)
        else:
            sys.exit(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileDialog()
    sys.exit(app.exec_())
