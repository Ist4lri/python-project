import pandas as pd
import re

##########################################################################################################
################### CHERCHER DANS LE GTF LES POSITION DE DEBUT ET FIN DES TRANSCRIPT #####################
##########################################################################################################


def split_gtf(file):
    mon_dict = dict()
    mon_dict_Start = dict()
    mon_dict_End = dict()
    # Fonction qui permet de supprimer toutes lignes contenant la chaîne de caractère 'start'
    with open(file, "r") as g_file:
        with open("hidedOut", "a") as out:
            for line in g_file.readlines():
                # Dans le cas où l'on trouve des régions introniques et des noms de colonnes
                if "start" not in line:
                    out.write(line)

    with open("hideOut", 'r') as clean_g_file:
        for i in clean_g_file:
            g_piece = i.split("\t")
            Start = int(g_piece[3])
            End = int(g_piece[4])
            Start_End = str(Start) + "-" + str(End)
            transcript_ID = g_piece[2]
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

##########################################################################################################
################### CHERCHER DANS LE GFF LES POSITION DE DEBUT ET FIN DES TRANSCRIPT #####################
##########################################################################################################


def split_gff(file):
    mon_dict = dict()
    mon_dict_Start = dict()
    mon_dict_End = dict()
    # Détection du format
   # On récupère l'extension en liste d'élément en fragmentant la chaîne de caratère
   # Fonction qui permet de supprimer toutes lignes contenant la chaîne de caractère 'intron'
    with open(file, "r") as g_file:
        with open("hidedOut", "a") as out:
            for line in g_file.readlines():
                # Dans le cas où l'on trouve des régions introniques et des noms de colonnes
                if "intron" not in line:
                    out.write(line)

    with open(file, 'r') as clean_g_file:
        for i in clean_g_file:
            g_piece = i.split("\t")
            Start = int(g_piece[3])
            End = int(g_piece[4])
            Start_End = str(Start) + "-" + str(End)
            transcript_ID = g_piece[2]
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

########################################################################################################################
################### UTILISER LES POSITIONS POUR FAIRE LA TRADUCTION DU FASTA PAR RAPPORT AUX GENES #####################
########################################################################################################################


def fasta(file2, mon_dict):
    liste_sequence = list()
    liste_transcript_ID = list()
    # Fonction qui permet de supprimer toutes lignes contenant la chaîne de caractère 'chromosome'
    with open(file2, "r") as chromosome_file:
        with open("hideOut", "w") as out:
            for line in chromosome_file.readlines():
                line = line.replace("\n", "")
                if "chromosome" not in line:
                    out.write(line)

    with open(file2, 'r') as clean_chromosome_file:
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

###########################################################################################################
################### CONSTRUIS UN DICTIONNAIRE DEPUIS UNE TABLE DONNEE PAR UTILISATEUR #####################
###########################################################################################################


def toPutDict(file):
    result = {}
    with open(file, "r") as userFile:
        for line in userFile.readlines():
            if re.match(r"^'[AUGC]{3}'\t'[A-Za-z]{1}'\n$", line):
                result[line[1:4]] = line[7]
    return result
