while True:
    Parol=input("Parolunuzu daxil edin: ")
    if not Parol:
        print("Parolu yazmadan sisteme daxil ola bilmezsiz")
    elif len(Parol)>3 or len(Parol)<8:
        print("Parolunuz 3 den kicik ve 8 den boyuk ola bilmez")
    else:
        print("Sisteme hos geldiniz")
        break

#Gisman