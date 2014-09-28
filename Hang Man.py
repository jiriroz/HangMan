﻿'''Hangman game with gui. Used tkinter and python 3.4. Author Jiri Roznovjak'''

from tkinter import *
import random
import os
import glob

path = os.getcwd()
ag = [] #seznam uz hadanych spatnych pismen
uzhadany = [] #vsechna uz hadana pismena
pocet = []
data = {}
data['ag'] = ag
data['uzhadany'] = uzhadany

def diakritika(nahrada): #REF
    def nahradit(nahrada,x,y):
        x = '[' + x + ']'
        nahrada = re.sub(x,y,nahrada)
        return nahrada
    nahrada = nahradit(nahrada,'á','a')
    nahrada = nahradit(nahrada,'ěé','e')
    nahrada = nahradit(nahrada,'í','i')
    nahrada = nahradit(nahrada,'óö','o')
    nahrada = nahradit(nahrada,'úůü','u')
    nahrada = nahradit(nahrada,'ý','y')
    nahrada = nahradit(nahrada,'š','s')
    nahrada = nahradit(nahrada,'č','c')
    nahrada = nahradit(nahrada,'ř','r')
    nahrada = nahradit(nahrada,'ž','z')
    nahrada = nahradit(nahrada,'ť','t')
    nahrada = nahradit(nahrada,'ň','n')
    nahrada = nahradit(nahrada,'ď','d')
    return nahrada

def letter(data): #REF
    #zpracovani zadaneho pismena a vypsani uz hadanych pismen
    slovo = data['slovo']
    ag = data['ag']
    uzhadany = data['uzhadany']
    slovo_test = slovo.lower()
    slovo_test = diakritika(slovo_test)
    pismeno = (vstup.get()).lower()
    vstup.delete(0,END)
    if (pismeno in uzhadany) or (pismeno not in 'abcdefghijklmnopqrstuwvxyz0123456789') or ((len(pismeno)) != 1)or(len(ag)==11):
        vstup.delete(0,END)
        return
    uzhadany+=pismeno
    uzhadany+=pismeno.upper()
    if pismeno == 'a':uzhadany+='áäAÄ'
    elif pismeno == 'e':uzhadany+='éëěÉĚË'
    elif pismeno == 'i':uzhadany+='íÍ'   
    elif pismeno == 'o':uzhadany+='óöÓÖ'   
    elif pismeno == 'u':uzhadany+='ůúüÚŮÜ'    
    elif pismeno == 'y':uzhadany+='ýÝ'
    elif pismeno == 'r':uzhadany+='řŘ'
    elif pismeno == 's':uzhadany+='šŠ'
    elif pismeno == 't':uzhadany+='ťŤ'
    elif pismeno == 'z':uzhadany+='žŽ'
    elif pismeno == 'd':uzhadany+='ďĎ'
    elif pismeno == 'c':uzhadany+='čČ'
    elif pismeno == 'n':uzhadany+='ňŇ'
    if pismeno in slovo_test: #kdyz se trefi
        pismena(slovo,uzhadany)
        hlp = 0
        for x in list(slovo):
            if x in uzhadany:
                hlp +=1
        if hlp == len(''.join(re.split("[ -?!;.,]",slovo))): #test, jestli uz vyhral
            hangman.create_text(275,200,text='Vyhrál jsi!',fill='red',font=('Times',28))
            tlacitko.config(state='active')
            vstup.config(state='disabled')
    else: #kdyz se netrefi
        ag.append(pismeno.upper())
        agprint = ', '.join(ag)
        hangman.create_text(20,375,text=agprint,font = ('Times,14'),anchor = NW)
        hangman.create_image(0,0,anchor=NW,image=list_of_images[len(ag)-1])
        if len(ag) == 11:
            hangman.create_text(275,200,text='Game Over',fill='red',font=('Times',28))
            uzhadany.extend(list(slovo))
            pismena(slovo,uzhadany)
            vstup.config(state='disabled')
            tlacitko.config(state='active')
    
def database(*args): #precte seznamy slov REF
    slova_path = r'' + path + '\Data\Words\ '
    os.chdir(slova_path)
    nazev = variable.get() + '.txt'
    fo = open(nazev,'r')
    seznam = fo.read()
    fo.close()
    seznam = seznam.split('\n')
    return seznam
    
def vybrat_nahodne_slovo(data): #zmacknutim tlacitka vybere nahodne slovo z databaze REF
    tlacitko.config(state='disabled')
    vstup.config(state='normal')
    seznam = database(variable)
    ag = data['ag']
    uzhadany = data['uzhadany']
    del ag[0:len(ag)]
    del uzhadany[0:len(uzhadany)]
    hangman.delete(ALL)
    a = random.randint(0,len(seznam))
    slovo= (seznam[a-1])
    pismena(slovo)
    data['slovo'] = slovo
    
def pismena(slovo,*uzhadany): #REF
    uzhadany = list(*uzhadany)
    hadanka_canvas.delete(ALL)
    y = 70 #y-souradnice umisteni line
    l_h = 25 #jak vysoko nad line bude letter
    okraj = 20 #odsazeni prvniho pismena od okraje
    mezera = 10 #mezera mezi pismeny
    sirka = 20 #sirka line
    height = 20 #velikost textu
    wordcount = 0
    lettercount = 0
    maxlen = 0
    ct = -1
    if len(slovo) > 18: #dosazeni rozdelovani na dva radky
        test = slovo.split(' ')
        for x in test:
            lettercount += len(x)+1
            if lettercount > 18:
                break
            wordcount +=1
        for x in range(wordcount):
            maxlen +=(1+len(test[x]))
        for n in range(maxlen):
            state = 'hidden'
            if (slovo[n] in uzhadany)or(slovo[n] in "-!,'?;."):
                state = 'normal'
            if slovo[n] in " -?!';.,":
                stateline = 'hidden'
            else:
                stateline = 'normal'
            y1 = y-30
            hadanka_canvas.create_line(okraj+n*(sirka+mezera),y1,okraj+n*(sirka+mezera)+sirka,y1,width=1,state=stateline)
            hadanka_canvas.create_text(okraj+n*(sirka+mezera)+sirka/2,y1-l_h/2,text=slovo[n],font=('Times',height),state=state)
        for n in range(maxlen,len(slovo)):
            ct +=1
            state = 'hidden'
            if (slovo[n] in uzhadany)or(slovo[n] in "-!,'?;."):
                state = 'normal'
            if slovo[n] in " -?!';.,":
                stateline = 'hidden'
            else:
                stateline = 'normal'
            y2 = y+20
            hadanka_canvas.create_line(okraj+ct*(sirka+mezera),y2,okraj+ct*(sirka+mezera)+sirka,y2,width=1,state=stateline)
            hadanka_canvas.create_text(okraj+ct*(sirka+mezera)+sirka/2,y2-l_h/2,text=slovo[n],font=('Times',height),state=state)        
    else:
        for n in range(len(slovo)):
            state = 'hidden'
            if (slovo[n] in uzhadany)or(slovo[n] in "-!,'?;."):
                state = 'normal'
            if slovo[n] in " -?!';.,":
                stateline = 'hidden'
            else:
                stateline = 'normal'
            hadanka_canvas.create_line(okraj+n*(sirka+mezera),y,okraj+n*(sirka+mezera)+sirka,y,width=1,state=stateline) #vytvoreni car pod pismeny
            hadanka_canvas.create_text(okraj+n*(sirka+mezera)+sirka/2,y-l_h/2,text=slovo[n],font=('Times',height),state=state) #vytvoreni pismena    

def enter(event): #REF
    letter(data)

def sel(data): #REF
    selection = v.get()
    data['selection'] = selection

podokno = Tk() #vyber tematu pred zahajenim hry REF
moznosti_path = 'Data\Words\*.txt' #cesta k souborum kde se nachazeji seznamy slov REF
moznosti0 = glob.glob(moznosti_path) #REF
moznosti = [] #REF
for x in moznosti0: #timto dostaneme list s nazvy seznamu slov
    x = (x.split('\\')) #REF
    x = re.sub(r'.txt$','',x[len(x)-1]) #REF
    moznosti.append(x) #REF
ram_vyber = LabelFrame(podokno,text='Choose a Topic',labelanchor=N) #REF
ram_vyber.pack() #REF
v = StringVar() #REF
v.set(None) #REF
selection = str #REF
for text in moznosti: #REF
    Radiobutton(ram_vyber,text=text,variable =v,value = text,command=lambda:selection(sel(data))).pack()
potvrdit = Button(ram_vyber,text='OK',width=7,command = podokno.destroy) #REF
potvrdit.pack() #REF
label = Label(podokno) #REF
label.pack() #REF
geometry = '200x'+str(30+30*len(moznosti)) #REF
podokno.geometry(geometry) #REF
podokno.resizable(width=FALSE, height=FALSE) #REF
podokno.mainloop() #REF

okno = Tk() #REF

try:  #REF
    selection = data['selection']  #REF
except Exception:  #REF
    sys.exit(0)  #REF


#obrazky
obrazky_path = 'Data\Pictures\ ' #REF
os.chdir(obrazky_path) #REF
list_of_images = [] #REF
for x in range(1,12): #REF
    name = str(x)+'.gif' #REF
    list_of_images.append(PhotoImage(file=name)) #REF


pozadi = Canvas(width=800, height=600, highlightthickness=0,bg='#FFEBD6') #REF
pozadi.pack(anchor=NW) #REF

variable = StringVar(okno) #REF
variable.trace('w',database) #REF
variable.set(selection) #REF
t = OptionMenu(okno,variable,*moznosti) #REF
t.config(highlightthickness=0) #REF
t.place(x=770,y=12,anchor=NE) #REF

hangman = Canvas(okno,width = 750,height = 400,bg = 'white',highlightthickness=0) #obrazek hangmana REF
hangman.place(x=20,y=40) #REF

slovo = str
hadanka_canvas = Canvas(okno, width = 590,height=120,bg = 'white',highlightthickness=0) #prazdne pismena, ktere se hadaji #REF
hadanka_canvas.place(x=180,y=445) #REF


tlacitko = Button(okno,text = 'Next Word',command=lambda:slovo(vybrat_nahodne_slovo(data)),highlightthickness=0) #dalsi slovo REF
tlacitko.place(x=20,y=15) #REF


entry_ram = LabelFrame(okno,text = 'Enter a Letter',relief = FLAT,bg='#FFEBD6') #pole, kde se zadavaji pismena REF
entry_ram.place(x = 45,y = 475) # REF

vstup = Entry(entry_ram,width=5,relief='sunken',font=('Times',14),state='normal') # REF
vstup.pack() # REF
vstup.focus_set() # REF
vstup.bind('<Return>',enter) # REF

pismeno = str # REF
vstup_tlacitko = Button(entry_ram,text='OK',command =lambda:pismeno(letter(data))) # REF
vstup_tlacitko.pack() # REF

vybrat_nahodne_slovo(data)


okno.title('Hang Man')  # REF
okno.mainloop() #REF
