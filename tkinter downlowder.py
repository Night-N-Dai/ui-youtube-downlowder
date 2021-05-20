from future.moves import tkinter
from tkinter import *
from pytube import YouTube
root = Tk()
root.geometry('500x300')
root.resizable(0,0)

#the main title of the program
root.title("YouTube Downlowder")
Label(root,text = 'Youtbe video downlowder' , font = 'arial 20 bold').pack
link = StringVar()

#the label up the downlowd faild
Label(root, text='Paste Link Here', font='arial 15 bold').place(x=160,y=60)

#the downlowd faild
link_enter = Entry(root, width = 70, textvariable = link).place(x= 32,y=90)

#the main downlowd def
def Downlowder():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    Label(root,text = 'DOWNLOWADED',font='arial 15').place(x=180,y=210)

#the downlowd button
Button(root,text='Downlowd',font='arial 15',bg='blue',padx=2,command=Downlowder).place(x=180,y=180)
root.mainloop()