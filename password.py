"""Пароль считается надежным, если его длина составляет не менее 12 символов, при этом он должен содержать 
хотя бы одну заглавную букву, хотя бы одну строчную букву, хотя бы одну цифру и хотя бы один спецсимвол. 
Напишите код, который обрабатывает строковые данные и выводит сообщение о том, надежен ли пароль или нет. 
В случае, если пароль не надежен, код должен выдавать рекомендации для усиления надежности пароля.
Цифры, которые можно использовать для пароля: '1234567890'
Строчные буквы, которые можно использовать для пароля: 'abcdefghijklmnopqrstuvwxyz'
Заглавные буквы, которые можно использовать для пароля: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Спецсимволы, которые можно использовать для пароля: '!@#$%^&*()-+'"""
digits = '1234567890'
characters = 'abcdefghijklmnopqrstuvwxyz'
cap_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_chars = '!@#$%^&*()-+'
len_password = bool(0)
digits_cnt = bool(0)
characters_cnt = bool(0)
cap_characters_cnt = bool(0)
special_chars_cnt = bool(0)
list_for_print = []
password = input()

if len(password) >= 12:
    len_password = True
for i in password:
    if (i not in digits) and (i not in characters) and (i not in cap_characters) and (i not in special_chars):
        print('Ошибка. Заперещенный символ.')
        exit()
    if digits.count(i)>=1:
        digits_cnt = True
    if characters.count(i)>=1:
        characters_cnt = True
    if cap_characters.count(i)>=1:
        cap_characters_cnt = True
    if special_chars.count(i)>=1:
        special_chars_cnt = True
    
if len_password == True and digits_cnt == True and characters_cnt == True and cap_characters_cnt == True and special_chars_cnt == True:
    print('Сильный пароль')
else:
    if len(password) < 12:
        list_for_print.append(('увеличить количество символов - ' + str(12-len(password))))
    if digits_cnt == False:
        list_for_print.append('добавить 1 цифру')
    if special_chars_cnt == False:
        list_for_print.append('добавить 1 спецсимвол')
    if cap_characters_cnt == False:
        list_for_print.append('добавить 1 заглавную букву')
    print('Слабый пароль. Рекомендации:', end = " ")
    print(', '.join(list_for_print))
  