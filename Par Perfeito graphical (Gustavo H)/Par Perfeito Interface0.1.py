#coding: utf-8
import sys
import os
from tkinter import *
import tkinter

#Janela

i = Tk()
i.geometry('1024x720')
i.title('Par Perfeito®')

#icone app
img = tkinter.PhotoImage(file='icone.gif')
i.tk.call('wm', 'iconphoto', i._w, img)

#Texto1

nome= Label(i, text='Nome', font=('Digital dream', 20), fg='black', bg='white')
nome.place(x='100',y='70')

entrada = Entry(i, width= '50', textvariable = nome).place(x='100',y='120')




i.mainloop()
