def is_a_letter(l):
    answer = False
    value = ord(l)
    if (64 < value < 91) or (96 < value < 123):
        answer = True
    return answer


def is_a_number(n):
    answer = False
    if 47 < ord(n) < 58:
        answer = True
    return answer


def is_a_typo(t):
    answer = False
    value = ord(t)
    typo = [32, 33, 34, 39, 40, 41, 43, 44,
            45, 46, 47, 58, 59, 63, 91, 92, 93, ]
    # if 31 < value < 48 or 57 < value < 65 or 90 < value < 97 or 122 < value
    # < 127:
    if value in typo:
        answer = True
    return answer


def is_string_letter(string):
    answer = False
    for i in string:
        if (is_a_letter(i)):
            answer = True
    return answer


def is_string_correct(string):
    answer = True
    for i in string:
        if not (is_a_typo(i) or is_a_letter(i) or is_a_number(i)):
            answer = False
    return answer


def is_string_only_letter(string):
    string = string[1:-1]  # remove quotes
    answer = True
    for i in string:
        if not (is_a_letter(i) or ord(i) == 32 or ord(i) == 39):
            answer = False
    return answer
