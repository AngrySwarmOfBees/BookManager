#Python
#Author : Bee Mowery
#Outline : ~/LibraryManagerOutline.md

#Package Setup
import json
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import tkinter.font as TkFont
from PIL import Image, ImageTk
from turtle import bgcolor, color, left, right, width
from pathlib import Path
from datetime import datetime




#globals
#global MainCanvasItems = []
global SideMenuPanel
global LaunchArgument
global DocPath
global FileName
global FileType
global FileInfo
global BookList
global BookData

#nonglobals

#--UI-----------------------------------
#UI Setup
Root = Tk() #initialize window

#UI Style Setup
HeaderFont = TkFont.Font(family="SF Pro Display", size=16, weight="bold")     #Initialize Font standard for headers
BodyFont = TkFont.Font(family="San Fransisco", size=14, weight="normal")    #initialize font standard for body text
SubBodyFont = TkFont.Font(family="San Fransisco", size=5, weight="normal")
DarkModeStyle = ttk.Style()
DarkModeStyle.configure("Dark.Mode", foreground='#bb86fc')
LightModeStyle = ttk.Style()
LightModeStyle.configure("Light.Mode", foreground='#6200ee')
Root.title("Library Manager")   #set window title   
Root.geometry('960x540+50+50')    #set window default size
Root.configure(bg="#121212")  #set background color(default dark mode)
Root.resizable(False, False)
Root.geometry('960x540+50+50')    #set window default size
Root.configure(bg="#121212")  #set background color(default dark mode)
Root.resizable(True, True)

#functions for buttons
def PlaceholderFunc():
    print("Button pressed")

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        # initialize the new_state
        self.new_state = 'normal'

        self.parent.bind('<Configure>', self._resize_handler)

    def _resize_handler(self, event):
        self.old_state = self.new_state # assign the old state value
        self.new_state = self.parent.state() # get the new state value

        if self.new_state == 'zoomed':
            print('maximize event')
        elif self.new_state == 'normal' and self.old_state == 'zoomed':
            print('restore event')
        else:
            #print('dragged resize event')
            #Update items
            Root.update()
            #Menu Bar---------------------------------------------------------------------------------------
            SideMenuPanel.config(height=(Root.winfo_height()))
            SideBarAddNewBookButton.place(x=0, y=0, relwidth="1", height=45)
            SideBarMenuButton.place(x=0, y=45, relwidth="1", height=45)
            SideBarFileButton.place(x=0, y=90, relwidth="1", height=45)    #update open file button
            SideBarDarkModeButton.place(x=0, y=135, relwidth="1", height=45)    #update toggle dark mode button
            SideBarSettingsButton.place(x=0, y=(Root.winfo_height() - 45), relwidth="1", height=45)   #update Settings Button


class FileManager():
    LocalSaveFile =  "Books.csv"

    def FileDialogOpen():
        global LaunchArgument
        global DocPath
        global FileName
        global FileType
        global FileInfo
        FileName = fd.askopenfilename(
            title='Select a library file',
            initialdir='/',
            filetypes=[("Comma separated value sheet", "*.csv")]
        )
        DocPath = Path(FileName)    #initializes a path refrence to the given file
        FileInfo = FileName.split(".")   #creates an array containing the split string, the latter half of the split string is the file extension
        FileType = FileInfo[1]  #saving file extension
        print(FileType)
        #OpenFile()
    def SaveData():
        global BookList
        global BookData
        with open(FileManager.LocalSaveFile, 'w') as csv_file:  
            writer = csv.writer(csv_file)
            for key, value in BookData.items():
                writer.writerow([key, value])

class BookManager():

    # csv format
    # Title, Add Date, Completeion percent
    def __init__():
        print("init book manager class")
        global BookList
        global BookData
        BookList = []
        BookData = {}
        BookDataFile = csv.reader(open(FileManager.LocalSaveFile))
        for row in BookDataFile:
            #print(row)
            BookList.append(row[0])
            BookData[row[0]] = [row[1], row[2]]
        #print(BookList)
        #Gather data from csv file and add to memory in booklist and bookdata vars
    def AddNewBook():
        global BookList
        #Add new book dialog
        NewBookName = tk.simpledialog.askstring("Book Name", "What is the name of the book?")
        print(NewBookName)
        BookList.append(NewBookName)
        BookData[NewBookName] = [str(datetime.today()), 0.0]
        print(BookData)




#Main window setup
MainCanvas = tk.Canvas(Root, background="#1F1B24", height=6, width=270, bd="0", highlightthickness="0")
MainCanvas.place(x=0, y=0, relheight="1", relwidth="1")
#placeholders
#PlaceHolderText = tk.Label(MainCanvas, text ="Placeholder", bg="#1F1B24", fg="#bb86fc", font=HeaderFont)
#PlaceHolderText.grid(row= 0, column=0)

SideMenuPanel=tk.Canvas(Root, background="#1f1f1f", height=6, width=50, bd="0", highlightthickness="0")     #Create left side bar
SideMenuPanel.pack(side=LEFT)   #add left side bar
SideBarAddNewBookButton=tk.Button(SideMenuPanel, text="+", command=BookManager.AddNewBook, bg="#1f1f1f", fg="#bb86fc", activebackground="#363636", activeforeground="#bb86fc", bd="0")
SideBarAddNewBookButton.place(x=0, y=0, relwidth="1", height=45)
SideBarMenuButton=tk.Button(SideMenuPanel, text="MB", command=PlaceholderFunc, bg="#1f1f1f", fg="#bb86fc", activebackground="#363636", activeforeground="#bb86fc", bd="0")  #Initialize Button
SideBarMenuButton.place(x=0, y=45, relwidth="1", height=45) #Place Menu button
SideBarFileButton = tk.Button(SideMenuPanel, text="FM", font=BodyFont, command=FileManager.FileDialogOpen, bg="#1f1f1f", fg="#bb86fc", activebackground="#363636", activeforeground="#bb86fc", bd="0")  #Initialize Button
SideBarFileButton.place(x=0, y=90, relwidth="1", height=45)    #Add open file button
SideBarDarkModeButton = tk.Button(SideMenuPanel, text="DM", font=BodyFont, command=FileManager.SaveData, bg="#1f1f1f", fg="#bb86fc", activebackground="#363636", activeforeground="#bb86fc", bd="0")  #Initialze button
SideBarDarkModeButton.place(x=0, y=180, relwidth="1", height=45)    #Add toggle dark mode button

#dark mode button is for saving atm

SideBarSettingsButton = tk.Button(SideMenuPanel, text="SM", font=BodyFont, command=PlaceholderFunc, bg="#1f1f1f", fg="#bb86fc", activebackground="#363636", activeforeground="#bb86fc", bd="0")  #Initialize Button
SideBarSettingsButton.place(x=0, y=480, relwidth="1", height=45)   #Place Settings Button

MyLibraryCanvas=tk.Canvas(MainCanvas, background="#1f1f1f", height=Root.winfo_height(), width=(Root.winfo_width() - 50))

App(Root).pack()
BookManager.__init__()
Root.mainloop()
