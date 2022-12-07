#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 23:29:54 2022

@author: lucasonelife
"""

from textwrap import wrap


ARN = ""
PROT = ""
counter = 0
dict_traduire = {
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AGA': 'Arg', 'AGG': 'Arg', 'AAU': 'Asn', 'AAC': 'Asn',
    'GAU': 'Asp', 'GAC': 'Asp', 'UGU': 'Cys', 'UGC': 'Cys',
    'CAA': 'Gln', 'CAG': 'Gln', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
    'CAU': 'His', 'CAC': 'His', 'AUU': 'Ile', 'AUC': 'Ile',
    'AUA': 'Ile', 'UUA': 'Leu', 'UUG': 'Leu', 'CUU': 'Leu',
    'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu', 'AAA': 'Lys',
    'AAG': 'Lys', 'AUG': 'Met', 'UUU': 'Phe', 'UUC': 'Phe',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'AGU': 'Ser', 'AGC': 'Ser', 'ACU': 'Thr', 'ACC': 'Thr',
    'ACA': 'Thr', 'ACG': 'Thr', 'UGG': 'Trp', 'UAU': 'Tyr',
    'UAC': 'Tyr', 'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val',
    'GUG': 'Val', 'UAG': 'Stop', 'UGA': 'Stop', 'UAA': 'Stop',
}

nucleotide = 0
with open("BRCA1.fasta", "r") as ADNSequence:
    for line in ADNSequence:
        counter += 1
        if line[0] != ">":
            for char in line:
                if (char != "N") & (char != "\n"):
                    nucleotide += 1
                    if char == "A":
                        ARN += "U"
                    elif char == "T":
                        ARN += "A"
                    elif char == "G":
                        ARN += "C"
                    else:
                        ARN += "G"
    with open('ARN_sequence.txt', 'w') as ARN_sequence:
        ARN_sequence.write(ARN)
        ARN_sequence.close()
        
with open('ARN_sequence.txt', 'r') as ARN_sequence:
    for i in ARN_sequence:
        start_index = i.find("AUG") +2
    print(start_index)
    ARN_sequence.close()

if len(ARN) > start_index:
    ARN = ARN[start_index + 1::]
    with open('ARN_sequence.txt', 'w') as ARN_sequence:
        ARN_sequence.write(ARN)
        ARN_sequence.close()
    with open('ARN_sequence.txt', 'r') as ARN_sequence:
        for i in ARN_sequence:
            stop_index_1 = i.find("UAG") 
            stop_index_2 = i.find("UGA") 
            stop_index_3 = i.find("UAA")
            stop_liste = [stop_index_1, stop_index_2, stop_index_3]
            stop_index = min(stop_liste)
        print(stop_liste)
        print(stop_index)
        ARN_sequence.close()
   
with open('ARN_sequence.txt', 'r+') as ARN_sequence:
    ARN_sequence_read = ARN_sequence.read()
    print(ARN_sequence_read)
    ARN_sequence_coding = ARN_sequence_read[0:stop_index]
    print(ARN_sequence_coding)
    ARN_sequence.close()
    


ARN_triplet_liste = wrap(ARN_sequence_coding, 3)
ARN_triplet=', '.join(ARN_triplet_liste)
print(ARN_triplet)

for i in ARN_triplet_liste:
    print(''.join(i))
    if dict_traduire.get(i):
        PROT += dict_traduire.get(i)
print(PROT)



