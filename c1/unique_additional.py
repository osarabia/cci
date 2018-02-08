import unittest


def is_unique(astring):
    already_seen = {}

    for c in astring:
        if c in already_seen:
            return False
        already_seen[c] = 1

    return True


class UniqueTestCases(unittest.TestCase):

    def test_unique(self):
        self.assertEqual(True, is_unique("omar"))

    def test_not_unique(self):
        self.assertEqual(False, is_unique("tree"))


if __name__ == "__main__":
    unittest.main()

