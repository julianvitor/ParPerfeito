#coding: utf-8
import sys
import os
import tkinter
from tkinter import*


#Janela

mae = Tk()
mae.geometry('1024x720')
mae.title('Par Perfeito®')

#icone app
img = tkinter.PhotoImage(file='icon.gif')
mae.tk.call('wm', 'iconphoto', mae._w, img)

#Texto1

nome= Label(mae, text='Nome', font=('Digital dream', 20), fg='black', bg='white')
nome.place(x='100',y='70')

entrada = Entry(mae, width= '50', textvariable = nome).place(x='100',y='120')




mae.mainloop()
