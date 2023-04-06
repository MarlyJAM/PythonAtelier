L=[10,12,3,14,1,-15,15,40,100,6]
L1=[]
L2=[]
# On vous demander de copier les valeurs paires dans une liste L1 et impaires L2
# à condition que les deux listes L1 et L2 soient finalement triées croissant
#parcourir tous les éléments de la liste initiale
for i in L:
#si la valeur est paire : on va la rajouter dans L1
    if(i % 2==0):
#on distingue deux cas : si L1 est vide ou on
        if(L1!=[]):
            position=0
            while (position<len(L1)) and  (i>L1[position]) :
                  position=position+1
            L1.insert(position,i)
            print(L1)
                  
        else:
               L1.append(i)     
print(L1)

