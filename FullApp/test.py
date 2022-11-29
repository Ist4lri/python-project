from tkinter import *
from tkinter import filedialog


def userChoose(difficulty):
    Trad = difficulty
    print(difficulty)


def choose():
    Dif = Toplevel()
    Button(Dif, text="ADN -> ARN", command=lambda: [
        Dif.destroy(), userChoose(1)]).grid(row=0, column=0)
    Button(Dif, text="ARN -> PROTEINES", command=lambda: [
        Dif.destroy(), userChoose(2)]).grid(row=0, column=1)
    Button(Dif, text="ADN -> PROTEINES", command=lambda: [
        Dif.destroy(), userChoose(3)]).grid(row=0, column=2)
    Button(Dif, text="Quitter",
           command=Dif.destroy).grid(row=1, column=1)


MainApp = Tk()
MainApp.title("Translation App")
MainApp.geometry(
    f'{MainApp.winfo_screenwidth()}x{MainApp.winfo_screenheight()}')
MainApp.resizable(width=False, height=False)
drawZone = Canvas(MainApp, width=MainApp.winfo_screenwidth()/2, height=MainApp.winfo_screenheight(), bg='ivory', cursor="target").pack(
    side=RIGHT, padx=20, pady=20)
inLabel = LabelFrame(
    MainApp, text="App Traducteur", padx=20, pady=20, fg="blue", cursor="trek")
inLabel.pack(padx=30, pady=20, side=TOP)
Label(inLabel, text="Entrez votre séquence ici :").pack(padx=5, pady=10)
seq = Entry(inLabel, width=20,
            cursor="trek").pack(padx=5, pady=10)
Button(inLabel, text='Choisissez en quoi voulez vous le convertir', command=choose).pack(
    padx=10, pady=10)
Button(inLabel, text='Charger un fichier FASTA').pack(padx=10, pady=10)
Button(inLabel, text='Quitter', command=MainApp.destroy).pack(padx=10, pady=10)


MainApp.mainloop()

#filename = filedialog.askopenfilename()
