"""
? Вам дана строка с действительным IP адресом - IPv4.
! На вход поступает строка следующего вида: address = "1.1.1.1"
* Необходимо в полученном адресе заменить все точки на [.]
---
Пример:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""

address = "255.100.50.0"

new_address = ""

for char in address:
    if char == '.':
       new_address += '[.]'
    else:
        new_address += char

print(new_address)