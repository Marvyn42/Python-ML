from game import Stark


arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.__doc__)
print(arya.is_alive)
arya.die()
print(arya.is_alive)
plop = Stark()
print(plop.__dict__)
