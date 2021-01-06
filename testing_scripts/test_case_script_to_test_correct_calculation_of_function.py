# For refrence https://pymbook.readthedocs.io/en/latest/testing.html

# Test case script



import unittest
# unittest module is library in python to write unit test scripts

from factorial import fact

class TestFactorial(unittest.Testcase):
    """
    Our basic test class
    """

    def test_fact(self):
        """
        The actual test.
        Any method which starts with ''test_'' will considered as a test case


        """
        res = fact(5)
        self.assertEqual(res, 120)

        if __name__ == '__main__':
            unittest.main()


#Description We are importing unittest module first and then the required functions which we want to test.

#A testcase is created by subclassing unittest.TestCase.



# Running the test script 
#  $ python factorial_test.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK            

