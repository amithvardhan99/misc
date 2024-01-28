import numpy as np
from scipy.ndimage import label
from scipy.stats import itemfreq
from skimage.measure import regionprops
from scipy.signal import find_peaks

def controlling(NR):
    Q, W = np.histogram(NR[:, 3], bins='auto')  # Histogram of the y-dimension widths of all boxes.
    ind = np.where(Q == 6)[0]  # Find indices from Q corresponding to frequency '6'.

    C_5 = NR[:, 1] * NR[:, 3]  # Taking the advantage of uniqueness of y-coordinate and y-width.
    NR2 = np.column_stack((NR, C_5))  # Appending new column in NR.

    E, R = np.histogram(NR2[:, 4], bins=20)
    Y = np.where(E == 6)[0]  # Searching for six characters.

    if len(ind) == 1:  # If six boxes of interest are successfully found, record the midpoint of the corresponding bin.
        MP = W[ind][0]
        binsize = W[1] - W[0]
        container = [MP - (binsize / 2), MP + (binsize / 2)]  # Calculating the complete container size.
        r = take_boxes(NR, container, 2)
    elif len(Y) == 1:
        MP = R[Y][0]
        binsize = R[1] - R[0]
        container = [MP - (binsize / 2), MP + (binsize / 2)]  # Calculating the complete container size.
        r = take_boxes(NR2, container, 2.5)  # Call to function take_boxes.
    elif not ind or len(ind) > 1:  # If there is no value of '6' in the Q vector.
        A, B = np.histogram(NR[:, 1], bins=20)  # Use y-coordinate approach only.
        ind2 = np.where(A == 6)[0]
        if len(ind2) == 1:
            MP = B[ind2][0]
            binsize = B[1] - B[0]
            container = [MP - (binsize / 2), MP + (binsize / 2)]  # Calculating the complete container size.
            r = take_boxes(NR, container, 1)
        else:
            container = guess_the_six(A, B, (B[1] - B[0]))  # Call of function guess_the_six.
            if container:
                r = take_boxes(NR, container, 1)  # Call the function take_boxes.
            else:
                container2 = guess_the_six(E, R, (R[1] - R[0]))
                if container2:
                    r = take_boxes(NR2, container2, 2.5)
                else:
                    r = []  # Otherwise assign an empty matrix to 'r'.
    return r

def guess_the_six(Q, W, bsize):
    for l in range(5, 1, -1):  # This condition has to be changed accordingly if number plates are other than six characters.
        val = np.where(Q == l)[0]  # Find the indices corresponding to the value of frequency equals 'l'.
        var = len(val)  # Check how many indices are found.
        if not var or var == 1:  # If no index or one index is found.
            if var == 1:
                index = val[0] + 1  # Since zero index is not allowed in NumPy.
            else:
                index = val[0]  # Assign that value to 'index'.
            if len(Q) == val[0]:  # In case if the last index value is reached,
                index = None  # then index+1 will be out of Q.
            if Q[index] + Q[index + 1] == 6:  # If the sum of frequencies with the subsequent bin equals six.
                container = [W[index] - (bsize / 2), W[index + 1] + (bsize / 2)]  # Calculate container and break looping
                break  # for more values.
            elif Q[index] + Q[index - 1] == 6:  # If the sum of frequencies with the previous bin equals six.
                container = [W[index - 1] - (bsize / 2), W[index] + (bsize / 2)]  # Calculate container and break looping
                break  # for more values.
        else:  # If more than one index is found.
            M = np.zeros(var, dtype=bool)
            for k in range(var):  # Repeat the analysis for every value of the bin and checks for the same condition
                if val[k] == 0:
                    index = val[k] + 1  # Since zero index is not allowed in NumPy.
                else:
                    index = val[k]  # that where the sum of frequencies equals six.
                if len(Q) == val[k]:  # In case if the last index value is reached,
                    index = None  # then index+1 will be out of Q.
                if Q[index] + Q[index + 1] == 6:
                    container = [W[index] - (bsize / 2), W[index + 1] + (bsize / 2)]  # Calculate the value of container and break.
                    M[k] = True
                    break
                elif Q[index] + Q[index - 1] == 6:
                    container = [W[index - 1] - (bsize / 2), W[index] + (bsize / 2)]
                    M[k] = True
                    break
            if not np.all(M):  # If for any value of index bins frequencies sum to six then just break.
                break
    else:
        container = None  # If looping is done and no frequencies sum to six then assign container the empty matrix.
    return container

def read_letter(snap, templates):
    snap = np.resize(snap, (42, 24))  # Resize the input image so it can be compared with the template's images.
    comp = []
    for template in templates:
        sem = np.corrcoef(template.flatten(), snap.flatten())[0, 1]  # Correlation the input image with every image in the template for best matching.
        comp.append(sem)  # Record the value of correlation for each template's character.
    vd = np.argmax(comp) + 1  # Find the index which corresponds to the highest matched character.

    # According to the index assign to 'letter'.
    if 1 <= vd <= 2:
        letter = 'A'
    elif 3 <= vd <= 4:
        letter = 'B'
    elif vd == 5:
        letter = 'C'
    elif 6 <= vd <= 7:
        letter = 'D'
    elif vd == 8:
        letter = 'E'
    elif vd == 9:
        letter = 'F'
    elif vd == 10:
        letter = 'G'
    elif vd == 11:
        letter = 'H'
    elif vd == 12:
        letter = 'I'
    elif vd == 13:
        letter = 'J'
    elif vd == 14:
        letter = 'K'
    elif vd == 15:
        letter = 'L'
    elif vd == 16:
        letter = 'M'
    elif vd == 17:
        letter = 'N'
    elif 18 <= vd <= 19:
        letter = 'O'
    elif 20 <= vd <= 21:
        letter = 'P'
    elif 22 <= vd <= 23:
        letter = 'Q'
    elif 24 <= vd <= 25:
        letter = 'R'
    elif vd == 26:
        letter = 'S'
    elif vd == 27:
        letter = 'T'
    elif vd == 28:
        letter = 'U'
    elif vd == 29:
        letter = 'V'
    elif vd == 30:
        letter = 'W'
    elif vd == 31:
        letter = 'X'
    elif vd == 32:
        letter = 'Y'
    elif vd == 33:
        letter = 'Z'
    # Numerals listings.
    elif vd == 34:
        letter = '1'
    elif vd == 35:
        letter = '2'
    elif vd == 36:
        letter = '3'
    elif 37 <= vd <= 38:
        letter = '4'
    elif vd == 39:
        letter = '5'
    elif 40 <= vd <= 42:
        letter = '6'
    elif vd == 43:
        letter = '7'
    elif 44 <= vd <= 45:
        letter = '8'
    elif 46 <= vd <= 48:
        letter = '9'
    else:
        letter = '0'

    return letter

def take_boxes(NR, container, chk):
    # Helps in determining the values of indices of interested Bounding boxes.
    takethisbox = []  # Initialize the variable to an empty matrix.
    for i in range(NR.shape[0]):
        if container[0] <= NR[i, 2 * chk] <= container[1]:  # If Bounding box is among the container plus tolerance.
            takethisbox.append(NR[i, :])  # Take that box and concatenate along the first dimension.

    r = []
    for k in range(len(takethisbox)):
        var = np.where(takethisbox[k, 0] == NR[:, 0])[0]  # Finding the indices of the interested boxes among NR
        if len(var) == 1:  # since x-coordinate of the boxes will be unique.
            r.append(var[0])
        else:  # In case if x-coordinate is not unique
            M = [NR[var[v], 2 * chk] >= container[0] and NR[var[v], 2 * chk] <= container[1] for v in range(len(var))]
            var = np.array(var)[M]
            r.extend(var)

    return r


