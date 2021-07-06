import mysql.connector as mysqlcon
class dbdata():
    @staticmethod
    def createdata():

        con=mysqlcon.connect(host="localhost",user="root",passwd="root",database="admin")
        return con