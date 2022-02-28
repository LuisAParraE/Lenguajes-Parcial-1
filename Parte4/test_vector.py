import unittest
from vector import vector

#ESTAS SON LAS PRUEBAS UNITARIAS, ADEMAS DE ALGUNOS CASOS GENERALES CON MULTIPLES OPERANDOS
class TestVector(unittest.TestCase):
    
    #PRUEBAS DE LA SUMA
    def test_add(self):
        vectorA = vector(2.4,5.7, 0.1)
        vectorB = vector(1,2.4, 0.76)
        result = vector(2.4 + 1,5.7 + 2.4, 0.1 + 0.76)

        self.assertEqual(vectorA + vectorB, result)
        
        vectorA = vector(40,5.7, 16)
        vectorB = vector(-12,-9, -0.84)
        result = vector(40 + -12,5.7 -9 , 16 + -0.84)
        
        self.assertEqual(vectorA + vectorB, result)

        vectorA = vector(40,5.7, 16)
        result = vector(40 + 5,5.7 + 5 , 16 + 5)
        
        self.assertEqual(vectorA + 5, result)

        vectorA = vector(29,5.7, 16)
        result = vector(29 + -29,5.7 + -29 , 16 + -29)
        
        self.assertEqual(vectorA + -29, result)
    
    #PRUEBAS DE LA RESTA
    def test_sub(self):
        vectorA = vector(2.4,5.7, 0.1)
        vectorB = vector(1,2.4, 0.76)
        result = vector(2.4 - 1,5.7 - 2.4, 0.1 - 0.76)

        self.assertEqual(vectorA - vectorB, result)
        
        vectorA = vector(40,5.7, 16)
        vectorB = vector(-12,-9, -0.84)
        result = vector(40 - -12,5.7 - -9 , 16 - -0.84)
        
        self.assertEqual(vectorA - vectorB, result)

        vectorA = vector(40,5.7, 16)
        result = vector(40 - 5,5.7 - 5 , 16 - 5)
        
        self.assertEqual(vectorA - 5, result)

        vectorA = vector(29,5.7, 16)
        result = vector(29 - -29,5.7 - -29 , 16 - -29)
        
        self.assertEqual(vectorA - -29, result)
    
    #PRUEBAS DE LA MULTIPLICACION
    def test_mult(self):
        vectorA = vector(2.4,5.7, 0.1)
        vectorB = vector(1,2.4, 0.76)
        result = vector(5.7 * 0.76 - (0.1 * 2.4) ,
                        -( 2.4 * 0.76 - (0.1 * 1) ), 
                        2.4 * 2.4 - (5.7 * 1))
        
        self.assertEqual(vectorA * vectorB, result)
        
        vectorA = vector(40, 5.7, 16)
        vectorB = vector(-12, -9, -0.84)
        result = vector(5.7 * -0.84 - (16 * -9) ,
                        -( 40 * -0.84 - (16 * -12) ), 
                        40 * -9 - (5.7 * -12))

        self.assertEqual(vectorA * vectorB, result)

        vectorA = vector(40,5.7, 16)
        result = vector(40 * 0,5.7 * 0 , 16 * 0)
        
        self.assertEqual(vectorA * 0, result)

        vectorA = vector(29,5.7, -16)
        result = vector(29 * -29,5.7 * -29 , -16 * -29)
        
        self.assertEqual(vectorA * -29, result)

    #PRUEBAS DEL MOD
    def test_mod(self):
        vectorA = vector(2.4,5.7, 0.1)
        vectorB = vector(1,2.4, 0.76)
        result = 2.4 * 1 + 5.7 * 2.4 +  0.1 * 0.76

        self.assertEqual(vectorA % vectorB, result)
        
        vectorA = vector(40,5.7, 16)
        vectorB = vector(-12,-9, -0.84)
        result = 40 * -12 + 5.7 * -9  + 16 * -0.84
        
        self.assertEqual(vectorA % vectorB, result)

        vectorA = vector(15,0, 43.12)
        vectorB = vector(-12.23,73, -1.84)
        result = 15 * -12.23 + 0 * 73  + 43.12 * -1.84
        
        self.assertEqual(vectorA % vectorB, result)

        vectorA = vector(40,5.7, 16)
        result = vector(40 % 1,5.7 % 1 , 16 % 1)
        
        self.assertEqual(vectorA % 1, result)

        vectorA = vector(29,5.7, -16)
        result = vector(29 % 29,5.7 % 29 , -16 % 29)
        
        self.assertEqual(vectorA % 29, result)

        vectorA = vector(40,5.7, 16)
        result = vector(40 % 7,5.7 % 7 , 16 % 7)
        
        self.assertEqual(vectorA % 7, result)
        
        self.assertRaises(ValueError, vector.__mod__,vectorA ,0)
    
    #PRUEBAS CON MUTIPLES OPERANDOS
    def test_alltogether(self):
        
        vectorA = vector(2.4,5.7, 0.1)
        vectorB = vector(1,2.4, 0.76)
        vectorC = vector(0, 7 , 2)
        result =(2.4 + 1)*(7 * 0.76 - (2 * 2.4)) + (5.7 + 2.4)*(-( 0 * 0.76 - (2 * 1) )) + (0.1 + 0.76)*(0 * 2.4 - (7 * 1))

        self.assertEqual((vectorA + vectorB) % (vectorC * vectorB), result)
        
        
        result = vector(2.4 + ((1 -5)*0 +(2.4 - 5) * 7 + (0.76 -5) * 2),
                        5.7 + ((1 -5)*0 +(2.4 - 5) * 7 + (0.76 -5) * 2),
                        0.1 + ((1 -5)*0 +(2.4 - 5) * 7 + (0.76 -5) * 2))
        
        self.assertEqual(vectorA + (vectorB - 5) % vectorC, result)

        vectorA = vector(65, 5.7, -25)
        vectorB = vector(12,9.5, 15.76)
        vectorC = vector(21, 0 , 11)
        result = vector((12 + 12) * ( 21 * 65 + 0 * 5.7 + 11 * -25),
                        (9.5 + 9.5) * (21 * 65 + 0 * 5.7 + 11 * -25),
                        (15.76 + 15.76) * (21 * 65 + 0 * 5.7 + 11 * -25))
        
        self.assertEqual((vectorB + vectorB) * (vectorC % vectorA), result)


if __name__ == '__main__':
    unittest.main()
