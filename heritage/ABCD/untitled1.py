voyelles=['A','E','I','O','U','Y']
mot=input("entrez un mot en majuscule")
n=len(mot)
S=0

for i in range(0,n) :
    if mot[i] in voyelles:
        print("la position de",mot[i]," est ",i+1 )
            
    
     
        
    