#                               15-dars Lugat

## Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi
# # har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib
# # konsolga chiqaring. 


python_0 = {
    'if':'Shartlarni tekshirish operatori',
    'integer':'Butun son',
    'float':'O\'nlik son',
    'tuple':'o\'zgarmas lugat',
    'for':'Biror amalni qayta-qayta bajarish tsikli'    
    }

for k, v in sorted(python_0.items()):
    print(f"{k.title()} - {v} ")
    
    
## Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
# #keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 

davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}

print("Dunyo davlatlari!")
for davlat in sorted(davlatlar):
    print(davlat.upper())
    
print("\n Davlatlar poytaxti")

for poytax in sorted(davlatlar.values()):
    print(poytax.upper()) 


# #Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini
# # konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa,
# # "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.


country = input('Qaysi davlatni poytaxtini bilishini hohlaysiz?')
capital = davlatlar.get(country)

if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")  

## Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
## Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan 
## taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating,
# # aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }

print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")


















