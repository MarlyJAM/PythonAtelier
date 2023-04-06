# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 11:06:21 2022

@author: User
"""

class CompteBancaire :
    def __init__(self, nom='Pierre',solde=500 ):
        self.nom=nom
        self.solde=solde
        
    def depot(self,somme):
        self.solde=self.solde+somme
    def retrait(self,sommes):
        self.solde=self.solde-sommes
    def affiche(self):
        print("Le solde du compte bancaire de",self.nom ,"est de",self.solde,"euros")
compte1= CompteBancaire('Alain', 800)
compte1.depot(1000)
compte1.retrait(500)
compte1.affiche()
compte2= CompteBancaire()
compte2.affiche()

        