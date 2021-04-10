#игра разговор.py
import random
name=input("какой твой ник?")
print ("приятно познакомится",name)
print ("ті находешся в пешере и тут три вихода")
while True:
    go=int (input ("вібери путь 1 2 или 3"))
    if go==1:
        print ("перед вами белій дракон")
        drakonxp=random.randint (1,20)
        print("вот его хєпє",drakonxp,'попитайся его убить')
        while drakonxp > 0 :
            wopros=int (input("ті хочеш ударить дракона???1-Да 2-нет"))
            if wopros==1:
                print ("-5 хп у ракона")
                drakonxp=drakonxp-5
            else:
                print("дркон вам недает пройти вам надо его убить")
        print ("проход закончился тупиком и вернулись обрано")
    if go==2:
        print("перед вами крастній дракон")
        dregonred=random.randint (1,40)
        print("у даракона",dregonred,"1-папробуй его убить или 2-отгадай загадку")
        anser=int (input (''))
        if anser==1:
            while dregonred > 0 :
                wopros=int (input("ті хочеш ударить дракона???1-Да 2-нет"))
                if wopros==1:
                    print ("-5 хп у ракона")
                    dregonred=dregonred-5
                else:
                    print ("дракон вам не дает пройти вам надо его убить")
        if anser==2:
            nevgadav = True
            while nevgadav:
                print("отгодай загадку")
                print("зимой и летом одним цветом")
                vidpobid=(input(""))
                if vidpobid=="ель":
                    print ("молодец дракон ушол")
                    print ("но нет проход закончился тупиком")
                    nevgadav = False
                else:
                    print("ответ не верен дракон вам недает пройти")