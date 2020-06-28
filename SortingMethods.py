from tkinter import *
from random import *
import time

root= Tk()
root.geometry("1000x500")

canvas= Canvas(root, width= 1000, height=400)
canvas.pack()

maxi, nbIndices = 0,0
liste, rectList= [],[]

root.update()


def createList(event=0):
    global liste, maxi, nbIndices, rectList
    nb= int(entNb.get())
    canvas.delete("all")
    liste= [randint(0,50) for i in range (0,nb)]
    maxi= max(liste)-1
    nbIndices = len(liste)
    rectList= []
    plot()
    print("created")

  
def canvUpdate():
    global liste, maxi, nbIndices, rectList
    canvas.delete("all")
    rectList= []
    plot()




def plot():
    for i in liste:
        rectValue(i)

    plotRect_init()



def rectValue(value):
    valueComparedToMax = value * 100 / maxi    
    valueComparedToMax = valueComparedToMax * canvas.winfo_height() / 100
    rectList.append(valueComparedToMax)


def plotRect_init():
    global canvas, rectArray
    actPosition = 0
    largeurCase= canvas.winfo_width() / nbIndices

    rectArray=[]
    for i in range (0,len(rectList)):
        rectArray.append(canvas.create_rectangle(actPosition, canvas.winfo_height(), actPosition+largeurCase,(canvas.winfo_height() - rectList[i]), fill='cyan'))
        
        actPosition += largeurCase


def rectToColor(i, color="cyan"):
    canvas.itemconfig(rectArray[i], fill=color)




# PARTIE QUICKSORT

def swap(pListe, a, b):
    global waitvar
    temp, tempr= pListe[a], rectArray[a]
    pListe[a], rectArray[a]= pListe[b], rectArray[b]
    pListe[b], rectArray[b] = temp, tempr

    

    xa= canvas.coords(rectArray[a])[0]
    xb= canvas.coords(rectArray[b])[0]

    canvas.move(rectArray[a], xb-xa, 0)
    canvas.move(rectArray[b], xa-xb, 0)

    rectToColor(a, "green")
    rectToColor(b, "green")

    var= IntVar()
    root.after(timeBetweenSteps, var.set, 1)
    root.wait_variable(var)

    rectToColor(a)
    rectToColor(b)


def segmenter(pListe, i, j):
    n= j-i
    k = i
    jp=k+1

    
    while(jp!=j):
        rectToColor(jp, "yellow")

        if(pListe[jp]<pListe[k]):
            swap(pListe, k+1, jp)
            swap(pListe, k, k+1)
            k+=1
            rectToColor(jp)


        var= IntVar()
        root.after(timeBetweenSteps, var.set, 1)
        root.wait_variable(var)

        rectToColor(jp)
        jp+=1

    
    return k

def qs(pListe, i, j):
    if(j-i>1):
        k= segmenter(pListe, i, j)

        qs(pListe, i, k)
        qs(pListe, k+1, j)


def parcours():
    time= int(3000/ len(liste))
    for i in range(0,len(liste)):
        rectToColor(i, "white")
        var= IntVar()
        root.after(time, var.set, 1)
        root.wait_variable(var)


def qss(event=0):
    print("before:")
    print(liste)
    qs(liste, 0, len(liste))
    print("\nAfter")
    print(liste)
    parcours()

#FIN PARTIE QUICKSORT


but= Button(root, text= "Generate random array", command= createList)
but.pack()

but2= Button(root, text= "Trier", command= qss)
but2.pack()

entNb= Entry(root)
entNb.insert(0, "100")
entNb.pack()

def test(event=0):
    rectToColor(0, "red")
    rectToColor(len(liste)-1, "red")


butdebug= Button(root, text= "DEbug", command= test)
butdebug.pack()

print("ready")

timeBetweenSteps= 50


root.mainloop()    
