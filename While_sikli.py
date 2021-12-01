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


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")





