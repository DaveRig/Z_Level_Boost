import sys, os
from pathlib import Path
from tkinter import *
from tkinter import filedialog

# Reads in cgode file and updates Z height commands 
def updateFile(userFile,zHeightBoost):
	savePath = os.path.dirname(os.path.abspath(userFile))
	fileName = Path(userFile).stem
	saveFile = os.path.join(savePath,fileName+'_Z-height-Boost.gcode')

	# Read gcode file	
	with open(userFile, 'r') as file:
		data = file.readlines()

	i = 0
	# Loop though each line looking for Z moves
	for line in data:
		FindZ = line.find('G1 Z')
		FindIgnore = line.find('-ignore Zboost-')

		# If ignore command not found and if "G1 Z" was found and the first character in the line is not a ;
		if FindIgnore == -1 and FindZ != -1 and line[0] != ';':
			FindZend = line.find(' ',3)
			ZheightInt = line[4:FindZend]

			#covnert both values to floats and add together
			ZheightFloat =  float(ZheightInt) + float(zHeightBoost)

			#Limit float to 2 decimal places
			Zheight = "{:.2f}".format(ZheightFloat)

			#replace value in line
			data[i]= line.replace(str(ZheightInt),str(Zheight))
		i += 1
		
	# and write everything back
	with open(saveFile, 'w') as file:
		file.writelines( data )

	# update UI msg that roccess completed
	error.config(text='DONE! New file at')
	complete.config(text=saveFile)

def pickFile():
	root.filename = filedialog.askopenfilename(initialdir = os.path.expanduser('~')+"\\Documents", title = "Pick your file", filetypes = (("gcode files","*.gcode"),("All files","*.*"))) # show an "Open" dialog box and return the path to the selected file
	if root.filename == "":
		root.filename = 'None'
	gcode_lable.config(text = root.filename)

def run():
	try:
		float(zheight_box.get())
		if gcode_lable.cget('text') != "None":
			updateFile(gcode_lable.cget('text'),zheight_box.get())

		else:
			error.config(text='Please Pick a File First')

	except ValueError:
		error.config(text='ERROR, Please enter a number')

root = Tk()
root.title('Z Level Boost')
root.geometry('400x250')

zheight_lable = Label(root, text = 'Enter your starting Z Height')
zheight_lable.pack()

zheight_box = Entry(root, width=5)
zheight_box.pack(pady=5)

gcode_btn = Button(root, text="Pick Gcode File", command=pickFile).pack()
gcode_lable = Label(root, text= "None")
gcode_lable.pack()

run_button = Button(root, text="Run", command=run, width=10)
run_button.pack(pady=5)

error = Label(root, text='')
error.pack(pady=5)

complete = Label(root, text='')
complete.pack(pady=5)

root.mainloop()

