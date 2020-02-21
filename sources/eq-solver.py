from fractions import Fraction #To implement algorithm without messing floats
from decimal import Decimal
import math as m
import sys#For CLI input
def factor(arg1):#Factor finding function
   l = [1]
   a = 2
   while a <= abs(arg1):
      if arg1%a == 0 :
         l.append(a)
      a = a + 1
   return l
def plot (o, d, t, dlist):#Taable maker function, for comments goto table-maker.py
   y = 0
   xlist=[]
   fxlist=[]
   r = o
   while o<= r and r<= d:
      for j in range(len(dlist)):
         y = dlist[j]*r**(len(dlist) -1 -j) + y
         xlist.append(r)
         fxlist.append(y)
         y = 0
         r = float(Decimal(r) + Decimal(t))
   return xlist, fxlist
def mark(lm, qlist):#Table maker function modified for single value
   kj = 0
   for re in range(len(qlist)):
      kj = qlist[re]*lm**(len(qlist) -1 -re) + kj
   return kj
inlist = list(map(float,sys.argv[1:]))#List of coefficients
zlist =[]
a = inlist[0]#Leading coefficient
t =-1
while inlist[t] == 0:#Constant or coefficient of smallest term
    t = t-1
    zlist.append(0)
c = inlist[t]
while m.ceil(c) != c  or m.ceil(a) != a:
   c =c*10
   a =a*10
   inlist=list(map(lambda num: num*10, inlist))
n = 2
alist =[*factor(a), *list(map(lambda x: x*(-1), (factor(a))))]#Factors of leading coefficient
clist =[*factor(c), *list(map(lambda x: x*(-1), (factor(c))))]#Factors of constant or smallest coefficient
for w in range (len(clist)): #Running the algorithm, the algorithm is described in README.md
   for q in range (len(alist)):
       z =  Fraction(clist[w], alist[q])
       if mark(float(z), inlist ) ==0:
         zlist.append(z)

print(' , '.join(list(set(map(str, zlist)))))
""" That's a big thing in one line. I took the answer list, converted them to string,
and converted the strings in a single line string. Thats the answer.
Note: The answer is shown in fraction. Pretty, right?"""
