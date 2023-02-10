# 3D_PrinterRetractionTest
A Retraction test gCode generator that translates user input to an array of print towers to test filament specific retraction settings.

This gCode is developed for a printer that uses .9 degree stepper motors, a geared extruder, and a .25mm nozzle on a 190/210mm print bed (Prusa Mk3S) with a .07mm layer height.
*Warning* This generator is specifically tuned for the above configuration, use in any other configuration could damage your printer!

When provided a retraction-distance and retraction-speed +Increment step, this code creates the gCode for a grid of nine 6-layer towers to test 54 settings.
