import os
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox

###############################################################################
################### VERIFIER SI LE FICHIER EST PAS VIDE #######################
###############################################################################


def empty_file(file):
    # check if it's an empty file:
    if os.path.getsize(file) == 0:
        return True
    else:
        return False

###############################################################################
#################### VERIFIER SI LE FICHIER EST UN GFF ########################
###############################################################################


def format_gff_file(file):
    # check what kind of file is it:
    df = pd.read_csv(file, sep="\t", header=None)
    row_count = df.shape[0]
    col_count = df.shape[1]
    if row_count > 10 and col_count == 9:
        with open(file, "r") as gtf_file:
            for line in gtf_file:
                pass
            piece = line.split("\t")
            Start = piece[3]
            End = piece[4]
            numeric_start = Start.isnumeric()
            numeric_end = End.isnumeric()
            if numeric_start == True and numeric_end == True:
                return "True_gff"
            else:
                return "False_gff"

###############################################################################
#################### VERIFIER SI LE FICHIER EST UN GTF ########################
###############################################################################


def format_gtf_file(file):
    # check what kind of file is it:
    df = pd.read_csv(file, sep="\t", header=None)
    row_count = df.shape[0]
    col_count = df.shape[1]
    if row_count > 10 and col_count == 10:
        with open(file, "r") as gtf_file:
            for line in gtf_file:
                pass
            piece = line.split("\t")
            Start = piece[3]
            End = piece[4]
            numeric_start = Start.isnumeric()
            numeric_end = End.isnumeric()
            if numeric_start == True and numeric_end == True:
                return "True_gtf"
            else:
                return "False_gtf"

###############################################################################
################### VERIFIER SI LE FICHIER EST UN FASTA #######################
###############################################################################


def format_fasta_file(file):
    with open(file, "r") as fasta_file:
        for line in fasta_file:
            header = line.count(">")
            if header == 0:
                return "False_fasta"
            else:
                return "True_fasta"

###############################################################################
################### VERIFIER SEQUENCE ARNique OU ADNique ######################
###############################################################################


def ADN_ARN(sequence):
    for char in sequence:
        if (char != "N") & (char != "\n"):
            if char == "A":
                return "ADN"
            elif char == "U":
                return "ARN"

###############################################################################
############################## NETTOYER L'INPUT ###############################
###############################################################################


def clear_input(_):
    return ''
