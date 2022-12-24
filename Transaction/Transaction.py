import psycopg2

class Transaction:
    def __init__(self,status):
        self.__status = status
        

    def make_transaction(self,transactionType:str,accountNumber:int):
        cnx = psycopg2.connect(host="bank-azure.postgres.database.azure.com",
    database="bidge-bank",
    user="postgres",
    password="asdASD123!")
        cursor = cnx.cursor()
        query="INSERT INTO transactions(status,customerid,transactionType) VALUES(%s,%s,%s)"
        cursor.execute(query,(self.__status,accountNumber,transactionType))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
