#програма вгадай число
win = False
a=5
while not win:
    s=input ("введіть число меньше десяти")
    if int(s) > 10:
        print ("число занабто велике")
    elif int (s)==a:
        print ("молодець вгадав")
        win = True
    else:
        print ("не вгадав починай знов")
