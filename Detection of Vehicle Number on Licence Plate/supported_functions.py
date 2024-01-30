import numpy as np
from scipy import signal as sci_signal
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import warnings
warnings.filterwarnings("ignore")



def create_templates():

    character_dict = {}

    start_letter = ord("A")
    end_letter = ord("Z") + 1

    start_number = ord("0")
    end_number = ord("9") + 1

    total_character_codes = sorted(list(range(start_letter,end_letter)) + list(range(start_number,end_number)))

    for i in total_character_codes:
        file_name = "data/" + chr(i) + ".bmp"
        image_read = cv2.imread(file_name)
        character_dict[chr(i)] = cv2.cvtColor(src=image_read,code=cv2.COLOR_BGR2GRAY)  / 255.0

    character_list = np.array(list(character_dict.values()))
    return character_list

def identify_letter(pos):
    p = ""
    if pos == 0 or pos == 1:
        p = "A"
    elif pos == 2 or pos == 3:
        p = "B"
    elif pos == 4:
        p = "C"
    elif pos == 5 or pos == 6:
        p = "D"
    elif pos == 7:
        p = "E"
    elif pos == 8:
        p = "F"
    elif pos == 9:
        p = "G"
    elif pos == 10:
        p = "H"
    elif pos == 11:
        p = "I"
    elif pos == 12:
        p = "J"
    elif pos == 13:
        p = "K"
    elif pos == 14:
        p = "L"
    elif pos == 15:
        p = "M"
    elif pos == 16:
        p = "N"
    elif pos == 17 or pos == 18:
        p = "O"
    elif pos == 19 or pos == 20:
        p = "P"
    elif pos == 21 or pos == 22:
        p = "Q"
    elif pos == 23 or pos == 24:
        p = "R"
    elif pos == 25:
        p = "S"
    elif pos == 26:
        p = "T"
    elif pos == 27:
        p = "U"
    elif pos == 28:
        p = "V"
    elif pos == 29:
        p = "W"
    elif pos == 30:
        p = "X"
    elif pos == 31:
        p = "Y"
    elif pos == 32:
        p = "Z"
    elif pos == 33:
        p = "1"
    elif pos == 34:
        p = "2"
    elif pos == 35:
        p = "3"
    elif pos == 36 or pos == 37:
        p = "4"
    elif pos == 38:
        p = "5"
    elif pos == 39 or pos == 40 or pos == 41:
        p = "6"
    elif pos == 42:
        p = "7"
    elif pos == 43 or pos == 44:
        p = "8"
    elif pos == 45 or pos == 46 or pos == 47:
        p = "9"
    else:
        p = "0"
    return pos

def detect_letters(image):
    image_resized = cv2.resize(image,(24,42))
    image_resized_grayscale = cv2.cvtColor(src=image_resized,code=cv2.COLOR_BGR2GRAY)  / 255.0
    ctr = 0
    corr_matrix_arr = []
    for i in create_templates():
        print(i.shape)
        print(image_resized_grayscale.shape)
        print()
        corr_matrix = sci_signal.correlate2d(i,image_resized_grayscale).max()
        corr_matrix_arr.append(corr_matrix)
    pos = np.argmax(corr_matrix_arr)
    det = identify_letter(pos)
    return det
#%%
