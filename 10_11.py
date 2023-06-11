'''
Створіть клас NumberString, успадкуйте його від класу UserString, 
визначте для нього метод number_count(self), 
який буде рахувати кількість цифр у рядку.
'''

from collections import UserString

string = "The resulting profit was: from the southern possessions $123, from the northern colonies $45, and the king gave $67890."

class NumberString(UserString):
    def number_count(self):
        # num = [i for i in self.data if i.isdigit()]
        return len([i for i in self.data if i.isdigit()])
    
num = NumberString(string)
print(num.number_count())