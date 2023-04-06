# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 11:43:38 2022

@author: User
"""

class Voiture:
    def __init__(self,marque='Ford',couleur='rouge',pilote='personne',vitesse=0):
        self.marque=marque
        self.couleur=couleur
        self.pilote=pilote
        self.vitesse=vitesse
    def choix_conducteur(self,nom):
        self.pilote=self.nom
    def accelerer(self, taux, duree):
        if self.pilote!= "personne":
            self.vitesse=self.vitesse+self.taux*self.durée
        else:
            self.vitesse=0
            print("voiture sans conducteur!")
    def afficher(self):
        print("la voiture est de marque",self.marque,"de couleur",self.couleur,"de pilote",self.pilote,"et de vitesse",self.vitesse)
        
Voiture1=Voiture()
Voiture1.afficher()