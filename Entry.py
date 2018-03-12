import Tkinter
import Fizika
import Piesimas
import random

def Callbackas(TkObj):
	Piesimas.PiestiKadra(TkObj)
	Fizika.LaikoEjimas(0.0001)
	TkObj.after(1,Callbackas,TkObj)

def Randf(a,b):
	return random.random()*(a-b) + b;


Fizika.SukurtiDalele(200,200,0,0,1000,10)
Fizika.SukurtiDalele(170,170,0,0,1000,10)
Fizika.SukurtiDalele(180,50,0,0,1000,10)


for i in range(0,random.randint(10,50)):
	Fizika.SukurtiDalele(Randf(100,200),Randf(100,200),0,0,10,3)

PagLangasTk = Tkinter.Tk()
PagLangasTk.minsize(400,400)
LaukasTk = Tkinter.Canvas(PagLangasTk,width=400,height=300,bg="#000000")
Piesimas.PiesimoAtnaujinimas(LaukasTk)
LaukasTk.pack()
LaukasTk.after(1,Callbackas,LaukasTk)
PagLangasTk.mainloop()