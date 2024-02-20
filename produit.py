from db import DB
import os 
from dotenv  import load_dotenv

load_dotenv()

class Produit():
    def __init__(self):
        self.select = ("""
            SELECT * FROM product
            """)

    def createProduit(self ,name ,description ,price ,quantity ,id_category):
        queries = ("""
            INSERT INTO product(name ,description ,price ,quantity ,id_category)
            VALUES
            (%s,%s,%s,%s,%s)
            """)
        params = (name ,description ,price ,quantity ,id_category)
        database.executeQuery(queries ,params)
    
    def readProduit(self):
        queries = ("SELECT * FROM product ")
        showData = database.fetch(queries)
        return showData


    def updateProduit(self ,name ,description ,price ,quantity ,id_category ,id):
        queries = ("""
            UPDATE product
            SET name = %s ,description = %s ,price = %s ,quantity = %s ,id_category = %s
            WHERE id = %s   
            """)
        params = (name ,description ,price ,quantity ,id_category ,id)
        database.executeQuery(queries ,params)
    
    def deleteProduit(self ,id):
        queries = ("""
            DELETE FROM product
            WHERE id = (%s)
            """)
        params = [id]
        database.executeQuery(queries ,params)
    
    def changeCategory(self ,idCategory ,idProduct):
        queries = ("""
                UPDATE product 
                SET id_category = (%s)
                WHERE id = %s
                   """)
        params = (idCategory ,idProduct)
        database.executeQuery(queries ,params)

    
        





database = DB(os.getenv("host") ,os.getenv("user") ,os.getenv("passwd") ,os.getenv("database"))
produit = Produit()
# produit.createProduit(("LEJUS") ,"boisson fruit" ,600 ,2400 ,3)
# produit.deleteProduit(16)
# produit.updateProduit("Ordinateur" ,"Machine capable de réaliser des calculs puissant" ,600 ,2400 ,1 ,12 ,27)
# produit.changeCategory(3 ,9)
# print (produit.readProduit())

# database.checkStock()
