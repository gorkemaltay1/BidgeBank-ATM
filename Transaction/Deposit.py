import psycopg2

class Deposit:
    def __init__(self,accountNumber,withdrawalMoney):
        self.__account_number = accountNumber
        self.__withdrawal_money = withdrawalMoney
        self.cnx = psycopg2.connect(host="bank-azure.postgres.database.azure.com",
    database="bidge-bank",
    user="postgres",
    password="asdASD123!")
        self.cursor = self.cnx.cursor()
    
    def deposit_transaction(self):
        query = "UPDATE account SET totalbalance=totalbalance+%s, availablebalance=availablebalance+%s , WHERE id = %s"
        self.cursor.execute(query,(self.__withdrawal_money,self.__withdrawal_money,self.__account_number))
        self.cnx.commit()
        return True
