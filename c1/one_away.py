import unittest

def one_away(s1, s2):
    if len(s1) == len(s2):
        replaced = False
        for i in xrange(0, len(s1)):
            if s1[i] != s2[i]:
                if replaced is False:
                    replaced = True
                else:
                    return False

        return True

    if len(s2) - 1 == len(s1):
        index = 0
        one_change = False
        for i in xrange(0, len(s2)):
            if index < len(s1):
                if s2[i] != s1[index]:
                    if one_change is False:
                        one_change = True
                    else:
                        return False
                else:
                    index += 1
            elif one_change and s1[index - 1] != s2[i]:
                    return False

        return True

    if len(s1) - 1 == len(s2):
        index = 0
        one_change = False
        for i in xrange(0, len(s1)):
            if index < len(s2):
                if s2[index] != s1[i]:
                    if one_change is False:
                        one_change = True
                    else:
                        return False
                else:
                    index += 1
            elif one_change:
                return False

        return True

    return False


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
