# Z_Level_Boost
Offset Z level in gcoge file for 3D printing

The .zip file containes a compiled version of the python script using Pyinstaller, so you can just run the EXE inside the folder and it will run using the contained version of python3 so you don't need to have python or the correct version on you PC

The app.zip file is the same process but for MAC's. It was made with py2app and there is a app file you can run.

The .py file is the raw python script.

When the app runs you can enter the height in mm you want to offest all "G1 Z" commands.
THe process will ignore all comments meaning lines starting with a ; 

and if you want a specific line to be ignored you can add the command -ignore Zboost- to the origial gcode file
for example in your start gcode script "G1 Z0.2 F3000 ; get ready to prime -ignore Zboost-" will ignore the priming command at the start of the print.

If you want a full description of what this does and why check out this video for a explination
https://youtu.be/xdAtwHVv_SI
