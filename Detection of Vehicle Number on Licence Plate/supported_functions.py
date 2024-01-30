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

    total_character_codes = list(range(start_number,end_number)) + list(range(start_letter,end_letter))

    for i in total_character_codes:
        file_name = "data/" + chr(i) + ".bmp"
        image_read = cv2.imread(file_name)
        character_dict[chr(i)] = cv2.cvtColor(src=image_read,code=cv2.COLOR_BGR2GRAY) / 255.0

    character_list = np.array(list(character_dict.values()))
    return character_list


def detect_letters(image):
    image_resized = cv2.resize(image,(24,42))
    image_resized_grayscale = cv2.cvtColor(src=image_resized,code=cv2.COLOR_BGR2GRAY)  / 255.0
    ctr = 0
    corr_matrix_arr = []
    for i in create_templates():
        corr_matrix = sci_signal.correlate2d(i,image_resized_grayscale).max()
        corr_matrix_arr.append(corr_matrix)
    pos = np.argmax(corr_matrix_arr)
    if pos < 10:
        det = str(pos)
    else:
        det = chr(55 + pos)
    return det
#%%
