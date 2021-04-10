# Програма яка складае два введених числа

while True:
    a = input("ведіть вироз який хочите порахувати ")
    l = a.split()
    if len(l) != 3:
        print ("вираз мае склодатися з двух чисел и оператором посередині виделеного пробілами")
    d1, op, d2 = l
    if op != "+,-,*,/":
        print ("тут такого действия нету")
    if op == "+":
        print (a,'= ', int(d1) + int(d2))
    elif op == "-":
        print (a,"=", int(d1) - int(d2))
    elif op == "*":
        print (a,"=",int(d1) * int(d2))
    elif op == "/":
        print (a,"=",int(d1) / int(d2))
    q = input("продовжимо? так = y, ні інша літера ")
    if q not in ("y", "e", "н", "у"):
        break