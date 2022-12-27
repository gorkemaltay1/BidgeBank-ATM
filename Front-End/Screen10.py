from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font

master = Tk()
master.geometry('1080x700')
master.title("Money Deposit Saving")
canvas= Canvas(master,height=560,width=850)

arka_plan=Frame(master,bg='#FDFDFD')
arka_plan.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.87)

logo1=tk.Frame(master,bg='#BCCEF8')
logo1.place(relx=0.12,rely=0.15)

img= ImageTk.PhotoImage(Image.open("logo1.jpg"))
photo= tk.Label(logo1, image=img )
photo.pack()

exit_button=Frame(master,bg='white')
exit_button.place(relx=0.77,rely=0.15,relwidth=0.1,relheight=0.1)

exit_button=Button(exit_button,text='CANCEL',font='Verdana 10 bold underline',bg='#A2B5BB')
exit_button.pack(padx=10,pady=10, side=RIGHT)

logo=Frame(master,bg='white')
logo.place(relx=0.12,rely=0.35,relwidth=0.60,relheight=0.1)

money_deposit=Label(logo,text='Money Deposit',font='Verdana 35 bold',bg='white')
money_deposit.pack(padx=10,pady=10,side=LEFT)

select=Frame(master,bg='white')
select.place(relx=0.2,rely=0.46,relwidth=0.70,relheight=0.2)
message=Label(select,text=' Your money added to saving amount. ',bg='lightgreen', font='Verdana 25 ', pady=20, padx=10)
message.pack(padx=60,pady=5,side=LEFT)

master.mainloop()
