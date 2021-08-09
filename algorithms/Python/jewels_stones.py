"""
? Вам дана строка jewels содержащая типы драгоценных камней и строка stones описывающая набор камней по их типу.
! На вход подаётся jewels = "aA", stones = "aAAbbbb"
* Необходимо посчитать количество камней строки stones, соответствующих указанным типам.
Важно заметить, что регист играет роль и типы "а" и "А" являются разными.
В ответ необходимо вывести количество совпадений.
---
Пример:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Explanation: a -- 1 + A -- 2
"""

jewels = 'aA'
stones = 'aAAbbbb'

def stones_counting(jewels, stones):
    stone_count = 0
    
    for char in stones:
        if char in jewels:
            stone_count += 1
    return stone_count

print(stones_counting(jewels, stones))