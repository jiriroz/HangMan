'''Hangman game with gui. Used tkinter and python 3.4. Author Jiri Roznovjak'''

from tkinter import *
import random
import os
import glob

class HangMan:
	'''Class that runs gui and game logic'''
	def __init__(self):
		self.currentWords = []
		self.topic = '' #current topic
		self.wordList = []
		self.currentWord = ''
	def loadPictures(self):
		'''loads pictures of hangman'''
		path = 'Data\Pictures\ '
		os.chdir(path)
		self.images = []
		for x in range(1,12):
			name = str(x)+'.gif'
			self.images.append(PhotoImage(file=name))
	def loadWords(self):
		'''loads and stores words from a certain topic'''
		path = '\Data\Words\ '
		os.chdir(path)
		title = self.topic + '.txt'
		wordFile = open(nazev,'r')
		wordList = wordFile.read()
		wordFile.close()
		wordList = wordList.split('\n')
		self.wordList = wordList
	def randomWord(self):
		'''chooses a random word from the current topic'''
		#tlacitko.config(state='disabled')
		#vstup.config(state='normal')
		#seznam = database(variable)
		#ag = data['ag']
		#uzhadany = data['uzhadany']
		#del ag[0:len(ag)]
		#del uzhadany[0:len(uzhadany)]
		#hangman.delete(ALL)
		i = random.randint(0,len(self.wordList))
		self.currentWord = (self.WordList[i-1])
		#pismena(slovo)
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
		startWindow.title('Hang Man')
		
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
		'''runs up the main window'''
		self.topic = self.v.get() #gets what topic I chose at the initial window.
		if self.topic == "None":
			sys.exit(0) #if no topic chosen, closes the program
		
		self.mainWindow = Tk()
		self.mainWindow.geometry('800x600')
		self.mainWindow.resizable(width=FALSE, height=FALSE)
		self.mainWindow.title('Hang Man')
		
		background = Canvas(self.mainWindow,width=800, height=600, highlightthickness=0,bg='#FFEBD6')
		background.pack(anchor=NW)
		
		hangmanCanvas = Canvas(self.mainWindow,width = 750,height = 400,bg = 'white',highlightthickness=0) #canvas with the pic of hangman
		hangmanCanvas.place(x=20,y=40)
		
		wordField = Canvas(self.mainWindow, width = 590,height=120,bg = 'white',highlightthickness=0) #canvas with the unknown word
		wordField.place(x=180,y=445)
		
		#nextWord = Button(okno,text = 'Next Word',command=lambda:slovo(vybrat_nahodne_slovo(data)),highlightthickness=0) #dalsi slovo
		#nextWord.place(x=20,y=15) need to implement random word first
		
		entryFrame = LabelFrame(self.mainWindow,text = 'Enter a Letter',relief = FLAT,bg='#FFEBD6') #frame that contains field where the letters are entered
		entryFrame.place(x = 45,y = 475)
		
		entryField = Entry(entryFrame,width=5,relief='sunken',font=('Times',14),state='normal')
		entryField.pack()
		entryField.focus_set()
		#entryField.bind('<Return>',enter) need to implement the enter function first
		
		topicVar = StringVar(self.mainWindow)
		topicVar.set(self.topic)
		changeTopic = OptionMenu(self.mainWindow,topicVar,*self.options)
		changeTopic.config(highlightthickness=0)
		changeTopic.place(x=770,y=12,anchor=NE)
		
		confirmLetter = Button(entryFrame,text='OK') #need to add the command to proceed the letter
		confirmLetter.pack()
		
		
		
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