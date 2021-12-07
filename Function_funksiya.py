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

# def kub_hisobla(son):
#     """
#     Sonning kvadrati va kubini hisoblovchi funksiya
#     """
#     kv = son**2
#     kub = son**3
#     print(f"{son} ning kvadrati {kv} ga, kubi {kub} ga teng.")
    
# son = int(input("Son kiriting: "))
# kub_hisobla(son)

# def oraliq(min, max, qadam = 1):
#     """
#     range funksiyasini uzbekchasi
#     """
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# # print(oraliq(2, 8))
# toq_sonlar = oraliq(1, 20, 2)
# juft_sonlar = oraliq(0, 21, 2)
# print(toq_sonlar)
# print(juft_sonlar)

# def avto_info(kompaniya, model, rangi, karobka, yili, narhi = None):
#     """ Avtomobil haqida ma'lumotlarni olib lug'at qilib qaytaradi """
#     avto = {
#         'kompaniya' : kompaniya,
#         'model' : model,
#         'rang' : rangi,
#         'karobka' : karobka,
#         'yil' : yili,
#         'narh' : narhi
#         }
#     return avto
# avtolar = []
# print("Avtomobil ma'lumotlarini kiriting")
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting", end='')
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     karobka = input("Karobkasi: ")
#     yili = input("Yili: ")
#     narhi = input("Narhi: ")
#     avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))
    
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break
# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model']} narhi {narh}")


# def user_info(ism, familiya, t_yili, t_joyi, email = '', phone = None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     user = {
#         'ism' : ism,
#         'familiya' : familiya,
#         't_yil' : t_yili,
#         't_joy' : t_joyi,
#         'yosh' : 2021-t_yili,
#         'email' : email,
#         'telefon' : phone
#         }
#     return user
# print("Ma'lumotlaringizni kiriting")
# users = []
# while True:
#     ism = input("Ismingiz: ")
#     familiya = input("Familiyangiz: ")
#     t_yil = int(input("To'g'ilyan yilingiz: "))
#     t_joy = input("To'g'ilgan joyingiz: ")
#     email = input("E-mail: ")
#     telefon = input("Tel. raqamingiz: ")
    
#     users.append(user_info(ism, familiya, t_yil, t_joy, email, telefon))
    
#     javob = input("Yana qo'shasizmi? (ha/yo'q): ")
#     if javob != 'ha':
#         break
# print("\nFoydalanuvchilar haqida ma'lumot':")
# for user in users:
#     print(f"{user['familiya'].title()} {user['ism'].title()} {user['yosh']}da {user['t_joy']}da yashaydi")
    

# def kattasi(x,y,z):
#     max = x
#     if y > max:
#         max = y
#     if z > max:
#         max = z
#     return max
#     # sonlar = [x,y,z]
#     # sonlar.sort(reverse=True)
#     # katta =sonlar[0]
#     # return katta
# print(kattasi(15, 82, 22))

# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri
# va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
# def aylana_hisobla(radus):
#     aylana = {
#         'radius' : radus,
#         'diametr' : 2*radus,
#         'perimetri' : 2*3.14*radus,
#         'yuzi' : 3.14*radus**2
#         }
#     return aylana
# print(aylana_hisobla(5))

# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar

# print(tub_sonlar_top(1,20))
# print(len(tub_sonlar_top(1, 20)))

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(10))

























