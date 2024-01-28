import numpy as np
from scipy.ndimage import label, find_objects
from skimage.measure import regionprops
from skimage.transform import resize


def controlling(NR):
    Q, W = np.histogram(NR[:, 3], bins='auto')
    ind = np.where(Q == 6)[0]

    C_5 = NR[:, 1] * NR[:, 3]
    NR2 = np.column_stack((NR, C_5))

    E, R = np.histogram(NR2[:, 4], bins=20)
    Y = np.where(E == 6)[0]

    if len(ind) == 1:
        MP = W[ind][0]
        binsize = W[1] - W[0]
        container = [MP - (binsize / 2), MP + (binsize / 2)]
        r = takeboxes(NR, container, 2)
    elif len(Y) == 1:
        MP = R[Y][0]
        binsize = R[1] - R[0]
        container = [MP - (binsize / 2), MP + (binsize / 2)]
        r = takeboxes(NR2, container, 2.5)
    elif len(ind) != 1 or len(ind) > 1:
        A, B = np.histogram(NR[:, 1], bins=20)
        ind2 = np.where(A == 6)[0]
        if len(ind2) == 1:
            MP = B[ind2][0]
            binsize = B[1] - B[0]
            container = [MP - (binsize / 2), MP + (binsize / 2)]
            r = takeboxes(NR, container, 1)
        else:
            container = guessthesix(A, B, (B[1] - B[0]))
            if container:
                r = takeboxes(NR, container, 1)
            elif not container:
                container2 = guessthesix(E, R, (R[1] - R[0]))
                if container2:
                    r = takeboxes(NR2, container2, 2.5)
                else:
                    r = []
    return r

def guessthesix(Q, W, bsize):
    for l in range(5, 1, -1):
        val = np.where(Q == l)[0]
        var = len(val)
        if not var or var == 1:
            index = val[0] + 1 if val[0] == 0 else val[0]
            if index == len(Q):
                index = None
            if Q[index] + Q[index + 1] == 6:
                container = [W[index] - (bsize / 2), W[index + 1] + (bsize / 2)]
                break
            elif Q[index] + Q[index - 1] == 6:
                container = [W[index - 1] - (bsize / 2), W[index] + (bsize / 2)]
                break
        else:
            for k in range(var):
                index = val[k] + 1 if val[k] == 0 else val[k]
                if index == len(Q):
                    index = None
                if Q[index] + Q[index + 1] == 6:
                    container = [W[index] - (bsize / 2), W[index + 1] + (bsize / 2)]
                    break
                elif Q[index] + Q[index - 1] == 6:
                    container = [W[index - 1] - (bsize / 2), W[index] + (bsize / 2)]
                    break
            if k != var:
                break
    else:
        container = []
    return container

def read_letter(snap):
    new_templates = np.load('NewTemplates.npy', allow_pickle=True)
    snap = resize(snap, (42, 24))
    comp = []

    for template in new_templates:
        sem = np.corrcoef(template, snap)[0, 1]
        comp.append(sem)

    vd = np.argmax(comp)

    if 0 <= vd <= 33:
        letter = chr(ord('A') + vd)
    elif 34 <= vd <= 48:
        letter = str(vd - 33)
    else:
        letter = '0'

    return letter


def take_boxes(NR, container, chk):
    takethisbox = []

    for i in range(NR.shape[0]):
        if NR[i, (2 * chk)] >= container[0] and NR[i, (2 * chk)] <= container[1]:
            takethisbox.append(NR[i, :])

    takethisbox = np.array(takethisbox)
    r = []

    for k in range(takethisbox.shape[0]):
        var = np.where(takethisbox[k, 0] == NR[:, 0])[0]
        if len(var) == 1:
            r.append(var[0])
        else:
            M = np.array([NR[val, (2 * chk)] >= container[0] and NR[val, (2 * chk)] <= container[1] for val in var])
            var = var[M]
            r.extend(var.tolist())

    return r
