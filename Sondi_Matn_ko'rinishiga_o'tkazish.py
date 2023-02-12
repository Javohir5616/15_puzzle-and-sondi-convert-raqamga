#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:45:08 2023

@author: javohir
"""

onliklar={1:"o'n",2:"yigirma",3:"o'ttiz",4:"qirq",5:"ellik",6:"oltmish",7:"yetmish",8:"sakson",9:"to'qson"}
birliklar={1:"bir",2:"ikki",3:"uch",4:"to'rt",5:"besh",6:"olti",7:"yetti",8:"sakkiz",9:"to'qqiz"}
son=int(input("Son kiriting:"))

print("Matn ko'rinishida:",end=" ")

if son==0:
    print("nol")

if len(str(son))==10:
    print("bir milliard",end=" ")
    son=son%1000000000
    

while son>0:
    buluvchi=10**(len(str(son))-1) # Sondi boshidan qisqartirib borish uchun yordam beradigan buluvchi u har doim sondi uzunligidan kelib chiqib o'garadi
    # Million uchun
    if len(str(son))>6 and len(str(son))<10:
        
        if len(str(son))%3==0:
            if int(str(son)[1])!=0 or int(str(son)[2])!=0:
                print(birliklar[int(str(son)[0])],"yuz",end=" ")
            elif int(str(son)[1])==0 or int(str(son)[2])==0:
                print(birliklar[int(str(son)[0])],"yuz million",end=" ")
                
        elif len(str(son))%3==2:
            if int(str(son)[1])!=0 and int(str(son)[2])!=0:
                print(onliklar[int(str(son)[0])],end=" ")
            elif int(str(son)[1])==0 and int(str(son)[2])==0:
                print(onliklar[int(str(son)[0])],"million",end=" ")
                
        elif len(str(son))%3==1:
            print(birliklar[int(str(son)[0])],"million",end=" ")
    # Minglik uchun
    elif len(str(son))>3 and len(str(son))<7:
        
        if len(str(son))%3==0:
            if int(str(son)[1])!=0 or int(str(son)[2])!=0:
                print(birliklar[int(str(son)[0])],"yuz",end=" ")
            elif int(str(son)[1])==0 or int(str(son)[2])==0:
                print(birliklar[int(str(son)[0])],"yuz ming",end=" ")
                
        elif len(str(son))%3==2:
            if int(str(son)[1])!=0:
                print(onliklar[int(str(son)[0])],end=" ")
            elif int(str(son)[1])==0:
                print(onliklar[int(str(son)[0])],"ming",end=" ")
                
        elif len(str(son))%3==1:
            print(birliklar[int(str(son)[0])],"ming",end=" ")
            
    # Yuzlik uchun
    elif len(str(son))==3:
        print(birliklar[int(str(son)[0])],"yuz",end=" ")
        
    # O'nlik uchun
    elif len(str(son))==2:
        print(onliklar[int(str(son)[0])],end=" ")
        
    # Birlik uchun
    elif len(str(son)):
        print(birliklar[int(str(son)[0])],end=" ")
    
    # Sondi bir honadan qisqartirib boradi
    son=son%buluvchi