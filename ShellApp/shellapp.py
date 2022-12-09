import check_format as cf
import trans_trad as tt
import function_shellapp as FSA
# interface shellapp

title = "Bienvenue dans le shellapp du logiciel!!!"
print(title.center(90))

########################################################################
################### QUESTION 1 : TYPE DE FICHIER #######################
########################################################################

question_1 = "Quelle est votre type de type de fichier ?"
print(question_1)

ordre_2 = "Si c'est un fichier fasta veuillez rentrer O sinon N."
print(ordre_2)

while True:
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
        if empty_fasta_file_format == True:
            print("Please check the file")
            continue
        else:
            print("Let's check format file")
            break

    if empty_fasta_file_format == False:
        while True:
            check_fasta_file_format = cf.format_fasta_file(file)
            if check_fasta_file_format == "True_fasta":
                print("It's a fasta file. Let's check the sequences")
                break
            elif check_fasta_file_format == "False_fasta":
                print("Please check your fasta file")
                continue

        #############################################################################
        ################### QUESTION 1 : SUPPLEMENT GTF/GFF ? #######################
        #############################################################################

    if check_fasta_file_format == "True_fasta":
        question_3 = input(
            "Voulez vous ajouter un gtf/gff.Si oui veuillez entrer O sinon N:")
        while True:
            if question_3 == "O":
                break
            if question_3 == "N":
                FSA.multifasta_shell(file)
                file = cf.clear_input(file)
                break

        #############################################################################
        ################### QUESTION 1 : IL FAUT CHOISIR VOTRE SAUCE, ###############
        ################ GREEN FLUORESCENT FILE, OU GREEN TURTLE FILE ? #############
        #############################################################################

    if question_3 == "O":
        gff_file_gtf_file = input(
            "Est ce un fichier gtf ou un gff. Si c'est un gtf entrez O sinon N:")
        while True:
            if gff_file_gtf_file == "O":
                FSA.gtf_shellapp(file)
                file = cf.clear_input(file)
                break
            if gff_file_gtf_file == "N":
                FSA.gff_shellapp(file)
                file = cf.clear_input(file)
                break

########################################################################
################### QUESTION 1 : SEQUENCE ENTREE #######################
########################################################################

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

        #############################################################################
        ################### QUESTION 1 : OPTION TRANSCRIPTION ? #####################
        #############################################################################

    if sequence_verif == "ADN":
        while True:
            question_4 = input(
                "Voulez vous transcrire les séquences. Si oui entrez O sinon N: ")
            if question_4 == "O":
                # Ici j'ai changé prend la ligne
                transcript_ADN = tt.Transcription([file_copy])
                verif_transcript_ARN = cf.ADN_ARN(transcript_ADN)
                print(transcript_ADN)
                break
                # Ce serait bien que la Traduction soir faites aussi en même temps, quitte a ajouter une autre question
            if question_4 == "N":
                traduction_ADN = tt.preTrad(file_copy)
                print(traduction_ADN)
                break

        ###############################################################################
        ################### QUESTION 1 : SUR PLACE OU A TRADUIRE ? #####################
        ################################################################################

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
