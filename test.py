import unittest
from random import randint
from FileNameComparator1 import compare

class CompareTestCase(unittest.TestCase):
    """Tests for `FileNameComparator.py`."""

    def test_works_on_equal(self):
        s1 = ""
        s2 = ""
        for i in xrange(randint(1,1000)):
        	char = chr(randint(32,126))
        	s1 += (char)
        	s2 += (char)
        def iscorrect(s1,s2):
        	if compare(s1,s2) == 0:
        		return True
        	else:
        		return False
        self.assertTrue(iscorrect(s1,s2))


    def test_works_on_num_change(self):
        s1 = ""
        s2 = ""
        for i in xrange(randint(5,1000)):
            if randint(1,5) == 1:
                x = randint(1,50)
                s1 += str(x)
                x = randint(50, 100)
                s2 += str(x)
            char = chr(randint(32,126))
            s1 += (char)
            s2 += (char)
        
        def iscorrect(s1,s2):
            if compare(s1,s2) == -1:
                return True
            else:
                return False
        self.assertTrue(iscorrect(s1,s2))

    def test_works_on_custom_cases(self):
        s1 = ["file2", "file1.txt", "v3a"]
        s2 = ["file10", "file2.txt", "v23"]
        ans = [-1,-1,-1]        
        def iscorrect(s1,s2):
            for i in xrange(len(s1)):
                if compare(s1[i],s2[i]) <> ans[i]:
                    return False
            return True
        self.assertTrue(iscorrect(s1,s2))

    def test_implicit_1(self):
        s1 = "playerAlgo"
        s2 = "player2Algo"
        def iscorrect(s1, s2):
            return compare(s1, s2) == -1
        self.assertTrue(iscorrect(s1,s2))


    def test_date(self):
        s1 = "DSC_09-23-1994.jpg"
        s2 = "DSC_01-01-2010.jpg"
        def iscorrect(s1, s2):
            return compare(s1, s2) == -1
        self.assertTrue(iscorrect(s1,s2))


    def test_replacement(self):
        s1 = "logolocation1.jpg"
        s2 = "logoloc1.jpg"
        def iscorrect(s1, s2):
            return compare(s1, s2) == 0
        self.assertTrue(iscorrect(s1,s2))




if __name__ == '__main__':
    unittest.main()