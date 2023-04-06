# -*- 

nbre1=float(input("entrer la premiere valeur: "))
nbre2=float(input("entrer la seconde valeur: "))
while (nbre2==nbre1):
  nbre2=float(input("entrer de nouveau la seconde valeur"))
nbre3=float(input("entrer la troisième valeur: "))
while (nbre3==nbre2 or nbre3==nbre1):
  nbre3=float(input("entrer de nouveau la troisième valeur"))
print ("La somme est = ",nbre1+nbre2+nbre3)
print ("La moyenne est = ", (nbre1+nbre2+nbre3)/3)


N=float(input("Saisie une valeur : "))
somme=0
while N!=-1:
   somme=somme+N
   N=float(input("Donnez la valeur suivante : "))
print(somme)