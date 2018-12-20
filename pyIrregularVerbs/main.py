#!/usr/bin/env python
# -*- coding:Latin-1 -*-
# Pinter Balazs 18/12/15



from tkinter import *
from random import randrange

class Main(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('Rendhagyó Igék')
        menu = MenuBar(self)
        menu.grid(row=1,sticky=W,padx=3,pady=3)
        flags = Flags()
        flags.grid(row=1,sticky=E)
        surf = Surface()
        surf.grid(row=2)
        surf.new()
        self.master.configure(bg='black')
class Surface(Frame):
    def __init__(self):
        Frame.__init__(self,bg='black')

        Label(self,text='Ige :',
              bg='black',fg='white',relief=RIDGE).grid(row=1,column=1,
                                           columnspan=2,pady=2)
        self.infVar = StringVar()
        self.inf = Entry(self,textvariable=self.infVar,
                         fg='black')
        self.inf.grid(row=2,column=1,columnspan=2,
                      pady=4)

        Label(self,text='Egyszeru mult :'
              ,bg='black',fg='white',relief=RIDGE).grid(row=3,column=1)
        self.psVar = StringVar()
        self.ps = Entry(self,textvariable=self.psVar,
                        fg='black')
        self.ps.grid(row=4,column=1,padx=4,pady=4)

        Label(self,text='Befejezett múlt :',
              bg='black', fg='white',relief=RIDGE).grid(row=3,column=2)
        self.ppVar = StringVar()
        self.pp = Entry(self,textvariable=self.ppVar,
                        fg='black')
        self.pp.grid(row=4,column=2,padx=4,pady=4)

        Label(self,text='Forditas :',
              bg='black',fg='white',relief=RIDGE).grid(row=5,column=1,
                                           columnspan=2)
        self.trdVar=StringVar()
        self.trd = Entry(self,textvariable=self.trdVar,
                         fg='black')
        self.trd.grid(row=6,column=1,columnspan=2,pady=4)

        Button(self,text='Új szó!',command=self.new,
               bg='black', fg='white',bd=3,relief=RAISED,
               font="bold",activebackground='white',
               activeforeground='black').grid(row=7,column=1,
                                             columnspan=2,
                                             pady=3)

    def new(self):
        "Affiche un nouveau verbe"
        iv = open("irregularverbs.irv","r")
        c = 1
        while 1:
            lign = iv.readline()
            c += 1
            if lign == '':
                break
        iv.close()
        iv = open("irregularverbs.irv","r")
        n = randrange(1,c)
        a = 0
        while 1:
            a += 1
            line = iv.readline()
            if a == n:
                ligne_ = line
                break
        ligne = ligne_[0:len(ligne_)-1]
        liste = []
        ch = ''
        for car in ligne:
            if car == ' ':
                liste.append(ch)
                ch = ''
            else:
                ch = ch + car
        inf = liste[0]
        ps = liste[2]
        pp = liste[1]
        b = 3
        trd = ''
        while 1:
            try:
                if trd == '':
                    trd = liste[b]
                else:
                    trd = trd+' '+liste[b]
            except:
                break
            b += 1
        iv.close()

        self.infVar.set(inf)
        self.psVar.set(ps)
        self.ppVar.set(pp)
        self.trdVar.set(trd)



class MenuBar(Frame):
    "ASD"

class Flags(Frame):
    "ASD"


Main().mainloop()