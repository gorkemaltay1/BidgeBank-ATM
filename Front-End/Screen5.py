from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font

master = Tk()
master.geometry('1080x700')
master.title("Change PIN")
canvas= Canvas(master,height=560,width=850)

arka_plan=Frame(master,bg='#FDFDFD')
arka_plan.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.87)

logo1=tk.Frame(master,bg='#BCCEF8')
logo1.place(relx=0.12,rely=0.15)

img= ImageTk.PhotoImage(Image.open("logo1.jpg"))
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
logo.place(relx=0.12,rely=0.3,relwidth=0.60,relheight=0.1)

change_pin=Label(logo,text='Change your PIN',font='Verdana 35 bold',bg='white')
change_pin.pack(padx=10,pady=10,side=LEFT)

select=Frame(master,bg='white')
select.place(relx=0.2,rely=0.42,relwidth=0.70,relheight=0.2)
message=Label(select,text=' Current PIN ',bg='#FDFDFD', font='Verdana 18 ', pady=20, padx=10)
message.pack(padx=60,pady=5,side=LEFT)

sayi_kutusu=Frame(master,bg='#EEEEEE')
sayi_kutusu.place(relx=0.25,rely=0.58,relwidth=0.45,relheight=0.09)

miktar_kutusu=Frame(master,bg='white')
miktar_kutusu.place(relx=0.3,rely=0.6,relwidth=0.35,relheight=0.03)

metin_alani=Text(miktar_kutusu, height=1.2, width=120)
metin_alani.tag_configure('stil',foreground='#bfbfbf',font=("Verdana 10 bold"))
metin_alani.place(relx=0.002,rely=0.04)



select2=Frame(master,bg='white')
select2.place(relx=0.2,rely=0.65,relwidth=0.70,relheight=0.2)
message2=Label(select2,text=' New PIN ',bg='#FDFDFD', font='Verdana 18 ', pady=20, padx=10)
message2.pack(padx=60,pady=5,side=LEFT)

sayi_kutusu2=Frame(master,bg='#EEEEEE')
sayi_kutusu2.place(relx=0.25,rely=0.8,relwidth=0.45,relheight=0.09)

miktar_kutusu2=Frame(master,bg='white')
miktar_kutusu2.place(relx=0.3,rely=0.82,relwidth=0.35,relheight=0.03)

metin_alani2=Text(miktar_kutusu2, height=1.2, width=120)
metin_alani2.tag_configure('stil',foreground='#bfbfbf',font=("Verdana 10 bold"))
metin_alani2.place(relx=0.002,rely=0.04)


save_button=Frame(master,bg='white')
save_button.place(relx=0.45,rely=0.9)

save_button=Button(save_button,text='Save',font='Verdana 14 bold',bg='white')
save_button.pack()


master.mainloop()
