#програма яка розкладае слово по буквах
#slovo=input("ведіть слово ")
#for letter in slovo:
#    print (letter)
import random
kkk=random.randint(1,9)
wq = [1,2,3,4,5,6,7,8,9]
wq.remove(kkk)
for letter in wq:
    print (letter)
wen = False
while not wen:
    print("всего 9 чисел")
    nt=int (input ("какое число пропушено?"))
    if nt>9:
        print("такого числа вообше нет в єтом переборе!!!")
    elif nt==kkk:
        print ("єто ано молодец")
        wen = True
    else:
        print ("єто не ано")
        if nt<kkk:
            print("оно слишком маленькое")
        else:
            print("оно слишкам большое")