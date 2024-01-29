import numpy as np
import pandas as pd
from PIL import Image

def identify_characters(full_path):

    input_images = {}

    begin = ord("A")
    end = ord("Z") + 1
    for i in range(begin,end):
        input_images[chr(i)] = np.array(Image.open(full_path + chr(i) + ".bmp"))

    begin = ord("0")
    end = ord("9") + 1
    for i in range(begin,end):
        input_images[chr(i)] = np.array(Image.open(full_path + chr(i) + ".bmp"))

    characters = np.array(list(input_images.values()))
    return characters