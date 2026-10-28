import statistics

class Kebabownia:
    ID = 1
    lista_obiektow=[]
    def __init__(self, miasto):
        self.miasto = miasto
        self.ocena = []
        self.nr = Kebabownia.ID
        Kebabownia.ID += 1
        Kebabownia.lista_obiektow.append(self)

    @property
    def miasto(self):
        return self._miasto

    @miasto.setter
    def miasto(self, tekst):
        if isinstance(tekst, str):
            self._miasto = tekst.title()
        else:
            raise TypeError("Wprowadzony tekst musi być typu string")

    def __str__(self):
        return f'{self.nr}. {self.miasto} | średnia: {self.oblicz_srednia()}'


    def oblicz_srednia(self):
        if len(self.ocena) != 0:
            return round(statistics.mean(self.ocena), 2)
        else:
            return 'brak ocen'


    def przyznaj_ocene(self, liczba):
        if isinstance(liczba, int):
            if 0 <= liczba <= 10:
                self.ocena.append(liczba)
            else:
                raise ValueError("Ocena musi być w zakresie 0–10")
        else:
            raise TypeError("Ocena powinna być liczbą całkowitą")



k1 = Kebabownia('Bydgoszcz')
k1.przyznaj_ocene(4)
k1.przyznaj_ocene(7)
print(k1)
k2 = Kebabownia('Torun')
k3 = Kebabownia('Warszawa')
k4 = Kebabownia('Zielona gora')
k2.przyznaj_ocene(3)
k2.przyznaj_ocene(3)
k2.przyznaj_ocene(4)
k4.przyznaj_ocene(10)
for element in Kebabownia.lista_obiektow:
    print(element)