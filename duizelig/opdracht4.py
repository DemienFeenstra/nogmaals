# Vraag een dag van de week op (ma,di,wo,do,vr,za,zo) Print alle dagen tot en met de opgegeven dag.

Day = input("Typ een dag van de week: ")
a = 2
while a < 3:
    if Day == "maandag":
        print("maandag")
        break
    elif Day == "dinsdag":
        print("maandag", "dinsdag")
        break
    elif Day == "woensdag":
        print("maandag", "dinsdag", "woensdag")
        break
    elif Day == "donderdag":
        print("maandag", "dinsdag", "woensdag", "donderdag")
        break
    elif Day == "vrijdag":
        print("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag")
        break
    elif Day ==  "zaterdag":
        print("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag")
        break
    elif Day == "zondag":
        print("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")
        break
    else:
        print("fout opgetreden!")
        break