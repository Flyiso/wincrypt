import pytesseract as pt
import numpy as np
import cv2


class TextReader:
    def __init__(self, frame) -> None:
        self.frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        self.read_content()

    def read_content(self):
        """
        Prints the text detected on frame
        """
        text = pt.image_to_string(self.frame)
        print(text)