import numpy as np

def controlling(NR):
    # Determine the array of indices of bounding boxes of interest.
    # NR is the matrix of order numberofregions x 4.

    # Histogram of y-dimension widths of all boxes.
    Q, W = np.histogram(NR[:, 3], bins='auto')

    # Find indices from Q corresponding to frequency '6'.
    ind = np.where(Q == 6)[0]

    for k in range(len(NR)):
        # Taking the advantage of uniqueness of y-coordinate and y-width.
        C_5 = NR[:, 1] * NR[:, 3]

    # Appending a new column in NR.
    NR2 = np.column_stack((NR, C_5))

    # Histogram of the new column.
    E, R = np.histogram(NR2[:, 4], bins=20)

    # Searching for six characters.
    Y = np.where(E == 6)[0]

    if len(ind) == 1:  # If six boxes of interest are successfully found.
        MP = W[ind[0]]  # The midpoint of the corresponding bin.
        binsize = W[1] - W[0]  # Calculate the container size.
        container = [MP - (binsize / 2), MP + (binsize / 2)]  # Calculate the complete container size.
        r = takeboxes(NR, container, 2)

    elif len(Y) == 1:
        MP = R[Y[0]]
        binsize = R[1] - R[0]
        container = [MP - (binsize / 2), MP + (binsize / 2)]  # Calculate the complete container size.
        r = takeboxes(NR2, container, 2.5)  # Call to function takeboxes.

    elif not ind or len(ind) > 1:  # If there is no value of '6' in the Q vector.
        A, B = np.histogram(NR[:, 1], bins=20)  # Use y-coordinate approach only.
        ind2 = np.where(A == 6)[0]

        if len(ind2) == 1:
            MP = B[ind2[0]]
            binsize = B[1] - B[0]
            container = [MP - (binsize / 2), MP + (binsize / 2)]  # Calculate the complete container size.
            r = takeboxes(NR, container, 1)

        else:
            # Call of function guessthesix.
            container = guessthesix(A, B, (B[1] - B[0]))

            if container:
                r = takeboxes(NR, container, 1)  # Call the function takeboxes.

            else:
                # Call of function guessthesix.
                container2 = guessthesix(E, R, (R[1] - R[0]))

                if container2:
                    r = takeboxes(NR2, container2, 2.5)

                else:
                    r = []  # Otherwise assign an empty list to 'r'.

    return r

# Function takeboxes() and guessthesix() would need to be implemented separately based on their functionality.
