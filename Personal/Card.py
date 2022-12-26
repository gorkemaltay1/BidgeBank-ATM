import psycopg2
class Card:
    def __init__(self, number, pin, customer_name="Bora", expiry="2025-01-01"):
        self.__card_number = number
        self.__customer_name = customer_name
        self.__card_expiry = expiry
        self.__pin = pin
        self.cnx = psycopg2.connect(host="bank-azure.postgres.database.azure.com",
    database="bidge-bank",
    user="postgres",
    password="asdASD123!")
        self.cursor = self.cnx.cursor()
        self.__account_number = 0
    
    def get_billing_address(self):
        cnx = psycopg2.connect(host="bank-azure.postgres.database.azure.com",
    database="bidge-bank",
    user="postgres",
    password="asdASD123!")
        cursor = cnx.cursor()
        query = "SELECT * FROM card INNER JOIN customer on customer.id = card.customerid"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        for result in results:
            if str(result[1]) == str(self.__card_number) and str(result[3]) == str(self.__pin):
                self.__customer_name = result[12]
                self.__card_expiry = result[2]
                self.__account_number = result[0]
                return True
        return False
    def get_customer_name(self):
        return self.__customer_name

    def get_customer_account_number(self):
        self.get_billing_address()
        return self.__account_number

    def change_pin(self,newPin):
        self.get_billing_address()
        query = "UPDATE card SET pin=%s WHERE accountid=%s"
        self.cursor.execute(query,(str(newPin),self.__account_number))
        self.cnx.commit()
        return True