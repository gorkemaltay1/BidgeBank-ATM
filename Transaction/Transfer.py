import psycopg2

class Transfer:
    def __init__(self, destination_account_number,sender_account_number):
        self.__sender_account_number = sender_account_number
        self.__destination_account_number = destination_account_number
        self.cnx = psycopg2.connect(host="bank-azure.postgres.database.azure.com",
    database="bidge-bank",
    user="postgres",
    password="asdASD123!")
        self.cursor = self.cnx.cursor()

    def get_destination_account(self):
        return self.__destination_account_number
    
    def get_sender_account(self):
        return self.__sender_account_number
    
    def transferring_money(self,transferredMoney):
        query = "UPDATE account SET totalbalance=totalbalance-%s, availablebalance = availablebalance-%s WHERE id = %s"
        self.cursor.execute(query,(transferredMoney,transferredMoney,self.__sender_account_number))
        self.cnx.commit()
        query = "UPDATE account SET totalbalance=totalbalance+%s, availablebalance = availablebalance+%s WHERE id = %s"
        self.cursor.execute(query,(transferredMoney,transferredMoney,self.__destination_account_number))
        self.cnx.commit()
    
    def destination_number_check(self):
        query = "SELECT * FROM account INNER JOIN customer ON customer.id = account.customerid"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        for result in results:
            if self.__destination_account_number == result[0]:
                return True
        return False