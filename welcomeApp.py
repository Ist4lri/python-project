from tkinter import *
import subprocess
import os

###############################################################################
######################## QUEL OPTIONS DE LANCEMENT ############################
###############################################################################


def launchApp():
    if appButton.click == True:
        welcomeW.destroy()
        os.system("python3 FullApp/appTranslate.py")
        appButton.click = False


def launchShell():
    if shellButton.click == True:
        welcomeW.destroy()
        os.system("python3 ShellApp/shellapp.py")
        shellButton.click = False


################################################################################
###################### GENERATION DE L'APP, DEFINITION TAILLE ##################
################################################################################

welcomeW = Tk()
h = welcomeW.winfo_screenheight()/3.2
w = welcomeW.winfo_screenwidth()/2
welcomeW.geometry(f'{int(w)}x{int(h)}')
welcomeW.title("Welcome Window")


################################################################################
###################### GENERATION DES OPTIONS AVEC DESCRIPTIF###################
################################################################################

inLabel = LabelFrame(
    welcomeW, text="Traducteur V1.0", padx=20, pady=20, fg="blue", cursor="trek")
inLabel.pack(fill="both", expand="no", padx=30, pady=20)
inLabel.columnconfigure(0, weight=1)
inLabel.columnconfigure(1, weight=5)
inLabel.columnconfigure(2, weight=1)

Label(inLabel, text="Bienvenue. Ceci est un traducteur d'ADN qui possèdes quelques fonctionnalités supplémentaire.\nVous avez la possibilité de lancer ses fonctionnalités depuis un terminal, ou depuis l'application.").grid(row=0, column=1)

shellButton = Button(inLabel, text="Terminal Shell",
                     command=launchShell)
shellButton.click = True
shellButton.grid(row=1, column=0)

appButton = Button(inLabel, text="Application", command=launchApp)
appButton.click = True
appButton.grid(row=1, column=2)

################################################################################
########### GENERATION DU BOUTON QUITTER, ET DEVELOPPEURS LABEL ################
################################################################################


Button(inLabel, text="Quitter", command=welcomeW.destroy).grid(row=2, column=1)

subLabel = LabelFrame(welcomeW, text="Développement",
                      padx=10, pady=10, fg="red", cursor="trek")
subLabel.pack(fill="none", expand="no", padx=15, pady=15)
Label(subLabel,
      text="Developpeurs :\nAUBERT Lucas\nGOUTTEBEL Pierre-Loïc").pack()

################################################################################
##################### GENERATION TDU RESULTAT FINAL ! ##########################
################################################################################

welcomeW.mainloop()
