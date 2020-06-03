from pynput.mouse import Button, Controller
from time import sleep

mouse = Controller()

x1 = 590; y1 = 400
x2 = 719; y2 = 400
x3 = 848; y3 = 400
x4 = 590; y4 = 525
x5 = 719; y5 = 525
x6 = 848; y6 = 525
x7 = 590; y7 = 650
x8 = 719; y8 = 650
x9 = 848; y9 = 650
x0 = 719; y0 = 775

#The code is 3986298476438073

def clickAtPoint(x, y):
    mouse.position = (x, y)
    sleep(0.005)
    mouse.click(Button.left, 1)
    sleep(0.005)
    return

print("Starting but we need to get mouse values yay")
sleep(5)
clickAtPoint(x3, y3)
clickAtPoint(x9, y9)
clickAtPoint(x8, y8)
clickAtPoint(x6, y6)
clickAtPoint(x2, y2)
clickAtPoint(x9, y9)
clickAtPoint(x8, y8)
clickAtPoint(x4, y4)
clickAtPoint(x7, y7)
clickAtPoint(x6, y6)
clickAtPoint(x4, y4)
clickAtPoint(x3, y3)
clickAtPoint(x8, y8)
clickAtPoint(x0, y0)
clickAtPoint(x7, y7)
clickAtPoint(x3, y3)
