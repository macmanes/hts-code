#!/usr/bin/env python

# based on this SeqAnswers thread
# http://seqanswers.com/forums/showthread.php?t=6140
# original written by Peter Cock
#
# modified by Bob Freeman
# bob_freeman@hms.harvard.edu
#
 
from Bio.SeqIO.QualityIO import FastqGeneralIterator #Biopython 1.51 or later

#######################################################
#
# Change the following settings to suit your needs
#

input_forward_filename = "all.p+s.unaligned_1.fastq"
input_reverse_filename = "all.p+s.unaligned_2.fastq"

#output_pairs_filename1 = "out_interleaved_pairs.fastq"
output_pairs_filename1 = "all.p+s.unaligned.pairs_1.fastq"
output_pairs_filename2 = "all.p+s.unaligned.pairs_2.fastq"
#output_orphan_filename = "out_unpaired_orphans.fastq"
output_orphan_filename1 = "all.p+s.unaligned.singles_1.fastq"
output_orphan_filename2 = "all.p+s.unaligned.singles_2.fastq"

f_suffix = ""
r_suffix = ""
#For older Illumina files use this instead:
#f_suffix = "/1"
#r_suffix = "/2"

#######################################################

if f_suffix:
    f_suffix_crop = -len(f_suffix)
    def f_name(title):
        """Remove the suffix from a forward read name."""
        name = title.split()[0]
        assert name.endswith(f_suffix), name
        return name[:f_suffix_crop]
else:
    def f_name(title):
        return title.split()[0]

if r_suffix:
    r_suffix_crop = -len(r_suffix)
    def r_name(title):
        """Remove the suffix from a reverse read name."""
        name = title.split()[0]
        assert name.endswith(r_suffix), name
        return name[:r_suffix_crop]
else:
    def r_name(title):
        return title.split()[0]

print "Scanning reverse file to build list of names..."    
reverse_ids = set()
paired_ids = set()
for title, seq, qual in FastqGeneralIterator(open(input_reverse_filename)):
    reverse_ids.add(r_name(title))

print "Processing forward file..."
#forward_handle = open(output_paired_forward_filename, "w")
#orphan_handle = open(output_orphan_filename, "w")
forward_handle = open(output_pairs_filename1, "w")
orphan_handle = open(output_orphan_filename1, "w")

for title, seq, qual in FastqGeneralIterator(open(input_forward_filename)):
    name = f_name(title)
    if name in reverse_ids:
        #Paired
        paired_ids.add(name)
        reverse_ids.remove(name) #frees a little memory
        forward_handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
    else:
        #Orphan
        orphan_handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
forward_handle.close()
orphan_handle.close()
del reverse_ids #frees memory, although we won't need more now

print "Processing reverse file..."
#reverse_handle = open(output_paired_reverse_filename, "w")
reverse_handle = open(output_pairs_filename2, "w")
orphan_handle = open(output_orphan_filename2, "w")
for title, seq, qual in FastqGeneralIterator(open(input_reverse_filename)):
    name = r_name(title)
    if name in paired_ids:
        #Paired
        reverse_handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
    else:
        #Orphan
        orphan_handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
orphan_handle.close()
reverse_handle.close()

