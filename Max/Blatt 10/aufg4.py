# current bpython session - make changes and save to reevaluate session.
# lines beginning with ### will be ignored.
# To return to bpython without reevaluating make no changes to this file
# or save an empty file.
# current bpython session - make changes and save to reevaluate session.
# lines beginning with ### will be ignored.
# To return to bpython without reevaluating make no changes to this file
# or save an empty file.
# current bpython session - make changes and save to reevaluate session.
# lines beginning with ### will be ignored.
# To return to bpython without reevaluating make no changes to this file
# or save an empty file.

from numpy import *

prior = array([0.8, 0.1, 0.1])


def roll(L):
    pn = L * prior
    N = sum(pn)
    return pn / N


b = array([2, .5, .05])
roll(b)
### array([ 0.96676737,  0.03021148,  0.00302115])
a = [0.13, 1.5, .5]
roll(a)
### array([ 0.34210526,  0.49342105,  0.16447368])
c = [.07, .5, 1.3]
roll(c)
### array([ 0.23728814,  0.21186441,  0.55084746])
###
