"""
? Вам дана строка "s" четной длинны. Разделив строку на две равные части образовываются две подстроки "a" и "b".
! На вход подаётся строка вида: s = "book"
* Необходимо проверить количество гласных в обеих подстроках и в случае равного количества вернуть "True".
('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
Пример:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
"""

s = "BooK"

def is_alike_strings(s):
    a_count = b_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    a_str = s[:len(s)//2]
    b_str = s[len(s)//2:]

    for a_char, b_char in zip(a_str, b_str):
        if a_char in vowels:
            a_count += 1
        if b_char in vowels:
            b_count += 1

    if a_count == b_count:
        return True
    else:
        return False    

print(is_alike_strings(s))