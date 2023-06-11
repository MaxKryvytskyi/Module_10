'''
У четвертому модулі ми реалізували функцію lookup_key для пошуку всіх ключів за значенням у словнику. 
Першим параметром у функцію ми передавали словник, а другим – значення, яке хотіли знайти. 
Результатом був список ключів або порожній список, якщо ми нічого не знаходили.

def lookup_key(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)
    return keys
Створіть клас LookUpKeyDict, батьком якого буде клас UserDict. 
Зробіть функцію lookup_key методом класу LookUpKeyDict.
'''

from collections import UserDict

class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        # l = []
        # for k, v in self.data.items():
        #     if v == value:
        #         l.append(k)
        # return l

        return [self.data[k] for k in self.data if value == self.data[k]]
                
        