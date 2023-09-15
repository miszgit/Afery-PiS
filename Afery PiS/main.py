from tkinter import *
import random
from os import listdir
from os.path import isfile, join

# pliki bez duplikatów
files = [f for f in listdir(r"Afery PiS\DATY") if isfile(join(r"Afery PiS\DATY", f)) and "_" not in f]

#------------------------------------------------------
# wylosowana afera
def losuj_afere():
    opis_afery.config(state=NORMAL, width=100)
    opis_afery.delete("1.0", END)
    zrodla_afery.config(width=100)
    zrodla_afery.delete("1.0", END)
    afera = random.choice(files)
    with open(f"Afery PiS\DATY\{afera}", encoding="utf-8") as f:
        calosc = f.readlines()
        data = calosc[0]
        opis = ''.join([line for line in calosc[1:] if 'http' not in line])
        zrodla = '\n'.join([zrodlo for zrodlo in calosc if 'http' in zrodlo])
    data_afery.config(text=f"\n{data}", font=("Arial", 20))
    if len(opis) > 1:
        opis_afery.insert("1.0", opis)
    else:
        opis_afery.insert("1.0", "Niesamowite, dzień bez afery?")

    opis_afery.config(state=DISABLED, font=("Arial", 14))
    zrodla_afery.insert(END, zrodla)
#------------------------------------------------------


# okno główne
screen = Tk()
screen.config(width=400, height=400, padx=50, pady=50)
screen.resizable(False, True)
screen.title("Afery Pis")

# tytuł
title = Label(text="Dzień jak co dzień, dzień po dniu,\n wciąż się dzieje pisu cud\n", font=("Courier",24,"italic"))
title.grid(column=0, row=0, columnspan=3)

# data afery
data_afery = Label(text="")
data_afery.grid(column=1, row=2)

# opis afery
opis_afery = Text(width=80, height=10, wrap=WORD, padx=10, pady=10)
opis_afery.grid(column=1, row=3)

# zrodla afery
zrodla_label = Label(text="Źródła:")
zrodla_label.grid(column=0, row=4, rowspan=2)
zrodla_afery = Text(width=120)
zrodla_afery.grid(column=1, row=5)

# losuj afere
losuj = Button(text="Popsuj sobie dzień", command=losuj_afere)
losuj.grid(column=1, row=1)












screen.mainloop()