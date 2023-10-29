#!/usr/bin/env python3

class Greeter:
    def __init__(self, meno):
        self._meno = meno
        self._vek = 30

    def pozdrav(self):
        for i in range(0, 10):
            if i % 2 == 0:
                print("Ahoj {0}, mas {1} rokov. Vitaj na PSA v 2023 ".format(self._meno, self._vek+i))
                print("Ahoj", self._meno, "mas ", self._vek+i, "rokov. Vitaj znovu na PSA v 2023")



meno = input("Zadajte svoje meno: ")

greet = Greeter(meno)
greet.pozdrav()

