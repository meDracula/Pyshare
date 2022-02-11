import unittest

class UserSubmittedTest(unittest.TestCase):
    def solve_vs_test(self, code):
        test = self
        try:
            exec(code)
            return True
        except:
            return False

def test_code(test_code, solve_text):
    code = solve_text + "\n" + test_code
    test = UserSubmittedTest()
    return test.solve_vs_test(code)
