from tkinter import *
from subprocess import call
from tkinter import ttk , Tk
from tkinter import messagebox
import mysql.connector
import os
import time

#creer la fenetre

window = Tk()
window.geometry("1920x1080")
window.minsize(960,500)
window.title("logged")
window.config(background='#00c2cb')
#creation de la frame d'en haut
top_frame = Frame(window ,bd=2 , bg='#23F1E2' ,width=1920,height = 500)
#creation de la frame d'en bas
bottom_frame = Frame(window ,bd=2 , bg='#8681EA' ,width=1920,height = 580)
#creation de la frame menu
menu_frame = Frame(top_frame ,bd=0 , bg='#0EBACB' ,width=1920,height=50)
#creation de la frame objet
object_frame=Frame(top_frame,bg='#E7E0EC' ,width=1920,height=50)
object_frame.place(x=0, y=50)

#creation des champs

#premier champs Categorie
labet_categorie= Label(object_frame,text="Catégorie", font=("Arial",12),background='#E7E0EC')
# créer la liste Python contenant les éléments de la liste Combobox
listeMatériaux = ["Tissue", "Machine à coudre", "Table à repasser", "Fer à repasser"]
#Création de la Combobox via la méthode ttk.Combobox()
listeCombo = ttk.Combobox(object_frame, values=listeMatériaux,width=15,font=("Arial",12))
# Choisir l'élément qui s'affiche par défaut
listeCombo.current(0)

#deuxieme champs Emplacement
labet_emplacement= Label(object_frame,text="Emplacement", font=("Arial",12),background='#E7E0EC')
# créer la liste Python contenant les éléments de la liste Combobox
listeEmplacement = ["Paris 13", "Noisy-le-Grand", "Paris 17"]
#Création de la Combobox via la méthode ttk.Combobox()
listeCombo1 = ttk.Combobox(object_frame, values=listeEmplacement,width=15,font=("Arial",12))
# Choisir l'élément qui s'affiche par défaut
listeCombo1.current(0)

#troisième champs Reference
labet_reference= Label(object_frame,text="Référence", font=("Arial",12),background='#E7E0EC')
# creer un champ/entrée/input
reference_entry= Entry(object_frame, font=("Arial",14),bg='#ffffff',width=15)

#troisième champs désignation
labet_designation= Label(object_frame,text="Désignation", font=("Arial",12),background='#E7E0EC')
# creer un champ/entrée/input
designation_entry= Entry(object_frame, font=("Arial",14),bg='#ffffff',width=20)




#creation de la table inventaire
table = ttk.Treeview(top_frame,columns=(1,2,3,4,5,6) ,height=10 , show= "headings")
table.place(x=0,y=125 , width=1080)
#definir les entetes de la table
table.heading(1,text='Categorie')
table.heading(2,text='Emplacement')
table.heading(3,text='Référence')
table.heading(4,text='Désignation')
table.heading(5,text='Etat du stock')
table.heading(6,text='Stock')

#définir les dimensions se chaque column
table.column(1,width=200)
table.column(2,width=300)
table.column(3,width=200)
table.column(4,width=300)
table.column(5,width=150)
table.column(6,width=180)
#inserer les données dans le tableau
#--------------------------------------------------------------------------------------------------------#

#frame d'opération supression,ajout,modification
op_frame=Frame(top_frame,bd=0 , bg='#E7E0EC' ,width=1920,height=50)

#creation de la frame de mouvement du produits
move_frame=Frame(bottom_frame, bg='#E7E0ED', width=650, height=300)

#creation de la frame de notes
notes_frame=Frame(bottom_frame, bg='#CD6155', width=650, height=300)

#Creations des boutons des opérations
#creation du bouton de supression
delete_button=Button(op_frame,background='#7393B3', font=("Lucida Console",12),text='supprimer',width=20,height=25)
delete_button.place(x=1920 ,y=50)

#creation du bouton de d'ajout
new_button=Button(op_frame,background='#7393B3', font=("Lucida Console",12),text='ajouter',width=20,height=25)
new_button.place(x=1820 ,y=50)

#creation du bouton de de modification
update_button=Button(op_frame,background='#7393B3', font=("Lucida Console",12),text='modifier',width=20,height=25)
update_button.place(x=1720 ,y=50)

#afficher les champs
labet_categorie.pack(side=LEFT,padx= 10)
listeCombo.pack(side=LEFT,padx= 10)
labet_emplacement.pack(side=LEFT,padx= 10)
listeCombo1.pack(side=LEFT,padx= 10)
labet_reference.pack(side=LEFT,padx= 10)
reference_entry.pack(side=LEFT,padx= 10)
labet_designation.pack(side=LEFT,padx= 10)
designation_entry.pack(side=LEFT,padx= 10)
#afficher les boutons d'opérations
new_button.pack(side=RIGHT,padx=10,pady=5)
update_button.pack(side=RIGHT,padx=10,pady=5)
delete_button.pack(side=RIGHT,padx=10,pady=5)
#afficher la frame d'opérations
op_frame.pack(side=BOTTOM)
op_frame.pack_propagate(False)
#afficher la frame menu
menu_frame.pack(side=TOP)
#afficher la frame object
object_frame.pack()
object_frame.pack_propagate(False)
#afficher la frame des notes
notes_frame.pack(side=RIGHT)
#afficher la frame des mouvements
move_frame.pack(side=LEFT)
#afficher la table
table.pack()
#afficher la frame d'en bas
bottom_frame.pack(side=BOTTOM)
#afficher la frame d'en haut
top_frame.pack(side=TOP)
#afficher la fenetre
window.mainloop()





