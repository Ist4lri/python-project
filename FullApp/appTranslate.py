from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import trans_trad as tt


###############################################################################
############################## CHOISIR UN FICHIER #############################
###############################################################################

def fileChoose(to_verif, secondOne=""):
    global fileFasta
    global fileGff
    global fileTxt
    global filename
    filename = filedialog.askopenfilename(
        title="Chosse " + to_verif + " File")
    fullPathName = filename.split(".")
    extension = fullPathName[1]
    while extension != to_verif and extension != secondOne:
        messagebox.showerror(
            "Error", "Veuillez sélectionner un fichier au format suivant : ." + to_verif + " ou ." + secondOne)
        filename = filedialog.askopenfilename(title="Chosse File")
        fullPathName = filename.split(".")
        extension = fullPathName[1]
    if extension == "fasta":
        fileFasta = filename
    elif extension == "gff3" or "gtf":
        fileGff = filename
    elif extension == "txt":
        fileTxt = filename


###############################################################################
#################### AFFICHER LE RESULTAT DANS UNE FENETRE ####################
###############################################################################

def displayResult(toBeDisplayed):
    displayWindow = Toplevel()
    drawZone = Canvas(displayWindow, width=w/2, height=h/2, bg='ivory',
                      cursor="target")
    drawZone.pack(side=LEFT, padx=20, pady=20)
    drawZone.create_text(
        w/4, h/6, text=toBeDisplayed, justify=LEFT, width=900)
    scl = Scrollbar(displayWindow, orient='vertical', command=drawZone.yview)
    scl.pack(side=RIGHT, fill=Y)
    drawZone.configure(yscrollcommand=scl.set,
                       scrollregion=drawZone.bbox("all"))

###############################################################################
####################### QUEL CHOIX L'UTILISATEUR A FAIT #######################
###############################################################################


def trans_trad(trad, type):
    ###################
    ## SI UN FICHIER ##
    ###################
    global catchFile
    if type == "file":
        ###################
        ## FICHIER - ARN ##
        ###################
        if trad == "ADAR":
            catchFile = tt.ExtractSequence(fileFasta)
            for k, v in catchFile.items():
                Button(resultLabel, text=k, command=lambda v=v:  displayResult(tt.Transcription(v))).pack(
                    padx=10, pady=10)

        #####################
        ## FICHIER - PROT ##
        #####################

        if trad == "ARP":
            print("bite")
            #####################
            ## SI UNE SEQUENCE ##
            #####################

    if type == "seq":

        ####################
        ## SEQUENCE - ARN ##
        ####################

        if trad == "ADAR":
            with open("FullApp/tempOut.txt", "w") as outFile:
                outFile.write(seq.get("1.0", "end"))
            catchFile = tt.ExtractSequence("FullApp/tempOut.txt")
            for k, v in catchFile.items():
                Button(resultLabel, text=k, command=lambda v=v:  displayResult(tt.Transcription(v))).pack(
                    padx=10, pady=10)

        #####################
        ## SEQUENCE - PROT ##
        #####################


###############################################################################
###################### CHOISIR TRANSCRIPTION/TRADUCTION #######################
###############################################################################


def choose():
    # Si la zone de texte est présente, on va envoyer la demande de faire la trans/trad a partir du contenus de la zone de texte.
    if seq.get("1.0", "end") != "\n":
        chooseWindow = Toplevel()
        Button(chooseWindow, text="ADN -> ARN", command=lambda: [
            chooseWindow.destroy(), trans_trad("ADAR", "seq")]).grid(row=0, column=0)
        Button(chooseWindow, text="ARN -> PROTEINES", command=lambda: [
            chooseWindow.destroy(), trans_trad("ARP", "seq")]).grid(row=0, column=1)
        Button(chooseWindow, text="ADN -> PROTEINES", command=lambda: [
            chooseWindow.destroy(), trans_trad("ADP", "seq")]).grid(row=0, column=2)
        Button(chooseWindow, text="Quitter",
               command=chooseWindow.destroy).grid(row=1, column=1)
    # Si la zone de texte est absente, on va envoyer la demande de faire la trans/trad à partir du fichier.
    else:
        chooseWindow = Toplevel()
        Button(chooseWindow, text="ADN -> ARN", command=lambda: [
            chooseWindow.destroy(), trans_trad("ADAR", "file")]).grid(row=0, column=0)
        Button(chooseWindow, text="ARN -> PROTEINES", command=lambda: [
            chooseWindow.destroy(), trans_trad("ARP", "file")]).grid(row=0, column=1)
        Button(chooseWindow, text="ADN -> PROTEINES", command=lambda: [
            chooseWindow.destroy(), trans_trad("ADP", "file")]).grid(row=0, column=2)
        Button(chooseWindow, text="Quitter",
               command=chooseWindow.destroy).grid(row=1, column=1)

################################################################################
######################### ENLEVER LES WIDGETS INUTILES #########################
################################################################################


def keyPress(event):
    fButton.pack_forget()
    if seq.get("1.0", "end") == "\n":
        quit.pack_forget()
        fButton.pack(padx=10, pady=10)
        quit.pack(padx=10, pady=10)


################################################################################
###################### GENERATION DE L'APP, DEFINITION TAILLE ##################
################################################################################

MainApp = Tk()
MainApp.title("Transcription/Translation App")
global w, h
w = MainApp.winfo_screenwidth()
h = MainApp.winfo_screenheight()
MainApp.geometry(f'{int(w/1.2)}x{int(h/1.2)}')


################################################################################
###################### GENERATION DE LA ZONE DE RESULTATS ######################
################################################################################

resultLabel = LabelFrame(MainApp, text='Résultats',
                         padx=20, pady=20, fg="red", cursor="target")
resultLabel.pack(padx=30, pady=20, side=RIGHT)

################################################################################
###################### GENERATION DE LA ZONE DE DEMANDE ########################
################################################################################

inLabel = LabelFrame(
    MainApp, text="App Traducteur", padx=20, pady=20, fg="blue", cursor="trek")
# Zone pour entourer la zone demande, esthétique.
inLabel.pack(padx=30, pady=20, side=LEFT)

lseq = Label(inLabel, text="Entrez votre séquence ici :")
lseq.pack(padx=5, pady=10)
seq = Text(inLabel, width=100, cursor="trek")
seq.pack(padx=5, pady=10)
MainApp.bind("<KeyPress>", keyPress)  # Un "surveillant" d'actions au claviers

Button(inLabel, text='Choisissez en quoi voulez vous le convertir',
       command=choose).pack(padx=10, pady=10)

fastaButton = Button(inLabel, text='Charger un fichier FASTA',
                     state=NORMAL, command=lambda: [fileChoose("fasta"), seq.pack_forget(), lseq.pack_forget()])
fastaButton.pack(padx=10, pady=10)

gffButton = Button(inLabel, text='Charger un fichier GTF/GFF',
                   command=lambda: [fileChoose("gff3", "gtf")])
gffButton.pack(padx=10, pady=10)

fButton = Button(inLabel, text='Charger une autre table de traduction en txt',
                 command=lambda: [fileChoose("txt")])
fButton.pack(padx=10, pady=10)

################################################################################
################################### QUITTER ####################################
################################################################################

quit = Button(inLabel, text='Quitter', command=MainApp.destroy)
quit.pack(padx=10, pady=10)

MainApp.mainloop()
