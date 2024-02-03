from db import DB


class Category():
    def __init__(self):
        pass

    def createCategory(self ,name):
        queries = ("""
            INSERT INTO category(name)
            VALUES
            (%s)
            """)
        params = [name]
        database.executeQuery(queries ,params)
    
    def readCategory(self):
        queries = ("""
            SELECT * FROM category
            """)
        database.fetch(queries)
    
    def updateCategory(self ,name,id):
        queries = ("""
            UPDATE category
            SET name = %s
            WHERE id = %s   
            """)
        params = (name ,id)
        database.executeQuery(queries ,params)
    
    def deleteCategory(self ,id):
        queries = ("""
            DELETE FROM category
            WHERE id = (%s)
            """)
        params = [id]
        database.executeQuery(queries ,params)




database = DB("localhost" ,"root" ,"root" ,"store")
category = Category()
# category.createCategory("Nourriture")
# category.deleteCategory(5)
# category.updateCategory('Boisson',3)
category.readCategory()
