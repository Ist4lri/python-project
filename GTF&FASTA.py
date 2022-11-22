# J'ai écrit deux codes pour la même fonction le premier ne retourne que le premier couple START/END de chaque exon
# Le second retourne la couverture génomique de chaque transcript
def split(file):
    mon_dict = dict()
    split = file.split(".")
    extension = split[1]
    print(extension)
    if extension == 'gtf' or extension == 'gff':
        G = open(file, 'r')
        for i in G:
            m = i.split("\t")
            Start_End = m[3] + "-" + m[4]
            gene_ID = m[8]
            if not mon_dict.get(gene_ID):
                mon_dict[gene_ID] = Start_End
        for key, value in mon_dict.items():
            print(key, value)
    else:
        print('Utilisez fichiers format gtf')


split("ensembl.gtf")

########################################################################################################
########################################################################################################
# Presque terminée mais il y a encore un dernier problème à régler. Le nouveau dictionnaire n'associe pas chaque transcript_ID à chaque séquence mais
# un seul pour toutes les séquences découpées il est donc impossible de les récupérer de manière individuelle dans ce nouveau dictionnaire.


def split(file):
    mon_dict = dict()
    mon_dict_Start = dict()
    mon_dict_End = dict()
    S = file.split(".")
    extension = S[1]
    print(extension)
    if extension == 'gtf' or extension == 'gff':
        # Fonction qui permet de supprimer toutes lignes contenant la chaîne de caractère 'start'
        with open(file, "r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if "start" not in line:
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
                    mon_dict_Start[transcript_ID] = Start
                    mon_dict[transcript_ID] = str(
                        mon_dict_Start[transcript_ID]) + "-" + str(mon_dict_End[transcript_ID])
                    if mon_dict_End[transcript_ID] < End:
                        mon_dict_End[transcript_ID] = End

        for key, value in mon_dict.items():
            print(key, value)
    else:
        print('Utilisez fichiers format gtf')

    def fasta(file2):
        S2 = file2.split(".")
        extension = S2[1]
        print(extension)
        mon_dict_fasta = dict()
        if extension == 'fasta':
            # Fonction qui permet de supprimer toutes lignes contenant la chaîne de caractère 'chromosome'
            with open(file2, "r+") as f2:
                new_f2 = f2.readlines()
                f2.seek(0)
                for line in new_f2:
                    if "chromosome" not in line:
                        f2.write(line)
                        f2.truncate()
            ################
            F = open(file2, 'r+')
            R = F.read()
            for key, value in mon_dict.items():
                m2 = value.split("-")
                transcript_ID2 = str(key)
                Start2 = int(m2[0])
                print(Start2)
                End2 = int(m2[1])
                print(End2)
                sequence = R[Start2:End2]
                if not mon_dict_fasta.get(transcript_ID2):
                    mon_dict_fasta[transcript_ID] = sequence
                else:
                    mon_dict_fasta[transcript_ID] += sequence

            for key, value in mon_dict_fasta.items():
                print(key, value)

        else:
            print("Utilisez fichiers format fasta")

    fasta("chromosome22.fasta")


split("ensembl.gtf")
