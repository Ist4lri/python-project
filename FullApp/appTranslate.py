from tkinter import *
from tkinter import filedialog
import trans_trad as tt


def fileChoose():
    global filename
    filename = filedialog.askopenfilename(title="Chosse File")
    if filename:
        seq.pack_forget()
        lseq.pack_forget()


def userChoose(trad, type):
    drawZone.delete('all')
    if type == "seq":
        if trad == "ADAR":
            drawZone.create_text(
                110, 60, text=tt.Transcription(seq.get("1.0", "end")), width=1500)


def choose():
    if seq.get("1.0", "end"):
        Dif = Toplevel()
        Button(Dif, text="ADN -> ARN", command=lambda: [
            Dif.destroy(), userChoose("ADAR", "seq")]).grid(row=0, column=0)
        Button(Dif, text="ARN -> PROTEINES", command=lambda: [
            Dif.destroy(), userChoose("ARP", "seq")]).grid(row=0, column=1)
        Button(Dif, text="ADN -> PROTEINES", command=lambda: [
            Dif.destroy(), userChoose("ADP", "seq")]).grid(row=0, column=2)
        Button(Dif, text="Quitter",
               command=Dif.destroy).grid(row=1, column=1)
    else:
        Dif = Toplevel()
        Button(Dif, text="ADN -> ARN", command=lambda: [
            Dif.destroy(), userChoose("ADAR", "file")]).grid(row=0, column=0)
        Button(Dif, text="ARN -> PROTEINES", command=lambda: [
            Dif.destroy(), userChoose("ARP", "file")]).grid(row=0, column=1)
        Button(Dif, text="ADN -> PROTEINES", command=lambda: [
            Dif.destroy(), userChoose("ADP", "file")]).grid(row=0, column=2)
        Button(Dif, text="Quitter",
               command=Dif.destroy).grid(row=1, column=1)


def keyPress(event):
    fButton.pack_forget()
    if seq.get("1.0", "end") == "\n":
        quit.pack_forget()
        fButton.pack(padx=10, pady=10)
        quit.pack(padx=10, pady=10)


MainApp = Tk()
MainApp.title("Transcription/Translation App")
global w, h
w = MainApp.winfo_screenwidth()
h = MainApp.winfo_screenheight()

MainApp.geometry(
    f'{w}x{h}')
MainApp.resizable(width=False, height=False)
drawZone = Canvas(MainApp, width=w/2, height=h, bg='grey', cursor="target")
drawZone.pack(
    side=LEFT, padx=20, pady=20)
inLabel = LabelFrame(
    MainApp, text="App Traducteur", padx=20, pady=20, fg="blue", cursor="trek")
inLabel.pack(padx=30, pady=20, side=TOP)
lseq = Label(inLabel, text="Entrez votre séquence ici :")
lseq.pack(padx=5, pady=10)
MainApp.bind("<KeyPress>", keyPress)
seq = Text(inLabel, width=100,
           cursor="trek", state=NORMAL)
seq.pack(padx=5, pady=10)
Button(
    inLabel, text='Choisissez en quoi voulez vous le convertir', command=choose).pack(
    padx=10, pady=10)
fButton = Button(
    inLabel, text='Charger un fichier FASTA', state=NORMAL, command=fileChoose)
fButton.pack(padx=10, pady=10)
quit = Button(inLabel, text='Quitter', command=MainApp.destroy)
quit.pack(padx=10, pady=10)


MainApp.mainloop()
