icazeli_simvollar = "0123456789+-/*= "

print("""
Sadə bir hesab maşını proqramı.

Operatorlar:

    +   toplama
    -   çıxma
    *   vurma
    /   bölmə

Hesablamaq istədiyiniz əməli yazıb ENTER
düyməsinə basın. (məsələn 23 və 46 rəqəqmlərini
vurmaq üçün 23 * 46 yazdıqdan sonra
ENTER düyməsinə basın.)
""")

while True:
    data = input("Əmriniz: ")
    if data == "q":
        print("Sistemdən çıxılır...")
        break

    for s in data:
        if s not in icazeli_simvollar:
            print("Nə etmək istıyirsiz?!")
            quit()

    hesab = eval(data)

    print(hesab)

#GISMAN