from tkinter import *
from tkinter import filedialog
import trans_trad as tt


###############################################################################
############################## CHOISIR UN FICHIER #############################
###############################################################################

def fileChoose():
    global filename
    filename = filedialog.askopenfilename(title="Chosse File")
    if filename:
        seq.pack_forget()
        lseq.pack_forget()


###############################################################################
####################### FAIRE TRANSCRIPTION/TRADUCTION ########################
###############################################################################

def trans_trad(trad, type):
    # On doit reset le Canvas à cahque fois sinon, le resultat se rajoute par dessus.
    drawZone.delete("all")
    if type == "seq":
        if trad == "ADAR":
            drawZone.create_text(w/4, h/6, text=(
                tt.Transcription(seq.get("1.0", "end"))), justify=LEFT, width=900)
            scl = Scrollbar(MainApp, orient='vertical', command=drawZone.yview)
            scl.pack(side=RIGHT, fill=Y)
            drawZone.configure(yscrollcommand=scl.set,
                               scrollregion=drawZone.bbox("all"))
    if type == "file":
        if trad == "ADAR":
            stockARN = ""
            with open(filename, "r") as mainFile:
                for line in mainFile:
                    if line[0] != ">":
                        stockARN += tt.Transcription(line)
                drawZone.create_text(
                    w/4, h/6, text=stockARN, justify=LEFT, width=900)
                scl = Scrollbar(MainApp, orient='vertical',
                                command=drawZone.yview)
                scl.pack(side=RIGHT, fill=Y)
                drawZone.configure(yscrollcommand=scl.set,
                                   scrollregion=drawZone.bbox("all"))


###############################################################################
###################### CHOISIR TRANSCRIPTION/TRADUCTION #######################
###############################################################################

def choose():
    # Si le chemin du fichier est présent, on va envoyer la demande de faire la trans/trad à partir du fichier.
    if seq.get("1.0", "end") != "\n":
        Dif = Toplevel()
        Button(Dif, text="ADN -> ARN", command=lambda: [
            Dif.destroy(), trans_trad("ADAR", "seq")]).grid(row=0, column=0)
        Button(Dif, text="ARN -> PROTEINES", command=lambda: [
            Dif.destroy(), trans_trad("ARP", "seq")]).grid(row=0, column=1)
        Button(Dif, text="ADN -> PROTEINES", command=lambda: [
            Dif.destroy(), trans_trad("ADP", "seq")]).grid(row=0, column=2)
        Button(Dif, text="Quitter",
               command=Dif.destroy).grid(row=1, column=1)
    else:
        Dif = Toplevel()
        Button(Dif, text="ADN -> ARN", command=lambda: [
            Dif.destroy(), trans_trad("ADAR", "file")]).grid(row=0, column=0)
        Button(Dif, text="ARN -> PROTEINES", command=lambda: [
            Dif.destroy(), trans_trad("ARP", "file")]).grid(row=0, column=1)
        Button(Dif, text="ADN -> PROTEINES", command=lambda: [
            Dif.destroy(), trans_trad("ADP", "file")]).grid(row=0, column=2)
        Button(Dif, text="Quitter",
               command=Dif.destroy).grid(row=1, column=1)
    # Si la zone de texte est présente, on va envoyer la demande de faire la trans/trad a partir du contenus de la zone de texte.


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
global filename
w = MainApp.winfo_screenwidth()
h = MainApp.winfo_screenheight()
MainApp.geometry(f'{w}x{h}')

################################################################################
######################## GENERATION DE LA BARRE DE MENU ########################
################################################################################


def pong():
    print("pong")


barMenu = Menu(MainApp)
fileMenu = Menu(barMenu, tearoff=0)
fileMenu.add_command(label="Enregistrer", command=pong)
fileMenu.add_command(label="Enregistrer Sous", command=pong)
barMenu.add_cascade(label="Fichier", menu=fileMenu)

editMenu = Menu(barMenu, tearoff=0)
editMenu.add_command(label="Copier la séquence résultat", command=pong)
barMenu.add_cascade(label="Edition", menu=editMenu)

actionMenu = Menu(barMenu, tearoff=0)
actionMenu.add_command(label="Requête BLAST NCBI", command=pong)
barMenu.add_cascade(label="Action", menu=actionMenu)

################################################################################
###################### GENERATION DE LA ZONE DE RESULTATS ######################
################################################################################

drawZone = Canvas(MainApp, width=w/2, height=h, bg='ivory',
                  cursor="target")
drawZone.pack(side=RIGHT, padx=20, pady=20)

################################################################################
###################### GENERATION DE LA ZONE DE DEMANDE ########################
################################################################################

inLabel = LabelFrame(
    MainApp, text="App Traducteur", padx=20, pady=20, fg="blue", cursor="trek")
# Zone pour entourer la zone demande, esthétique.
inLabel.pack(padx=30, pady=20, side=TOP)

lseq = Label(inLabel, text="Entrez votre séquence ici :")
lseq.pack(padx=5, pady=10)
seq = Text(inLabel, width=100, cursor="trek", state=NORMAL)
seq.pack(padx=5, pady=10)
MainApp.bind("<KeyPress>", keyPress)
Button(inLabel, text='Choisissez en quoi voulez vous le convertir',
       command=choose).pack(padx=10, pady=10)
fButton = Button(inLabel, text='Charger un fichier FASTA',
                 state=NORMAL, command=fileChoose)
fButton.pack(padx=10, pady=10)


################################################################################
################################### QUITTER ####################################
################################################################################

quit = Button(inLabel, text='Quitter', command=MainApp.destroy)
quit.pack(padx=10, pady=10)

MainApp.config(menu=barMenu)
MainApp.mainloop()
