import unittest
import importlib
import sys
sys.path.append('.')
import function_2

# run as: python3 test_2.py -v
# or      python3 -m unittest -v

class TestProprietaryTerms(unittest.TestCase):

    def setUp(self):
        # These are command run before the test to create the proper environment
        # In this case, it is reading in the "base" or "known good" version of the
        # email that we will use for comparison
        # Note how I've created a file handle/object from the open() command and
        # then read() the file contents into a variable for comparison

        self.email2_base = open("email_two.base", "r")
        self.proprietary_terms_base = self.email2_base.read()
        #self.maxDiff = None

    def tearDown(self):
        # These commands are run after the test methods to clean up the environment.
        # In this case, I close the file. If you comment out the code below, you will
        # see that the unittest module flags a warning about the open file.

        self.email2_base.close()


    def test_proprietaryTerms(self):
        # Methods beginning with test_ are test methods. In this case, it calls the cato
        # function as you do in your code and then checks the ouput against the base version
        # loaded in the setup.

        self.assertEqual(function_2.cato(function_2.proprietary_terms, function_2.email_two), self.proprietary_terms_base)

if __name__ == '__main__':
    unittest.main()