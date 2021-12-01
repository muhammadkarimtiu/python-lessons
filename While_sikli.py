# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 20:33:20 2021

@author: Muhammadkarim
"""

# print("Yaxshi ko'rgan kitoblarni kirituvchi dastur")
# savol = "Kitob kiriting"
# savol += "(to'xtatish uchun \"Stop\" so'zini yozing): "
# kitob = ''
# while True:
#     kitob = input(savol)
#     if kitob.lower() == 'stop':
#         break
# print("Dastur tugadi")


# savol = "Yoshingizni kiriting: "
# ishora = True
# while ishora:
#     yosh = input(savol)
#     if yosh == 'exit' or yosh == 'quit':
#         ishora = False
#         continue
#     yosh = int(yosh)
    
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh == 0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta narhi {narh} so'm")


# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")


# # While sikli orqali lug'at tuzish
# frinds = {}
# flag = True
# while flag:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = int(input(f"{ism.title()}ning yoshini kiriting: "))
#     frinds[ism] = yosh
    
#     javob = input("Yana ma'lumot qo'shasizmi ?")
#     if javob != 'ha':
#         flag = False
# print("Do'stlaringizning yoshlari")
# for ism, yosh in frinds.items():
#     print(f"{ism.title()} {yosh} yoshda")

# Buyurtma qabul qiluvchi dastur
buyurtmalar = []
print("Buyurtmalaringizni kirting!")
while True:
    buyurtma = input("Mahsulot kiriting: ")
    buyurtmalar.append(buyurtma)
    javob = input("Yana qo'shasizmi (ha/yo'q)")
    if javob != 'ha':
        break


# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
mahsulotlar = {}
while True:
    mahsulot = input("Mahsulot kiriting: ")
    narx = input(f"{mahsulot.title()}ning narxini kiriting: ")
    mahsulotlar[mahsulot] = int(narx)
    javob = input("Yana kiritasizmi (ha/yo'q)")
    if javob != 'ha':
        break
# for mah, narx in mahsulotlar.items():
#     print(f"{mah.title()}ning narxi {narx} so'm")

# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni
# e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin).
# Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda
# "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

# for buyurtma in buyurtmalar:
#     if buyurtma in mahsulotlar:
#         print(f"{buyurtma.title()}ning narxi {mahsulotlar[buyurtma]} so'm")
#     else:
#         print(f"Bizda {buyurtma.lower()} yo'q")

while buyurtmalar:
    buyurtma = buyurtmalar.pop();
    if buyurtma in mahsulotlar:
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"{buyurtma.title()} yo'q")

