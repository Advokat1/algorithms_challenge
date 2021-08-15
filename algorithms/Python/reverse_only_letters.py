"""
? Вам дана строка "s" состоящая из символов и букв.
! На вход подаётся одна строка: s = "a-bC-dEf-ghIj"
* Необходимо вернуть перевернутую строку, но при этом переворачиваются только буквы, символы свой порядок не меняют.
Пример:
Input: s = "ab-cd"
Output: "dc-ba"
"""

s = "a-bC-dEf-ghIj"

def reverse_letters(s):
        letters = [c for c in s if c.isalpha()]
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)

print(reverse_letters(s))