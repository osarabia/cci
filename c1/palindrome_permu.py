from collections import Counter
import string

letter = set(string.letters)

def odd_palin(counter):
    impar_seen = False

    for k in counter.keys():
        if counter[k] % 2 == 0:
            continue
        else:
            if impar_seen is False:
                impar_seen = True
            else:
                return False

    return impar_seen

def even_palin(counter):
    for k in counter.keys():
        if counter[k] % 2 > 0:
            return False

    return True

def is_palindrome_permu(s):
    total_letters = 0
    letters_counter = Counter()

    for i in s:
        if i in letter:
            letters_counter[i.lower()] += 1
            total_letters += 1

    if total_letters % 2 == 0:
        return even_palin(letters_counter)

    return odd_palin(letters_counter)


assert(is_palindrome_permu('Tact Coa')) == True
assert(is_palindrome_permu('jhsabckuj ahjsbckj')) == True
assert(is_palindrome_permu('Able was I ere I saw Elba')) == True
assert(is_palindrome_permu('So patient a nurse to nurse a patient so')) == False
assert(is_palindrome_permu('Random Words')) == False
assert(is_palindrome_permu('Not a Palindrome')) == False
assert(is_palindrome_permu('no x in nixon')) == True
assert(is_palindrome_permu('azAZ')) == True
