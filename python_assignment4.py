#Assignment 4 - Python
#=====================

#!/usr/bin/env python3

import glob
import pandas as pd
import matplotlib.pyplot as plt
import sys

#1. Create a Seq object that accepts a DNA sequence (a string).
class Seq(object):

    def __init__(self,sequence):
        self.sequence = sequence

    def __len__(self):
        '''redefine length as length of sequence'''
        return len(self.sequence)

    def knum(self,k):
        return k

    def observedkmers(self,k):
        '''2. Add a method to count kmers of size k, where k is specified as a argument.'''
        counter = {}
        for i in range(len(self.sequence)-k+1):
            kmer = seq[i:i+k]
            if kmer not in counter:
                counter[kmer] = 0
            counter[kmer]+=1
        return len(counter)

    def possiblekmers(self,k):
        '''2. Add a method to count kmers of size k, where k is specified as a argument.'''
        #for k in range(1, len(self.sequence)+1):
        if k == 1:
            poss = 4**1
        else:
            if 4**k < (len(self.sequence)):
                poss = 4**k
            else:
                poss = (len(self.sequence)) - k + 1
        return poss

    #def ligcomplexity(self,k):
        #'''5. Add a method to calculate linguistic complexity.'''
        #self.sequence.observedkmers(k) = obs
        #self.sequence.possiblekmers(k) = poss
        #lc = obs/poss
        #return lc


#main function
if __name__ == "__main__":
    counter = {}
    k = int(sys.argv[1])
    if k > 0:   #more checking: because k = 0 is doing funny thing, so we make this rule
        for filename in glob.glob('*.fastq'):
            f = open('sampleseq.fasta', 'r')
            fastq = f.readlines()
            sequence = Seq(fasta[1].rstrip())
        print([sequence.observedkmers(3),sequence.observedkmers(4)])
        print(sequence.possiblekmers(3))
        print(sequence.observedkmers(4))
        print(sequence.possiblekmers(4))
        print(sequence.observedkmers(5))
        print(sequence.possiblekmers(5))

    else:
        print('k should be > 0')


#3. Add a method to create a pandas data frame containing all possible k and the associated
#number of observed and expected kmers (see above table).
#counter_df = pd.DataFrame(sequence.observedkmers(3), index=['kmer'])
#print(counter_df)
#4. Add a method to produce a graph from the data frame of the proportion of each kmer
#observed.
#counter_df.plot(kind='bar')


df_obs = pd.DataFrame
df_poss = pd.DataFrame


for i in range(1,(len(sequence)+1)):
    observed = sequence.observedkmers(i)
    df_obs = pd.DataFrame
    df_obs.append(observed(i))
    possible = sequence.possiblekmers(i)
    df_poss = pd.DataFrame
    df_poss.append(possible(i))
