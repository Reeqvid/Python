int_item = 10
comp_item = 18
multi_int = int_item * 2
item_2 = True
item_3 = False
item_4 = 0
item_5 = 14

usd_item = "usd"
usd_usd_rate = 1

eur_item = "eur"
usd_eur_rate = 0.86

uah_item = "uah"
usd_uah_rate = 26.23

chf_item = "chf"
usd_chf_rate = 0.91

byn_item = "byn"
usd_byn_rate = 2.46

if multi_int > comp_item:
    print("Переменная multi_int больше", comp_item)

div_int  = int_item / 2
if div_int < comp_item:
    print("Переменная div_int меньше", comp_item)

item_1 =int_item + 10
if item_1 < comp_item:
    print("Переменная item_1 меньше", comp_item)
else:
    print("Переменная item_1 больше или равна", comp_item)

if item_2:
    print("Переменна item_2 =", item_2)
else:
    print("Переменная item_2 =", item_3)

if item_3:
    print("Переменна item_3 =", item_2)
else:
    print("Переменная item_3 =", item_3)

if item_5:
    print("Переменна item_5 =", item_5)
else:
    print("Переменная item_5 =", item_4)

if item_4:
    print("Переменна item_4 =", item_5)
else:
    print("Переменная item_4 =", item_4)


currency_convertor = item_2
if currency_convertor:
    currency_usd = usd_item
    target_currency = input("Выберите валюу eur,uah,chf,byn - ")
    target_currency_amount = input("Введите количество валюты для конвертации - ")
    currency_result = 0
    if target_currency == "eur":
        currency_result = float(target_currency_amount) / usd_eur_rate
        print(target_currency_amount, eur_item, "=", currency_result, usd_item)
    elif target_currency == "uah":
        currency_result = float(target_currency_amount) / usd_uah_rate
        print(target_currency_amount, usd_item, "=", currency_result, uah_item)
    elif target_currency == "chf":
        currency_result = float(target_currency_amount) / usd_chf_rate
        print(target_currency_amount, chf_item, "=", currency_result, usd_item)
    elif target_currency == "byn":
        currency_result = float(target_currency_amount) / usd_byn_rate
        print(target_currency_amount, byn_item, "=", currency_result, usd_item)
    else:
        print("Неккоректная валюта")
else:
    print("Перменная currency_convertor =", item_3)