'''Hangman game with gui. Used tkinter and python 3.4. Author Jiri Roznovjak'''

from tkinter import *
import random
import os
import glob

class HangMan:
	'''Class that runs gui and game logic'''
	def __init__(self):
		self.currentWords = []
		self.topic = ''
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
		
		frameOptions = LabelFrame(startWindow,text='Choose a Topic',labelanchor=N)
		frameOptions.pack()
		confirm = Button(frameOptions,text='OK',width=7,command=startWindow.destroy)
		confirm.pack()
		label = Label(startWindow)
		label.pack()
		self.v = StringVar()
		self.v.set(None)
		for word in self.options:
			Radiobutton(frameOptions,text=word,variable=self.v,value = word).pack()
		geometry = '200x'+str(30+30*len(self.options))
		startWindow.geometry(geometry)
		startWindow.resizable(width=FALSE, height=FALSE)
		startWindow.mainloop()
	
	def runMainWindow(self):
		'''runs the main window'''
		self.topic = self.v.get() #gets what topic I chose at the initial window.
		self.mainWindow = Tk()
		self.mainWindow.mainloop()

	def run(self):
		'''method called at the end, wraps up the methods and runs the program'''
		self.accessOptions()
		self.runInitialWindow()
		self.runMainWindow()


try:
	game = HangMan()
	game.run()
except Exception as e:
	print (e)


input()