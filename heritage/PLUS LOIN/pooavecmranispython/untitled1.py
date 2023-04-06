from random import *
a=randint(0,100)
nombre=-1
while nombre!=a :
  nombre=int(input("devinez le nombre a"))
  if nombre<a :
    print("réessayez ,c'est petit")
  elif nombre>a :
    print("réessayez,c'est grand")
  else :
    print("bingo")
    