import tkinter as tk
import string
import time
import random
import re

valeur= None
valeur2 = None

def recuperer_valeur(entry):
    global valeur
    valeur = entry.get()
    print(valeur)
    valeur2_liste = []
    for i in valeur:
        valeur2_liste.append(i)
        print(valeur2_liste)
    valeur2_liste = valeur2_liste [:8]
    print(valeur2_liste)

def recuperer_valeur2(entry):
    global valeur2
    valeur2 = entry.get()
    print(valeur2)
    valeur3_liste = []
    for i in valeur2:
        valeur3_liste.append(i)
        print(valeur3_liste)
    valeur3_liste = valeur3_liste [:8]
    print(valeur3_liste)

def sortir():
    canvas.create_text(300, 750, text=("cette fenetre va etre detruite dans : 3 secondes"), font=("arial", 14), fill="darkred")
    canvas.create_rectangle(10, 720, 580, 780)
    fenetre.after(2000, fenetre.destroy)
    global d
    d = None

def rester():
    global d
    d = True

def attendre_condition():
    global d
    if d:
        ajouter_mot_de_passe()
    else:
        fenetre.after(100, attendre_condition)

d = None
def ajouter_mot_de_passe():
            global x, u, d
            d = False
            tous_les_caractères = string.ascii_uppercase + string.ascii_lowercase + string.digits +string.ascii_lowercase +  "?,.:;#)(&_-|°" + "?,.:;#)(&_-|°"
            longueur = ""
            while len(longueur) < 10:
                hasard = random.choice(tous_les_caractères)
                longueur += hasard
                print(longueur)
            if u == 1:
                r = "er"
            else:
                r = "ieme"
            
            canvas.create_rectangle(260, x + 120, 400, x + 160) 
            canvas.create_rectangle(10, x + 120, 250, x + 160)
            canvas.create_text(330, x + 140, text=f"{longueur}", font=("arial", 14), fill="red")
            canvas.create_text(100, x + 140, text=f"{u}{r} mot de passe :", font=("arial", 14), fill="black")

            button = tk.Button(fenetre, text="Sortir", font=("Arial", 12), width=4, bg="red",
                            command=sortir)
            canvas.create_window(440, x + 190, window=button)
            button2 = tk.Button(fenetre, text="rester", font=("Arial", 12), width=4, bg="green",
                            command=rester)
            canvas.create_window(520, x + 190, window=button2)
            
            canvas.create_text(195, x + 190, text="""voulez vous sauvegarder d'autre 
                    mots de passe ?""", font=("arial", 14), fill="black")
            canvas.create_rectangle(10, x + 170, 400, x + 210)
            
            c.append(longueur)
        
            attendre_condition()
            if len(c) == 5:
                canvas.create_text(300, 750, text=("cette fenetre va etre detruite dans : 3 secondes"), font=("arial", 14), fill="darkred")
                canvas.create_rectangle(10, 720, 580, 780)
                fenetre.after(2000, fenetre.destroy)
                    
            print(c)
            print(a)
            u += 1
            x += 100
fenetre = tk.Tk()
fenetre.geometry("600x800")
fenetre.title("generateur de mot de passe")

canvas = tk.Canvas(width=600, height=800, bg="lightblue")
canvas.pack(side="bottom", padx=5, pady=5)

canvas.create_rectangle(10, 10, 580, 50)
canvas.create_text(300, 30, text="bienvenue sur le logiciel de sauvegarde de mot de passe crypté!", font=("arial", 14), fill="darkblue")
canvas.create_rectangle(10, 60, 250, 100)
canvas.create_text(120, 80, text="mot de passe generale :", font=("arial", 14), fill="darkblue")


entry = tk.Entry(fenetre, font=("Arial", 15), width=20)
button = tk.Button(fenetre, text="OK", font=("Arial", 10), width=4,
                        command=lambda e=entry:recuperer_valeur(e))
canvas.create_window(390, 80,  window=entry)  
canvas.create_window(500, 80, window=button)


a = ["", "", "", "", ""]
x = 10
u = 1
c = []
ajouter_mot_de_passe()

fenetre.mainloop()
print(valeur)
print(c)





fenetre2 = tk.Tk()
fenetre2.geometry("400x600")
fenetre2.title("recuperateur de mot de passe.")

canvas2 = tk.Canvas(width=400, height=500, bg="lightgray")
canvas2.pack(side="top", padx=5, pady=5)
t = True
y = True


entry2 = tk.Entry(fenetre2, font=("Arial", 15), width=20)
button2 = tk.Button(fenetre2, text="OK", font=("Arial", 10), width=4,
                            command=lambda o=entry2:recuperer_valeur2(o))
canvas2.create_window(150, 80,  window=entry2)  
canvas2.create_window(250, 80, window=button2)

def verifier_valeur():
    global t, x, valeur2, c, w, v
    if valeur2 is None:
        fenetre2.after(100, verifier_valeur)  
    else:
        canvas2.create_rectangle(10, 10, 380, 60)
        canvas2.create_text(200, 35, text=f"recuperation des mots de passe : ", font=("arial", 14), fill="darkblue")
        print(valeur2)
        print(c)
        print(valeur)
        number = 1
        x = 10
        if valeur2 == valeur:
            print("hello world")
            for i in c:
                canvas2.create_rectangle(10, x + 110, 190, x + 160)
                canvas2.create_text(100, x + 135, text=f"mot de passe n°{number}", font=("arial", 14), fill="darkblue")
                canvas2.create_rectangle(200, x + 110, 380, x + 160)
                canvas2.create_text(300, x + 135, text=i, font=("arial", 14), fill="green")
                number += 1
                x += 60
                v = 0
                
        else:
            w = []
            for i in c:
                iV2 = re.sub(r"\w", "X", i)
                iV3 = re.sub(r"\W", "X", iV2)
                iV4 = re.sub(r"\d{}", "X", iV3)
                iV5 = re.sub(r"[?,.:;#)(&_-|°]", "X", iV4)
                w.append(iV5)
                print(w)
                canvas2.create_rectangle(10, x + 110, 190, x + 160)
                canvas2.create_text(100, x + 135, text=f"mot de passe n°{number}", font=("arial", 14), fill="darkblue")
                canvas2.create_rectangle(200, x + 110, 380, x + 160)
                canvas2.create_text(300, x + 135, text=iV5, font=("arial", 14), fill="red")
                number += 1
                x += 60
                v = 1
                
        t = False


verifier_valeur()              
    
def fichier_texte():
    if v == 0:
        with open("mon_fichier.txt", "w") as fichier:  
            u = "les mots de passe sont : "
            c.insert(0, u)
            for item in c:
                fichier.write(item + "\n")
    elif v == 1:
        with open("mon_fichier.txt", "w") as fichier:  
            u = "les mots de passe sont : "
            w.insert(0, u)
            for item in w:
                fichier.write(item + "\n")

def close():
    fenetre2.destroy()

canvas3 = tk.Canvas(width=400, height=200, bg="lightgray")
canvas3.pack(side="bottom", padx=5, pady=5)
button3 = tk.Button(fenetre2, text="Enrengistrer les mots de passe", font=("Arial", 14), bg="lightblue",width=25,
                            command=fichier_texte)
canvas3.create_window(150, 40,  window=button3)
button4 = tk.Button(fenetre2, text="Fermer", font=("Arial", 14), bg="red",width=7,
                            command=close)
canvas3.create_window(335, 40,  window=button4)
fenetre2.mainloop()