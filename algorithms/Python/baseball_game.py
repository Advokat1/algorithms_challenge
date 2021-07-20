"""
? Вам дан лист команд для записи очков в некоторой игре. Подсчёт итогового набора баллов идёт за счёт последовательного выполнения указанных ранее правил.
! На вход подаётся массив вида: ops = ["5","2","C","D","+"]
* Необходимо посчитать итоговую сумму баллов для раунда некоторой игры, применив последовательно команды из переданного списка.
Переданное число x - новая запись для переменной total.
"+" - Добавить в total сумму двух последних элементов.
"D" - Добавить в total двойное значение последнего элемента.
"C" - Удалить из total последний элемент.
---
Пример:
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
"""


ops = ["5","2","C","D","+"]
total = []

#*Цикл по элементам ops для выполнения действия с переменной total  
for item in ops:
    if item == 'C':
        total.pop()
    elif item == 'D':
        total.append(total[-1]*2)
    elif item == '+':
        total.append(total[-1]+total[-2])
    else:
        total.append(int(item))

print(sum(total))