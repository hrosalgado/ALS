# Exercise 1
#help(int)
#help(float)
#help(str)
#help(bool)

# Exercise 2
class Loan:
    def __init__(self, num_fee, cost, interest):
        self.num_fee = num_fee
        self.cost = cost
        self.interest = interest

        self.amount = (cost + (cost * interest))
        self.fee = self.amount / num_fee

    @property
    def num_fee(self):
        return self.__num_fee

    @property
    def fee(self):
        return self.__fee

    @num_fee.setter
    def num_fee(self, value):
        self.__num_fee = value

    @fee.setter
    def fee(self, value):
        self.__fee = value

    def pay_fee(self):
        self.amount -= self.fee
        self.num_fee -= 1

    def recover(self, x):
        self.amount -= x
        self.fee = (self.amount + (self.amount * self.interest)) / self.num_fee

# Exercise 3
class Part:
    def __init__(self, serial_number, price):
        self.serial_number = serial_number
        self.price = price

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def price(self):
        return self.__price

    @serial_number.setter
    def serial_number(self, value):
        self.__serial_number = value

    @price.setter
    def price(self, value):
        self.__price = value

    def __str__(self):
        return str.format('Número de serie: {0}, Precio: {1}', self.serial_number, self.price)

class Pipe(Part):
    def __init__(self, serial_number, price, length):
        Part.__init__(self, serial_number, price)
        self.length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    def __str__(self):
        return str.format('Número de serie: {0}, Precio: {1}, Longitud: {2}', self.serial_number, self.price, self.length)

class Nut(Part):
    def __init__(self, serial_number, price, diameter):
        Part.__init__(self, serial_number, price)
        self.diameter = diameter

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, value):
        self.__diameter = value

    def __str__(self):
        return str.format('Número de serie: {0}, Precio: {1}, Diámetro: {2}', self.serial_number, self.price, self.diameter)

class Kink(Part):
    def __init__(self, serial_number, price, angle):
        Part.__init__(self, serial_number, price)
        self.angle = angle

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, value):
        self.__angle = value

    def __str__(self):
        return str.format('Número de serie: {0}, Precio: {1}, Ángulo: {2}', self.serial_number, self.price, self.angle)

class Stock(Part):
    def __init__(self):
        self.parts = []

    @property
    def parts(self):
        return self.__parts

    @parts.setter
    def parts(self, value):
        self.__parts = value

    def add(self, part):
        self.parts.append(part)

    def delete(self, part):
        self.parts.remove(part)

    def update(self, part, newPart):
        self.parts.remove(part)
        self.parts.append(newPart)

    def __str__(self):
        toRet = ''

        for part in self.parts:
            toRet += str(part)
            toRet += '\n'

        return toRet

# Exercise 4
class TV:
    def __init__(self, serial_number, pricePerHour):
        self.pricePerHour = pricePerHour

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def pricePerHour(self):
        return self.__pricePerHour

    @serial_number.setter
    def serial_number(self, value):
        self.__serial_number = value

    @pricePerHour.setter
    def pricePerHour(self, value):
        self.__pricePerHour = value

    def __str__(self):
        return str.format('TV - Serial number: {0}, Precio por hora: {1}', self.serial_number, self.pricePerHour)

class DVD:
    def __init__(self, serial_number, pricePerHour):
        self.serial_number = serial_number
        self.pricePerHour = pricePerHour

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def pricePerHour(self):
        return self.__pricePerHour

    @serial_number.setter
    def serial_number(self, value):
        self.__serial_number = value

    @pricePerHour.setter
    def pricePerHour(self, value):
        self.__pricePerHour = value

    def __str__(self):
        return str.format('DVD - Serial number: {0}, Precio por hora: {1}', self.serial_number, self.pricePerHour)

class Receipt:
    def __init__(self):
        self.lines = dict()

    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, value):
        self.__lines = value

    def add(self, line):
        self.lines[line.id] = line

    def __str__(self):
        toRet = '----Receipt----\nSerial number\tPrice per hour\tHour\tPrice\n'
        price = 0

        for v in self.lines.values():
            toRet += str(v)
            price += v.price

        toRet += '\nPrice: ' + str(price)

        return toRet

class Line:
    def __init__(self, id, device, hour):
        self.id = id
        self.device = device
        self.hour = hour
        self.price = device.pricePerHour * hour

    @property
    def id(self):
        return self.__id

    @property
    def device(self):
        return self.__device

    @property
    def hour(self):
        return self.__hour

    @property
    def price(self):
        return self.__price

    @id.setter
    def id(self, value):
        self.__id = value

    @device.setter
    def device(self, value):
        self.__device = value

    @hour.setter
    def hour(self, value):
        self.__hour = value

    @price.setter
    def price(self, value):
        self.__price = value

    def __str__(self):
        return str.format('{0}\t{1}\t{2}\t{3}', self.id, self.device.pricePerHour, self.hour, self.price)

# Exercise 5
class User:
    def __init__(self):
        self.name = input('Dame tu nombre:')
        self.mail = input('Dame tu correo electrónico:')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self, value):
        self.__mail = value

    def __str__(self):
        return str.format('Nombre: {0}\t Email: {1}',self.name, self.mail)


class Contacts:
    def __init__(self):
        self.contacts = dict()

    @property
    def contacts(self):
        return self.__contacts

    @contacts.setter
    def contacts(self, value):
        self.__contacts = value

    def add(self):
        contact = User()
        self.contacts[contact.name] = contact.mail

    def delete(self):
        #del self.contacts[user]
        self.contacts.pop(input('Nombre del contacto a eliminar'))

    def find(self):
        user = input('Nombre del contacto a buscar')
        return str(user + '\t' + self.contacts[user])

    def __str__(self):
        toret = '----Lista de contactos----\n'

        for k, v in self.contacts.items():
            toret += str(k) + '\t' + str(v) + '\n'

        return toret

# Main
# Exercise 2
loan = Loan(4, 100, 0.04)

print('Número de cuotas: ' + str(loan.num_fee))
print('Cuota: ' + str(loan.fee))

loan.pay_fee()

print('Número de cuotas: ' + str(loan.num_fee))
loan.pay_fee()

print('Número de cuotas: ' + str(loan.num_fee))

loan.recover(20)

print('Amortizando...')
print('Cuota: ' + str(loan.fee))

# Exercise 3
pipe = Pipe(1, 10, 4)
nut = Nut(2, 5, 5)
kink = Kink(3, 2, 60)

stock = Stock()
stock.add(pipe)
stock.add(nut)
stock.add(kink)

print(stock)

stock.delete(pipe)

print(stock)

print('Actualizando...')
updateNut = Nut(2, 6, 10)
stock.update(nut, updateNut)

print(stock)

# Exercise 4
tv = TV('TV1', 1)
dvd = DVD('DVD1', 2)
line1 = Line(1, tv, 4)
line2 = Line(2, dvd, 8)
receipt = Receipt()
receipt.add(line1)
receipt.add(line2)
print(receipt)

# Exercise 5
print('Menú')
print('1. Nuevo contacto')
print('2. Buscar contacto')
print('3. Lista contactos')
print('4. Borrar contacto')
print('0. Salir')

op = input('Selecciona una opción')
contacts = Contacts()
flag = False

while True:
    if op == '1':
        contacts.add()
    elif op == '2':
        contacts.find()
    elif op == '3':
        print(contacts)
    elif op == '4':
        contacts.delete()
    elif op == '0':
        print('Adiós')
        break
    else:
        print('Opción incorrecta')
    op = input('Selecciona una opción')