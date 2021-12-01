# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:38:12 2021

@author: Muhammadkarim
"""

# otam = {'ismi' : 'bahodir', 't_yil' : 1969, 't_joy' : 'samarqand'}
# print(f"Otamning ismi {otam['ismi'].title()}, {otam['t_yil']}-yilda, {otam['t_joy'].title()} viloyatida to'g'ilgan")

python_atamlar = {
    'int' : 'Butun son',
    'string' : 'Matn',
    'list' : 'Ro\'yxat',
    'dictionary' : "lo'g'at",
    'if' : 'Shart operatori',
    'for' : 'Uchun takrorlash operatori',
    'bool' : 'Mantiqiy amal'
    }
# atama = input("Python atamasini kiriting: ")
# print(python_atamlar.get(atama, 'Bunday atama mavjud emas'))

# for k, q in sorted(python_atamlar.items()):
#     print(f"{k.title()} - {q}")
# for key in sorted(python_atamlar.keys()): print(key)
# for value in sorted(python_atamlar.values()): print(value)


davlatlar = {
    "o‘zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'
    }
# davlat = input("Istalgan davlat kiriting: ").lower()
# capital = davlatlar.get(davlat)
# if capital == None:
#     print("Bizda bunday ma'lumot yo'q")
# else:
#     print(capital.title())


buyurtmalar = []
menu = {        
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom: ").lower())
for taom in buyurtmalar:
    if taom in menu:
        print(f"{taom}ning narhi: {menu[taom]}")
    else:
        print("Bizda bunday taom yo'q")
    
    