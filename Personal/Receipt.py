import psycopg2
import smtplib
'''
1-smtplib kütüphanesi importlanır.
2- Adı-soyadı, kullanıcı işlem türü, creationdate,mail
'''
import smtplib
import datetime
import psycopg2
class Receipt:
    def __init__(self,amount,accountNumber):
        self.__transactionType = ""
        self.__amount = amount
        self.__accountNumber = accountNumber
        self.__customerName = ""
        self.__date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__mail = ""
        self.cnx = psycopg2.connect(host="bank-azure.postgres.database.azure.com",
    database="bidge-bank",
    user="postgres",
    password="asdASD123!")
        self.cursor = self.cnx.cursor()
    
    def gettingAttributes(self):
        query = "SELECT * FROM transactions INNER JOIN customer ON customer.id = transactions.customerid INNER JOIN account ON customer.id=account.customerid WHERE account.id = %s"
        self.cursor.execute(query,(self.__accountNumber,))
        results = self.cursor.fetchall()
        self.__customerName = results[-1][10]
        self.__transactionType = results[-1][4]
        self.__mail = str(results[-1][6])
    
    def sendEmail(self):
        self.gettingAttributes()
        content = f'''|----------------------------------------------------------------------------------------------------------------------------------------------------------|

                                                                                                                                                                            
                                                                                            BIDGE BANK FATURA                                                                


                    Sayın, {self.__customerName}, {self.__date} tarihinde yapılan işlem özetiniz aşağıda yer verilmiştir.                                                                                                                             

                    -----------------------------------------------------                                                                                                      

                    Yapılan işlem :  {self.__transactionType}                                                                                                                        

                    İşlem yapılan hesap numarası: {self.__accountNumber}

                    İşlem yapılan miktar: ${self.__amount}                                                                                                                            

                    -----------------------------------------------------                                                                                                                                                                                                                                          

                    Gmail hesabı: {self.__mail}                                                                                                                         

                    -----------------------------------------------------                                                                                                      

                    Ailemizin bir bireyi olduğunuz için teşekkür ederiz iyi günler 😊

                    -----------------------------------------------------

                    Bu işlem bilginiz dahilinde değilse en yakın şubemize başvurun.                                                                                      
        |-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|'''.encode('utf-8')
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("bidgebank@gmail.com","sppdzhsspndijpgp")
        toMail = self.__mail
        mail.sendmail("bidgebank@gmail.com",toMail,content)