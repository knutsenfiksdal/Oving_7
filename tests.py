import unittest, math

from tur_fixed import Tur

tur1 = Tur("navn", 0, 10)

class TestTur(unittest.TestCase):
    def test_navn(self):
        with self.assertRaises(TypeError):
            tur1.navn = 1
        with self.assertRaises(TypeError):
            tur1.navn = list




if __name__ == "__main__":
    unittest.main()

"""
Skriv enhetstester for egenskapen slutt-tidspunkt og metodene som er oppgitt over. 
Lag turer med eksempelverdiene oppgitt over for å teste «hoydemeter» og «er_rundtur» metodene. 
Du kan gjerne lage flere turer også. 
Testen for slutt-tidspunkt skal sjekke at du får en exception hvis du prøver å lage en tur som slutter før den starter.
"""
