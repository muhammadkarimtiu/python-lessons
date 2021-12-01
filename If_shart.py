# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:42:34 2021

@author: Muhammadkarim
"""

# yosh = int(input("Yoshingiz nechada? "))

# if yosh < 18: print(f"Uzr yoshingiz {yosh} da ekan")

# print(f"Marhamat sizga mumkin {yosh} da ekansiz") if yosh >= 18 else print(f"Uzr yoshingiz {yosh} da ekan")

# cars = ['toyota', 'nessan', 'gm', 'volvo']
# for car in cars:
# #    print(car.upper()) if car == 'gm' elsa print(car.title())
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# user = input("Login kiriting: ")
# if user.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {user}!")

# son = float(input("Sonni kiriting "))
# # print("Manfiy son") if son < 0 else print("Musbat son")
# print("Musbat son kiriting") if son < 0 else print(f"{son**(1/2)}")

# son = float(input("Juft son kiriting "))
# print("Rahmat!") if son%2 == 0 else print("Bu son juft emas")

# yosh = int(input("Yoshingiz: "))
# if yosh < 4 or yosh > 60:
#     narh = 0;
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Bilet narhi {narh} so'm")

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa
# "Mahsulot do'konimizda bor" aks holda,"Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulatlar = ['non', 'guruch', 'mosh', 'sabzi', 'piyoz', 'kartoshka', 'karam', 'tuz', 'choy', 'loviya', 'un', 'makaron']
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulot: "))
# for mahsulot in savat:
#     if mahsulot in mahsulatlar:
#         print("Mahsulot do'konimizda bor")
#     else:
#         print("Mahsulot do'konimizda yo'q")
        
# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga,
# do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa,
# "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

# mahsulatlar = ['non', 'guruch', 'mosh', 'sabzi', 'piyoz', 'kartoshka', 'karam', 'tuz', 'choy', 'loviya', 'un', 'makaron']
# savat = []

# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulot: "))

# bor_mahsulotlar = []
# mavjud_emas = []

# for mahsulot in savat:
#     if mahsulot in mahsulatlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("Quyidagi mahsulotlar do'konimizda yo'q:" )
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
# users = ['mktiu', 'olim', 'anvar', 'sobir', 'dinmuhammad']
# user = input("Yangi login kiriting: ")
# if user.lower() in users:
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {user.title()}!")

son = int(input("Butun son kiriting: "))
for n in range(2, 11):
    if not son % n:
        print(n)


