import math


class Posisjon:
    def __init__(self, x_koordinat, y_koordinat, hoyde):
        self.x_koordinat = x_koordinat
        self.y_koordinat = y_koordinat
        self.hoyde = hoyde

    def hoydeforskjell(self, annen_posisjon):
        return abs(self.hoyde - annen_posisjon.hoyde)

    def avstand(self, annen_posisjon):
        return math.sqrt((self.x_koordinat - annen_posisjon.x_koordinat)**2 +
                         (self.y_koordinat - annen_posisjon.y_koordinat)**2 +
                         (self.hoyde - annen_posisjon.hoyde)**2)

    def __eq__(self, other):
        if self.x_koordinat != other.x_koordinat:
            return False
        if self.y_koordinat != other.y_koordinat:
            return False
        if self.hoyde != other.hoyde:
            return False
        return True


class Tur:
    def __init__(self, navn, starttidspunkt, sluttidspunkt):
        self.navn = navn
        self.starttidspunkt = starttidspunkt
        self.sluttidspunkt = sluttidspunkt
        self.posisjoner = list()

    # La til en property for sluttidspunktet, samt en sluttidspunkt.setter
    # Her sjekkes det at sluttidspunktet er etter starttidspunktet
    @property
    def sluttidspunkt(self):
        return self.__sluttidspunkt

    @sluttidspunkt.setter
    def sluttidspunkt(self, ny_slutt):
        if ny_slutt > self.starttidspunkt:
            self.__sluttidspunkt = ny_slutt
        else:
            raise ValueError('Du kan ikke avslutte turen før den har begynt, slask!')

    def add_posisjon(self, posisjon):
        self.posisjoner.append(posisjon)

    # Endret fra (self, x_koordinat, x_koordinat, hoyde)
    # til (self, x_koordinat, y_koordinat, hoyde)
    def add_posisjon_koordinater(self, x_koordinat, y_koordinat, hoyde):
        self.posisjoner.append(Posisjon(x_koordinat, y_koordinat, hoyde))

    # Endret range fra range(len(self.posisjoner)) til range(len(self.posisjoner)-1)
    # Endret fra resultat += self.posisjoner[i-1].hoydeforskjell(self.posisjoner[i])
    # Til resultat += self.posisjoner[i].hoydeforskjell(self.posisjoner[i+1])
    def hoydemeter(self):
        resultat = 0.0
        for i in range(len(self.posisjoner)-1):
            resultat += self.posisjoner[i].hoydeforskjell(self.posisjoner[i+1])
        return resultat

    def er_rundtur(self):
        if self.posisjoner[0] == self.posisjoner[-1]:
            return True
        return False
