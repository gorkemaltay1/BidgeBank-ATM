from tkinter import *

master = Tk()
# FRONT-END
master.geometry('1080x700')
canvas= Canvas(master,height=560,width=850) #arayüzün büyüklüğünü atıyoruz

arka_plan=Frame(master,bg='#FDFDFD')
arka_plan.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.87) #0.1 kenarın yüzde onuna denk geliyor

merhaba_yazisi=Frame(master,bg='white',relief='sunken')
merhaba_yazisi.place(relx=0.20,rely=0.31 ,relwidth=0.6,relheight=0.055)
merhaba_yazisi=Label(merhaba_yazisi,bg='white', text='Good Morning,Nilgün.', font='Verdana 12 bold')
merhaba_yazisi.pack(padx=10,pady=7,side=LEFT)

islem_sec=Frame(master,bg='white',relief='sunken')
islem_sec.place(relx=0.20,rely=0.35,relwidth=0.6,relheight=0.055)
islem_sec=Label(islem_sec,bg='white', text='Please select your transaction.', font='Verdana 9')
islem_sec.pack(padx=10,pady=10,side=LEFT)

gün_yazisi=Frame(master,bg='white',relief='sunken')
gün_yazisi.place(relx=0.50,rely=0.35,relwidth=0.31,relheight=0.055)
islem_sec=Label(gün_yazisi,bg='white', text='28 December Wednesday', font='Verdana 9')
islem_sec.pack(padx=10,pady=10,side='right')


frame_sol_ust=Frame(master,bg='#D7EFEB',relief='sunken', borderwidth=2, )
frame_sol_ust.place(relx=0.20,rely=0.40,relwidth=0.20,relheight=0.20)

money_withdrawal=Button(frame_sol_ust,text='Money Withdrawal',command="", font="Verdana 14 bold",padx="74", pady="59", bg="#D7EFEB", fg="black", cursor="hand2",activeforeground="green", activebackground="black")
# BURDAKİ COMMAND GÖNDER BUTONUNUN HANGİ İŞLEVİ YERİNE GETİRECEĞİNİ SÖYLER
#COMMANDI ATADIĞIMIZ GONDER DEĞİŞKENİ DE FONKSİYONDUR,NE YAPMASI GEREKTİĞİNİ FONKSİYONLA İFADE EDERİZ
money_withdrawal.pack()

frame_sol_alt=Frame(master,bg='#D7EFEB',relief='sunken', borderwidth=2)
frame_sol_alt.place(relx=0.20,rely=0.60,relwidth=0.20,relheight=0.20)

money_deposite=Button(frame_sol_alt,text='Money Deposite',command="", font="Verdana 14 bold",padx="74", pady="59", bg="#D7EFEB", fg="black", cursor="hand2",activeforeground="green", activebackground="black")
# BURDAKİ COMMAND GÖNDER BUTONUNUN HANGİ İŞLEVİ YERİNE GETİRECEĞİNİ SÖYLER
#COMMANDI ATADIĞIMIZ GONDER DEĞİŞKENİ DE FONKSİYONDUR,NE YAPMASI GEREKTİĞİNİ FONKSİYONLA İFADE EDERİZ
money_deposite.pack()

frame_orta_ust=Frame(master,bg='#E6E6E6',relief='sunken', borderwidth=2, )
frame_orta_ust.place(relx=0.40,rely=0.40,relwidth=0.20,relheight=0.20)

balance_ınquiry=Button(frame_orta_ust,bg='#F9F9F9', text='Balance Inquiry',font='Verdana 14 bold',padx="74", pady="59")
balance_ınquiry.pack()

frame_orta_alt=Frame(master,bg='#E6E6E6',relief='sunken', borderwidth=2, )
frame_orta_alt.place(relx=0.40,rely=0.60,relwidth=0.20,relheight=0.20)

internal_transfer=Button(frame_orta_alt,bg='#F9F9F9', text='Internal Transfer', font='Verdana 14 bold',padx="74", pady="59")
internal_transfer.pack()

frame_sağ_ust=Frame(master,bg='#D7EFEB',relief='sunken', borderwidth=2, )
frame_sağ_ust.place(relx=0.60,rely=0.40,relwidth=0.20,relheight=0.20)

change_pın=Button(frame_sağ_ust,bg='#D7EFEB', text='Change PIN', font='Verdana 14 bold',padx="78", pady="60")
change_pın.pack()

frame_sağ_alt=Frame(master,bg='#D7EFEB',relief='sunken', borderwidth=2, )
frame_sağ_alt.place(relx=0.60,rely=0.60,relwidth=0.20,relheight=0.20)

exit_take_card=Button(frame_sağ_alt,bg='#D7EFEB', text='Exit/Take Card', font='Verdana 14 bold',padx="74", pady="59")
exit_take_card.pack()

master.mainloop() # tk nın kapanmaması için sürekli loope alıyo-master da arayüzümüzün ismi





