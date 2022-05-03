# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 23:59:38 2020

@author: ray34
"""
n=int(input()) 
ipline=input() 
scores=list(map(int,ipline.split()))
scores.sort()
s=-1
for i in range(len(scores)):
    print(scores[i], end=' ')  
    if scores[i] < 60 :
        s= i   
print()        
if s== -1:     
    print( 'best case')
else:
    print(scores[s])  
if s== n-1 :  
    print( 'worst case')
else:    
    print(scores[s+1])


    


    
