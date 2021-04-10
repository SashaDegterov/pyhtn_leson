# kod = input("Введіть код для зачинення сейфу: ")
# if len(kod) > 5:
#     print("second condtion")
#     if len(kod) < 10:
#         print("third condtion")
#         if input("введіть код ще раз")==kod:
#             print("код вірно сейф зачинено")
#         else:
#             print("не вірно почінайте знову")
#     else:
#         print("код занадто великий")
# else:
#     print ("Код занадто малий")

# рограмма для зачинення сейфу

safe_open = True

while safe_open:
    kod = input("Введіть код для зачинення сейфу: ")
    if len(kod) <= 5:
        print ("Код занадто малий")
    elif len(kod) >= 10:
        print("код занадто великий")
    elif input("введіть код ще раз")==kod:
        print("код вірно сейф зачинено")
        safe_open = False
    else:
        print("не вірно почінайте знову")