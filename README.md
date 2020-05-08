# SlackDrawing
Bots for drawing svg images in slack. Very dangerous because this does clicking all over your window and is difficult to stop once you start it. Use with caution. Command-tab quickly to get back to your terminal and press ctrl-c may be important.

Install dependencies:

```
pip -r svg.path pyautogui
```

You also may need to give terminal permission to control your mouse. 

To make the lines file from svg:

```
python3 makeLines.py input.svg output.lines
```

Feel free to change numInterp to get more or less smooth lines depending on your svg (if the value is too high the drawing may be very slow)

To make a bot draw a lines file, scaled twice as big (adjust scale according to drawing)

```
python3 drawThing.py output.lines 2.0
```

Then quickly move your mouse to the offset position (usually at the top of the screen above where you want to draw) and in two sections the drawing will start. It may require some experimentation to figure out how to get it to draw properly.

Once you find good values, it may be useful to just make a script to draw a specific thing. drawFire.py contains an example usage of this.
