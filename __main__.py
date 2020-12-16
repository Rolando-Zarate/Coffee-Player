#import pygame
import tkinter,webbrowser
from tkinter import filedialog,messagebox,ttk
from tkinter import *
class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.resizable(False,False)
        self.root.geometry("400x300")
        self.vol = tkinter.IntVar()
main = Main()
class Actions:
    def loadFile(self):
        pass
    def about(self):
        aboutWin = tkinter.Tk()
        aboutWin.geometry("300x255")
        aboutWin.resizable(False,False)
        aboutText = tkinter.Text(aboutWin,height=11,font="Calibri,15")
        aboutText.pack()
        aboutText.insert("1.0","Coffee Player is a free music ")
        ttk.Separator(aboutWin).place(x=0, y=213, relwidth=1)
        exitButton = ttk.Button(aboutWin,text="Exit",command=lambda:aboutWin.destroy())
        exitButton.place(x=215,y=222)
        print(exitButton.cget("text"))
        ttk.Button(aboutWin,text="Visit our website",command=lambda:webbrowser.open("https://rolando-zarate.github.io/Cat-Software-Page/")).place(x=110,y=222)
        aboutWin.mainloop()
    def vol(self,catsoftware):#The reason by the parameter cat software is because tkinter scales will make an error 'function rolando takes 1 arguments but 0 were given'
        print(main.vol.get())
    def play(self):
        pass
    def next(self):
        pass
    def previous(self):
        pass
    def repeat(self):
        pass
    def stop(self):
        pass
    def unstop(self):
        pass
actions = Actions()
class Widgets:
    def __init__(self):
        ttk.Label(main.root,text="CoffeePlayer").place(x=0,y=0)
        #Menubar
        self.volScale = ttk.Scale(main.root,from_=0, to=100,variable=main.vol,command=actions.vol)
        self.volScale.set(main.vol.get())
        self.volScale.pack()

        self.buttonPlay = ttk.Button(main.root,text="Play")
        self.buttonPlay.pack()

        self.button = ttk.Button(main.root,text="Play")
        self.button.pack()

        self.menubar = tkinter.Menu(main.root)
        self.files = tkinter.Menu(self.menubar,tearoff=False)
        self.settings = tkinter.Menu(self.menubar,tearoff=False)
        self.about = tkinter.Menu(self.menubar,tearoff=False)
        self.menubar.add_cascade(label="File menu",menu=self.files)
        self.menubar.add_cascade(label="Settings",menu=self.settings)
        self.menubar.add_cascade(label="About CoffeePlayer",menu=self.about)
        self.about.add_command(label="About",command=actions.about)
        main.root.configure(menu=self.menubar)
widgets = Widgets()
main.root.mainloop()
