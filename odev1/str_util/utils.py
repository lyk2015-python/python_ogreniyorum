__author__ = 'lyk-py'


class UtilException(Exception):
    pass


def is_palindrome(string):
    return string == string[::-1]


def gen_word(letters, count):
    from random import choice
    r_list = []
    for i in range(count):
        r_list.append(choice(letters))
    return "".join(r_list)


def is_url(string):
    tests = {
        "test1": "http://www." in string,
        "test2": string[-1] == "/",
    }
    return all(tests.values())


def title_make(string):
    words = string.split()
    words = [word[0].capitalize() + word[1:] for word in words]
    return " ".join(words)


def zip_str(string1, string2):
    index = 0
    maxlen = max([len(string1), len(string2)])
    r_list = []
    while index <= maxlen - 1:
        try:
            r_list.append(string1[index])
            r_list.append(string2[index])
        except IndexError:
            raise UtilException("Abi uzunluklar eşit değil")

        index += 1

    return "".join(r_list)
