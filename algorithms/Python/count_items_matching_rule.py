"""
? Вам дан массив items, который состоит из элементов следующего вида: items[i] = [typei, colori, namei] где тип, цвет и название - пояснения раскрывающие данные об элементе.
! На вход подается строка, состоящаяя из двух элементов: ruleKey, ruleValue.
* Необходимо посчитать количество элементов массива items, соответствующик указанным данным в переданной строке.
---
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]
ruleKey = "color", ruleValue = "silver"
На выходе будет выдано: 1, так как всего одна запись в массиве соответствует правилу color = silver
"""

items = [
    ["phone","blue","pixel"],
    ["computer","silver","lenovo"],
    ["phone","gold","iphone"]
]

ruleKey = input('Введите ключ')
ruleValue = input('Введите значение')

def count_items(items, ruleKey, ruleValue):
    count = 0
    rule = {
        'type': 0,
        'color': 1,
        'name': 2,
    }
    for item in items:
        if item[rule[ruleKey]] == ruleValue:
            count+=1
    
    return count


print(count_items(items, ruleKey, ruleValue))