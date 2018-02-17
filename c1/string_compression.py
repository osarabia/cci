import unittest

def string_compression(astring):
    count = 1
    prev = astring[0]
    letter = ""

    letters = []

    for i in xrange(1, len(astring)):
        letter = astring[i]
        if prev == letter:
            count += 1
            prev = letter
            letter = ""
        else:
            letters.append(prev)
            letters.append(str(count))
            prev = letter
            count = 1

        if i == len(astring) - 1:
            letters.append(prev)
            letters.append(str(count))

    if len(letters) < len(astring):
        return "".join(letters)

    return astring


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
