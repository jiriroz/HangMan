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
		self.alreadyGuessed = [] #all already guessed words (right and wrong)
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
		path = 'Data\Words\ '
		os.chdir(path)
		title = self.topic + '.txt'
		wordFile = open(title,'r')
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
		#del ag[0:len(ag)]
		self.alreadyGuessed = []
		#hangman.delete(ALL)
		i = random.randint(0,len(self.wordList))
		self.currentWord = (self.wordList[i-1])
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
	
	def getTopic(self):
		'''gets what topic I chose at the initial window.'''
		self.topic = self.v.get()
		
	def runMainWindow(self):
		'''runs up the main window'''
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
		
		self.wordField = Canvas(self.mainWindow, width = 590,height=120,bg = 'white',highlightthickness=0) #canvas with the unknown word
		self.wordField.place(x=180,y=445)
		
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

	def drawLetters(self):
		""" draws the word that I'm guessing """
		word = self.currentWord
		self.wordField.delete(ALL)
		y = 70 #y-coordinate of the line
		l_h = 25 #how high above the line will the letter be
		offset = 20 #offset of the first letter from the margin
		space = 10 #space between the letters
		lineWidth = 20 #width of the line
		height = 20 #height of the letters
		wordcount = 0
		lettercount = 0
		maxlen = 0
		ct = -1
		if len(word) > 18: #if the lenght is bigger, split it into two lines
			test = word.split(' ')
			for x in test:
				lettercount += len(x)+1
				if lettercount > 18:
					break
				wordcount +=1
			for x in range(wordcount):
				maxlen +=(1+len(test[x]))
			for n in range(maxlen):
				state = 'hidden'
				if (word[n] in self.alreadyGuessed)or(word[n] in "-!,'?;."):
					state = 'normal'
				if word[n] in " -?!';.,":
					stateline = 'hidden'
				else:
					stateline = 'normal'
				y1 = y-30
				self.wordField.create_line(offset+n*(lineWidth+space),y1,offset+n*(lineWidth+space)+lineWidth,y1,width=1,state=stateline)
				self.wordField.create_text(offset+n*(lineWidth+space)+lineWidth/2,y1-l_h/2,text=word[n],font=('Times',height),state=state)
			for n in range(maxlen,len(word)):
				ct +=1
				state = 'hidden'
				if (word[n] in self.alreadyGuessed)or(word[n] in "-!,'?;."):
					state = 'normal'
				if word[n] in " -?!';.,":
					stateline = 'hidden'
				else:
					stateline = 'normal'
				y2 = y+20
				self.wordField.create_line(offset+ct*(lineWidth+space),y2,offset+ct*(lineWidth+space)+lineWidth,y2,width=1,state=stateline)
				self.wordField.create_text(offset+ct*(lineWidth+space)+lineWidth/2,y2-l_h/2,text=word[n],font=('Times',height),state=state)        
		else:
			for n in range(len(word)):
				state = 'hidden'
				if (word[n] in self.alreadyGuessed)or(word[n] in "-!,'?;."):
					state = 'normal'
				if word[n] in " -?!';.,":
					stateline = 'hidden'
				else:
					stateline = 'normal'
				self.wordField.create_line(offset+n*(lineWidth+space),y,offset+n*(lineWidth+space)+lineWidth,y,width=1,state=stateline) #vytvoreni car pod pismeny
				self.wordField.create_text(offset+n*(lineWidth+space)+lineWidth/2,y-l_h/2,text=word[n],font=('Times',height),state=state) #vytvoreni pismena    


	def run(self):
		'''method called at the end, wraps up the methods and runs the program'''
		self.accessOptions()
		self.runInitialWindow()
		self.getTopic()
		self.loadWords()
		self.randomWord()
		self.runMainWindow()
		self.drawLetters()
		self.mainWindow.mainloop()

try:
	game = HangMan()
	game.run()
except Exception as e:
	print (e)


input()