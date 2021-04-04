from tkinter import *

root = Tk()
root.title("Probabilidade de eventos independentes")
txta1 = StringVar()
txta2 = StringVar()
txta3 = StringVar()
z = 0


def adding():
    x1 = 0
    PA = float(E1.get())
    PB = float(E2.get())

    PA_e_B = (PA * PB)
    PA_ou_B = (PA + PB - PA_e_B)
    PA_xou_B = PA * (1 - PB) + (1 - PA) * PB
    txta1.set(str(PA_e_B))
    txta2.set(str(PA_ou_B))
    txta3.set(str(PA_xou_B))


L1 = Label(root, text="Entre com a Probabilidade de A e B no intervalo entre 0 e 1")
L1.grid(row=0, column=0, columnspan=2)

#Entrada de valores para PA
LA = Label(root, text="PA = ")
LA.grid(row=1, column=0)
E1 = Entry(root)
E1.grid(row=1, column=1)

#Entrada de valores para PB
LB = Label(root, text="PB = ")
LB.grid(row=2, column=0)
E2 = Entry(root)
E2.grid(row=2, column=1)

#Probabilidade de A e B
L4 = Label(root, text="PA^B = ")
L4.grid(row=5, column=0)
E4 = Entry(root, textvariable=txta1)
E4.grid(row=5, column=1)

#Probabilidade de A ou B
L5 = Label(root, text="PAvB = ")
L5.grid(row=6, column=0)
E5 = Entry(root, textvariable=txta2)
E5.grid(row=6, column=1)

#Probabilidade de A XOR B
L6 = Label(root, text="PAØB = ")
L6.grid(row=7, column=0)
E6 = Entry(root, textvariable=txta3)
E6.grid(row=7, column=1)

#Botão Solve
Button(root, text="Solve", command=lambda: adding()).grid(row=4, column=1)
mainloop()