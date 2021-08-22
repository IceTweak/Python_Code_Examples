# Условие задачи:
'''
Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания
пространств имен и добавление в них переменных.
В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
Вашей программе на вход подаются следующие запросы:
    - create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
    - add <namespace> <var> – добавить в пространство <namespace> переменную <var>
    - get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
      пространства <namespace>, или None, если такого пространства не существует
'''

scopes = {'global': {'parent': None, 'variables': set()}}  # Создаем словарь с namespace'ами
def create(namesp, parent):
    scopes[namesp] = {'parent': parent, 'variables': set()}
def add(namesp, var):
    scopes[namesp]['variables'].add(var)
def get(namesp, var):
    if var in scopes[namesp]['variables']:
        return namesp
    try:  # На тот случай если перенной не обнаружилось ни в одном namespace
        return get(scopes[namesp]['parent'], var)
    except KeyError:
        return None
for _ in range(int(input())):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        create(namesp, arg)
    elif cmd == 'add':
        add(namesp, arg)
    else:
        print(get(namesp, arg))