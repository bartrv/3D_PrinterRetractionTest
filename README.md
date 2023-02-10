# 3D_PrinterRetractionTest
A Retraction test gCode generator that translates user input to an array of print towers to test filament specific retraction settings.
<br />
This command line script generates gCode specifically for a printer that uses .9 degree stepper motors, a geared extruder, and a .25mm nozzle on a 190/210mm print bed (Prusa Mk3S) with a .07mm layer height.
<br /><br />
<strong>*Warning*</strong> This generator is specifically tuned for the above configuration, use in any other configuration could damage your printer!
<br /><br />
When provided a retraction-distance and retraction-speed +Increment step, this code creates the gCode for a grid of nine 6-layer towers to test 54 settings.
<li>V1 - Created the basic code to generate the towers
<li>V2 - Generated the resulting speeds/distances as numbers printed on the bases for referance after the print was complete
<li>V2.1 - added options to specify nozzle/bed temperature and fan speed
