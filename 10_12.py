"""
Створіть клас IDException, який успадковуватиме клас Exception.

Також реалізуйте функцію add_id(id_list, employee_id), яка додає до списку id_list 
ідентифікатор користувача employee_id та повертає вказаний оновлений список id_list.

Функція add_id буде викликати власне виключення IDException, якщо employee_id не починається з '01', 
інакше employee_id буде додано до списку id_list.
"""

class IDException(Exception):
    pass


def add_id(id_list, i):
    if str(i).find("01") >= 0:
        id_list.append(i)
    else:
        raise IDException
    return id_list
    
    
    