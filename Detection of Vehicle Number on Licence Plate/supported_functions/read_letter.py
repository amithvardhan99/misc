import numpy as np
from scipy.signal import correlate2d
from skimage.transform import resize

def read_letter(snap):
    # Load the templates of characters into memory
    new_templates = np.load('NewTemplates.npy', allow_pickle=True)

    # Resize the input image
    snap = resize(snap, (42, 24), anti_aliasing=True)

    comp = []
    for template in new_templates:
        # Correlate the input image with every template image
        sem = correlate2d(snap, template, mode='valid')
        comp.append(np.max(sem))

    # Find the index which corresponds to the highest matched character
    vd = np.argmax(comp)

    # Assign the letter according to the index
    if 0 <= vd <= 1:
        letter = 'A'
    elif 2 <= vd <= 3:
        letter = 'B'
    elif vd == 4:
        letter = 'C'
    elif 5 <= vd <= 6:
        letter = 'D'
    elif vd == 7:
        letter = 'E'
    elif vd == 8:
        letter = 'F'
    elif vd == 9:
        letter = 'G'
    elif vd == 10:
        letter = 'H'
    elif vd == 11:
        letter = 'I'
    elif vd == 12:
        letter = 'J'
    elif vd == 13:
        letter = 'K'
    elif vd == 14:
        letter = 'L'
    elif vd == 15:
        letter = 'M'
    elif vd == 16:
        letter = 'N'
    elif 17 <= vd <= 18:
        letter = 'O'
    elif 19 <= vd <= 20:
        letter = 'P'
    elif 21 <= vd <= 22:
        letter = 'Q'
    elif 23 <= vd <= 24:
        letter = 'R'
    elif vd == 25:
        letter = 'S'
    elif vd == 26:
        letter = 'T'
    elif vd == 27:
        letter = 'U'
    elif vd == 28:
        letter = 'V'
    elif vd == 29:
        letter = 'W'
    elif vd == 30:
        letter = 'X'
    elif vd == 31:
        letter = 'Y'
    elif vd == 32:
        letter = 'Z'
    elif vd == 33:
        letter = '0'
    elif 34 <= vd <= 35:
        letter = '1'
    elif vd == 36:
        letter = '2'
    elif 37 <= vd <= 38:
        letter = '3'
    elif vd == 39:
        letter = '4'
    elif vd == 40 or 41 <= vd <= 42:
        letter = '5'
    elif vd == 43:
        letter = '6'
    elif 44 <= vd <= 45:
        letter = '8'
    elif 46 <= vd <= 48:
        letter = '9'
    else:
        letter = '0'

    return letter

# Example usage:
# result = read_letter(snap_image)
# print(result)
