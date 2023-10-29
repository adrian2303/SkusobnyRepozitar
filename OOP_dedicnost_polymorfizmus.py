class Zviera:
    def __int__(self, hmotnost, vyska, vek):
        self.hmotnost = hmotnost
        self.vyska = vyska
        self.vek = vek


class Pes(Zviera):
    def __init__(self, meno):
        self.meno = meno

    def zobrazInfo(self):
        print("Pes {0} meria {1} cm, vazi {2} kg a ma {3} rokov".format(self.meno, self.vyska, self.hmotnost, self.vek))

    def lahni(self):
        print("Pes {0} si lahol".format(self.meno))

    def sadni(self):
        print("Pes {0} si sadol".format(self.meno))


class Ryba(Zviera):
    def __init__(self, druh):
        self.druh = druh

    def zobrazInfo(self):
        print("Ryba {0} ma {1} rokov a vazi {2} kg".format(self.druh, self.vek, self.hmotnost))

    def plavaj(self):
        print("Ryba {0} plava".format(self.druh))

    def vynorSa(self):
        print("Ryba {0} sa vynorila".format(self.druh))


class Vtak(Zviera):
    def __init__(self, druh):
        self.druh = druh

    def zobrazInfo(self):
        print("Vtak {0} ma {1} rokov a vazi {2} kg".format(self.druh, self.vek, self.hmotnost))

    def let(self):
        print("Vtak {0} leti".format(self.druh))


pes1 = Pes("Rex")
pes1.vyska = 90
pes1.hmotnost = 40
pes1.vek = 10
pes1.zobrazInfo()
pes1.lahni()
pes1.sadni()
print()

ryba1 = Ryba("pstruh")
ryba1.vek = 5
ryba1.hmotnost = 10
ryba1.zobrazInfo()
ryba1.plavaj()

ryba2 = Ryba("losos")
ryba2.vynorSa()
print()

vtak1 = Vtak("bocian")
vtak1.vek = 8
vtak1.hmotnost = 15
vtak1.zobrazInfo()
vtak1.let()

