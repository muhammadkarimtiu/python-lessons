# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 20:02:47 2021

@author: Muhammadkarim
"""
# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

# def tyil_hisobla(ism, yosh):
#     """
#     Ism va yoshni so'rab, foydalanuvchining yilini hisoblab beruvchi funksiya
#     """
#     print(f"{ism.title()} {2021 - yosh}-yilda to'g'ilgan")

# ism = input("Ismingiz: ")
# yosh = int(input("Yoshingiz: "))
# tyil_hisobla(ism, yosh)

# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

def kub_hisobla(son):
    """
    Sonning kvadrati va kubini hisoblovchi funksiya
    """
    kv = son**2
    kub = son**3
    print(f"{son} ning kvadrati {kv} ga, kubi {kub} ga teng.")
    
son = int(input("Son kiriting: "))
kub_hisobla(son)