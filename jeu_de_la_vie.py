from tkinter import *

def evolution():
    global cellules
    suivant=[ligne[:] for ligne in cellules] # copier le tableau proprement
    for x in range(hauteur):
        for y in range(largeur):
            nb=0
            # tests de présence de cellules
            # le bord est considéré comme un obstacle infranchissable
            if x<hauteur-1:
                if cellules[x+1][y]==1: nb+=1
                if y<hauteur-1 and cellules[x+1][y+1]==1: nb+=1
            if y<largeur-1 and cellules[x][y+1]==1: nb+=1
            if x>0:
                if cellules[x-1][y]==1: nb+=1
                if y>0 and cellules[x-1][y-1]==1: nb+=1
            if y>0 and cellules[x][y-1]==1: nb+=1
            if x<hauteur-1 and y>0 and cellules[x+1][y-1]==1: nb+=1
            if x>0 and y<largeur-1 and cellules[x-1][y+1]==1: nb+=1

            # seulement les tests qui changent la valeur d'une cellule
            if cellules[x][y]==0 and nb==3: suivant[x][y]=1
            elif cellules[x][y]==1 and nb not in [2,3]: suivant[x][y]=0
    cellules=suivant

def evolutionGraphique():
    evolution()
    updateGraphique()

def updateGraphique():
    # on efface tout, puis on remet les cases cellule par cellule
    canvas.delete("all")
    for x in range(hauteur):
        for y in range(largeur):
            if cellules[x][y]==0: canvas.create_rectangle(cote*x,cote*y,cote*(x+1),cote*(y+1),fill="white")
            else: canvas.create_rectangle(cote*x,cote*y,cote*(x+1),cote*(y+1),fill="black")

def ajouterCellule(event):
    global cellules
    # coordonnees cellule correspondant au clic
    x=event.x//cote
    y=event.y//cote
    cellules[x][y]=(cellules[x][y]+1)%2 # alterne entre 0 et 1
    updateGraphique()

largeur=30 #int(input("Largeur de la fenêtre en cellules : "))
hauteur=30 #int(input("Hauteur de la fenêtre en cellules : "))
cote=20 #int(input("Côté d'une cellule en pixels : "))
larFen=largeur*cote
hautFen=hauteur*cote
cellules=[[0 for y in range(largeur)] for x in range(hauteur)]

fen=Tk()
fen.title("Jeu de la vie")
fen.geometry(str(larFen)+"x"+str(hautFen+50))
fen.resizable(width=False,height=False)
canvas=Canvas(fen,bg="white",width=larFen,height=hautFen)
canvas.place(x=0,y=0)
canvas.bind("<ButtonPress-1>",ajouterCellule)
evoluer=Button(fen,text="ÉVOLUTION !",command=evolutionGraphique)
evoluer.place(x=larFen//2-60,y=hautFen+10) # choisit positionnement bouton
updateGraphique()
fen.mainloop()
