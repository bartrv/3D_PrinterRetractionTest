# 3D_PrinterRetractionTest
A Retraction test gCode generator that translates user input to an array of print towers to test filament specific retraction settings.

This command line script generates gCode specifically for a printer that uses .9 degree stepper motors, a geared extruder, and a .25mm nozzle on a 190/210mm print bed (Prusa Mk3S) with a .07mm layer height.

*Warning* This generator is specifically tuned for the above configuration, use in any other configuration could damage your printer!

When provided a retraction-distance and retraction-speed +Increment step, this code creates the gCode for a grid of nine 6-layer towers to test 54 settings.
V1 - Created the basic code to generate the towers
V2 - Generated the resulting speeds/distances as numbers printed on the bases for referance after the print was complete
V2.1 - added options to specify nozzle/bed temperature and fan speed
