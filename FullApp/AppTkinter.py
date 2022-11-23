from tkinter import *


welcomeW = Tk()
h = welcomeW.winfo_screenheight()/2
w = welcomeW.winfo_screenwidth()/2
welcomeW.geometry(f'{int(w)}x{int(h)}')
welcomeW.title("Welcome Window")
inLabel = LabelFrame(
    welcomeW, text="Démineur V1.0", padx=20, pady=20, fg="blue", cursor="trek")
inLabel.pack(fill="both", expand="yes", padx=30, pady=20)
Label(inLabel,
      text="Developpeur :\nAUBERT Lucas\nGOUTTEBEL Pierre-Loïc").pack(padx=5, pady=5)
Entry(inLabel).pack(padx=5, pady=10)
welcomeW.mainloop()
