from __future__ import print_function
from zxcvbn import main

__all__ = ['password_strength']

password_strength = main.password_strength


if __name__ == '__main__':
    import fileinput
    ignored = ('match_sequence', 'password')

    for line in fileinput.input():
        pw = line.strip()
        print("Password: " + pw)
        out = password_strength(pw)
        for key, value in out.items():
            if key not in ignored:
                print("\t%s: %s" % (key, value))
