# -*- coding: UTF-8 -*-


def checkString(string):
    '''Check string of brackets for correctness'''

    # First symbol should be open bracket only
    if (string[0] == ')' or string[0] == '}' or string[0] == ']'):
        return False

    string_of_open_brackets = ''
    string_of_close_brackets = ''

    for index, symbol in enumerate(string):
        if (symbol == '('):
            string_of_open_brackets += symbol
        if (symbol == ')'):
            string_of_close_brackets += symbol
        if (symbol == '['):
            string_of_open_brackets += symbol
        if (symbol == ']'):
            string_of_close_brackets += symbol
        if (symbol == '{'):
            string_of_open_brackets += symbol
        if (symbol == '}'):
            string_of_close_brackets += symbol

    # Length of strings should be equals
    if (len(string_of_open_brackets) == len(string_of_close_brackets)):
        right_parentheses_pair = '()'
        right_braces_pair = '{}'
        right_square_brackets_pair = '[]'

        while (right_parentheses_pair in string):
            string = string.replace(right_parentheses_pair, '')

        while (right_braces_pair in string):
            string = string.replace(right_braces_pair, '')

        while (right_square_brackets_pair in string):
            string = string.replace(right_square_brackets_pair, '')

        while (right_parentheses_pair in string):
            string = string.replace(right_parentheses_pair, '')

        while (right_braces_pair in string):
            string = string.replace(right_braces_pair, '')

        while (right_square_brackets_pair in string):
            string = string.replace(right_square_brackets_pair, '')

        if (len(string) != 0):
            return False
        elif (len(string) == 0):
            return True
    else:
        return False


def main():
    user_string = ''
    allow_tuple = ('(', ')', '{', '}', '[', ']')

    running = True
    while (running):
        wrong_symbol_meeting = 0
        user_string = input('Please, write string:\n')

        for index, symbol in enumerate(user_string):
            if (symbol not in allow_tuple):
                wrong_symbol_meeting = 1
                break

        if (wrong_symbol_meeting == 1):
            print('Your string is not sequence of brackets. Enter again.')
            continue
        elif (wrong_symbol_meeting != 1):
            break

    answer = checkString(user_string)

    if (answer == True):
        print('Your string is right sequence of brackets. Program '
              'will exit.')
        return 0
    elif (answer == False):
        print('Your string is wrong sequence of brackets. Program '
              'will exit.')
        return 0
    else:
        print('Program was unable to check string.')

if __name__ == '__main__':
    main()
