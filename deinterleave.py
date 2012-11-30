#! /usr/bin/env python
import screed, sys, itertools

in_file = sys.argv[1]
out1_file = sys.argv[2]
out2_file = sys.argv[3]


for r1, r2 in itertools.izip(screed.open(in_file)):
    name1 = r1.name
    if name1.endswith('/1'):
	out1_file.write(print '@%s\n%s\n+\n%s' % (name1,
                                              r1.sequence,
                                              r1.accuracy)) 
	#print to out1_file
    name2 = r2.name
    if  name2.endswith('/2'):
        out2_file.write(print '@%s\n%s\n+\n%s' % (name2,
                                              r2.sequence,
                                              r2.accuracy)) 


