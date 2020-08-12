def foo(iterable):  # BAD UGLY SLOW
    return [item.upper() for item in iterable]


def bar(iterable):
    return [name.upper() for name in iterable]


def main():
    udacity_tas = ['Peter', 'Andy', 'Sarah', 'Gundega', 'Job', 'Sean']
    
    print(*foo(udacity_tas), sep = '\n', end = '\n\n')
    print(*bar(udacity_tas), sep = '\n', end = '\n\n')
