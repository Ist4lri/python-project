
PROT = ""
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


def Transcription(sequence):
    ARN = ""
    for char in sequence:
        if (char != "N") & (char != "\n"):
            if char == "A":
                ARN += "U"
            elif char == "T":
                ARN += "A"
            elif char == "G":
                ARN += "C"
            else:
                ARN += "G"

    return ARN


def Tarduction(sequence):
    print("bite")
# counter = 0

# for i in range(0, len(ARN)):
#     if dict_traduire.get(ARN[i:i+3]) == "Met":
