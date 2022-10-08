from itertools import *
def bts(str):
     k= permutations(str)
     for i in list(k):
         print (''.join(i))
str=input()
bts(str)