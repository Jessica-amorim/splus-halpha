# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:11:10 2020

@author: 55119
"""
''
p1=int(input("digite nota 1:" ))
p2=int(input("digite nota 2:" ))
p3=int(input("digite nota 3:" ))
MedA=((p1+p2+p3)/3)
MedF=MedA
if MedF>5:
    print("aprovado")
else:
    print("recuperação")
    rec=int(input("nota rec:" ))
    if rec<5:
        print("reprovado")
    else:
        print("aprovado")
        