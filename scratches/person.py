class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    @property
    def fullname(self):
        return f'{self.name} {self.lastname}'

    def fullname2(self):
        return f'{self.name} {self.lastname}'
    
    @fullname.setter
    def fullname(self, first_last):
        self.name, self.lastname = first_last.split()

    @fullname.deleter
    def fullname(self):
        self.lastname = None
        print('Dane usunięte!')

    def __str__(self):
        return f'{self.name, self.lastname}'
    
        
Anna = Person('Anna', 'Kowalska', 30)

print(Anna.fullname)
print(Anna.fullname2())

Anna.fullname = 'Anna Nowak'

print(Anna.name, Anna.lastname)

del Anna.fullname

print(Anna.name, Anna.lastname)
