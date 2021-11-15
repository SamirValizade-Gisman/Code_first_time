giriş = """
(1) toplama
(2) çıxma
(3) vurma
(4) bölmə
(5) kvadratını hesapla
(6) kvadrat kökü hesapla
"""

print(giriş)

sual = input("Hesablamaq istədiyiniz əməlin nömrəsini daxil edin: ")

if sual == "1":
    say1 = int(input("Toplama əməli üçün ilk rəqəmi daxil edin: "))
    say2 = int(input("Toplama əməli üçün ikinci rəqəmi daxil edin: "))
    print(say1, "+", say2, "=", say1 + say2)

elif sual == "2":
    say3 = int(input("Çıxma əməli üçün ilk rəqəmi daxil edin: "))
    say4 = int(input("Çıxma əməli üçün ikinci rəqəmi daxil edin: "))
    print(say3, "-", say4, "=", say3 - say4)

elif sual == "3":
    say5 = int(input("Vurma əməli üçün ilk rəqəmi daxil edin: "))
    say6 = int(input("Vurma əməli üçün ikinci rəqəmi daxil edin: "))
    print(say5, "x", say6, "=", say5 * say6)

elif sual == "4":
    say7 = int(input("Bölmə əməli üçün ilk rəqəmi daxil edin: "))
    say8 = int(input("Bölmə əməli üçün ikinci rəqəmi daxil edin: "))
    print(say7, "/", say8, "=", say7 / say8)

elif sual == "5":
    say9 = int(input("Kvadratını hesablamaq istədiyiniz rəqəmi daxil edin: "))
    print(say9, "rəqəmin kvadratı =", say9 ** 2)

elif sual == "6":
    say10 = int(input("Kvadrat kökünü hesablamaq istədiyiniz rəqəmi daxil edin: "))
    print(say10, "rəqəmin kvadrat kökü = ", round((say10 ** 0.5),2))

else:
    print("Səhv giriş")
    print("Aşağıdakı girişlərdən birini seçin:", giriş)