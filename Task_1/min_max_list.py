import sys


def remove_duplicates(list):
    seen = set()
    result = []
    for x in list:
        if x not in seen:
            seen.add(x)
            result.append(x)
    print(result)
    return tuple(result)


def find_minimum(list):
    smallest = list[0]
    for x in list:
        if x < smallest:
            smallest = x
        else:
            smallest = smallest

    return smallest


def find_maximum(list):
    largest = list[0]
    for x in list:
        if x > largest:
            largest = x
    return largest
