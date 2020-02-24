import unittest
from Libreria_ampliada import *

#complex numbers
a = [1,1]
b = [2,2]
c = [3,3]
d = [7,8]

class TestLibComplex(unittest.TestCase):
    
    def testSumaVector(self):        
        self.assertEqual(SumaVecto([a,b],[a,b]), [(2,2),(4,4)] )
        self.assertEqual(SumaVecto([a,c],[c,b]), [(4, 4),(5, 5)])
    def testRestaVector(self):
        self.assertEqual(RestaVecto([a,b],[a,b]), [(0,0),(0,0)] )
        self.assertEqual(RestaVecto([a,c],[c,b]), [(-2,-2),(1,1)])
    
    def testInverseVector(self):
        self.assertEqual(InversaVector([a,c]), [[-1, -1], [-3, -3]])
        self.assertEqual(InversaVector([b,a]), [[-2, -2],[-1, -1]])
        
    def testEscalVector(self):
        self.assertEqual(EscalarVector([a,b],b), [(0, 4), (0, 8)])
        self.assertEqual(EscalarVector([b,c],c), [(0, 12), (0, 18)])

    def testSumMat(self):
        self.assertEqual(SumaMatriz([[a,a],[b,b]],[[b,a],[a,b]]), [[(3, 3), (2, 2)], [(3, 3), (4, 4)]])
        self.assertEqual(SumaMatriz([[c,a],[a,b]],[[b,c],[b,b]]), [[(5, 5), (4, 4)], [(3, 3), (4, 4)]])
        
    def testInverseMatriz(self):
        self.assertEqual(InversaMatriz([[a],[b],[c]]), [[[-1, -1]], [[-2, -2]], [[-3, -3]]])
        self.assertEqual(InversaMatriz([[a,c],[c,a],[d,b]]), [[[-1, -1], [-3, -3]], [[-3, -3], [-1, -1]], [[-7, -8], [-2, -2]]])
        
    def testMultiEscalMat(self):
        self.assertEqual(MultipEscalarMatriz(d,[[c,a],[a,d]]), [[(-3, 45), (-1, 15)], [(-1, 15), (-15, 112)]])
        self.assertEqual(MultipEscalarMatriz(c,[[a,a],[b,b]]), [[(0, 6), (0, 6)], [(0, 12), (0, 12)]])
        
    def testTranspMatrix( self ):

        self.assertEqual(MatTranspuesta([[b,a,a],[a,b,a]]), [[[2, 2], [1, 1]], [[1, 1], [2, 2]], [[1, 1], [1, 1]]])
        self.assertEqual(MatTranspuesta([[a,b,c],[c,b,a]]), [[[1, 1], [3, 3]], [[2, 2], [2, 2]], [[3, 3], [1, 1]]])
        
    def testConjugatedMatrix( self ):
        self.assertEqual(MatrizConjugada([[b,a,c],[c,b,d]]), [[[2, -2], [1, -1], [3, -3]], [[3, -3], [2, -2], [7, -8]]])
        self.assertEqual(MatrizConjugada([[a,b,c],[c,b,a]]), [[[1, -1], [2, -2], [3, -3]], [[3, -3], [2, -2], [1, -1]]])
        
    def testAdjointMatrix( self ):
        
        self.assertEqual(MatrizAdjunta([[b,a,a],[a,b,a]]), [[[2, -2], [1, -1]], [[1, -1], [2, -2]], [[1, -1], [1, -1]]])
        self.assertEqual(MatrizAdjunta([[a,b,c],[c,b,a]]), [[[1, -1], [3, -3]], [[2, -2], [2, -2]], [[3, -3], [1, -1]]] )

    def testMultiplicaMat( self ):

        self.assertEqual(MatrizMultip([[a,a],[b,b]], [[b,a],[a,b]]), [[(0, 6), (0, 6)], [(0, 12), (0, 12)]] )
        self.assertEqual(MatrizMultip([[a,a,b],[b,b,a]],[[b,a],[a,b],[b,b]]), None)

    def testInternalProduct( self ):

        self.assertEqual(ProductoInterno([a,b,c],[a,b,c]),(0, 28))
        self.assertEqual(ProductoInterno([b, d, c], [d, b, a]), (-4, 66))
    
    def testNormVector( self ):

        self.assertEqual(VectorNormal([a, b, c ] ),0)
        self.assertEqual(VectorNormal([d, b, c]), 3.872983346207417)

    def testDistVector( self ) :
        self.assertEqual(DistanciaVector([a,b,c],[c,c,d] ), 3)
        self.assertEqual(DistanciaVector([d,d], [c,a]), 4.69041575982343)
        
    def testIsUnitary( self ):
        a, b, c = [1, 0], [0, 0],[0, 1]
        self.assertEqual(Unitaria([[c,b], [b,c]]), False)
        self.assertEqual(Unitaria([[a,b], [b,a]]), False )

        

    def testIsHermitan( self ):
        self.assertEqual(Hermitania([[a,a], [a,a] ] ), False)



if __name__ == '__main__':
    unittest.main()
