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


#Variable Setup

#globals

#nonglobals

#--UI-----------------------------------
#UI Setup
Window = tk.Tk() #initialize window

#UI Style Setup
HeaderFont = TkFont.Font(family="SF Pro Display", size=16, weight="bold")     #Initialize Font standard for headers
BodyFont = TkFont.Font(family="San Fransisco", size=14, weight="normal")    #initialize font standard for body text
SubBodyFont = TkFont.Font(family="San Fransisco", size=5, weight="normal")
DarkModeStyle = ttk.Style()
DarkModeStyle.configure("Dark.Mode", foreground='#bb86fc')
LightModeStyle = ttk.Style()
LightModeStyle.configure("Light.Mode", foreground='#6200ee')
Window.title("Library Manager")   #set window title   
Window.geometry('960x540+50+50')    #set window default size
Window.configure(bg="#121212")  #set background color(default dark mode)
Window.resizable(False, False)
Window.geometry('960x540+50+50')    #set window default size
Window.configure(bg="#121212")  #set background color(default dark mode)
Window.resizable(True, True)

#Main window setup
MainCanvas = tk.Canvas(Window, background="#1F1B24", height=960, width=270, bd="0", highlightthickness="0")
MainCanvas.place(x=0, y=0, relheight="1", relwidth="1")

#placeholders
PlaceHolderText = MainCanvas.create_text(0, 0, text="Placeholder!", fill="#bb86fc", font=HeaderFont)


def UpdateWindow(newX, newY) {
    #update item locations
}



Window.mainloop()