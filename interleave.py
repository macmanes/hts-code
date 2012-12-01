#! /usr/bin/env python
##
#Mod from C. Titus Brown's interleave script in the khmer package. 
#Contact Matthew MacManes macmanes@gmail.com for support
##

import screed, sys, itertools

s1_file = sys.argv[1]
s2_file = sys.argv[2]

for r1, r2 in itertools.izip(screed.open(s1_file), screed.open(s2_file)):
    if not r1.name.endswith('/1'):
        r1.name += '/1'
    if not r2.name.endswith('/2'):
        r2.name += '/2'

    print '@%s\n%s\n+\n%s\n@%s\n%s\n+\n%s' % (r1.name,
                                              r1.sequence,
                                              r1.accuracy,
                                              r2.name,
                                              r2.sequence,
                                              r2.accuracy)
