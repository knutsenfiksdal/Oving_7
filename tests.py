import unittest
from tur import Tur, Posisjon


class TestTur(unittest.TestCase):
    def test_slutt_tidspunkt(self):
        tur1 = Tur('tur', 0, 15)
        tur2 = Tur('tur', 4, 6)
        self.assertGreater(tur1.sluttidspunkt, tur1.starttidspunkt)
        self.assertEqual(15, tur1.sluttidspunkt)
        self.assertEqual(6, tur2.sluttidspunkt)
        with self.assertRaises(ValueError):
            tur2.sluttidspunkt = 3

    def test_add_posisjon(self):
        tur1 = Tur('Tur1', 0, 15)
        punkt1 = Posisjon(2, 3, 2)
        punkt2 = Posisjon(4, 4, 7)
        tur1.add_posisjon(punkt1)
        self.assertEqual(1, len(tur1.posisjoner))
        self.assertEqual(2, tur1.posisjoner[0].x_koordinat)
        self.assertEqual(3, tur1.posisjoner[0].y_koordinat)
        self.assertEqual(2, tur1.posisjoner[0].hoyde)
        tur1.add_posisjon(punkt2)
        self.assertEqual(2, len(tur1.posisjoner))
        self.assertEqual(4, tur1.posisjoner[1].x_koordinat)
        self.assertEqual(4, tur1.posisjoner[1].y_koordinat)
        self.assertEqual(7, tur1.posisjoner[1].hoyde)

    def test_add_posisjon_koordinater(self):
        tur1 = Tur('Tur1', 0, 15)
        tur1.add_posisjon_koordinater(2, 3, 2)
        self.assertEqual(1, len(tur1.posisjoner))
        self.assertEqual(2, tur1.posisjoner[0].x_koordinat)
        self.assertEqual(3, tur1.posisjoner[0].y_koordinat)
        self.assertEqual(2, tur1.posisjoner[0].hoyde)
        tur1.add_posisjon_koordinater(4, 4, 7)
        self.assertEqual(2, len(tur1.posisjoner))
        self.assertEqual(4, tur1.posisjoner[1].x_koordinat)
        self.assertEqual(4, tur1.posisjoner[1].y_koordinat)
        self.assertEqual(7, tur1.posisjoner[1].hoyde)

    def test_hoydemeter(self):
        tur1 = Tur('Tur', 0, 15)
        tur2 = Tur('Tur', 4, 6)
        punkt1 = Posisjon(2, 3, 2)
        punkt2 = Posisjon(20, 5, 20)
        punkt3 = Posisjon(18, 13, 22)
        punkt4 = Posisjon(2, 3, 2)
        punkt5 = Posisjon(5, 3, 10)
        punkt6 = Posisjon(15, 5, 18)
        punkt7 = Posisjon(12, 15, 12)
        tur1.add_posisjon(punkt1)
        tur1.add_posisjon(punkt2)
        tur1.add_posisjon(punkt3)
        tur1.add_posisjon(punkt4)
        self.assertEqual(40, tur1.hoydemeter())
        tur2.add_posisjon(punkt5)
        tur2.add_posisjon(punkt6)
        tur2.add_posisjon(punkt7)
        self.assertEqual(14, tur2.hoydemeter())

    def test_er_rundtur(self):
        tur1 = Tur('Tur', 0, 15)
        tur2 = Tur('Tur', 4, 6)
        punkt1 = Posisjon(2, 3, 2)
        punkt2 = Posisjon(20, 5, 20)
        punkt3 = Posisjon(18, 13, 22)
        punkt4 = Posisjon(2, 3, 2)
        punkt5 = Posisjon(5, 3, 10)
        punkt6 = Posisjon(15, 5, 18)
        punkt7 = Posisjon(12, 15, 12)
        tur1.add_posisjon(punkt1)
        tur1.add_posisjon(punkt2)
        tur1.add_posisjon(punkt3)
        tur1.add_posisjon(punkt4)
        tur2.add_posisjon(punkt5)
        tur2.add_posisjon(punkt6)
        tur2.add_posisjon(punkt7)
        self.assertTrue(tur1.er_rundtur())
        self.assertFalse(tur2.er_rundtur())


if __name__ == '__main__':
    unittest.main()
