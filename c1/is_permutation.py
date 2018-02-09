from collections import Counter


def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    counter_s1 = Counter()
    counter_s2 = Counter()

    for c1 in s1:
        counter_s1[c1] += 1

    for c2 in s2:
        counter_s2[c2] += 1

    for c in s1:
        if counter_s1.get(c, 0) != counter_s2.get(c, 0):
            return False

    return True


assert(is_permutation("ramo","roma")) == True
assert(is_permutation("ssfare", "test")) == False
assert(is_permutation("monta", "valee")) == False
