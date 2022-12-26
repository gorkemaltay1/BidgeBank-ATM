from tkinter import *

master = Tk()
master.geometry('1080x700')
canvas= Canvas(master,height=560,width=850)

arka_plan=Frame(master,bg='#FDFDFD')
arka_plan.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.87)

exit_go_back=Frame(master,bg='white')
exit_go_back.place(relx=0.79,rely=0.13,relwidth=0.1,relheight=0.1)

exit_go_back=Button(exit_go_back,text='CANCEL',font='Verdana 10 bold',bg='#A2B5BB')
exit_go_back.pack(padx=10,pady=10, side=RIGHT)

exit_go_back2=Frame(master,bg='white')
exit_go_back2.place(relx=0.74,rely=0.13,relwidth=0.08,relheight=0.1)

exit_go_back2=Button(exit_go_back2,text='Go Back',font='Verdana 10 bold',bg='white')
exit_go_back2.pack(padx=10,pady=10, side=LEFT)

balance_inquiry=Frame(master,bg='white')
balance_inquiry.place(relx=0.12,rely=0.32,relwidth=0.60,relheight=0.1)

balance_inquiry1=Label(balance_inquiry,text='Balance Inquiry',font='Verdana 35 ',bg='white')
balance_inquiry1.pack(padx=10,pady=10,side=LEFT)

frame_sol_bir=Frame(master,bg='#D7EFEB',relief='sunken', borderwidth=2)
frame_sol_bir.place(relx=0.16,rely=0.48,relwidth=0.25,relheight=0.18)

total_balance=Button(frame_sol_bir, text='Total Balance', font="Verdana 14 bold",padx="105", pady="59", bg="#D7EFEB", fg="black")
total_balance.pack()

frame_sol_iki=Frame(master,bg='#EEEEEE',relief='sunken', borderwidth=2)
frame_sol_iki.place(relx=0.408,rely=0.48,relwidth=0.38,relheight=0.18)

frame_sol_iki2=Label(frame_sol_iki,text='           $15.897,99',font='Verdana 22 ',bg='#EEEEEE')
frame_sol_iki2.pack(padx=10,pady=10,side=LEFT)

frame_sol_bir=Frame(master,bg='#D7EFEB',relief='sunken', borderwidth=2)
frame_sol_bir.place(relx=0.16,rely=0.68,relwidth=0.25,relheight=0.18)

avaliable_balance=Button(frame_sol_bir, text='Avaliable Balance', font="Verdana 14 bold",padx="105", pady="59", bg="#D7EFEB", fg="black")
avaliable_balance.pack()

frame_alt_iki=Frame(master,bg='#EEEEEE',relief='sunken', borderwidth=2)
frame_alt_iki.place(relx=0.408,rely=0.68,relwidth=0.38,relheight=0.18)

frame_alt_iki2=Label(frame_alt_iki,text='           $12.367,89',font='Verdana 22 ',bg='#EEEEEE')
frame_alt_iki2.pack(padx=10,pady=10,side=LEFT)


master.mainloop()

