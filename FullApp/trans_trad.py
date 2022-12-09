dict_aa = {
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGA": "Arg", "AGG": "Arg", "AAU": "Asn", "AAC": "Asn",
    "GAU": "Asp", "GAC": "Asp", "UGU": "Cys", "UGC": "Cys",
    "CAA": "Gln", "CAG": "Gln", "GAA": "Glu", "GAG": "Glu",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
    "CAU": "His", "CAC": "His", "AUU": "Ile", "AUC": "Ile",
    "AUA": "Ile", "UUA": "Leu", "UUG": "Leu", "CUU": "Leu",
    "CUC": "Leu", "CUA": "Leu", "CUG": "Leu", "AAA": "Lys",
    "AAG": "Lys", "AUG": "Met", "UUU": "Phe", "UUC": "Phe",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "AGU": "Ser", "AGC": "Ser", "ACU": "Thr", "ACC": "Thr",
    "ACA": "Thr", "ACG": "Thr", "UGG": "Trp", "UAU": "Tyr",
    "UAC": "Tyr", "GUU": "Val", "GUC": "Val", "GUA": "Val",
    "GUG": "Val", "UAG": "*", "UGA": "*", "UAA": "*",
}

################################################################################
################ EXTRAIRE LES SEQUENCES DANS UN DICTIONNAIRE ###################
################################################################################


def ExtractSequence(file):
    transcript_ID = ""
    sequenceList = {}
    with open(file, "r") as file:
        for line in file.readlines():
            if line[0] == ">":
                transcript_ID = line.replace("\n", "")
                fusion = []
            else:
                if transcript_ID == "":
                    transcript_ID = "Transcript 1"
                    fusion = []
                fusion.append(line.replace("\n", ""))
            sequenceList[transcript_ID] = ["".join(fusion)]

    return sequenceList

################################################################################
############### FAIRE LA TRANSCRIPTION DE LA SEQUENCE ENVOYEE ##################
################################################################################


def Transcription(sequence):
    if check(sequence) != "ADN":
        return ("Warning, only ADN can be Transcripted. Please, make another attempt.")
    ARN = ""
    for char in sequence:
        if (char != "N") & (char != "\n"):
            if char == "A":
                ARN += "U"
            elif char == "T":
                ARN += "A"
            elif char == "G":
                ARN += "C"
            elif char == "C":
                ARN += "G"
            else:
                ARN += "-UN-"

    return ARN

################################################################################
######### FAIRE LA TRADUCTION EN CHANGEANT DE DICTIONNAIRE (Option) ############
################################################################################


def Traduction(sequence, dict_aa=dict_aa):
    PROT = ""
    for codon in sequence:
        if dict_aa[codon] == "*":
            PROT += dict_aa[codon]
            break
        else:
            PROT += dict_aa[codon]

    return PROT

################################################################################
############## FAIRE DES CODONS PORU TRADUIRE PLUS RAPIDEMENT ##################
################################################################################


def preTrad(sequence, dict_aa=dict_aa):
    if check(sequence) == "ARN":
        result = {}
        codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]

        index = 0
        result[str(index+1)] = Traduction(codons, dict_aa)
        return result

    else:
        ARN = Transcription(sequence)
        result = preTrad(ARN)
        return result

################################################################################
############### VERIFIER SI LA SEQUENCE EST ARNique OU ADNique #################
################################################################################


def check(sequence):
    for char in sequence:
        if (char != "N") & (char != "\n"):
            if char == "T":
                return "ADN"
            elif char == "U":
                return "ARN"
