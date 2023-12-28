'''Создайте классы, реализуйте иерархию классов, определите для каждого класса конструктор и метод __str__ для вывода
полной информации об экземпляре класса, согласно своего варианта. Постройте диаграмму классов.Создать иерархию, описывающую
транспорт, корабль, пассажирский транспорт и пассажирский корабль.'''
class Transport:#новый класс Transport
    def __init__(self, name, speed):#конструктор с параметрами name speed
        self.name = name
        self.speed = speed#инициализация параемтров
    def __str__(self):#функция str
        return f"{self.name} {self.speed} км/ч"#возвращает сообщение
class Ship(Transport):#новый класс Ship наследующий от Transport
    def __init__(self, name, speed, displacement):#конструктор с параметрами name speed displacement
        super().__init__(name, speed)#наследующие параметры
        self.displacement = displacement#инизиализация параметра
    def __str__(self):#функция str
        return f"{super().__str__()}, {self.displacement} тонн"#возвращает сообщение
class PassengerShip(Ship):#ковый класс PassengerShip
    def __init__(self, name, speed, displacement, passengers):#конструктор с параметрами name speed displacement passengers
        super().__init__(name, speed, displacement)#наследующие параметры
        self.passengers = passengers#инициализация параметра
    def __str__(self):#функция str
        return f"{super().__str__()}, {self.passengers} пассажиров"#возвращает сообщение
transport = Transport("Транспорт", 80)                                                              #П
print(transport)                                                                                                 #Р
ship = Ship("Корабль", 150, 1043)                                                         #И
print(ship)                                                                                                      #М
passenger_ship = PassengerShip("Пассажирский корабль", 100, 2058, 605)         #Е
print(passenger_ship)#примеры                                                                                    #Р