# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def add_numbers(*args):
    result = 0
    for number in args:
        result += number
    return result


if __name__ == '__main__':
    print(add_numbers(2, 5, 7, 8, 10, 200))
