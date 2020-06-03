#Yo mad ting
from pynput.mouse import Button, Controller
from pynput.keyboard import Key
from pynput.keyboard import Controller as keyController
from time import sleep

#This or issues
keyboard = keyController()
mouse = Controller()

#Change these accordingly 
resetx = 890; resety = 575
textx = 539; texty = 520
x = 10000

#You might be able to squeeze more time but this was as good as I could get
timeToSleepForFailSafeLol = 0.05

#So that you can go to the window
sleep(10)

#gl
while x < 99999:
    mouse.position = (textx, texty)
    sleep(timeToSleepForFailSafeLol)
    mouse.click(Button.left, 3)
    sleep(timeToSleepForFailSafeLol)
    keyboard.type("xkc-" + str(x))
    mouse.position = (resetx, resety)
    sleep(timeToSleepForFailSafeLol)
    mouse.click(Button.left, 1)
    sleep(timeToSleepForFailSafeLol)
    x += 1
    


