from tkinter import image_types
import cv2 as cv
from pytesseract import pytesseract
import pyautogui

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def img_read_text(target_image_path, word):
    words_in_image = pytesseract.image_to_string(target_image_path)
    if word in words_in_image:
        d = pytesseract.image_to_data(target_image_path, output_type=pytesseract.Output.DICT)
        decline_idx = d['text'].index(word)
        if not decline_idx:
            raise Exception("word not found")
        (x, y) = (d['left'][decline_idx], d['top'][decline_idx])
        return True

    else:
        pass




img_read_text("accept.png")

