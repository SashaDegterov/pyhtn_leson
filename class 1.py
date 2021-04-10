import random
answer=random.randint (0,10)
wen = False
while not wen:
    cod=int(input("угадай число"))
    if cod == answer :
        print("вы угадали число!")
        wen = True
    else:
        print("ваш ответ не верный!")
        if cod > answer : 
            print("слишком большое число")
        if cod < answer : 
            print("слишком маленькое число")
