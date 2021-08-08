from random import *

# Create string constants
digits = '0123456789'
lowercase_letters = ''.join([chr(i) for i in range(97, 123)])
uppercase_letters = ''.join([chr(i) for i in range(65, 91)])
punctuation = '!#$%&*+-=?@^_'

# Create a variable that will include all symbols
# of generating pass
chars = ''

# User requests
# ------------------Rus lang version----------------------
sum_pass = int(input('Количество паролей которые вы хотите сгенерировать: '))
len_pass = int(input('Длина сгенерированного пароля: '))


# Нужно сделать проверку чтобы пользователь вводил только да или нет!!!!
include_numb = input('Включать ли цифры 0123456789:\nДа/Нет ')
include_upper_case = input('Включать ли прописные буквы:\nДа/Нет ')
include_lower_case = input('Включать ли строчные буквы:\nДа/Нет ')
include_symbols = input('Включать ли символы " !#$%&*+-=?@^_ ":\nДа/Нет ')

# Positive and negative answers
pos_ans = ['да', '+', 'yes', 'ok']
neg_ans = ['нет', '-', 'no']

if include_numb.lower() in pos_ans:
    chars += digits
if include_upper_case.lower() in pos_ans:
    chars += uppercase_letters
if include_lower_case.lower() in pos_ans:
    chars += lowercase_letters
if include_symbols.lower() in pos_ans:
    chars += punctuation

# Generating pass function
def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += choice(chars)
    return password
# Loop for generating more than 1 pass
for i in range(1, sum_pass + 1):
    print('%s. Ваш пароль:' % i)
    print(generate_password(len_pass, chars))
