from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font

master = Tk()
master.geometry('1080x700')
master.title("Money Deposit")
canvas= Canvas(master,height=560,width=850)

arka_plan=Frame(master,bg='#FDFDFD')
arka_plan.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.87)

logo1=tk.Frame(master,bg='#BCCEF8')
logo1.place(relx=0.12,rely=0.15)

img= ImageTk.PhotoImage(Image.open("Img/logo1.jpg"))
photo= tk.Label(logo1, image=img )
photo.pack()

goback_button=Frame(master,bg='white')
goback_button.place(relx=0.7,rely=0.15,relwidth=0.08,relheight=0.1)

goback_button=Button(goback_button,text='Go Back',font='Verdana 10 bold',bg='white')
goback_button.pack(padx=10,pady=10, side=LEFT)

exit_button=Frame(master,bg='white')
exit_button.place(relx=0.77,rely=0.15,relwidth=0.1,relheight=0.1)

exit_button=Button(exit_button,text='CANCEL',font='Verdana 10 bold underline',bg='#A2B5BB')
exit_button.pack(padx=10,pady=10, side=RIGHT)

logo=Frame(master,bg='white')
logo.place(relx=0.12,rely=0.35,relwidth=0.60,relheight=0.1)

money_deposit=Label(logo,text='Money Deposit',font='Verdana 35 bold',bg='white')
money_deposit.pack(padx=10,pady=10,side=LEFT)

select=Frame(master,bg='white')
select.place(relx=0.2,rely=0.46,relwidth=0.60,relheight=0.07)
message=Label(select,text=' Do you want to checking or saving?',bg='white', font='Verdana 16 ')
message.pack(padx=120,pady=10,side=LEFT)

frame_checking=Frame(master,bg='#D7EFEB',relief='sunken', borderwidth=2)
frame_checking.place(relx=0.33,rely=0.60,relwidth=0.17,relheight=0.20)

checking=Button(frame_checking, text='Checking', font="Verdana 14 bold",padx="105", pady="59", bg="#D7EFEB", fg="black")
checking.pack()

frame_saving=Frame(master,bg='#D7EFEB',relief='sunken', borderwidth=2)
frame_saving.place(relx=0.52,rely=0.60,relwidth=0.17,relheight=0.20)

saving=Button(frame_saving, text='Saving', font="Verdana 14 bold",padx="95", pady="59", bg="#D7EFEB", fg="black")
saving.pack()

master.mainloop()
