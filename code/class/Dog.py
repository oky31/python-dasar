class Dog:
    def __init__(self, nama):
        self.nama = nama
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


# instance object dog
dog = Dog('Aggi')
dog.add_trick('rolling')
dog.add_trick('jump')

dog2 = Dog('tama')

print(dog2.tricks)