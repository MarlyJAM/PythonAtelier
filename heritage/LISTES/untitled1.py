
#Enoncé : dénombre les valeurs distinctes dans une liste
L=[10,12,3,-10,80,80,10, 3,12]
n=0
p=0
#les valeurs distinctes : 10, 12 3,-1 et 80
for i in range (len(L) ):
    for j in range( i+1,len(L) ):
        if L[i]==L[j]:
            n=n+1
            print(L[i], "à la position",i,"et",L[j],"à la position ",j)
print("La liste L a ",n,"nombres qui se repète chacun  deux fois et ",p== len(L)-n*2 , "nombre qui se repète pas.")
        
