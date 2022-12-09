import check_format as cf
import extraction as ext
import trans_trad as tt

################################################################################################################################
################### ELLES VONT DEMANDER SI ON VEUT UTILISER LES OPTIONS GTF POUR TRANSCRIRE ET/OU TRADUIRE #####################
################################################################################################################################


def gtf_shellapp(file):
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
        sequence_ID_data = ext.fasta(file, sequence_ID_coord)
        print(sequence_ID_data)
        gene_sequence_index_list = sequence_ID_data.index[sequence_ID_data["Transcript_ID"] == "gene"].tolist(
        )
        gene_sequence_index = gene_sequence_index_list[0]
        gene_sequence = str(sequence_ID_data.iat[gene_sequence_index, 1])
        question_4 = input(
            "Voulez vous transcrire la séquence. Si oui entrez O sinon N:")
        while True:
            if question_4 == "O":
                trans_chro_gtf = tt.Transcription(gene_sequence)
                print(trans_chro_gtf)
                question_5 = input(
                    "Voulez vous traduire la/les séquences. Si oui entrez O sinon N:")
                if question_5 == "O":
                    trad_chro_gtf = tt.preTrad(trans_chro_gtf)
                    print(trad_chro_gtf)
                    break
                if question_5 == "N":
                    break
            if question_4 == "N":
                DNA_trad_chro_gtf = tt.preTrad(gene_sequence)
                print(DNA_trad_chro_gtf)
                break
        gtf_file = cf.clear_input(gtf_file)

################################################################################################################################
################### ELLES VONT DEMANDER SI ON VEUT UTILISER LES OPTIONS GFF POUR TRANSCRIRE ET/OU TRADUIRE #####################
################################################################################################################################


def gff_shellapp(file):
    gff_file = input("Donner le chemin d'accès du fichier gff:")
    empty_gff_file_format = cf.empty_file(gff_file)
    while True:
        if empty_gff_file_format == True:
            print("Please check the file")
            continue
        if empty_gff_file_format == False:
            print("Let's check format file")
            break
    if empty_gff_file_format == False:
        check_gff_file_format = cf.format_gff_file(gff_file)
        while True:
            if check_gff_file_format == "False_gff":
                print("Please check your gff/gtf file")
                continue
            elif check_gff_file_format == "True_gff":
                print("Let's check the sequences")
                break
    if check_gff_file_format == "True_gff":
        sequence_ID_coord = ext.split_gff(gff_file)
        sequence_ID_data = ext.fasta(file, sequence_ID_coord)
        print(sequence_ID_data)
        gene_sequence_index_list = sequence_ID_data.index[sequence_ID_data["Transcript_ID"] == "gene"].tolist(
        )
        gene_sequence_index = gene_sequence_index_list[0]
        gene_sequence = str(sequence_ID_data.iat[gene_sequence_index, 1])
        question_4 = input(
            "Voulez vous transcrire la séquence. Si oui entrez O sinon N:")
        while True:
            if question_4 == "O":
                trans_chro_gff = tt.Transcription(gene_sequence)
                print(trans_chro_gff)
                question_5 = input(
                    "Voulez vous traduire la/les séquences. Si oui entrez O sinon N:")
                if question_5 == "O":
                    trad_chro_gff = tt.preTrad(trans_chro_gff)
                    print(trad_chro_gff)
                    break
                if question_5 == "N":
                    break
            if question_4 == "N":
                DNA_trad_chro_gff = tt.preTrad(gene_sequence)
                print(DNA_trad_chro_gff)
                break
        gff_file = cf.clear_input(gff_file)

#######################################################################################################################################
################### ELLES VONT DEMANDER SI ON VEUT UTILISER LES OPTIONS MULTIFASTA POUR TRANSCRIRE ET/OU TRADUIRE #####################
#######################################################################################################################################


def multifasta_shell(file):
    sequence_ID_data = ext.fasta_file(file)
    for key, value in sequence_ID_data.items():
        question_4 = input(
            "Voulez vous transcire la/les séquences. Si oui entrez O sinon N:")
        while True:
            if question_4 == "O":
                trans_multifasta = tt.Transcription(value[0])
                print(key, trans_multifasta)
                question_5 = input(
                    "Voulez vous traduire la/les séquences. Si oui entrez O sinon N:")
                if question_5 == "O":
                    trad_multifasta = tt.preTrad(trans_multifasta)
                    print(key, trad_multifasta)
                    break
                if question_5 == "N":
                    break
            if question_4 == "N":
                DNA_trad_mulitfasta = tt.preTrad(value[0])
                print(key, DNA_trad_mulitfasta)
                break
