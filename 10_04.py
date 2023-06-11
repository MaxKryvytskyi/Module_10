'''
Додамо в клас Animal змінну класу color, значення якої спочатку дорівнює 'white', 
і метод change_color, який повинен змінювати значення змінної класу color.

Створіть екземпляри об'єкта: first_animal та second_animal

Викличте функцію change_color("red") для будь-якого екземпляра об'єкту Animal 
та змініть значення змінної класу color на "red".
'''

class Animal:
    color = 'white'
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return f"Hi {self.nickname}"

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, colors):
        type(self).color = colors

first_animal = Animal('bill', 12)
second_animal = Animal('Ted', 14)
second_animal.change_color('red')
