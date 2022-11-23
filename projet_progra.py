# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Partie 1 

import pandas as pd 

def split(file):
    mon_dict = dict()
    mon_dict_Start = dict()
    mon_dict_End = dict()
    S = file.split(".")
    extension = S[1]
    print(extension)
    if extension == 'gtf' or extension == 'gff':
        #################Fonction qui permet de supprimer toutes lignes contenant la chaîne de caractère 'start'
        with open(file,"r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
        #################Dans le cas où l'on trouve des régions introniques et des noms de colonnes
                if "start" not in line:
                    f.write(line)
                if "intron" not in line :
                    f.write(line)
            f.truncate()
        ################
        G = open(file, 'r')
        for i in G:
            m = i.split("\t")
            Start = int(m[3])
            End = int(m[4])
            Start_End = str(Start) + "-" + str(End)
            transcript_ID = m[9]
            if not mon_dict.get(transcript_ID):
                mon_dict_Start[transcript_ID] = Start
                mon_dict_End[transcript_ID] = End
                mon_dict[transcript_ID] = Start_End
            else:
                if mon_dict_Start[transcript_ID] > Start:
                    mon_dict_Start[transcript_ID]= Start
                    mon_dict[transcript_ID] = str(mon_dict_Start[transcript_ID]) + "-" + str(mon_dict_End[transcript_ID])
                    if mon_dict_End[transcript_ID] < End:                   
                        mon_dict_End[transcript_ID] = End
                    
        for key,value in mon_dict.items():
            print(key,value)
    else:
        print('Utilisez fichiers format gtf')
          
    def fasta(file2):
        S2 = file2.split(".")
        extension = S2[1]
        print(extension)
        liste_sequence = list()
        liste_transcript_ID = list()
        if extension == 'fasta':
            ################Fonction qui permet de supprimer toutes lignes contenant la chaîne de caractère 'chromosome'
            with open(file2,"r+") as f2:
                new_f2 = f2.readlines()
                f2.seek(0)
                for line in new_f2:
                    line = line.replace("\n","")
                    if "chromosome" not in line:
                        f2.write(line)
                        f2.truncate()
            ################
            F = open(file2, 'r+')
            R = F.read()
            for key,value in mon_dict.items():
                m2 = value.split("-")
                transcript_ID2 = str(key).replace("\n","")
                Start2 = int(m2[0])
                print(Start2)
                End2 = int(m2[1])
                print(End2)
                sequence = R[Start2:End2]
                liste_sequence.append(str(sequence))
                liste_transcript_ID.append(transcript_ID2)
                
                #Créer un tableau
                df = pd.DataFrame()
                df['Transcript_ID'] = pd.Series(liste_transcript_ID)
                df['Sequence'] = pd.Series(liste_sequence)
            print(df)
    
            
        
            
        else:
            print("Utilisez fichiers format fasta")
            
    fasta("chromosome22.fasta")
        
split("MYH9.gtf") 


  




