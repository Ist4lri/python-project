# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Partie 1

import pandas as pd
import re


def split_gtf(file):
    mon_dict = dict()
    mon_dict_Start = dict()
    mon_dict_End = dict()
    # Détection du format
    # On récupère l'extension en liste d'élément en fragmentant la chaîne de caratère
    splited_g_file = file.split(".")
    extension = splited_g_file[1]  # On récupère la
    if extension == 'gtf' or extension == 'gff':
        # Fonction qui permet de supprimer toutes lignes contenant la chaîne de caractère 'start'
        with open(file, "r+") as g_file:
            new_f = g_file.readlines()
            g_file.seek(0)
            for line in new_f:
                # Dans le cas où l'on trouve des régions introniques et des noms de colonnes
                if "start" not in line:
                    g_file.write(line)
                    g_file.truncate()
        ################
        with open(file, 'r') as clean_g_file:
            for i in clean_g_file:
                g_piece = i.split("\t")
                Start = int(g_piece[3])
                End = int(g_piece[4])
                Start_End = str(Start) + "-" + str(End)
                transcript_ID = g_piece[9]
                if not mon_dict.get(transcript_ID):
                    mon_dict_Start[transcript_ID] = Start
                    mon_dict_End[transcript_ID] = End
                    mon_dict[transcript_ID] = Start_End
                else:
                    if mon_dict_Start[transcript_ID] > Start:
                        mon_dict_Start[transcript_ID] = Start
                        mon_dict[transcript_ID] = str(
                            mon_dict_Start[transcript_ID]) + "-" + str(mon_dict_End[transcript_ID])
                    if mon_dict_End[transcript_ID] < End:
                        mon_dict_End[transcript_ID] = End

    return mon_dict


def split_gff(file):
    mon_dict = dict()
    mon_dict_Start = dict()
    mon_dict_End = dict()
    # Détection du format
    # On récupère l'extension en liste d'élément en fragmentant la chaîne de caratère
    splited_g_file = file.split(".")
    extension = splited_g_file[1]  # On récupère la
    if extension == 'gtf' or extension == 'gff':
        # Fonction qui permet de supprimer toutes lignes contenant la chaîne de caractère 'start'
        with open(file, "r+") as g_file:
            new_f = g_file.readlines()
            g_file.seek(0)
            for line in new_f:
                # Dans le cas où l'on trouve des régions introniques et des noms de colonnes
                if "intron" not in line:
                    g_file.write(line)
                    g_file.truncate()
        ################
        with open(file, 'r') as clean_g_file:
            for i in clean_g_file:
                g_piece = i.split("\t")
                Start = int(g_piece[3])
                End = int(g_piece[4])
                Start_End = str(Start) + "-" + str(End)
                transcript_ID = g_piece[8]
                if not mon_dict.get(transcript_ID):
                    mon_dict_Start[transcript_ID] = Start
                    mon_dict_End[transcript_ID] = End
                    mon_dict[transcript_ID] = Start_End
                else:
                    if mon_dict_Start[transcript_ID] > Start:
                        mon_dict_Start[transcript_ID] = Start
                        mon_dict[transcript_ID] = str(
                            mon_dict_Start[transcript_ID]) + "-" + str(mon_dict_End[transcript_ID])
                    if mon_dict_End[transcript_ID] < End:
                        mon_dict_End[transcript_ID] = End

    return mon_dict


def fasta(file2, mon_dict):
    splited_chromosome_file = file2.split(".")
    extension = splited_chromosome_file[1]
    liste_sequence = list()
    liste_transcript_ID = list()
    if extension == 'fasta':
        # Fonction qui permet de supprimer toutes lignes contenant la chaîne de caractère 'chromosome'
        with open(file2, "r+") as chromosome_file:
            new_f2 = chromosome_file.readlines()
            chromosome_file.seek(0)
            for line in new_f2:
                line = line.replace("\n", "")
                if "chromosome" not in line:
                    chromosome_file.write(line)
                    chromosome_file.truncate()
            ################
        with open(file2, 'r+') as clean_chromosome_file:
            reading_chromosome_file = clean_chromosome_file.read()
            for key, value in mon_dict.items():
                chromosome_piece = value.split("-")
                transcript_ID2 = str(key).replace("\n", "")
                Start2 = int(chromosome_piece[0])
                End2 = int(chromosome_piece[1])
                sequence = reading_chromosome_file[Start2:End2]
                liste_sequence.append(str(sequence))
                liste_transcript_ID.append(transcript_ID2)
                # Créer un tableau
                df_chromosome = pd.DataFrame()
                df_chromosome['Transcript_ID'] = pd.Series(liste_transcript_ID)
                df_chromosome['Sequence'] = pd.Series(liste_sequence)
            print(df_chromosome)

    return df_chromosome


def fasta_file(file):
    liste_transcript_ID = list()
    liste_sequence = list()
    splited_file = file.split(".")
    extension = splited_file[1]
    if extension == 'fasta':
        with open(file, "r") as file:
            for line in file.readlines():
                if line[0] == ">":
                    transcript_ID = line.replace("\n", "")
                    liste_transcript_ID.append(transcript_ID)
                else:
                    sequence = line.replace("\n", "")
                    liste_sequence.append(sequence)

                df_fasta = pd.DataFrame()
                df_fasta['Transcript_ID'] = liste_transcript_ID
                df_fasta['Sequence'] = pd.Series(liste_sequence)
            print(df_fasta)

    return df_fasta


def toPutDict(file):
    result = {}
    with open(file, "r") as userFile:
        for line in userFile.readlines():
            if re.match(r"^'[AUGC]{3}'\t'[A-Za-z]{1}'\n$", line):
                result[line[0:4]] = line[6:8]
    return result
