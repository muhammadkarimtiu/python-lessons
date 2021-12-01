# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:37:24 2021

@author: Muhammadkarim
"""

mevalar = ['olma', 'anor', 'shaftoli', 'gilos', 'banan']

mevalar.append('uzum')
print(sorted(mevalar))
print(sorted(mevalar, reverse=True))

# uzunlik = len(mevalar)

# sonlar = list(range(1, 11))

# toq_sonlar = list(range(1, 10, 2))
# print(toq_sonlar)

# print(mevalar[1:5])

olingan_mevalar = mevalar[:3]
print(olingan_mevalar)
olinmagan_mevalar = mevalar[3:]
print(olinmagan_mevalar)
