#coding: utf-8
import sys
import os
import tkinter
from tkinter import*
#from PIL import ImageTk,Image

#Janela

mae = Tk()
mae.geometry('1024x768')
mae.title('Par Perfeito®')

#icone app
img = tkinter.PhotoImage(file='icone.gif')
mae.tk.call('wm', 'iconphoto', mae._w, img)

#Imagem de Fundo
button_image = PhotoImage(file="fundo.gif")
ok_button = Button(mae, text="ok",image=button_image,compound=LEFT)
ok_button.grid()
canvasWidth=1024
canvasHeight=720


#Texto1

nome= Label(mae, text='Nome', font=('Digital dream', 20), fg='black', bg='light blue')
nome.place(x='100',y='70')

entrada = Entry(mae, width= '50', textvariable = nome).place(x='100',y='120')

#Botão de Busca

def comandobusca ():
    busca = nome.get()
    buscafeita = Label(mae, text='Concluído', fg='black', bg='white').place(x='200',y='300')
    return

botão = Button(mae,text = 'Buscar', fg='black', bg='white', command= comandobusca)
botão.place(x='430',y='115')
botão.pack

#Texto2

nome= Label(mae, text='Aqui, voce encontra seu Par Perfeito®!', font=('Digital dream', 20), fg='black')
nome.place(x='100',y='230')

nome= Label(mae, text='Julian Vitor©', font=('Arial', 12), fg='black')
nome.place(x='900',y='500')


nome= Label(mae, text='2017.', font=('Arial', 12), fg='black', bg='light blue')
nome.place(x='20',y='500')






mae.mainloop()
