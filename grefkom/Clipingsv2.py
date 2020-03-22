from graphics import *
import math

# Fungsi untuk mendapatkan titik hasil refleksi

def jrkTitik(x,y, A, B, C):
    # D adalah jarak dari garis cermin
    D = A * x + B * y + C
    return Point(x-2*A*D, y-2*B*D)

# Defining region codes 
INSIDE = 0  #0000 
LEFT = 1    #0001 
RIGHT = 2   #0010 
BOTTOM = 4  #0100 
TOP = 8     #1000 
  
# Function to compute region code for a point(x,y) 
def computeCode(x, y, x_min, y_min, x_max, y_max): 
    code = INSIDE 
    if x < x_min:      # to the left of rectangle 
        code |= LEFT 
    elif x > x_max:    # to the right of rectangle 
        code |= RIGHT 
    if y < y_min:      # below the rectangle 
        code |= BOTTOM 
    elif y > y_max:    # above the rectangle 
        code |= TOP 
  
    return code  
  
# Implementing Cohen-Sutherland algorithm 
# Clipping a line from P1 = (x1, y1) to P2 = (x2, y2) 
def cohenSutherlandClip(x1, y1, x2, y2, x_min, y_min, x_max, y_max): 
  
    # Compute region codes for P1, P2 
    code1 = computeCode(x1, y1, x_min, y_min, x_max, y_max) 
    code2 = computeCode(x2, y2, x_min, y_min, x_max, y_max) 
    accept = False
  
    while True: 
  
        # If both endpoints lie within rectangle 
        if code1 == 0 and code2 == 0: 
            accept = True
            break
  
        # If both endpoints are outside rectangle 
        elif (code1 & code2) != 0: 
            break
  
        # Some segment lies within the rectangle 
        else: 
  
            # Line Needs clipping 
            # At least one of the points is outside,  
            # select it 
            x = 1.0
            y = 1.0
            if code1 != 0: 
                code_out = code1 
            else: 
                code_out = code2 
  
            # Find intersection point 
            # using formulas y = y1 + slope * (x - x1),  
            # x = x1 + (1 / slope) * (y - y1) 
            if code_out & TOP:  
                # point is above the clip rectangle 
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1) 
                y = y_max 
  
            elif code_out & BOTTOM: 
                  
                # point is below the clip rectangle 
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1) 
                y = y_min 
  
            elif code_out & RIGHT: 
                  
                # point is to the right of the clip rectangle 
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1) 
                x = x_max 
  
            elif code_out & LEFT: 
                # point is to the left of the clip rectangle 
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1) 
                x = x_min 
  
            # Now intersection point x,y is found 
            # We replace point outside clipping rectangle 
            # by intersection point 
            if code_out == code1: 
                x1 = x 
                y1 = y 
                code1 = computeCode(x1, y1, x_min, y_min, x_max, y_max)
  
            else: 
                x2 = x 
                y2 = y 
                code2 = computeCode(x2, y2, x_min, y_min, x_max, y_max) 
  
    if accept: 
         line = Line(Point(x1,y1), Point(x2,y2))
         line.draw(win)
  
        # Here the user can add code to display the rectangle 
        # along with the accepted (portion of) lines  
  
# Ganti untuk menyesuaikan ukuran window/canvas
WinX = 800
WinY = 600

# Membuat window
win = GraphWin("Fadhlan Pasyah A F - 18/42776/PA/18536", WinX, WinY, autoflush=False)

# Ganti untuk menyesuaikan lokasi segitiga pertama
x1 = 100
y1 = 100

x2 = 150
y2 = 200

x3 = 200
y3 = 150

# Menggambar segitiga pertama
p1 = Point(x1,y1)
p2 = Point(x2,y2)
p3 = Point(x3,y3)
line = Line(p1,p2)
line.draw(win)
line = Line(p2,p3)
line.draw(win)
line = Line(p1,p3)
line.draw(win)

# Defining x_max,y_max and x_min,y_min for rectangle 
# Since diagonal points are enough to define a rectangle 
box1 = win.getMouse()
box1.draw(win)
box2 = win.getMouse()
box2.draw(win)

for item in win.items[:]:
    item.undraw()
win.update()

rect = Rectangle(box1, box2)
rect.draw(win)

a = box1.getX()
b = box2.getX()
if(a>b):
    x_max = a
    x_min = b
else:
    x_max = b
    x_min = a

a = box1.getY()
b = box2.getY()
if(a>b):
    y_max = a
    y_min = b
else:
    y_max = b
    y_min = a

#Sutherland segitiga pertama
cohenSutherlandClip(p1.getX(), p1.getY(), p2.getX(), p2.getY(), x_min, y_min, x_max, y_max)
cohenSutherlandClip(p2.getX(), p2.getY(), p3.getX(), p3.getY(), x_min, y_min, x_max, y_max)
cohenSutherlandClip(p1.getX(), p1.getY(), p3.getX(), p3.getY(), x_min, y_min, x_max, y_max)

# Mendapatkan input mouse sebagai garis cermin
in1 = win.getMouse()
in1.draw(win)
mx1 = int(in1.getX())
my1 = int(in1.getY())
in2 = win.getMouse()
in2.draw(win)
mx2 = int(in2.getX())
my2 = int(in2.getY())
line = Line(in1,in2)
line.draw(win)


# vektor dari cermin
A = my2 - my1
B = -(mx2 - mx1)
C = -A * mx1 - B * my1

M = math.sqrt(A*A + B*B)

Aa = A / M
Ba = B / M
Ca = C / M

# Driver Script 
# First Line segment 
# P11 = (5, 5), P12 = (7, 7)

# jarak dari tiga titik segitiga pertama
# dan mencari point pada arah berlawanan garis cermin
D1 = jrkTitik(x1,y1,Aa,Ba,Ca)
D2 = jrkTitik(x2,y2,Aa,Ba,Ca)
D3 = jrkTitik(x3,y3,Aa,Ba,Ca)
# duh = Line(D1,D2)
# duh2 = Line(D1,D3)
# duh3= Line(D2,D3)
# duh.draw(win)
# duh2.draw(win)
# duh3.draw(win)

#Menggambar garis hasil clipping
cohenSutherlandClip(D1.getX(), D1.getY(), D2.getX(), D2.getY(), x_min, y_min, x_max, y_max)   
cohenSutherlandClip(D2.getX(), D2.getY(), D3.getX(), D3.getY(), x_min, y_min, x_max, y_max) 
cohenSutherlandClip(D1.getX(), D1.getY(), D3.getX(), D3.getY(), x_min, y_min, x_max, y_max)

# Menggambar segitiga hasil cermin

win.getMouse()
win.getMouse()
win.close()