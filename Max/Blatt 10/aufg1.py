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
# current bpython session - make changes and save to reevaluate session.
# lines beginning with ### will be ignored.
# To return to bpython without reevaluating make no changes to this file
# or save an empty file.
from numpy import *


def l(N_on, N_off, alpha):
    s = (N_on + N_off)
    return (s / (1 + 1 / alpha) / N_on)**N_on * (s / (1 + alpha) / N_off)**N_off


def sigma(N_on, N_off, alpha):
    D = sqrt(-2 * log(l(N_on, N_off, alpha)))
    return sqrt(-2 * log(sqrt(2 * pi) * D))

params1 = [120, 160, 0.6]
params2 = [150, 320, 0.3]


sigma(*params1)
# 1.7473629738215635
print(sigma(*params2))
# 2.1887855850666247
###
