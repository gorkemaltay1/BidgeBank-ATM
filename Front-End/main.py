from tkinter import *
class MainPage(Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Page")
        self.geometry("1080x700")
        canvas= Canvas(self,height=560,width=850) #arayüzün büyüklüğünü atıyoruz

        arka_plan=Frame(self,bg='#FDFDFD')
        arka_plan.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.87)

        exit_go_back=Frame(self,bg='white')
        exit_go_back.place(relx=0.79,rely=0.13,relwidth=0.1,relheight=0.1)

        exit_go_back=Button(exit_go_back,text='CANCEL',font='Verdana 10 bold',bg='#A2B5BB')
        exit_go_back.pack(padx=10,pady=10, side=RIGHT)

        exit_go_back2=Frame(self,bg='white')
        exit_go_back2.place(relx=0.74,rely=0.13,relwidth=0.08,relheight=0.1)

        exit_go_back2=Button(exit_go_back2,text='Go Back',font='Verdana 10 bold',bg='white')
        exit_go_back2.pack(padx=10,pady=10, side=LEFT)

        enter_inf=Frame(self,bg='white')
        enter_inf.place(relx=0.25,rely=0.50,relwidth=0.60,relheight=0.07)

        enter_inf=Label(enter_inf,bg='white', text='                                Please enter your information.', font='Verdana 12 ')
        enter_inf.pack(padx=10,pady=10,side=LEFT)

        card_number=Frame(self,bg='#EEEEEE')
        card_number.place(relx=0.25,rely=0.58,relwidth=0.55,relheight=0.09)

        card_number=Label(card_number,text=' Card Number', font='Verdana 12 ')
        card_number.pack(padx=10,pady=10,side=LEFT)

        card_number2=Frame(self,bg='white')
        card_number2.place(relx=0.42,rely=0.61,relwidth=0.35,relheight=0.03)

        metin_alani=Text(card_number2, height=1.2, width=120)
        metin_alani.tag_configure('stil',foreground='#bfbfbf',font=("Verdana 10 bold"))
        #tag_configure text boxdaki default mesajın yazım stili ayarlamasını yapmamızı sağladı
        metin_alani.place(relx=0.002,rely=0.04)

        karsilama_metni=""
        metin_alani.insert(END,karsilama_metni,'stil')

        password=Frame(self,bg='#EEEEEE')
        password.place(relx=0.25,rely=0.71,relwidth=0.55,relheight=0.09)

        password2=Label(password,text=' Password', font='Verdana 12 ')
        password2.pack(padx=10,pady=10,side=LEFT)

        password3=Frame(self,bg='white')
        password3.place(relx=0.42,rely=0.74,relwidth=0.35,relheight=0.03)

        metin_alani=Text(password3, height=1.2, width=120)
        metin_alani.tag_configure('stil',foreground='#bfbfbf',font=("Verdana 10 bold"))
        #tag_configure text boxdaki default mesajın yazım stili ayarlamasını yapmamızı sağladı
        metin_alani.place(relx=0.002,rely=0.04)

        karsilama_metni=""
        metin_alani.insert(END,karsilama_metni,'stil')
        
    def open_second_page(self):
        second_page = SecondPage()
        second_page.mainloop()
        self.destroy()
    
    
class SecondPage(Tk):
    def __init__(self):
        super().__init__()
        self.title("Second Page")
        self.geometry("1080x700")
        button = Button(self, text="Open main page", command=self.open_main_page)
        button.pack()
        
    def open_main_page(self):
        main_page = MainPage()
        main_page.mainloop()
        self.destroy()

class ThirdPage(Tk):
    def __init__(self):
        super().__init__()
        self.title("Second Page")
        self.geometry("1080x700")
        button = Button(self, text="Open main page", command=self.open_main_page)
        button.pack()
        
    def open_main_page(self):
        main_page = MainPage()
        main_page.mainloop()
        self.destroy()

class FourthPage(Tk):
    def __init__(self):
        super().__init__()
        self.title("Second Page")
        self.geometry("1080x700")
        button = Button(self, text="Open main page", command=self.open_main_page)
        button.pack()
        
    def open_main_page(self):
        main_page = MainPage()
        main_page.mainloop()
        self.destroy()
    

root = MainPage()
root.mainloop()
