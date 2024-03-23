import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit
from PySide6.QtCore import QTimer
import pyautogui
from read_text import TextReader
import numpy as np


class ResizableWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Resizable Window")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowOpacity(0.8)

        # Create a text edit widget to display captured content
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Timer to periodically capture content
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.capture_content)
        self.timer.start(1000)  # Capture content every 1 second

    def capture_content(self):
        # Get window geometry
        geometry = self.geometry()
        left, top, width, height = geometry.left(), geometry.top(), geometry.width(), geometry.height()

        # Capture the content inside the window
        content = pyautogui.screenshot(region=(left, top, width, height))

        # TODO: Process the captured content (e.g., OCR)
        TextReader(np.array(content))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ResizableWindow()
    window.show()
    sys.exit(app.exec())
