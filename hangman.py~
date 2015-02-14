'''Hangman game with gui. Used tkinter and python 3.4. Author Jiri Roznovjak'''

from tkinter import *
import random
import os
import glob

CZECH = {'á':'a','é':'e','ě':'e','í':'i','ó':'o','ú':'u','ů':'u','ý':'y','š':'s',
         'č':'c','ř':'r','ž':'z','ň':'n','ť':'t','ĺ':'l','ď':'d'}

class HangMan:
	'''Class that runs gui and game logic'''
	def __init__(self):
		self.path = os.getcwd()
		self.currentWords = []
		self.topic = '' #current topic
		self.wordList = []
		self.currentWord = ''
		self.alreadyGuessed = [] #all already guessed letters (right and wrong)
		self.alreadyGuessedWrong = [] #wrong already guessed letters (for display)
		self.images = []
		
	def accessOptions(self):
		'''Accesses folder with the list of topics and stores the names'''
		optionsPath = 'Data\Words\*.txt' #path to the lists of words
		optionNames = glob.glob(optionsPath) #gets names of lists
		self.options = []
		for x in optionNames:
			x = (x.split('\\'))
			x = re.sub(r'.txt$','',x[len(x)-1])
			self.options.append(x)
		
	def loadPictures(self):
		'''loads pictures of hangman'''
		path = r'' + self.path + '\Data\Pictures\ '
		os.chdir(path)
		for x in range(1,12):
			name = str(x)+'.gif'
			self.images.append(PhotoImage(file=name))
			
	def loadWords(self):
		'''loads and stores words from a certain topic'''
		path = r'' + self.path + '\Data\Words\ '
		os.chdir(path)
		title = self.topic + '.txt'
		wordFile = open(title,'r')
		wordList = wordFile.read()
		wordFile.close()
		wordList = wordList.split('\n')
		self.wordList = wordList
		
	def randomWord(self):
		'''chooses a random word from the current topic'''
		i = random.randint(0,len(self.wordList))
		self.currentWord = (self.wordList[i-1])
		
	def newWord(self):
		'''called after click on next word button. Deletes canvas, chooses new word'''
		self.checkTopic()
		self.nextWord.config(state='disabled')
		self.entryField.config(state='normal')
		self.alreadyGuessed = []
		self.alreadyGuessedWrong = []
		self.hangmanCanvas.delete(ALL)
		self.randomWord()
		self.drawLetters()
	
	def runInitialWindow(self):
		'''initial window, selection of a topic at the start of the program'''
		startWindow = Tk()
		startWindow.title('Hang Man')
		frameOptions = LabelFrame(startWindow,text='Choose a Topic',labelanchor=N)
		frameOptions.pack()
		self.topicVar = StringVar()
		self.topicVar.set(None)
		for word in self.options:
			Radiobutton(frameOptions,text=word,variable=self.topicVar,value = word).pack()
		confirm = Button(frameOptions,text='OK',width=7,command=startWindow.destroy)
		confirm.pack()
		geometry = '200x'+str(30+30*len(self.options))
		startWindow.geometry(geometry)
		startWindow.resizable(width=FALSE, height=FALSE)
		startWindow.mainloop()
	
	def getTopic(self):
		'''gets what topic I chose at the initial window.'''
		return self.topicVar.get()
		
	def runMainWindow(self):
		'''runs up the main window. Need to call window mainloop separately after this'''
		self.mainWindow = Tk()
		self.mainWindow.geometry('800x600')
		self.mainWindow.resizable(width=FALSE, height=FALSE)
		self.mainWindow.title('Hang Man')
		
		background = Canvas(self.mainWindow,width=800, height=600, highlightthickness=0,bg='#FFEBD6')
		background.pack(anchor=NW)
		
		self.hangmanCanvas = Canvas(self.mainWindow,width = 750,height = 400,bg = 'white',highlightthickness=0)   			#canvas with the pic of hangman
		self.hangmanCanvas.place(x=20,y=40)
		
		self.wordField = Canvas(self.mainWindow, width = 590,height=120,bg = 'white',highlightthickness=0) 			#canvas with the unknown word
		self.wordField.place(x=180,y=445)
		
		self.nextWord = Button(self.mainWindow,text = 'Next Word',command=self.newWord,highlightthickness=0,state='disabled') #next word button
		self.nextWord.place(x=20,y=15)
		#frame that contains field where the letters are entered
		entryFrame = LabelFrame(self.mainWindow,text = 'Enter a Letter',relief = FLAT,bg='#FFEBD6')
		entryFrame.place(x = 45,y = 475)
		
		self.entryField = Entry(entryFrame,width=5,relief='sunken',font=('Verdana',14),state='normal')
		self.entryField.pack()
		self.entryField.focus_set()
		self.entryField.bind('<Return>',self.proceedLetterEvent)
		
		self.topicVar = StringVar(self.mainWindow)
		self.topicVar.set(self.topic)
		changeTopic = OptionMenu(self.mainWindow,self.topicVar,*self.options)
		changeTopic.config(highlightthickness=0)
		changeTopic.place(x=770,y=12,anchor=NE)
		
		confirmLetter = Button(entryFrame,text='OK',command=self.proceedLetter)
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
				self.wordField.create_line(offset+n*(lineWidth+space),y,offset+n*(lineWidth+space)+lineWidth,y,width=1,state=stateline) #lines under letters
				self.wordField.create_text(offset+n*(lineWidth+space)+lineWidth/2,y-l_h/2,text=word[n],font=('Times',height),state=state) #letter 

	def replaceCzech(self,word):
		'''takes a word and replaces all czech letters with their english equivalent'''
		word = list(word)
		for x in range(len(word)):
			if word[x] in CZECH:
				word[x] = CZECH[word[x]]
		return ''.join(word)

	def proceedLetterEvent(self,event):
		self.proceedLetter()

	def proceedLetter(self):
		'''proceeds the entered letter'''
		word = self.currentWord
		word_test = word.lower()
		word_test = self.replaceCzech(word_test)
		letter = (self.entryField.get()).lower()
		self.entryField.delete(0,END)
		if (letter in self.alreadyGuessed) or (letter not in 'abcdefghijklmnopqrstuwvxyz0123456789') or ((len(letter)) != 1):
			return #return if the letter has been already guessed or is not in the alphabet
		self.alreadyGuessed+=letter
		self.alreadyGuessed+=letter.upper()
		for let in CZECH:
			if letter == CZECH[let]:
				self.alreadyGuessed+=let
				self.alreadyGuessed+=let.upper()
				break
		if letter in word_test: #if the letter is correct
			self.drawLetters()
			hlp = 0
			for x in list(word):
				if x in self.alreadyGuessed:
					hlp +=1
			if hlp == len(''.join(re.split("[ -?!;.,]",word))): #if the game if won
				self.youWin()
				self.endGame()
		else: #if the letter is wrong
			self.alreadyGuessedWrong.append(letter.upper())
			self.drawAlreadyGuessed()
			self.drawHangman()
			if len(self.alreadyGuessedWrong) == 11: #if the game is lost
				self.youLose()
				self.endGame()
				self.alreadyGuessed.extend(list(word))
				self.drawLetters()
				
	
	def drawHangman(self):
		'''draws the picture of hangman'''
		self.hangmanCanvas.create_image(0,0,anchor=NW,image=self.images[len(self.alreadyGuessedWrong)-1])
	
	def drawAlreadyGuessed(self):
		'''draws already guessed letters'''
		agprint = ', '.join(self.alreadyGuessedWrong)
		self.hangmanCanvas.create_text(20,375,text=agprint,font = ('Verdana,14'),anchor = NW)
				
	def youWin(self):
		'''called after the whole word is guessed'''
		self.hangmanCanvas.create_text(275,200,text='You win!',fill='red',font=('Verdana',40))
	
	def youLose(self):
		'''called after you run out of attempts'''
		self.hangmanCanvas.create_text(275,200,text='Game Over',fill='red',font=('Verdana',40))

	def endGame(self):
		'''after the game ends, configures widgets and checks if the topic has been changed'''
		self.nextWord.config(state='active')
		self.entryField.config(state='disabled')

	def checkTopic(self):
		'''checks if the topic has been changed and if it has, loads the new one'''
		if self.topic != self.getTopic():
			self.topic = self.getTopic()
			self.loadWords()
	
	def run(self):
		'''method called at the end, wraps up the methods and runs the program'''
		self.accessOptions()
		self.runInitialWindow()
		self.topic = self.getTopic()
		if self.topic == "None":
			sys.exit(0) #if no topic chosen, closes the program
		self.loadWords()
		self.randomWord()
		self.runMainWindow()
		self.loadPictures()
		self.drawLetters()
		self.mainWindow.mainloop()

game = HangMan()
game.run()
