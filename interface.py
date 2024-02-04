from tkinter import *
from tkinter import ttk
from produit import *

# Permet de créer la fenetre
surf = Tk()
surf.geometry("800x600+100+10")

# Permet de créer le tableau
tree = ttk.Treeview(surf ,columns=(1,2,3,4,5,6) ,height=9 ,show="headings")
tree.place(x=100 ,y=170 ,width=600 ,height=275)

# Définit le titre des colonnes
tree.heading(1 ,text="ID")
tree.heading(2 ,text="Name")
tree.heading(3 ,text="Description")
tree.heading(4 ,text="Price")
tree.heading(5 ,text="Quantity")
tree.heading(6 ,text="ID_category")
#Definit la taille des colonnes
tree.column(1 ,width=50)
tree.column(2 ,width=100)
tree.column(3 ,width=100)
tree.column(4 ,width=100)
tree.column(5 ,width=100)
tree.column(6 ,width=50)


# Permet d'insérer les valeurs de la table produit dans le tableau
for row in produit.readProduit():
    tree.insert('' ,END ,values = row)

# Text area
def get_text():
    text = Text(surf ,height=1 ,width=10)
    text.pack()

#Button area
button_delete = Button(surf ,text ="Supprimer une ligne" ,command=get_text())
button_delete.pack()
button_delete.place(x=582 ,y=448)



surf.mainloop()
