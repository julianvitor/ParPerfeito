#coding: utf-8
import sys
import os
import tkinter
from tkinter import*
#from PIL import ImageTk,Image

#Janela

mae = Tk()
mae.geometry('1024x720')
mae.title('Par Perfeito®')

#Texto1

nome= Label(mae, text='Nome', font=('Digital dream', 20), fg='black', bg='white')
nome.place(x='100',y='70')

entrada = Entry(mae, width= '50', textvariable = nome).place(x='100',y='120')

#Botão de Busca

def comandobusca ():
    busca = nome.get()
    buscafeita = Label(mae, text='Concluído', fg='black', bg='white').place(x='200',y='300')
    return

botão = Button(mae,text = 'Buscar', fg='black', bg='white', command= comandobusca)
botão.place(x='430',y='115')

#Imagem de Fundo

#image = Image.open('icone.gif')
#backgroundImage=Imagetk.PhotoImage(image)




mae.mainloop()
