from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from zxcvbn import main

__all__ = ['password_strength']

password_strength = main.password_strength


if __name__ == '__main__':
    import fileinput
    # Ensure fields are displayed in a deterministic order
    display_fields = [
            'crack_time_display',
            'crack_time',
            'score',
            'entropy',
            'calc_time',
            ]

    for line in fileinput.input():
        pw = line.strip()
        print("Password: " + pw)
        out = password_strength(pw)
        for key in display_fields:
            print("\t%s: %s" % (key, out[key]))
