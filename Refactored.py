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
		'''Accesses folder with the list of topics and returns them'''
		
	def runInitialWindow(self):
		'''initial window, selection of a topic at the start of the program'''
		startWindow = Tk()
		startWindow.resizable(width=FALSE, height=FALSE)
		startWindow.mainloop()
	def run(self):
		'''method called at the end, wraps up the methods and runs the program'''
		self.runInitialWindow()


try:
	game = HangMan()
	game.run()
except Exception as e:
	print (e)


input()