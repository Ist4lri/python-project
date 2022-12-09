#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 23:37:20 2022

@author: lucasonelife
"""

import check_format as cf
import trans_trad  as tt
import extraction as ext
#interface shellapp 

title = "Bienvenue dans le shellapp du logiciel!!!" 
print(title.center(90))

question_1 = "Quelle est votre type de type de fichier ?" 
print(question_1)

ordre_2 = "Si c'est un fichier fasta veuillez rentrer O sinon N."
print(ordre_2)

while True :
    question_1 = input("type de fichier: ")
    if question_1 == "O":
        print("C'est un fichier fasta")
        break
    elif question_1 == "N":
        print("C'est un autre type de fichier")
        break
    continue

if question_1 == "O":
    while True:
        file = input("Donner le chemin d'accès du ficher fasta:")
        empty_fasta_file_format = cf.empty_file(file)
        if empty_fasta_file_format == True :
            print("Please check the file")
            continue
        else:
            print("Let's check format file")
            break

    if empty_fasta_file_format == False : 
       while True: 
           check_fasta_file_format = cf.format_fasta_file(file)
           if check_fasta_file_format == "True_fasta":
               print("It's a fasta file. Let's check the sequences")
               break
           elif check_fasta_file_format== "False_fasta":
               print("Please check your fasta file")
               continue
    
    if check_fasta_file_format == "True_fasta":
        question_3 = input("Voulez vous ajouter une gtf.Si c'est un fichier fasta veuillez rentrer O sinon N:")
        while True:
            if question_3 == "O":
                break
            elif question_3 == "N":
                break
    
    if question_3 == "O":
        gtf_file = input("Donner le chemin d'accès du fichier gtf:")
        empty_gtf_file_format = cf.empty_file(gtf_file)
        while True:
            if empty_gtf_file_format == True:
                print("Please check the file")
                continue
            if empty_gtf_file_format == False:
                print("Let's check format file")
                break
            
    if empty_gtf_file_format == False:
        check_gtf_file_format = cf.format_gtf_file(gtf_file)
        while True:
            if check_gtf_file_format == "False_gtf":
                print("Please check your gff/gtf file")
                continue
            elif check_gtf_file_format == "True_gtf":
                print("Let's check the sequences")
                break
            
    if check_gtf_file_format == "True_gtf":
        sequence_ID_coord = ext.split_gtf(gtf_file)
        sequence_ID_data = ext.fasta(file,sequence_ID_coord)
        print(sequence_ID_data)
            

##########Si l'utilisateur choisi de copier coller une sequence dans le shell
if question_1 == "N": 
    while True:
        file_copy = input("Copier coller les séquences ADN ou ARN:")
        sequence_verif = cf.ADN_ARN(file_copy)
        if sequence_verif == "ADN":
            print("C'est une séquence ADN")
            break
        if sequence_verif == "ARN": 
            print("C'est une séquence ARN")
            break
        
    if sequence_verif == "ADN":
        while True:
            question_4 = input(
                "Voulez vous transcrire les séquences. Si oui entrez O sinon N: ")
            if question_4 == "O":
                transcript_ADN = tt.Transcription([file_copy]) #Ici j'ai changé prend la ligne
                verif_transcript_ARN = cf.ADN_ARN(transcript_ADN)
                print(transcript_ADN)
                break
                # Ce serait bien que la Traduction soir faites aussi en même temps, quitte a ajouter une autre question
            if question_4 == "N":
                break

                
    if sequence_verif == "ARN":
        while True:
            question_5 = input(
                "Voulez vous traduire les séquences. Si oui entrez O sinon N: ")
            if question_5 == "O":
                traduction_ARN = tt.preTrad(file_copy)
                print(traduction_ARN)
                break
            if question_5 == "N":
                break
                
   
            
        
        



    
    
    