'''
Завершуємо функціональність класу Contacts. 
На цьому етапі ми додамо до класу метод remove_contacts. 
Метод винен видаляти контакт по унікальному id у списку contacts. 
Якщо словника із зазначеним id у списку contacts не знайдено, метод жодних дій над списком contacts не робить.

Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.
'''

class Contacts:
    current_id = 0

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        type(self).current_id += 1
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )

    def get_contact_by_id(self, ids):
        for i in self.contacts:
             return i if i['id'] == ids else None

    def remove_contacts(self, id):
        for i in self.contacts:
            flag = True if i['id'] == id else False
            if flag:
                self.contacts.remove(i)
        