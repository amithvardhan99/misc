from PIL import Image

A = Image.open('A.bmp')
B = Image.open('B.bmp')
C = Image.open('C.bmp')
D = Image.open('D.bmp')
E = Image.open('E.bmp')
F = Image.open('F.bmp')
G = Image.open('G.bmp')
H = Image.open('H.bmp')
I = Image.open('I.bmp')
J = Image.open('J.bmp')
K = Image.open('K.bmp')
L = Image.open('L.bmp')
M = Image.open('M.bmp')
N = Image.open('N.bmp')
O = Image.open('O.bmp')
P = Image.open('P.bmp')
Q = Image.open('Q.bmp')
R = Image.open('R.bmp')
S = Image.open('S.bmp')
T = Image.open('T.bmp')
U = Image.open('U.bmp')
V = Image.open('V.bmp')
W = Image.open('W.bmp')
X = Image.open('X.bmp')
Y = Image.open('Y.bmp')
Z = Image.open('Z.bmp')
Afill = Image.open('fillA.bmp')
Bfill = Image.open('fillB.bmp')
Dfill = Image.open('fillD.bmp')
Ofill = Image.open('fillO.bmp')
Pfill = Image.open('fillP.bmp')
Qfill = Image.open('fillQ.bmp')
Rfill = Image.open('fillR.bmp')

# Number
one = Image.open('1.bmp')
two = Image.open('2.bmp')
three = Image.open('3.bmp')
four = Image.open('4.bmp')
five = Image.open('5.bmp')
six = Image.open('6.bmp')
seven = Image.open('7.bmp')
eight = Image.open('8.bmp')
nine = Image.open('9.bmp')
zero = Image.open('0.bmp')
zerofill = Image.open('fill0.bmp')
fourfill = Image.open('fill4.bmp')
sixfill = Image.open('fill6.bmp')
sixfill2 = Image.open('fill6_2.bmp')
eightfill = Image.open('fill8.bmp')
ninefill = Image.open('fill9.bmp')
ninefill2 = Image.open('fill9_2.bmp')

# Concatenate images
letter = [A, Afill, B, Bfill, C, D, Dfill, E, F, G, H, I, J, K, L, M,
          N, O, Ofill, P, Pfill, Q, Qfill, R, Rfill, S, T, U, V, W, X, Y, Z]

number = [one, two, three, four, fourfill, five, six, sixfill, sixfill2,
          seven, eight, eightfill, nine, ninefill, ninefill2, zero, zerofill]

character = letter + number

# Save as new templates
for idx, img in enumerate(character):
    img.save(f'Template_{idx}.bmp')