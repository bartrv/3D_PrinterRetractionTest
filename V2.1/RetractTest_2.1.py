# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:15:43 2022

@author: bvoigt
"""

import os
#import copy
"""
***DEV Notes for Text Markings***
Use a displacement function: X,Y,Z
    Perhaps integrate E, F as well so one function controlls all displacement and modifiers
    XYZ 1st, then explore others...

SPD and DST letters to be incorporated into new BASE gcode file
Numbers: 
    Origin point for offset: X,Y,Z = 0,0,0
    Increment: 2.0mm (X)
    Z Target = +0.5mm (0.57 mm) = 1st layer of collumns
    Locations...
    location of base 0 = 30,30,0.15 (offsets = 0,0,0)
    4 digits for each value: Speed Min/max expected = 000 / 150 (Integers only), Dist Min/Max = 0.00 / 3.00
    Formatting:     DST(1-3)     0.00 0.00 0.00
                    SPD               000
                    DST(2-6)     0.00 0.00 0.00
    At Location 0, change from offset point (0,0,0): SPD [[-2,0,.57],[-0,0,.57],[2,0,.57]]
                                                     DST [[[-10,3.5,.57],[-8.75,3.5,.57],[-7.5,3.5,.57],[-5.5,3.5,.57]],
                                                          [[2.25,3.5,.57],[],[],[]] All Offset:  7.75, 0, 0
                                                          [[5.5,3.5,.57],[],[],[]]  All Offset: 15.50, 0, 0
                                                          [[-10,-3.5,.57],[],[],[]] All Offset:     0,-7, 0
                                                          [[2.25,-3.5,.57],[],[],[]]All Offset:  7.75,-7, 0
                                                          [[5.5,-3.5,.57],[],[],[]]]All Offset: 15.50,-7, 0
                                                     
    At Location 0, Real Coordinates referance Point: SPD [[28,28.625,.57],[30,28.625,.57],[32,28.625,.57]]
                                                     DST [[[20,27.88.12,.57],[21.25,27.88,.57],[22.5,27.88,.57],[24.5,27.88,.57]],
"""

#Define Variables and constants
nozzleTemp = 215
bedTemp = 60
FanSpeed = 255
custom_K_Value = 0
layerCount=6
L1Start = .57 #mm
default_Speed = 25 #mm/s
default_FSpd = default_Speed*60
ColSectionOffset = 5.18 #mm
FirstLayerHeight = ""
gCode_Path = "H:/ClientProjects/VC_GeneralTests/_3DPrint/_Prusa_MK3S_PrinterMaintenance/CalibrationModels/_Custom/"
gCodeBaseFile = gCode_Path+"CustomRetract_app_v2_BASE.gcode"
gCodeColmnFile = gCode_Path+"CustomRetract_app_v2_ColsL1.gcode"
gCodeToWriteOut = []
gCode_base = []
gCode_columnSet = []
gcode_RAWbuild = []
gcode_RAWArray = []
#distNumberOffset_Start = ((-10,3.5,.57),(-8.75,3.5,.57),(-7.5,3.5,.57),(-5.5,3.5,.57))
distNumLoc_Start = ((20,33.5,.57),(21.25,32.45,.57),(22.5,33.5,.57),(24.5,33.5,.57))
distNumOffsets = (7.75,-7,0)
distNumLocArray = [] # [[gCode_0],[Location 1],[location2],...]
for a in range(0,2):
    for b in range(0,3):
        distNumLocArray.append([])
        for c in distNumLoc_Start:
            distNumLocArray[-1].append([0])
            distNumLocArray[-1][-1].append([round(c[0]+(distNumOffsets[0]*b),5), round(c[1]+(distNumOffsets[1]*a),5), c[2]])
SpeedNumLoc_Start = ((28,28.625,.57),(30,28.625,.57),(32,28.625,.57))

max_Z = (5.93*layerCount)+2
xOffset = 0 #mm
yOffset = 0 #mm
retractDist = [] #mm
retractSpd = [] #30mm/s = 1800mm/min
originalXY = [30,30] #XY Center of original model in Slicer
xyLocations = [[30,30],[125,30],[220,30],
               [30,105],[125,105],[220,105],
               [30,180],[125,180],[220,180]]
xyOffsets = [[float(n[0]-originalXY[0]),float(n[1]-originalXY[1])] for n in xyLocations]
#Generate Layer offset distances based on the layerCount
layerOffsets = [x*ColSectionOffset for x in range(layerCount)]

gCode_0 = [['G1', ['Z', 0.15]], ['G1', ['X', 29.485], ['Y', 28.899]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 30.515], ['Y', 28.899], ['E', 0.01399]], ['G1', ['X', 30.515], ['Y', 31.101], ['E', 0.02991]], ['G1', ['X', 29.485], ['Y', 31.101], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 28.937], ['E', 0.0294]], ['M204', 'S800'], ['G1', ['X', 29.449], ['Y', 28.652], ['F', 10800.0]], ['G1', ['X', 29.343], ['Y', 28.997]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 29.583], ['Y', 28.757], ['E', 0.00462]], ['G1', ['X', 30.417], ['Y', 28.757], ['E', 0.01132]], ['G1', ['X', 30.657], ['Y', 28.997], ['E', 0.00462]], ['G1', ['X', 30.657], ['Y', 31.003], ['E', 0.02724]], ['G1', ['X', 30.417], ['Y', 31.243], ['E', 0.00462]], ['G1', ['X', 29.583], ['Y', 31.243], ['E', 0.01132]], ['G1', ['X', 29.343], ['Y', 31.003], ['E', 0.00462]], ['G1', ['X', 29.343], ['Y', 29.035], ['E', 0.02673]], ['M204', 'S800'], ['G1', ['X', 29.593], ['Y', 28.989], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]]]
gCode_1 = [['G1', ['Z', 0.15]], ['G1', ['X', 29.538], ['Y', 28.757]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 30.462], ['Y', 28.757], ['E', 0.01254]], ['G1', ['X', 30.462], ['Y', 28.899], ['E', 0.00193]], ['G1', ['X', 30.071], ['Y', 28.899], ['E', 0.00531]], ['G1', ['X', 30.071], ['Y', 31.243], ['E', 0.03184]], ['G1', ['X', 29.867], ['Y', 31.243], ['E', 0.00277]], ['G1', ['X', 29.64], ['Y', 30.936], ['E', 0.00519]], ['G1', ['X', 29.64], ['Y', 30.813], ['E', 0.00167]], ['G1', ['X', 29.929], ['Y', 30.813], ['E', 0.00393]], ['G1', ['X', 29.929], ['Y', 28.899], ['E', 0.026]], ['G1', ['X', 29.538], ['Y', 28.899], ['E', 0.00531]], ['G1', ['X', 29.538], ['Y', 28.795], ['E', 0.00142]], ['M204', 'S800'], ['G1', ['X', 29.787], ['Y', 28.786], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]]]
gCode_2 = [['G1', ['Z', 0.15]], ['G1', ['X', 29.343], ['Y', 28.757]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 30.657], ['Y', 28.757], ['E', 0.01785]], ['G1', ['X', 30.657], ['Y', 29.094], ['E', 0.00458]], ['G1', ['X', 30.515], ['Y', 29.094], ['E', 0.00193]], ['G1', ['X', 30.515], ['Y', 28.899], ['E', 0.00265]], ['G1', ['X', 29.485], ['Y', 28.899], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 29.929], ['E', 0.01399]], ['G1', ['X', 30.417], ['Y', 29.929], ['E', 0.01265]], ['G1', ['X', 30.657], ['Y', 30.169], ['E', 0.00462]], ['G1', ['X', 30.657], ['Y', 31.003], ['E', 0.01132]], ['G1', ['X', 30.417], ['Y', 31.243], ['E', 0.00462]], ['G1', ['X', 29.583], ['Y', 31.243], ['E', 0.01132]], ['G1', ['X', 29.343], ['Y', 31.003], ['E', 0.00462]], ['G1', ['X', 29.343], ['Y', 30.906], ['E', 0.00132]], ['G1', ['X', 29.485], ['Y', 30.906], ['E', 0.00193]], ['G1', ['X', 29.485], ['Y', 31.101], ['E', 0.00265]], ['G1', ['X', 30.515], ['Y', 31.101], ['E', 0.01399]], ['G1', ['X', 30.515], ['Y', 30.071], ['E', 0.01399]], ['G1', ['X', 29.583], ['Y', 30.071], ['E', 0.01265]], ['G1', ['X', 29.343], ['Y', 29.831], ['E', 0.00462]], ['G1', ['X', 29.343], ['Y', 28.795], ['E', 0.01407]], ['M204', 'S800'], ['G1', ['X', 29.567], ['Y', 28.869], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]]]
gCode_3 = [['G1', ['Z', 0.15]], ['G1', ['X', 29.343], ['Y', 28.997]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 29.583], ['Y', 28.757], ['E', 0.00462]], ['G1', ['X', 30.417], ['Y', 28.757], ['E', 0.01132]], ['G1', ['X', 30.657], ['Y', 28.997], ['E', 0.00462]], ['G1', ['X', 30.657], ['Y', 29.831], ['E', 0.01132]], ['G1', ['X', 30.488], ['Y', 30.0], ['E', 0.00325]], ['G1', ['X', 30.657], ['Y', 30.169], ['E', 0.00325]], ['G1', ['X', 30.657], ['Y', 31.003], ['E', 0.01132]], ['G1', ['X', 30.417], ['Y', 31.243], ['E', 0.00462]], ['G1', ['X', 29.583], ['Y', 31.243], ['E', 0.01132]], ['G1', ['X', 29.343], ['Y', 31.003], ['E', 0.00462]], ['G1', ['X', 29.343], ['Y', 30.906], ['E', 0.00132]], ['G1', ['X', 29.485], ['Y', 30.906], ['E', 0.00193]], ['G1', ['X', 29.485], ['Y', 31.101], ['E', 0.00265]], ['G1', ['X', 30.515], ['Y', 31.101], ['E', 0.01399]], ['G1', ['X', 30.515], ['Y', 30.071], ['E', 0.01399]], ['G1', ['X', 30.125], ['Y', 30.071], ['E', 0.0053]], ['G1', ['X', 30.125], ['Y', 29.929], ['E', 0.00193]], ['G1', ['X', 30.515], ['Y', 29.929], ['E', 0.0053]], ['G1', ['X', 30.515], ['Y', 28.899], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 28.899], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 29.094], ['E', 0.00265]], ['G1', ['X', 29.343], ['Y', 29.094], ['E', 0.00193]], ['G1', ['X', 29.343], ['Y', 29.035], ['E', 0.00081]], ['M204', 'S800'], ['G1', ['X', 29.58], ['Y', 28.918], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]]]
gCode_4 = [['G1', ['Z', 0.15]], ['G1', ['X', 29.485], ['Y', 29.679]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 30.32], ['Y', 29.679], ['E', 0.01134]], ['G1', ['X', 30.32], ['Y', 30.545], ['E', 0.01176]], ['G1', ['X', 30.067], ['Y', 30.617], ['E', 0.00357]], ['G1', ['X', 29.505], ['Y', 29.711], ['E', 0.01448]], ['M204', 'S800'], ['G1', ['X', 29.422], ['Y', 29.437], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]], ['G1', ['X', 30.462], ['Y', 28.899], ['F', 10800.0]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 30.462], ['Y', 29.537], ['E', 0.00867]], ['G1', ['X', 30.657], ['Y', 29.537], ['E', 0.00265]], ['G1', ['X', 30.657], ['Y', 29.679], ['E', 0.00193]], ['G1', ['X', 30.462], ['Y', 29.679], ['E', 0.00265]], ['G1', ['X', 30.462], ['Y', 31.243], ['E', 0.02124]], ['G1', ['X', 30.264], ['Y', 31.243], ['E', 0.00269]], ['G1', ['X', 29.343], ['Y', 29.768], ['E', 0.02362]], ['G1', ['X', 29.343], ['Y', 29.537], ['E', 0.00314]], ['G1', ['X', 30.32], ['Y', 29.537], ['E', 0.01327]], ['G1', ['X', 30.32], ['Y', 28.899], ['E', 0.00867]], ['G1', ['X', 30.124], ['Y', 28.899], ['E', 0.00265]], ['G1', ['X', 30.124], ['Y', 28.757], ['E', 0.00193]], ['G1', ['X', 30.657], ['Y', 28.757], ['E', 0.00723]], ['G1', ['X', 30.657], ['Y', 28.899], ['E', 0.00193]], ['G1', ['X', 30.499], ['Y', 28.899], ['E', 0.00214]], ['M204', 'S800'], ['G1', ['X', 30.217], ['Y', 28.951], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]]]
gCode_5 = [['G1', ['Z', 0.15]], ['G1', ['X', 29.343], ['Y', 28.997]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 29.583], ['Y', 28.757], ['E', 0.00462]], ['G1', ['X', 30.417], ['Y', 28.757], ['E', 0.01132]], ['G1', ['X', 30.657], ['Y', 28.997], ['E', 0.00462]], ['G1', ['X', 30.657], ['Y', 29.831], ['E', 0.01132]], ['G1', ['X', 30.417], ['Y', 30.071], ['E', 0.00462]], ['G1', ['X', 29.485], ['Y', 30.071], ['E', 0.01265]], ['G1', ['X', 29.485], ['Y', 31.101], ['E', 0.01399]], ['G1', ['X', 30.657], ['Y', 31.101], ['E', 0.01592]], ['G1', ['X', 30.657], ['Y', 31.243], ['E', 0.00193]], ['G1', ['X', 29.343], ['Y', 31.243], ['E', 0.01785]], ['G1', ['X', 29.343], ['Y', 30.169], ['E', 0.01458]], ['G1', ['X', 29.583], ['Y', 29.929], ['E', 0.00462]], ['G1', ['X', 30.515], ['Y', 29.929], ['E', 0.01265]], ['G1', ['X', 30.515], ['Y', 28.899], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 28.899], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 29.094], ['E', 0.00265]], ['G1', ['X', 29.343], ['Y', 29.094], ['E', 0.00193]], ['G1', ['X', 29.343], ['Y', 29.035], ['E', 0.00081]], ['M204', 'S800'], ['G1', ['X', 29.58], ['Y', 28.918], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]]]
gCode_6 = [['G1', ['Z', 0.15]], ['G1', ['X', 29.485], ['Y', 28.899]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 30.515], ['Y', 28.899], ['E', 0.01399]], ['G1', ['X', 30.515], ['Y', 29.929], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 29.929], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 28.937], ['E', 0.01348]], ['M204', 'S800'], ['G1', ['X', 29.42], ['Y', 28.658], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]], ['G1', ['X', 29.485], ['Y', 30.071], ['F', 10800.0]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 29.485], ['Y', 31.101], ['E', 0.01399]], ['G1', ['X', 30.515], ['Y', 31.101], ['E', 0.01399]], ['G1', ['X', 30.515], ['Y', 30.906], ['E', 0.00265]], ['G1', ['X', 30.657], ['Y', 30.906], ['E', 0.00193]], ['G1', ['X', 30.657], ['Y', 31.003], ['E', 0.00132]], ['G1', ['X', 30.417], ['Y', 31.243], ['E', 0.00462]], ['G1', ['X', 29.583], ['Y', 31.243], ['E', 0.01132]], ['G1', ['X', 29.343], ['Y', 31.003], ['E', 0.00462]], ['G1', ['X', 29.343], ['Y', 28.997], ['E', 0.02724]], ['G1', ['X', 29.583], ['Y', 28.757], ['E', 0.00462]], ['G1', ['X', 30.417], ['Y', 28.757], ['E', 0.01132]], ['G1', ['X', 30.657], ['Y', 28.997], ['E', 0.00462]], ['G1', ['X', 30.657], ['Y', 29.831], ['E', 0.01132]], ['G1', ['X', 30.417], ['Y', 30.071], ['E', 0.00462]], ['G1', ['X', 29.523], ['Y', 30.071], ['E', 0.01214]], ['M204', 'S800'], ['G1', ['X', 29.236], ['Y', 30.088], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]]]
gCode_7 = [['G1', ['Z', 0.15]], ['G1', ['X', 29.345], ['Y', 28.757]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 30.14], ['Y', 28.757], ['E', 0.01081]], ['G1', ['X', 30.14], ['Y', 28.899], ['E', 0.00193]], ['G1', ['X', 29.792], ['Y', 28.899], ['E', 0.00472]], ['G1', ['X', 30.655], ['Y', 31.001], ['E', 0.03086]], ['G1', ['X', 30.655], ['Y', 31.243], ['E', 0.00329]], ['G1', ['X', 29.345], ['Y', 31.243], ['E', 0.01781]], ['G1', ['X', 29.345], ['Y', 30.906], ['E', 0.00458]], ['G1', ['X', 29.487], ['Y', 30.906], ['E', 0.00193]], ['G1', ['X', 29.487], ['Y', 31.101], ['E', 0.00265]], ['G1', ['X', 30.464], ['Y', 31.101], ['E', 0.01328]], ['G1', ['X', 29.595], ['Y', 28.899], ['E', 0.03216]], ['G1', ['X', 29.345], ['Y', 28.899], ['E', 0.0034]], ['G1', ['X', 29.345], ['Y', 28.795], ['E', 0.00142]], ['M204', 'S800'], ['G1', ['X', 29.591], ['Y', 28.8], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]]]
gCode_8 = [['G1', ['Z', 0.15]], ['G1', ['X', 29.485], ['Y', 30.071]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 30.515], ['Y', 30.071], ['E', 0.01399]], ['G1', ['X', 30.515], ['Y', 31.101], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 31.101], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 30.109], ['E', 0.01348]], ['M204', 'S800'], ['G1', ['X', 29.42], ['Y', 29.83], ['F', 10800.0]], ['G1', ['X', 29.485], ['Y', 29.929]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 29.485], ['Y', 28.899], ['E', 0.01399]], ['G1', ['X', 30.515], ['Y', 28.899], ['E', 0.01399]], ['G1', ['X', 30.515], ['Y', 29.929], ['E', 0.01399]], ['G1', ['X', 29.523], ['Y', 29.929], ['E', 0.01348]], ['M204', 'S800'], ['G1', ['X', 29.244], ['Y', 29.994], ['F', 10800.0]], ['G1', ['X', 29.463], ['Y', 29.951]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 29.343], ['Y', 29.831], ['E', 0.00231]], ['G1', ['X', 29.343], ['Y', 28.997], ['E', 0.01132]], ['G1', ['X', 29.583], ['Y', 28.757], ['E', 0.00462]], ['G1', ['X', 30.417], ['Y', 28.757], ['E', 0.01132]], ['G1', ['X', 30.657], ['Y', 28.997], ['E', 0.00462]], ['G1', ['X', 30.657], ['Y', 29.831], ['E', 0.01132]], ['G1', ['X', 30.488], ['Y', 30.0], ['E', 0.00325]], ['G1', ['X', 30.657], ['Y', 30.169], ['E', 0.00325]], ['G1', ['X', 30.657], ['Y', 31.003], ['E', 0.01132]], ['G1', ['X', 30.417], ['Y', 31.243], ['E', 0.00462]], ['G1', ['X', 29.583], ['Y', 31.243], ['E', 0.01132]], ['G1', ['X', 29.343], ['Y', 31.003], ['E', 0.00462]], ['G1', ['X', 29.343], ['Y', 30.169], ['E', 0.01132]], ['G1', ['X', 29.512], ['Y', 30.0], ['E', 0.00325]], ['G1', ['X', 29.49], ['Y', 29.977], ['E', 0.00044]], ['M204', 'S800'], ['G1', ['X', 29.572], ['Y', 29.82], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]]]
gCode_9 = [['G1', ['Z', 0.15]], ['G1', ['X', 29.485], ['Y', 30.071]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 30.515], ['Y', 30.071], ['E', 0.01399]], ['G1', ['X', 30.515], ['Y', 31.101], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 31.101], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 30.109], ['E', 0.01348]], ['M204', 'S800'], ['G1', ['X', 29.42], ['Y', 29.83], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]], ['G1', ['X', 30.515], ['Y', 29.929], ['F', 10800.0]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 30.515], ['Y', 28.899], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 28.899], ['E', 0.01399]], ['G1', ['X', 29.485], ['Y', 29.094], ['E', 0.00265]], ['G1', ['X', 29.343], ['Y', 29.094], ['E', 0.00193]], ['G1', ['X', 29.343], ['Y', 28.997], ['E', 0.00132]], ['G1', ['X', 29.583], ['Y', 28.757], ['E', 0.00462]], ['G1', ['X', 30.417], ['Y', 28.757], ['E', 0.01132]], ['G1', ['X', 30.657], ['Y', 28.997], ['E', 0.00462]], ['G1', ['X', 30.657], ['Y', 31.003], ['E', 0.02724]], ['G1', ['X', 30.417], ['Y', 31.243], ['E', 0.00462]], ['G1', ['X', 29.583], ['Y', 31.243], ['E', 0.01132]], ['G1', ['X', 29.343], ['Y', 31.003], ['E', 0.00462]], ['G1', ['X', 29.343], ['Y', 30.169], ['E', 0.01132]], ['G1', ['X', 29.583], ['Y', 29.929], ['E', 0.00462]], ['G1', ['X', 30.477], ['Y', 29.929], ['E', 0.01214]], ['M204', 'S800'], ['G1', ['X', 30.764], ['Y', 29.912], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]]]
gCode_D = [['G1', ['Z', 0.15]], ['G1', ['X', 29.88], ['Y', 29.88]], ['G1', ['E', 0.6], ['F', 1800.0]], ['M204', 'S500'], ['G1', ['F', 900.0]], ['G1', ['X', 30.12], ['Y', 29.88], ['E', 0.00326]], ['G1', ['X', 30.12], ['Y', 30.12], ['E', 0.00326]], ['G1', ['X', 29.88], ['Y', 30.12], ['E', 0.00326]], ['G1', ['X', 29.88], ['Y', 29.918], ['E', 0.00275]], ['M204', 'S800'], ['G1', ['X', 30.112], ['Y', 29.942], ['F', 10800.0]], ['G1', ['E', -0.6], ['F', 1800.0]]]
gCodeNumbers = (gCode_0, gCode_1, gCode_2, gCode_3, gCode_4, gCode_5, gCode_6, gCode_7, gCode_8, gCode_9, gCode_D)

gCode_header = ["M73 P0 R15","M73 Q0 S16","M201 X800 Y800 Z200 E4000 ; sets maximum accelerations, mm/sec^2",
                "M203 X200 Y200 Z12 E120 ; sets maximum feedrates, mm/sec",
                "M204 P800 R800 T800 ; sets acceleration (P, T) and retract acceleration (R), mm/sec^2",
                "M205 X6.00 Y6.00 Z0.40 E4.50 ; sets the jerk limits, mm/sec",
                "M205 S0 T0 ; sets the minimum extruding and travel feed rate, mm/sec",
                "M107",
                ";TYPE:Custom","M862.3 P 'MK3SMMU2S' ; printer model check","M862.1 P0.25 ; nozzle diameter check",
                "M115 U3.9.1 ; tell printer latest fw version","G90 ; use absolute coordinates","M83 ; extruder relative mode",
                "M104 S215 ; set extruder temp","M140 S60 ; set bed temp","M190 S60 ; wait for bed temp",
                "M109 S215 ; wait for extruder temp","G28 W ; home all without mesh bed level","G80 ; mesh bed leveling",
                "; Send the filament type to the MMU2.0 unit.",
                "; E stands for extruder number, F stands for filament type (0: default; 1:flex; 2: PVA)",
                "M403 E0 F0","M403 E1 F0","M403 E2 F0","M403 E3 F0","M403 E4 F0",
                ";go outside print area","G1 Y-3.0 F1000.0","G1 Z0.4 F1000.0","; select extruder","T0",
                "; initial load","G1 X55.0 E29.0 F1073.0","G1 X5.0 E29.0 F1800.0","M73 P0 R14","M73 Q0 S15",
                "G1 X55.0 E8.0 F2000.0","G1 Z0.3 F1000.0","G92 E0.0","G1 X240.0 E25.0 F2200.0","G1 Y-2.0 F1000.0",
                "M73 P1 R14","M73 Q1 S15","G1 X55.0 E25 F1400.0","G1 Z0.20 F1000.0","M73 P2 R14","M73 Q2 S15",
                "G1 X5.0 E4.0 F1000.0","G92 E0.0",";M221 S100","G92 E0.0",
                "; Don't change E values below. Excessive value can damage the printer.",
                "G21 ; set units to millimeters","G90 ; use absolute coordinates","M83 ; use relative distances for extrusion",
                "M900 K"+str(custom_K_Value),"M107"]

gCode_footer = ["G1 E-.2 F1500","M107","G1 X0 Y210 F7200","G1 E2 F5000","G1 E2 F5500","G1 E2 F6000","G1 E-15.0000 F5800",
                "G1 E-20.0000 F120","G1 E-10.0000 F3250","M702 C","G4 ; wait","M221 S100 ; reset flow",
                "M900 K0 ; reset LA","M104 S0 ; turn off temperature","M140 S0 ; turn off heatbed","M107 ; turn off fan",
                "G1 Z"+str(max_Z)+" ; Move print head up","G1 X0 Y200 F3000 ; home X axis","M84 ; disable motors",
                "M73 P100 R0","M73 Q100 S0"]

#Gather user inpurt parameters for retraction distance, speed, and increments therof
def setRetParams(nozzleTemp,bedTemp,FanSpeed): 
    global layerCount
    rDist, rSpd = [],[]
    retractMIN = float(input("What is the MINimum retraction Distance?(float, mm):"))
    retractIncrement = float(input("What is the retraction Distance increment(6 layers, float, mm):"))
    speedMin = int(input("What is the minimum retraction Speed?(int, mm/s):"))
    speedImcrement = int(input("What is the retraction Speed Increment?(9 objects, int, mm/s):"))
    nozzleTemp = int(input("Specify the Nozzle temperature (default = "+str(nozzleTemp)+"):") or nozzleTemp)
    bedTemp = int(input("Specify the Heat Bed temperature (default = "+str(bedTemp)+"):") or bedTemp)
    FanSpeed = int(input("Fan Speed after layer 5 [8 - 255] (default = "+str(FanSpeed)+"):") or FanSpeed)
                         
    #Apply input to generate retraction distance array
    for n in range(layerCount):
        rDist.append(round(retractMIN+(n*retractIncrement),5))

    #Apply input to generate retraction speed array
    for n in range(9):
        rSpd.append(round(speedMin+(n*speedImcrement),5))
    
    return rDist, rSpd, nozzleTemp, bedTemp, FanSpeed

def moveXYZ(gObject, gOrigin, gTarget):
    gObject = tuple(gObject)
    print(gObject[0],",",gOrigin,",",gTarget)
    #xyzOffset = [round(a - b,5) for (a, b) in zip(gTarget, gOrigin)]
    xyzOffset = [round(a - gOrigin[n],5) for n,a in enumerate(gTarget)]
    print(xyzOffset)
    moveXYZ_Ret = []
    for line in gObject:
        line = tuple(line)
        lineAdjust = [0 for x in range(len(line))]
        if line[0] == 'G1':
            lineAdjust[0] = 'G1'
            for xyzEnum,gItem in enumerate(line):
                gItem = tuple(gItem)
                if gItem[0] == 'X':
                    lineAdjust[xyzEnum] = ['X',0]
                    lineAdjust[xyzEnum][1] = round(line[xyzEnum][1] + xyzOffset[0],5)
                elif gItem[0] == 'Y':
                    lineAdjust[xyzEnum] = ['Y',0]
                    lineAdjust[xyzEnum][1] = round(line[xyzEnum][1] + xyzOffset[1],5)
                elif gItem[0] == 'Z':
                    lineAdjust[xyzEnum] = ['Z',0]
                    #print(lineAdjust[xyzEnum])
                    lineAdjust[xyzEnum][1] = round(line[xyzEnum][1] + xyzOffset[2],5)
                    print(lineAdjust[xyzEnum][1])
                else:
                    lineAdjust[xyzEnum] = line[xyzEnum]
        else:
            lineAdjust = [x for x in line]
        moveXYZ_Ret.append(lineAdjust)
    return moveXYZ_Ret

def parse_gCodeFile(RAWfile):
    gCodeFileReturn = []
    for x in RAWfile:
        #print("x = ",x)
        a = x.split()
        #print("a = ",a)
        for num, gItem in enumerate(a):
            if a[0] == "G1" and num>0 and (gItem[0]=="X" or gItem[0]=="Y" or gItem[0]=="Z" or gItem[0]=="E" or gItem[0]=="F"):
                a[num] = [gItem[0], float(gItem[1:])]
            if a[0] == "M104" or a[0] == "M109":
                print(a)
                a[1] = 'S'+str(nozzleTemp)
                
        if a!=[]: gCodeFileReturn.append(a)
        
       
        if "M140" in gCodeFileReturn[-1]:
            print(gCodeFileReturn[-1])
            gCodeFileReturn[-1] = 'M140 S'+str(bedTemp)+' ; set bed temp.'
        if 'M190' in gCodeFileReturn[-1]:
            print(gCodeFileReturn[-1])
            gCodeFileReturn[-1] = 'M190 S'+str(bedTemp)+' ; wait for bed temp.'

        
    return gCodeFileReturn

#Call function to gather user parameters as long as the values are not satisfactory
GoodValues = "N"
while not (GoodValues =="Y" or GoodValues =="y"):
    retractDist, retractSpd, nozzleTemp, bedTemp, FanSpeed = setRetParams(nozzleTemp, bedTemp, FanSpeed)
    print("Based on your input, you will have the following:")
    print("Retraction Distances:",retractDist)
    print("Retraction Speeds:",retractSpd)    
    print("Nozzle Temperature:",nozzleTemp)
    print("Print Bed Temperature:",bedTemp)
    print("Fan Speed:",FanSpeed)
    GoodValues = input("Are these values satisfactory? (Y/N)")
    print(GoodValues)
    #if GoodValues != "Y": retractDist, retractSpd = setRetParams()

#Process header data with user input:
for gLine,gLineData in enumerate(gCode_header):
    if "M140" in gLineData:
        gCode_header[gLine] = 'M140 S'+str(bedTemp)+' ; set bed temp.'
    if 'M190' in gLineData:
        gCode_header[gLine] = 'M190 S'+str(bedTemp)+' ; wait for bed temp.'
    if "M104" in gLineData:
        gCode_header[gLine] = 'M104 S'+str(nozzleTemp)+' ; set temperature'
    if 'M109' in gLineData:
        gCode_header[gLine] = 'M109 S'+str(nozzleTemp)+' ; wait for temperature'
        
#Load gcode file for the Model base and parse it to a list line by line, separating out x,y,z,e, and f codes from their values
with open(gCodeBaseFile) as data_baseFile:
    gCode_base = parse_gCodeFile(data_baseFile)

del data_baseFile

#Turn off fan for 1st layer of base
gCode_base.insert(1,['M107',';','Turn','Fan','Off'])

#Load the gcode file for the model collumn layer (1st) and parse it to a list line by line
with open(gCodeColmnFile) as data_columnFile:
    gCode_columnSet = parse_gCodeFile(data_columnFile)

del data_columnFile

#Turn on Fan to specified speed at collumn/Base transition
gCode_columnSet.insert(1,['M106', 'S'+str(FanSpeed),';Set_Fan_Speed'])


# for each value in retractDist create a new tower layer with the corresponting retraction distance
rawColSet = []
for layerOffsetEnum, currentLayerOffset in enumerate(layerOffsets):
    print("layerNumber=",layerOffsetEnum)
    rawLayer = []  
    for gData in gCode_columnSet:
        gcData = [0,[0,0]]
        #gcData = gcData+gData
        #gcData=list(gData)
        #gcData=gData.copy()
        if gData[0] == "G1":
            gcData[0] = "G1"
            if "Z" in gData[1]:
                gcData[1][0] = "Z"
                gcData[1][1] = round(gData[1][1] + currentLayerOffset,2)
                #print("z:",currentLayerOffset,"Ret:",retractDist[layerOffsetEnum]," gcode:", gcData)
            elif "E" in gData[1]:
                gcData[1][0] = "E"
                if gData[1][1] == -.12345:
                    gcData[1][1] = -retractDist[layerOffsetEnum]
                elif gData[1][1] == .12345:
                    gcData[1][1] = retractDist[layerOffsetEnum]
            else:
                gcData = gData
                #print("z:",currentLayerOffset,"Ret:",retractDist[layerOffsetEnum]," gcode:", gcData)
        else:
            gcData = gData
        if len(gData) > len(gcData):
            for extend in range(len(gcData),len(gData)):
                gcData.append(gData[extend])
        """
        gcData = list(gData)
        if gData[0] == "G1":
            if "Z" in gData[1]:
                gcData[1][1] = gData[1][1] + currentLayerOffset
            if "E" in gData[1]:
                if gData[1][1] == -.6:
                    gcData[1][1] = -retractDist[layerNumber]
                elif gData[1][1] == .6:
                    gcData[1][1] = retractDist[layerNumber]
                print(retractDist[layerNumber])
        """
        rawLayer.append(gcData)   
        #print(retractDist[layerNumber])
    rawColSet = rawColSet + rawLayer

#Add Retract Distance Numbers to Base
for enum, retDistItem in enumerate(retractDist):
    #[0.15, 0.2, 0.25, 0.3, 0.35, 0.4]
    #distNumLocArray
    for nEnum,n in enumerate(str(retDistItem)):
        if n == ".":
            distNumLocArray[enum][nEnum][0]=10 #gCodeNumbers[10]
        else:
            distNumLocArray[enum][nEnum][0]=int(n) #gCodeNumbers[int(n)]

for n in distNumLocArray:
    for a in n:
        gCode_base = gCode_base + [[";Digit: "+str(a[0])]]
        gCode_base = gCode_base + [[";Digit X,Y,Z: "+str(a[1])]]
        gCode_base = gCode_base + moveXYZ(gCodeNumbers[a[0]], (30,30,.15), a[1])

gCode_base = gCode_base + ["***ReplaceRetSpeed***"]
        
print(gCode_base[-30:-1])    
#Add Header to Export list
gCodeToWriteOut = gCodeToWriteOut + gCode_header


#Generate gCode for the RAW/imported tower location
gcode_RAWbuild = gcode_RAWbuild + gCode_base #Append Base code
print(gCode_base[-30:-1])

#Combine Base and collumns
gcode_RAWbuild = gcode_RAWbuild + rawColSet
gcode_rawArray = []

#Reposition and duplicate to 9 pre-calculated "safe" locations around print bed and adjust retract speed accordingly
xyEnum = -1
for platterLoc in xyOffsets:
    print("Object",(xyEnum+2),"...")
    xyEnum += 1
    #tempTower = copy.deepcopy(gcode_RAWbuild)

    for gLayer in gcode_RAWbuild:
        temp_gLayer = [0,0,0]
        if gLayer[0]=="G1":
            temp_gLayer[0] = "G1"
            for gLayerEnum, gLayerItem in enumerate(gLayer):
                #print(gLayerEnum,",",gLayerItem)
                if "X" in gLayerItem:
                    temp_gLayer[1] = ["X", round(platterLoc[0] + (gLayerItem[1]/1),5)]
                    #print(platterLoc[0],",",gLayerItem[1]/1)
                elif "Y" in gLayerItem:
                    temp_gLayer[2] = ["Y", round(platterLoc[1] + (gLayerItem[1]/1),5)]
                elif "E" in gLayerItem:
                    pass
                elif "F" in gLayerItem:
                    pass
                else:
                    temp_gLayer[gLayerEnum] = gLayer[gLayerEnum]
                #print(temp_gLayer)
            if gLayer[1][0] == "F" or gLayer[1][0] == "Z" :
                temp_gLayer = gLayer
            if gLayer[1][0] =="E" and gLayer[2][0] == "F":
                temp_gLayer[1] = ["E",gLayer[1][1]]
                temp_gLayer[2] = ["F",retractSpd[xyEnum]*60]
        else:
            temp_gLayer = gLayer
        if len(gLayer) > len(temp_gLayer):
            for n in range(len(temp_gLayer),len(gLayer)):
                temp_gLayer.append(gLayer[n])
                
        gcode_rawArray.append(temp_gLayer)
        if temp_gLayer[0] == "G1":
            if temp_gLayer[1][0] =="E":
                if temp_gLayer[2][0] == "F":
                    if temp_gLayer[1][1] >= 0:
                        gcode_rawArray.append(["G1", ["F", default_FSpd]])
                        
    gcode_rawArray.append(["G1",["Z",max_Z+5]])
    
#Add retract Speed digits

#function to Log line numbers in file to replace content
def insertLocList(gtest):
    dupe = []
    for e,n in enumerate(gtest):
        if n == "***ReplaceRetSpeed***":
            dupe.insert(0,e)
    return dupe
#Derive individual digits from user settings
SPD_gLocList = []
for es,s in enumerate(retractSpd):
    SPD_gLocList.append([[0,[SpeedNumLoc_Start[0]]],[0,[SpeedNumLoc_Start[1]]],[0,[SpeedNumLoc_Start[2]]]]) #[digit,[x offset,y offset,z offset]]
    s = str(s)
    if len(s) == 1: s = "00"+s
    if len(s) == 2: s = "0"+s
    for ei,i in enumerate(s):
        SPD_gLocList[es][ei][0] = int(i)

#Develope offsets for digit locations
for enSPD,nSPD in enumerate(SPD_gLocList):
    for enaSPD,aSPD in enumerate(nSPD):
        targetLoc = [x for x in xyLocations[enSPD]]+[.57]
        targetLoc[0] = targetLoc[0]+(2*enaSPD)
        aSPD[0] = moveXYZ(gCodeNumbers[aSPD[0]],(30,30,.15),targetLoc)
  
#  Activate line number logging functionto to gather line/record numbers for insert points                              
SpeenNumInserts = insertLocList(gcode_rawArray)

#Insterion location order must be from last to first or the target insertion points will incriment 
# as the operation progresses
SPD_gLocList.reverse()

#Replace and insert digit gCode into file at insert points 
for EnumSpdInsert, newInsertLine in enumerate(SpeenNumInserts):
    for SpdDigitSingle in SPD_gLocList[EnumSpdInsert]:
        
        gcode_rawArray[newInsertLine] = ";"
        for EnumDigi, digitLine in enumerate(SpdDigitSingle[0]):
            gcode_rawArray.insert(newInsertLine+EnumDigi,digitLine)
        gcode_rawArray.insert(newInsertLine,[";Speed Digits"])
    

#Collapse data format into single text blocks
#Comprehension that iterates through all lines to produce a flattend text only array
print("Collapsing into writable code...")
gCode_Collapsed = [" ".join(["".join([str(elem) for elem in sublist]) for sublist in lineList]) for lineList in gcode_rawArray]

"""
Hang checking for list comprehension - not fully functional, but iterates  to isolate problems
gCode_Collapsed = []
for lineList in gcode_rawArray:
    tempSublist = ""
    for sublist in lineList:
        tempelem = ""
        for elem in sublist:
            t = "".join([tempelem,str(elem)])
        t2 = " ".join([tempSublist,t])
    gCode_Collapsed.append(t2)
"""    
#Combine header(in WriteOut already) and _collapsed into Writeout
gCodeToWriteOut = gCodeToWriteOut + gCode_Collapsed

#Append Footer gCode without any temperature adjustment (Everything is to be set to 0)
gCodeToWriteOut = gCodeToWriteOut + gCode_footer

#Save out as gCode file - filePath + CustomRetract_app_Output.gcode
outputFile = gCode_Path+"CustomRetract_app_v2_test.gcode"
print("Writing gCode to file...")
with open(outputFile,"w") as outFile:

    for enum, outlines in enumerate(gCodeToWriteOut):
        try:
            outFile.write(outlines+"\n")
        except:
            print(enum)
            
print("Export Successful.")