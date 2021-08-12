"""
? Вам заголовок бинарного числа в виде массива, состоящего из последовательного набора "0" и "1".
! На вход подаётся массива вида: head = [1, 0, 1]"
* Необходимо вернуть десятичное представление указанного в заголовке двоичного числа.
Пример:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
"""
head = [1, 0, 1, 0]

def convert_to_decimal(head):
    rank = 0
    decimal = 0
    for i in range(len(head)-1, -1, -1):
        decimal += head[i] * 2**rank
        rank += 1
    return (decimal)

print(convert_to_decimal(head))