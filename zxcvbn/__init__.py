__all__ = ['password_strength']
import main

password_strength = main.password_strength

if __name__ == '__main__':
    import fileinput
    ignored = ['match_sequence', 'password']
    for line in fileinput.input():
        pw = line.strip()
        print "Password: " + pw
        out = password_strength(pw)
        for k,v in out.iteritems():
            if k not in ignored: print "\t%s: %s" % (k,v)

