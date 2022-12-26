from tkinter import *

master = Tk()
master.geometry('1080x700')
canvas= Canvas(master,height=560,width=850)

arka_plan=Frame(master,bg='#FDFDFD')
arka_plan.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.87)

exit_go_back=Frame(master,bg='white')
exit_go_back.place(relx=0.77,rely=0.15,relwidth=0.1,relheight=0.1)

exit_go_back=Button(exit_go_back,text='CANCEL',font='Verdana 10 bold',bg='#A2B5BB')
exit_go_back.pack(padx=10,pady=10, side=RIGHT)

logo=Frame(master,bg='white')
logo.place(relx=0.12,rely=0.35,relwidth=0.60,relheight=0.1)

money_withdrawal=Label(logo,text='Money Withdrawal',font='Verdana 35 ',bg='white')
money_withdrawal.pack(padx=10,pady=10,side=LEFT)

select=Frame(master,bg='white')
select.place(relx=0.12,rely=0.46,relwidth=0.60,relheight=0.07)
select_yazi=Label(select,text=' Please select the amount that you want.',bg='white', font='Verdana 12 ')
select_yazi.pack(padx=10,pady=10,side=LEFT)

frame_sol_bir=Frame(master,bg='#D7EFEB',relief='sunken', borderwidth=2)
frame_sol_bir.place(relx=0.14,rely=0.60,relwidth=0.17,relheight=0.20)

twenty_dolar=Button(frame_sol_bir, text='$20', font="Verdana 14 bold",padx="105", pady="59", bg="#D7EFEB", fg="black")
twenty_dolar.pack()

frame_sol_iki=Frame(master,bg='#D7EFEB',relief='sunken', borderwidth=2)
frame_sol_iki.place(relx=0.33,rely=0.60,relwidth=0.17,relheight=0.20)

forty_dolar=Button(frame_sol_iki, text='$40', font="Verdana 14 bold",padx="105", pady="59", bg="#D7EFEB", fg="black")
forty_dolar.pack()

frame_sol_uc=Frame(master,bg='#D7EFEB',relief='sunken', borderwidth=2)
frame_sol_uc.place(relx=0.52,rely=0.60,relwidth=0.17,relheight=0.20)

hundered_dolar=Button(frame_sol_uc, text='$100', font="Verdana 14 bold",padx="95", pady="59", bg="#D7EFEB", fg="black")
hundered_dolar.pack()

frame_sol_dort=Frame(master,bg='#D7EFEB',relief='sunken', borderwidth=2)
frame_sol_dort.place(relx=0.71,rely=0.60,relwidth=0.17,relheight=0.20)

other_amount=Button(frame_sol_dort, text='Other amount', font="Verdana 14 bold",padx="74", pady="59", bg="#D7EFEB", fg="black")
other_amount.pack()

master.mainloop()

