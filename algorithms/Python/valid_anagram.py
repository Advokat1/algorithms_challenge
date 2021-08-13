"""
? Вам даны две строки "s" и "t". Проверить являются ли они анограмами друг для друга
! На вход подаются две строки: s = "anagram", t = "nagaram"
* Необходимо проверить являются ли строки анаграмами друг для друга
Пример:
Input: s = "rat", t = "car"
Output: false
"""

s = "anagram"
t = "nagaram"

def is_anagram(s, t):
    s = list(s)
    t = list(t)
    if (len(s) == len(t)) & (sorted(s) == sorted(t)):
        return True
    else:
        return False

print(is_anagram(s, t))