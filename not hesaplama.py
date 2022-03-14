def nothesaplama(satır):
    satır=satır[:-1]
    liste=satır.split(",")
    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])
    ortalama=not1*(3/10)+not2*(3/10)+not3*(4/10)

    if ortalama>=90:
        harf="AA"
    elif ortalama>=80:
        harf="BA"
    elif ortalama>=70:
        harf="BB"
    elif ortalama>=60:
        harf="CB"
    elif ortalama>=50:
        harf="CC"
    else:
        harf="FF"

    return isim+"---------->"+harf+"\n "


with open("dosya.txt","r",encoding="utf-8") as b:
    yeniliste=[]
    for i in b:
        yeniliste.append(nothesaplama(i))
    with open("harfnotları.txt","w",encoding="utf-8") as c:
        for i in yeniliste:
            c.write(i)

