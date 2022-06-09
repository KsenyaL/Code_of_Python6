class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return (f'Class: "{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."')
    def get_guest(self):       #16.9.4
        return (f'Class: {self.name} {self.surname}. {self.city}.')

client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Петр', 'Иванов', 'Екатеринбург', 150)
client_3 = Client('Екатерина', 'Сидорова', 'Тула', 70)

print(client_1)   #16.9.3

clients = [client_1, client_2, client_3]
for guest in clients:
    print(guest.get_guest())    #16.9.4



