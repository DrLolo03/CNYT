#Lorenzo marquez , 16/01/2020
from Complejos import *
import unittest
class TestStringMethods(unittest.TestCase):
    def test_suma(self):
        a = (3,-1)
        b = (1,4)
        self.assertEqual( suma(a,b),(4,3))
        a = (1,-1)
        b = (1,2)
        self.assertEqual( suma(a,b),(2,1))
        a = (4,5)
        b = (3,0)
        self.assertEqual( suma(a,b),(7,5))
    def test_resta(self):
        a = (3,-1)
        b = (1,4)
        self.assertEqual( resta(a,b),(2,-5))
        a = (-5,1)
        b = (-3,-4)
        self.assertEqual( resta(a,b),(-2,5))
        a = (1,-1)
        b = (1,-1)
        self.assertEqual( resta(a,b),(0,0))
    def test_multi(self):
        a = (3,-1)
        b = (1,4)
        self.assertEqual( multip(a,b),(7,11))
        a = (1,2)
        b = (3,-2)
        self.assertEqual( multip(a,b),(7,4))
    def test_moodle(self):
        a = (1,1)
        self.assertEqual( moodule(a),2**0.5)
        a = (1,-1)
        self.assertEqual( moodule(a),2**0.5)
        a = (-1,1)
        self.assertEqual( moodule(a),2**0.5)
    def test_div(self):
        a = (-2,1)
        b = (1,2)
        self.assertEqual( div(a,b),(0,1))
    def test_polar(self):
        a= (1,1)
        self.assertEqual(cartpol(a), (2**0.5, 0.7853981633974483))
        a= (1,3)
        self.assertEqual(cartpol(a), (3.1622776601683795, 1.2490457723982544))
    def test_face(self):
        a= (1,1)
        self.assertEqual(fase(a), (0.7853981633974483))

if __name__ == '__main__':
    unittest.main()
