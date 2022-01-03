import math
1. Создать переменную item_1 типа integer.
item_1 = 10
2. Создать переменную item_2 типа integer.
item_2 = 25
3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.
result_sum = item_1 + item_2
4. Вывести result_sum в консоль.
print(result_sum)
5. Создать переменную result_subtr в которой вы вычитаете 
большую по значению переменную из меньшей по значению.
result_subtr = item_2 - item_1
print(result_subtr)
6. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
result_m_exp = item_1 ** item_2
print(result_m_exp)
7. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item 
result_s_root = item_2 ** 0.5
print("Sqrt of item_2 - ", result_s_root)
7. Создать переменную result_m_s_root в которой вы item_1 возводите в степень item_2 используя библиотеку math.
result_m_s_root = math.sqrt(item_2)
print("Kvadratniu koren - ", result_m_s_root)
8. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
result_mp_s_root = math.pow(item_2, 0.5)
print("Math pow square = ", result_mp_s_root)
9. Присвоить переменной item_1 odd значение
item_1 = 13
10. Присвоить переменной item_2 even значение
item_2 = 12
11. Создать переменную result_division в которой вы разделите item_1 на item_2.
result_division = item_1 / item_2
print("Item1 / item 2 = ", result_division)

12. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
result_m_floor = math.floor(result_division)
print("Okryglenie =", result_m_floor)

13.  Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
result_m_ceil =math.ceil(result_division)
print("Okryglenie 1 <", result_m_ceil)

14. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
result_int = int(result_division)
print("Celoe =", result_int)

15. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
result_no_division_loss = item_1 // item_2
print("Bez ostatka =", result_no_division_loss)

16. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
result_division_loss = item_1 % item_2
print("Ostatok =", result_division_loss)

17. Создать переменную item_3 и присвоить ей целое число
item_3 = 10
18. Прибавить 10 к item_3 с присвоением.
item_3 += 10
print("+", item_3)

19. Отнять 5 от item_3 с присвоением. 
item_3 -=5
print("- ", item_3)

20. Умножить item_3 на 3 с присвоением.
item_3 *=3
print("*", item_3)

21. Разделить item_3 на 2 с присвоением.
item_3 /=2
print("/ ", item_3)

22. Возвести в степень 2 item_3 с присвоением.
item_3 **=2
print("Stepen 2 =", item_3)

23. Найти квадратный корень item_3 с присвоением.
item_3 **=0.5
print("Koren` =", item_3)

24.  Присвоить остаток от деления item_3
item_3 %=5
print("Ostatok =", item_3)


#boolean
25. Создать переменную b_item_t и присвоить True
b_item_t = True

26. Создать переменную b_item_f и присвоить False
b_item_f = False

27. Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
b_item_result_sum =b_item_t + b_item_f
print("True + False =", b_item_result_sum)

28. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
b_item_result_subtr = b_item_t - b_item_f
print("True - False =", b_item_result_subtr)

29. Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
b_item_result_multi = b_item_t * b_item_f
print("True * False =", b_item_result_multi)

30. Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f
31. Вывести b_item_relult_division в консоль. (Получить ошибку)
#error b_item_division = b_item_t / b_item_f
#error print(b_item_division)

32. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
b_item_1_int = int(b_item_t)

33. Создать переменную b_item_2_int и присвоить явное приведение b_item_2 к int 
b_item_2_int = int(b_item_f)
print("True int =" + str(b_item_1_int) + " False int " + str(b_item_2_int))
