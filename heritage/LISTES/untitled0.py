L=[-15,3,12,10,14,1,15,40,100,6]

#fixer les valeurs une par une avec une boucle for
for i in range(len(L)):
#pour chaque position rechercher dans le suite s'il y a des valeurs plus petites
    for j in range(i+1, len(L)):
       if L[j]<L[i]:
         V=L[i]
         L[i]=L[j]
         L[j]=V
print(L)
   
        