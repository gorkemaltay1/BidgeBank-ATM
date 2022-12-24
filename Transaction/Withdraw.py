import psycopg2

class Withdraw:
    def __init__(self,accountNumber):
        self.__account_number = accountNumber
        self.cnx = psycopg2.connect(host="bank-azure.postgres.database.azure.com",
    database="bidge-bank",
    user="postgres",
    password="asdASD123!")
        self.cursor = self.cnx.cursor()

    def accountBalanceWithdraw(self,withdrawalMoney:int):
        query = "UPDATE account SET totalbalance=totalbalance-%s, availablebalance=availablebalance-%s WHERE id=%s"
        self.cursor.execute(query,(withdrawalMoney,withdrawalMoney,self.__account_number))
        self.cnx.commit()
        return True
