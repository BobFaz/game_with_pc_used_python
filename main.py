# --------------------so'z topish o'yinini komputer bilan o'ynash.----------------------------------
#-------BobFaz----------

import random


# ------------ komputer son o'ylidi biz topamiz ---------------------------
def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi ?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato, Men o'ylagan son bundan kattaroq. Yana harakat qiling")
        elif taxmin>tasodifiy_son:
            print("Xato, Men o'ylagan son bundan kichikroq. Yana harakat qiling")
        else:
            break
    print(f"Tabriklayman, siz {taxminlar} ta taxmin bilan topdingiz")
    return taxminlar

#---------- biz son o'ylimiz komputer topadi.---------------------
def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing, men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0

    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'gri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin -1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim")
    return taxminlar

#--------------------- ikkala funksiyani jamlash va taxminlarda ham kim yutganini ko'rsatish ---------------------
def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)

        if taxminlar_user > taxminlar_pc:
            print("Men yutdim")
        elif taxminlar_pc > taxminlar_user:
            print("Siz yutdingiz")
        else:
            print("Durrang")
        yana = int(input("Yana o'ynaysizmi ? ha(1)/ yo'q(0):"))
    if yana ==0:
        print("Qiziqarli o'yin uchun tashakkur")
play()
