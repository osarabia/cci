import unittest

def is_unique(astring):
    for i1 in xrange(0, len(astring)):
        c = astring[i1]
        for i2 in xrange(i1+1, len(astring)):
            if c == astring[i2]:
                return False

    return True

class UniqueTestCases(unittest.TestCase):

    def test_unique(self):
        self.assertEqual(True, is_unique("omar"))

    def test_not_unique(self):
        self.assertEqual(False, is_unique("tree"))


if __name__ == "__main__":
    unittest.main()


