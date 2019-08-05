class Person():
    name: str = ''
    age: int = 0

    def __init__(self: 'Person', name: str, age: int):
        self.name = name
        self.age = age

    def greet(self: 'Person', person: 'Person' = None) -> None:
        if (person):
            print('Hi %s, my name is %s, i am %i' % (person.name, self.name, self.age))
        else:
            print('Hi, my name is %s, i am %i' % (self.name, self.age))


def word_length(param: str) -> int:
    return len(param)


def create_person(name: str, age: int) -> Person:
    return Person(name, age)


if __name__ == "__main__":
    print(word_length('Holaaaa'))
    fran: Person = Person(name='Francisco', age=27)
    fran.greet()
    fran.greet(Person('Alejandra', 26))
