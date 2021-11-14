# A class method is a method which is bound to the class and not the object of the class.
# It can modify a class state that would apply across all the instances of the class. For example,
# it can modify a class variable that would be applicable to all the instances.

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

if __name__ == '__main__':
    person1= Person('Anderson', 30)
    person2 = Person.fromBirthYear('Luciane', 1973)
    print(person1.age)
    print(person2.age)

    print(person1.name)
    print(person2.name)

    print(Person.isAdult(22))

#Observe que através do méthos fromBithYear eu consegui criar um objeto luciane,
#diferente do objeto 'Anderson', em que eu iniciei pela maneira tradicional( nome e idade)
#o método de classe modificou a criação através de outra inicializacao(nome e ano_de_nascimento)