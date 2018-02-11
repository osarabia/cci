def urlify(s, s_length):
    s = list(s)
    index = len(s)

    for i in range(s_length-1, -1, -1):
        if s[i] == ' ':
            s[index-3:index] = '%20'
            index -= 3
        else:
            s[index-1] = s[i]
            index -= 1

    return "".join(s)

assert(urlify("Mr John Smith    ", 13)) == "Mr%20John%20Smith"
