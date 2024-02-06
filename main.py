from tkinter import *
from tkinter import ttk
from produit import *


# Permet de créer la fenetre
surf = Tk()
surf.geometry("800x600+100+10")

params_add = []
params_edit = []

style = ttk.Style()
style.theme_use('clam')

TEXTE = "Manage Your Store"
 
label = Label(surf, text=TEXTE,
                 # Wrapper le texte selon X (pixelsFrame, pas par caractères)
                 wraplength = 150,
                 # Place tout le texte au centre.
                 justify = CENTER)
label.pack()

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


def delete():
    # Renvoie l'id (machine) de l'élément sélectionnée
    selected_item = tree.focus()
    #Permet de récupérer les informations de l'élément sélectionnée et de les stocker dans 'values'
    item_values = tree.item(selected_item, 'values')
    # Supprime l'élément sélectionné uniquement en graphique
    tree.delete(selected_item)
    
    # Permer de récupérer l'id de l'élément et de le supprimer de la base de données
    if item_values:
        item_id = item_values[0]
        produit.deleteProduit(item_id)


def open_popup_add():
    #Permet de créer la fenetre pop up
    top = Toplevel(surf)
    top.geometry("300x250")
    top.title("Ajouter un produit")
    #Permet d'afficher les textes
    Label(top, text= "Ajouter un produit", font=('Mistral 18')).place(x=60,y=30)
    Label(top, text= "(nom ,description ,prix ,quantité ,id_category)", font=('Mistral 10')).place(x=20,y=60)

    # Fonction appeler lorsqu'on clique sur le bouton valider pour recuperer les input et créer le produit
    def verify():
            data = user_input.get()
            entry.delete(0, END)
            params_add.append(data)
            produit.createProduit(params_add[0],params_add[1],params_add[2],params_add[3],params_add[4])
            for i in tree.get_children():
                tree.delete(i)
            for row in produit.readProduit():
                tree.insert('' ,END ,values = row)

    #Créer et place les différents boutons
    user_input = StringVar(top)
    entry = Entry(top, textvariable=user_input)
    valider = Button(top ,text="Valider" ,command=verify)
    valider.pack()
    valider.place(x=130,y=130)
    entry.pack()
    entry.place(x=90 ,y=80)
    top.mainloop()


def open_popup_edit():
    top = Toplevel(surf)
    top.geometry("300x250")
    top.title("Modifier un produit")
    Label(top, text= "Modifier un produit", font=('Mistral 18')).place(x=60,y=30)
    Label(top, text= "(nom ,description ,prix ,quantité ,id_category ,id)", font=('Mistral 9')).place(x=20,y=60)

    def verify():
            data = user_input.get()
            entry.delete(0, END)
            params_edit.append(data)
            produit.updateProduit(params_edit[0],params_edit[1],params_edit[2],params_edit[3],params_edit[4],params_edit[5])
            for i in tree.get_children():
                tree.delete(i)
            for row in produit.readProduit():
                tree.insert('' ,END ,values = row)

    user_input = StringVar(top)
    entry = Entry(top, textvariable=user_input)
    valider = Button(top ,text="Valider" ,command=verify)
    valider.pack()
    valider.place(x=130,y=130)
    entry.pack()
    entry.place(x=90 ,y=80)
    top.mainloop()






#Button area
getTextArea = Button(surf ,text="Supprimer" ,command=delete)
getTextArea.pack()
getTextArea.place(x=630 ,y=448)
edit_btn = Button(surf, text="Modifier", command=open_popup_edit)
edit_btn.pack()
edit_btn.place(x=560 ,y=448)
add_btn = Button(surf, text="Ajouter",command=open_popup_add)
add_btn.pack()
add_btn.place(x=500 ,y=448)

# getCreate = Button(surf ,text="Créer" ,command=get_delete_text)
# getCreate.pack()
# getCreate.place(x= 400 ,y= 500)



surf.mainloop()
