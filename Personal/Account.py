import psycopg2
class Account:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__total_balance = 0.0
        self.__available_balance = 0.0
        self.cnx = psycopg2.connect(host="bank-azure.postgres.database.azure.com",
    database="bidge-bank",
    user="postgres",
    password="asdASD123!")
        self.cursor = self.cnx.cursor()
        

    def AccountAmount(self):
        query = "SELECT * FROM ACCOUNT INNER JOIN customer ON customer.id = account.customerid INNER JOIN card ON customer.id = card.customerid"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        for result in results:
            if self.__account_number == result[0]:
                return result[1],result[2],result[3]
        return False
    def accountBalanceWithdraw(self,withdrawalMoney:int):
        query = "UPDATE account SET totalbalance=totalbalance-%s, availablebalance=availablebalance-%s WHERE id=%s"
        self.cursor.execute(query,(withdrawalMoney,withdrawalMoney,self.__account_number))
        self.cnx.commit()
        return True