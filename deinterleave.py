#! /usr/bin/env python

##
#Adapted from C. Titus Brown's interleave script in the khmer package.  
#Contact Matthew MacManes macmanes@gmail.com for support
##

##Usage: python deinterleave.py interleaved.fq left.fq right.fq

import screed, sys

in_file = sys.argv[1]
out1_file = sys.argv[2]
out2_file = sys.argv[3]


for r1 in screed.open(in_file):
    if r1.name.endswith('/1'):
	fh = open(out1_file, "a")
	fh.write("@%s\n%s\n+\n%s\n" % (r1.name,
                                            r1.sequence,
                                            r1.accuracy))
    if  r1.name.endswith('/2'):
	fh2 = open(out2_file, "a")
        fh2.write('@%s\n%s\n+\n%s\n' % (r1.name,
                                            r1.sequence,
                                            r1.accuracy)) 

