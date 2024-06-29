import unittest

from math import pi
from common.r3 import R3
from tests.matchers import R3ApproxMatcher
from math import sqrt


class TestR3(unittest.TestCase):

    def setUp(self):
        self.a = R3(1.0, 2.0, 3.0)

    def test_add01(self):
        self.assertIsInstance(self.a + R3(0.0, 0.0, 0.0), R3)

    def test_add02(self):
        self.assertEqual(R3ApproxMatcher(self.a + R3(0.0, 0.0, 0.0)), self.a)

    def test_add03(self):
        self.assertEqual(R3ApproxMatcher(self.a + R3(0.0, 1.0, 2.0)),
                         R3(1.0, 3.0, 5.0))

    def test_add04(self):
        self.assertEqual(R3ApproxMatcher(self.a + R3(-1.0, -2.0, -3.0)),
                         R3(0.0, 0.0, 0.0))

    def test_sub01(self):
        self.assertIsInstance(self.a - R3(0.0, 0.0, 0.0), R3)

    def test_sub02(self):
        self.assertEqual(R3ApproxMatcher(self.a - R3(0.0, 0.0, 0.0)), self.a)

    def test_sub03(self):
        self.assertEqual(R3ApproxMatcher(self.a - R3(0.0, 1.0, 2.0)),
                         R3(1.0, 1.0, 1.0))

    def test_sub04(self):
        self.assertEqual(R3ApproxMatcher(self.a - self.a), R3(0.0, 0.0, 0.0))

    def test_mul01(self):
        self.assertIsInstance(self.a * 3, R3)

    def test_mul02(self):
        self.assertEqual(R3ApproxMatcher(self.a * 1), self.a)

    def test_mul03(self):
        self.assertEqual(R3ApproxMatcher(self.a * 3.0),
                         R3(3.0, 6.0, 9.0))

    def test_mul04(self):
        self.assertEqual(R3ApproxMatcher(self.a + self.a), self.a * 2)

    def test_rz01(self):
        self.assertIsInstance(self.a.rz(45.0), R3)

    def test_rz02(self):
        self.assertEqual(R3ApproxMatcher(self.a.rz(0.0)), self.a)

    def test_rz03(self):
        self.assertEqual(R3ApproxMatcher(self.a.rz(pi)),
                         R3(-self.a.x, -self.a.y, self.a.z))

    def test_rz04(self):
        self.assertEqual(R3ApproxMatcher(self.a.rz(2 * pi)), self.a)

    def test_ry01(self):
        self.assertIsInstance(self.a.ry(45.0), R3)

    def test_ry02(self):
        self.assertEqual(R3ApproxMatcher(self.a.ry(0.0)), self.a)

    def test_ry03(self):
        self.assertEqual(R3ApproxMatcher(self.a.ry(pi)),
                         R3(-self.a.x, self.a.y, -self.a.z))

    def test_ry04(self):
        self.assertEqual(R3ApproxMatcher(self.a.ry(2 * pi)), self.a)

    def test_dot01(self):
        self.assertIsInstance(self.a.dot(self.a), float)

    def test_dot02(self):
        self.assertEqual(self.a.dot(R3(0.0, 0.0, 0.0)), 0.0)

    def test_dot03(self):
        b = R3(3.0, 2.0, 1.0)
        self.assertAlmostEqual(self.a.dot(b), 10.0)

    def test_dot04(self):
        b = R3(-3.0, -2.0, -1.0)
        self.assertAlmostEqual(self.a.dot(b), b.dot(self.a))

    def test_dot05(self):
        b = R3(1.0, -2.0, 1.0)
        self.assertAlmostEqual(self.a.dot(b), 0.0)

    def test_cross01(self):
        self.assertIsInstance(self.a.cross(self.a), R3)

    def test_cross02(self):
        self.assertEqual(R3ApproxMatcher(self.a.cross(R3(0.0, 0.0, 0.0))),
                         R3(0.0, 0.0, 0.0))

    def test_cross03(self):
        self.assertEqual(R3ApproxMatcher(self.a.cross(self.a)),
                         R3(0.0, 0.0, 0.0))

    def test_cross04(self):
        self.assertEqual(R3ApproxMatcher(self.a.cross(R3(3.0, -2.0, 1.0))),
                         R3(8.0, 8.0, -8.0))

    def test_ocruz01(self):
        self.assertEqual(self.a.ocruz(), True)

    def test_ocruz02(self):
        self.assertEqual(R3(0.0, 0.0, 0.0).ocruz(), False)

    def test_ocruz03(self):
        self.assertEqual(R3(1.0, 0.0, 0.0).ocruz(), False)

    def test_sered01(self):
        self.assertIsInstance(self.a.sered(self.a), R3)

    def test_sered02(self):
        self.assertEqual(R3ApproxMatcher(self.a.sered(self.a)), self.a)

    def test_sered03(self):
        self.assertEqual(R3ApproxMatcher(self.a.sered(R3(0.0, 0.0, 0.0))),
                         R3(0.5, 1.0, 1.5))

    def test_sered04(self):
        self.assertEqual(R3ApproxMatcher(R3(2.0, 2.0, 2.0).
                                         sered(R3(0.0, 0.0, 0.0))),
                         R3(1.0, 1.0, 1.0))

    def test_dlina01(self):
        self.assertIsInstance(self.a.dlina(self.a), float)

    def test_dlina02(self):
        self.assertEqual(self.a.dlina(R3(0.0, 2.0, 3.0)),
                         1.0)

    def test_dlina03(self):
        self.assertEqual(self.a.dlina(R3(0.0, 0.0, 0.0)),
                         sqrt(14))