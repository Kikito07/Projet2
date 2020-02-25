import unittest
import sys
from Dico import *

class TestAbs(unittest.TestCase):

    def test0_get(self):
        keyInput = 1
        valueInput = "Hello"
        dico = Dico()
        dico.updateCorr(keyInput, valueInput)
        try:
            student_ans = dico.get(1)
        except:
            self.fail("fail")
        self.assertEqual(student_ans, dico.getCorr(1))
    
    def test1_pop(self):
        keyInput = 1
        valueInput = "Hello"
        dico = Dico()
        dico.updateCorr(keyInput, valueInput)
        try:
            student_ans = dico.get(1)
        except:
            self.fail("fail")
        self.assertEqual(student_ans, "hello")
        
    def test2_update(self):
        dico = Dico()
        try:
            dico.updateStudent(1,"hello")
        except:
            self.fail("fail")
        self.assertEqual("hello", dico.getCorr(1))


    
if __name__ == '__main__':
    unittest.main()