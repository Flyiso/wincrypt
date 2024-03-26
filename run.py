import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QPen
import mss
import mss.tools


class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Transparent Window")
        self.setGeometry(100, 100, 400, 200)
        
        # Make the window transparent
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.button = QPushButton("Capture", self)
        self.button.resize(120, 30)
        self.button.clicked.connect(self.capture_screen)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
        
        # Calculate the transparent area rectangle
        transparent_rect = QRect(0, 0, self.width() * 4 / 5, self.height())
        
        # Fill the transparent area with a transparent color
        painter.fillRect(transparent_rect, Qt.transparent)
        
        # Calculate the opaque area rectangle
        opaque_rect = QRect(self.width() * 4 / 5, 0, self.width() * 1 / 5, self.height())
        
        # Fill the opaque area with white color
        painter.fillRect(opaque_rect, Qt.white)
        
        # Adjust button position to fit within the opaque area
        button_x = self.width() * 4 / 5 + (self.width() * 1 / 5 - self.button.width()) // 2
        button_y = (self.height() - self.button.height()) // 2
        self.button.move(button_x, button_y)
        
    def capture_screen(self):
        print("Capture button clicked")
        # Capture the screen
        with mss.mss() as sct:
            monitor = {"top": self.geometry().top(), "left": self.geometry().left(), "width": int(self.width() * 4 / 5), "height": int(self.height())}  
            sct_img = sct.grab(monitor)
        
        # Save the image directly
        mss.tools.to_png(sct_img.rgb, sct_img.size, output="captured_image.png")
        print("Image saved")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    sys.exit(app.exec())
