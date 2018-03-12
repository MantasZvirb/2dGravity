import Tkinter
import Fizika

ApskritimuMasyvas = []


def PridetiApskritima(Laukas,dal):
	a = Laukas.create_oval(dal.x-dal.spindulys,dal.y-dal.spindulys,dal.x+dal.spindulys,dal.y+dal.spindulys,fill = "#FF0000")
	ApskritimuMasyvas.append(a)


def PiesimoAtnaujinimas(Laukas):
	indeksas = 0
	for i in ApskritimuMasyvas:
		Laukas.delete(i)
		del ApskritimuMasyvas[indeksas]
		indeksas+=1

	for dal in Fizika.DaleliuMasyvas:
		a = Laukas.create_oval(dal.x-dal.spindulys,dal.y-dal.spindulys,dal.x+dal.spindulys,dal.y+dal.spindulys,fill = "#FF0000")
		ApskritimuMasyvas.append(a)

def PiestiKadra(Laukas):
	indeksas = 0
	for dal in Fizika.DaleliuMasyvas:
		Aps = ApskritimuMasyvas[indeksas]
		Laukas.coords(Aps,dal.x-dal.spindulys,dal.y-dal.spindulys,dal.x+dal.spindulys,dal.y+dal.spindulys)
		indeksas+=1
		