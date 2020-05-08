



import pyautogui
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False
import time

import sys

import csv


def drawThing(file, scale, startPos, sleepBetween=False):
    f = open(file, "r")
    lines = [l for l in csv.reader(f) if len(l) == 3]
    f.close()
    for (x,y,changeMouse) in lines:
      xPos = float(x)*scale+startPos[0]
      yPos = float(y)*scale+startPos[1]
      pyautogui.moveTo(xPos, yPos)
      if changeMouse == "d":
          pyautogui.mouseDown()
          time.sleep(0.05)
      elif changeMouse == "u":
          pyautogui.mouseUp()
          time.sleep(0.05)
      elif sleepBetween:
          time.sleep(0.03)

if __name__ == "__main__":
    time.sleep(2)
    startPos = pyautogui.position().x, pyautogui.position().y
    file = sys.argv[1]
    scale = float(sys.argv[2])
    drawThing(file, scale, startPos)