'''Hangman game with gui. Used tkinter and python 3.4. Author Jiri Roznovjak'''

from tkinter import *
import random
import os
import glob

class HangMan:
	'''Class that runs gui and game logic'''
	def __init__(self):
		pass
	def accessOptions(self):
		'''Accesses folder with the list of topics and stores the names'''
		optionsPath = 'Data\Words\*.txt' #path to the lists of words
		optionNames = glob.glob(optionsPath) #gets names of lists
		self.options = []
		for x in optionNames:
			x = (x.split('\\'))
			x = re.sub(r'.txt$','',x[len(x)-1])
			self.options.append(x)

	def runInitialWindow(self):
		'''initial window, selection of a topic at the start of the program'''
		startWindow = Tk()
		startWindow.resizable(width=FALSE, height=FALSE)
		frameOptions = LabelFrame(startWindow,text='Choose a Topic',labelanchor=N)
		frameOptions.pack()
		confirm = Button(frameOptions,text='OK',width=7,command=startWindow.destroy)
		confirm.pack()
		
		v = StringVar()
		v.set(None)
		selection = str
		for word in self.options:
			Radiobutton(frameOptions,text=word,variable=v,value = word,command=lambda:selection(sel(data))).pack()
		geometry = '200x'+str(30+30*len(self.options))
		startWindow.geometry(geometry)
		startWindow.mainloop()
		

	def run(self):
		'''method called at the end, wraps up the methods and runs the program'''
		self.accessOptions()
		self.runInitialWindow()


try:
	game = HangMan()
	game.run()
except Exception as e:
	print (e)


input()