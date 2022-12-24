import psycopg2

class Balance:
    def __init__(self,accountNumber):
        self.__account_number = accountNumber
        self.cnx = psycopg2.connect(host="bank-azure.postgres.database.azure.com",
    database="bidge-bank",
    user="postgres",
    password="asdASD123!")
        self.cursor = self.cnx.cursor()

    def accountBalance(self):
        query = "SELECT totalbalance,availablebalance FROM account WHERE id=%s"
        self.cursor.execute(query,self.__account_number)
        result = self.cursor.fetchall()
        return result
