# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:35:37 2021

@author: User
"""
Moyenne=int(input("Donnez la moyenne :"))
while Moyenne<0 or Moyenne>20 :
    print("Donnez la vrai moyenne :")
    
if Moyenne<10 :
    print("Vous êtes refusé")

else:
   if Moyenne<12:
     print("Vous êtes Admis Passable")
   else:
      if Moyenne<14:
          print("Admis Assez Bien")
      else:
          if Moyenne<16 :
             print("admis bien")
          else:
              if Moyenne<18 :
                  print("admis très bien")
              else :
                  print("Admis excellen")
