

import json
import time
time.sleep(2)
from xml.dom import minidom
import sys
from svg.path import parse_path
svg_file = sys.argv[1]
print("drawing:" + svg_file)
doc = minidom.parse(svg_file)  # parseString also exists

current_milli_time = lambda: int(round(time.time() * 1000))
path_strings = [parse_path(path.getAttribute('d')) for path
                in doc.getElementsByTagName('path')]

numInterp = 60
print("parsed, writing to file: " + sys.argv[2])
f = open(sys.argv[2], "w")
for i, pathStr in enumerate(path_strings):
    curve = pathStr
    print(str(i+1) + "/" + str(len(path_strings)))
    for interp in range(0, numInterp):
        val = interp / float(numInterp-1)
        point = curve.point(val)
        x = point.real
        y = point.imag

        if interp == 0: res = (x,y, "d")
        elif interp == numInterp-1: res = (x,y, "u")
        else: res = (x,y,"n")

        f.write(str(res[0]) + "," + str(res[1]) + "," + str(res[2]) + "\r\n")
print("done")
f.close()