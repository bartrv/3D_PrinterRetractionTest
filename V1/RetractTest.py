# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:15:43 2022

@author: bvoigt
"""

import os
#import copy

#Define Variables and constants
layerCount=6
L1Start = .57 #mm
default_Speed = 25 #mm/s
default_FSpd = default_Speed*60
ColSectionOffset = 5.18 #mm
FirstLayerHeight = ""

#Local Path
gCode_Path = os.path.dirname(os.path.abspath(__file__))+"/"
print("Current Folder: ",gCode_Path)

gCodeBaseFile = gCode_Path+"CustomRetract_app_BASE.gcode"
gCodeColmnFile = gCode_Path+"CustomRetract_app_ColsL1.gcode"
gCodeToWriteOut = []
gCode_base = []
gCode_columnSet = []
gcode_RAWbuild = []
gcode_RAWArray = []

max_Z = (5.93*layerCount)+2
xOffset = 0 #mm
yOffset = 0 #mm
retractDist = [] #mm
retractSpd = [] #30mm/s = 1800mm/min
originalXY = [125,30] #XY Center of original model in Slicer
xyLocations = [[30,30],[125,30],[220,30],
               [30,105],[125,105],[220,105],
               [30,180],[125,180],[220,180]]
xyOffsets = [[float(n[0]-originalXY[0]),float(n[1]-originalXY[1])] for n in xyLocations]
#Generate Layer offset distances based on the layerCount
layerOffsets = [x*ColSectionOffset for x in range(layerCount)]

gCode_header = ["M73 P0 R15","M73 Q0 S16","M201 X800 Y800 Z200 E4000 ; sets maximum accelerations, mm/sec^2",
"M203 X200 Y200 Z12 E120 ; sets maximum feedrates, mm/sec",
"M204 P800 R800 T800 ; sets acceleration (P, T) and retract acceleration (R), mm/sec^2",
"M205 X6.00 Y6.00 Z0.40 E4.50 ; sets the jerk limits, mm/sec",
"M205 S0 T0 ; sets the minimum extruding and travel feed rate, mm/sec",
"M107",";TYPE:Custom","M862.3 P \"MK3SMMU2S\" ; printer model check",
"M862.1 P0.25 ; nozzle diameter check",
"M115 U3.9.1 ; tell printer latest fw version",
"G90 ; use absolute coordinates",
"M83 ; extruder relative mode",
"M104 S210 ; set extruder temp",
"M140 S60 ; set bed temp",
"M190 S60 ; wait for bed temp",
"M109 S210 ; wait for extruder temp",
"G28 W ; home all without mesh bed level",
"G80 ; mesh bed leveling",
"",
"; Send the filament type to the MMU2.0 unit.",
"; E stands for extruder number, F stands for filament type (0: default; 1:flex; 2: PVA)",
"M403 E0 F0","M403 E1 F0","M403 E2 F0","M403 E3 F0","M403 E4 F0",
";go outside print area","G1 Y-3.0 F1000.0","G1 Z0.4 F1000.0","; select extruder","T0",
"; initial load","G1 X55.0 E29.0 F1073.0","G1 X5.0 E15.0 F1800.0","G1 X55.0 E8.0 F2000.0","G1 Z0.3 F1000.0",
"G92 E0.0","G1 X240.0 E25.0 F2200.0","G1 Y-2.0 F1000.0","M73 P1 R15","M73 Q1 S16",
"G1 X55.0 E25 F1400.0","G1 Z0.20 F1000.0","M73 P2 R15","M73 Q2 S15","G1 X5.0 E4.0 F1000.0","G92 E0.0",
"","G92 E0.0","","G21 ; set units to millimeters","G90 ; use absolute coordinates",
"M83 ; use relative distances for extrusion","M900 K0",
"M107"]

gCode_footer = ["G1 E-.6 F1800", "G1 Z"+str(max_Z)+" F10800","M107",
";TYPE:Custom","; Filament-specific end gcode","","G1 X0 Y210 F7200","G1 E2 F5000","M73 P89 R1","G1 E2 F5500",
"G1 E2 F6000","G1 E2 F5000","G1 E2 F5500","G1 E2 F6000","G1 E-15.0000 F5800","G1 E-10.0000 F5500","G1 E-20.0000 F30",
"","; Unload filament","M702 C","","G4 ; wait",
"M221 S100 ; reset flow","M900 K0 ; reset LA",
"","M104 S0 ; turn off temperature","M140 S0 ; turn off heatbed","M107 ; turn off fan",
"; Lift print head a bit","G1 Z"+str(max_Z+30)+" ; Move print head up",
"M73 P93 R1","M73 Q93 S1","G1 X0 Y200 F3000 ; home X axis",
"M84 ; disable motors","M73 P100 R0","M73 Q100 S0"]

#Gather user inpurt parameters for retraction distance, speed, and increments therof
def setRetParams(): 
    global layerCount
    rDist, rSpd = [],[]
    retractMIN = float(input("What is the MINimum retraction Distance?(float, mm):"))
    retractIncrement = float(input("What is the retraction Distance increment(6 layers, float, mm):"))
    speedMin = int(input("What is the minimum retraction Speed?(int, mm/s):"))
    speedImcrement = int(input("What is the retraction Speed Increment?(9 objects, int, mm/s):"))
    
    #Apply input to generate retraction distance array
    for n in range(layerCount):
        rDist.append(round(retractMIN+(n*retractIncrement),5))

    #Apply input to generate retraction speed array
    for n in range(9):
        rSpd.append(round(speedMin+(n*speedImcrement),5))
    
    return rDist, rSpd

#Call function to gather user parameters as long as the values are not satisfactory
GoodValues = "N"
while not (GoodValues =="Y" or GoodValues =="y"):
    retractDist, retractSpd = setRetParams()
    print("Based on your input, you will have the following:")
    print("Retraction Distances:",retractDist)
    print("Retraction Speeds:",retractSpd)    
    GoodValues = input("Are these values satisfactory? (Y/N)")
    print(GoodValues)
    #if GoodValues != "Y": retractDist, retractSpd = setRetParams()
    
#Load gcode file for the Model base and parse it to a list line by line, separating out x,y,z,e, and f codes from their values
with open(gCodeBaseFile) as data_baseFile:
    #gCode_base = [x.split() for x in data_baseFile]
    for x in data_baseFile:
        a = x.split()
        for num, gItem in enumerate(a):
            if a[0] == "G1" and num>0 and (gItem[0]=="X" or gItem[0]=="Y" or gItem[0]=="Z" or gItem[0]=="E" or gItem[0]=="F"):
                a[num] = [gItem[0], float(gItem[1:])]
        if a!=[]: gCode_base.append(a)

#Load the gcode file for the model collumn layer (1st) and parse it to a list line by line
with open(gCodeColmnFile) as data_columnFile:
    #gCode_base = [x.split() for x in data_baseFile]
    for x in data_columnFile:
        a = x.split()
        for num, gItem in enumerate(a):
            if a[0] == "G1" and num>0 and (gItem[0]=="X" or gItem[0]=="Y" or gItem[0]=="Z" or gItem[0]=="E" or gItem[0]=="F"):
                a[num] = [gItem[0], float(gItem[1:])]
        if a!=[]: gCode_columnSet.append(a)

#Add Header to Export list
gCodeToWriteOut = gCodeToWriteOut + gCode_header

#Generate gCode for the RAW/imported tower location
gcode_RAWbuild = gcode_RAWbuild + gCode_base #Append Base code

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
                if gData[1][1] == -.6:
                    gcData[1][1] = -retractDist[layerOffsetEnum]
                elif gData[1][1] == .6:
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
    

#Collapse data format into single text blocks
#preliminary comprehension for isolated RAW single column set testing
#gCode_Collapsed = [" ".join(["".join([str(elem) for elem in sublist]) for sublist in lineList]) for lineList in gcode_RAWbuild]

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

#Append Footer gCode
gCodeToWriteOut = gCodeToWriteOut + gCode_footer

#Save out as gCode file - filePath + CustomRetract_app_Output.gcode
outputFile = gCode_Path+"CustomRetract_app_Output.gcode"
print("Writing gCode to file...")
with open(outputFile,"w") as outFile:

    for enum, outlines in enumerate(gCodeToWriteOut):
        try:
            outFile.write(outlines+"\n")
        except:
            print(enum)
            
print("Export Successful.")