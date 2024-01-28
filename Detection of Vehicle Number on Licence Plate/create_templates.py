from PIL import Image
import numpy as np

# Function to read images
def read_image(file_path):
    return np.array(Image.open(file_path).convert('L'))

# Letter


# Resize function
def resize_image(image, target_height):
    current_height = image.shape[0]
    ratio = target_height / current_height
    return np.array(Image.fromarray(image).resize((int(image.shape[1] * ratio), target_height)))

# Function to read images with resizing
def read_resized_image(file_path, target_height):
    return resize_image(np.array(Image.open(file_path).convert('L')), target_height)

# Letter
def create_templates():

    path_full = "Character Images\\"
    A = read_image(path_full+'A.bmp')
    B = read_image(path_full+'B.bmp')
    C = read_image(path_full+'C.bmp')
    D = read_image(path_full+'D.bmp')
    E = read_image(path_full+'E.bmp')
    F = read_image(path_full+'F.bmp')
    G = read_image(path_full+'G.bmp')
    H = read_image(path_full+'H.bmp')
    I = read_image(path_full+'I.bmp')
    J = read_image(path_full+'J.bmp')
    K = read_image(path_full+'K.bmp')
    L = read_image(path_full+'L.bmp')
    M = read_image(path_full+'M.bmp')
    N = read_image(path_full+'N.bmp')
    O = read_image(path_full+'O.bmp')
    P = read_image(path_full+'P.bmp')
    Q = read_image(path_full+'Q.bmp')
    R = read_image(path_full+'R.bmp')
    S = read_image(path_full+'S.bmp')
    T = read_image(path_full+'T.bmp')
    U = read_image(path_full+'U.bmp')
    V = read_image(path_full+'V.bmp')
    W = read_image(path_full+'W.bmp')
    X = read_image(path_full+'X.bmp')
    Y = read_image(path_full+'Y.bmp')
    Z = read_image(path_full+'Z.bmp')
    Afill = read_image(path_full+'fillA.bmp')
    Bfill = read_image(path_full+'fillB.bmp')
    Dfill = read_image(path_full+'fillD.bmp')
    Ofill = read_image(path_full+'fillO.bmp')
    Pfill = read_image(path_full+'fillP.bmp')
    Qfill = read_image(path_full+'fillQ.bmp')
    Rfill = read_image(path_full+'fillR.bmp')

    # Number
    one = read_image(path_full+'1.bmp')
    two = read_image(path_full+'2.bmp')
    three = read_image(path_full+'3.bmp')
    four = read_image(path_full+'4.bmp')
    five = read_image(path_full+'5.bmp')
    six = read_image(path_full+'6.bmp')
    seven = read_image(path_full+'7.bmp')
    eight = read_image(path_full+'8.bmp')
    nine = read_image(path_full+'9.bmp')
    zero = read_image(path_full+'0.bmp')
    zerofill = read_image(path_full+'fill0.bmp')
    fourfill = read_image(path_full+'fill4.bmp')
    sixfill = read_image(path_full+'fill6.bmp')
    sixfill2 = read_image(path_full+'fill6_2.bmp')
    eightfill = read_image(path_full+'fill8.bmp')
    ninefill = read_image(path_full+'fill9.bmp')
    ninefill2 = read_image(path_full+'fill9_2.bmp')

    # Combine letters and numbers
    letter = [A, Afill, B, Bfill, C, D, Dfill, E, F, G, H, I, J, K, L, M,
              N, O, Ofill, P, Pfill, Q, Qfill, R, Rfill, S, T, U, V, W, X, Y, Z]

    number = [one, two, three, four, fourfill, five,
              six, sixfill, sixfill2, seven, eight, eightfill, nine, ninefill, ninefill2, zero, zerofill]

    # Resize images to have the same number of rows
    target_height = max(max(img.shape[0] for img in letter), max(img.shape[0] for img in number))
    letter_resized = [resize_image(img, target_height) for img in letter]
    number_resized = [resize_image(img, target_height) for img in number]

    # Concatenate resized arrays
    character = np.concatenate((letter_resized, number_resized), axis=1)

    # Reshape to create templates
    NewTemplates = np.split(character, 42, axis=1)

    # Save templates
    np.savez('NewTemplates', *NewTemplates)

# Call the function
create_templates()

