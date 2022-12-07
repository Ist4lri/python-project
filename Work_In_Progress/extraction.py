# # -*- coding: utf-8 -*-
# """
# Spyder Editor

# This is a temporary script file.
# """

# #Partie 1

import pandas as pd

# def split(file):
#     mon_dict = dict()
#     mon_dict_Start = dict()
#     mon_dict_End = dict()
#     #Détection du format
#     splited_g_file = file.split(".") #On récupère l'extension en liste d'élément en fragmentant la chaîne de caratère
#     extension = splited_g_file[1] #On récupère la
#     print(extension)
#     if extension == 'gtf' or extension == 'gff':
#         #Fonction qui permet de supprimer toutes lignes contenant la chaîne de caractère 'start'
#         with open(file,"r+") as g_file:
#             new_f = g_file.readlines()
#             g_file.seek(0)
#             for line in new_f:
#         #Dans le cas où l'on trouve des régions introniques et des noms de colonnes
#                 if "start" not in line:
#                     g_file.write(line)
#                 elif "intron" not in line :
#                     g_file.write(line)
#             g_file.truncate()
#         ################
#         clean_g_file = open(file, 'r')
#         for i in clean_g_file:
#             g_piece = i.split("\t")
#             Start = int(g_piece[3])
#             End = int(g_piece[4])
#             Start_End = str(Start) + "-" + str(End)
#             transcript_ID = g_piece[9]
#             if not mon_dict.get(transcript_ID):
#                 mon_dict_Start[transcript_ID] = Start
#                 mon_dict_End[transcript_ID] = End
#                 mon_dict[transcript_ID] = Start_End
#             else:
#                 if mon_dict_Start[transcript_ID] > Start:
#                     mon_dict_Start[transcript_ID]= Start
#                     mon_dict[transcript_ID] = str(mon_dict_Start[transcript_ID]) + "-" + str(mon_dict_End[transcript_ID])
#                     if mon_dict_End[transcript_ID] < End:
#                         mon_dict_End[transcript_ID] = End

#         for key,value in mon_dict.items():
#             print(key,value)
#     else:
#         print('Utilisez fichier format gtf')

#     def fasta(file2):
#         splited_chromosome_file = file2.split(".")
#         extension = splited_chromosome_file[1]
#         print(extension)
#         liste_sequence = list()
#         liste_transcript_ID = list()
#         if extension == 'fasta':
#             ################Fonction qui permet de supprimer toutes lignes contenant la chaîne de caractère 'chromosome'
#             with open(file2,"r+") as chromosome_file:
#                 new_f2 = chromosome_file.readlines()
#                 chromosome_file.seek(0)
#                 for line in new_f2:
#                     line = line.replace("\n","")
#                     if "chromosome" not in line:
#                         chromosome_file.write(line)
#                         chromosome_file.truncate()
#             ################
#             clean_chromosome_file = open(file2, 'r+')
#             reading_chromosome_file = clean_chromosome_file.read()
#             for key,value in mon_dict.items():
#                 chromosome_piece = value.split("-")
#                 transcript_ID2 = str(key).replace("\n","")
#                 Start2 = int(chromosome_piece[0])
#                 print(Start2)
#                 End2 = int(chromosome_piece[1])
#                 print(End2)
#                 sequence = reading_chromosome_file[Start2:End2]
#                 liste_sequence.append(str(sequence))
#                 liste_transcript_ID.append(transcript_ID2)

#                 #Créer un tableau
#                 df = pd.DataFrame()
#                 df['Transcript_ID'] = pd.Series(liste_transcript_ID)
#                 df['Sequence'] = pd.Series(liste_sequence)
#             print(df)


#         else:
#             print("Utilisez fichier format fasta")

#     fasta("chromosome22.fasta")

# split("MYH9.gtf")

def fasta_file(file):
    transcript_ID = ""
    extension = file.split(".")[1]
    sequenceList = {}
    fusion = []
    if extension == 'fasta':
        with open(file, "r") as file:
            for line in file.readlines():
                if line[0] == ">":
                    transcript_ID = line.replace("\n", "")
                    fusion = []
                else:
                    fusion.append(line.replace("\n", ""))
                sequenceList[transcript_ID] = ["".join(fusion)]
            print(sequenceList)
    else:
        print("Utilisez fichier format fasta")


fasta_file("Données/B.fasta")
