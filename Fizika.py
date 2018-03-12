import math
Konst = 1000000
AsiesRiba = 400
DaleliuMasyvas = []

class Dalele():
	def __init__(self,KordinateX,KordinateY,GreitisX,GreitisY,Mase,Spindulys):
		self.x = KordinateX
		self.y = KordinateY
		self.gx = GreitisX
		self.gy = GreitisY
		self.mase = Mase
		self.spindulys = Spindulys

def SukurtiDalele(x,y,gx,gy,mase,spindulys):
	d1 = Dalele(x,y,gx,gy,mase,spindulys)
	return DaleliuMasyvas.append(d1)
	
def LaikoEjimas(LaikoTarpas):	
	for Dalele1 in DaleliuMasyvas:
		for Dalele2 in DaleliuMasyvas:
			if(Dalele1 != Dalele2):
				AtstumasX = (Dalele1.x-Dalele2.x)
				AtstumasY = (Dalele1.y-Dalele2.y)
				AtstumasKvad = AtstumasX**2 + AtstumasY**2
				Atstumas = math.sqrt(AtstumasKvad)
				Jega = -(Konst*Dalele1.mase*Dalele2.mase)/AtstumasKvad
				if(Atstumas <= Dalele1.spindulys+Dalele2.spindulys):
					Jega = Jega*-1
				JegaX = (AtstumasX/Atstumas)*Jega
				JegaY = (AtstumasY/Atstumas)*Jega
				GreitisX = (JegaX/Dalele1.mase)*LaikoTarpas
				GreitisY = (JegaY/Dalele1.mase)*LaikoTarpas

				Dalele1.gx+=GreitisX
				Dalele1.gy+=GreitisY

	for Dalele1 in DaleliuMasyvas:
		NaujaX = Dalele1.x+Dalele1.gx*LaikoTarpas
		NaujaY = Dalele1.y+Dalele1.gy*LaikoTarpas
		
		if((NaujaX < 0) or (NaujaX > AsiesRiba)):
			Dalele1.gx = Dalele1.gx*-1
		if((NaujaY < 0) or (NaujaY > AsiesRiba)):
			Dalele1.gy = Dalele1.gy*-1

		Dalele1.x+= Dalele1.gx*LaikoTarpas
		Dalele1.y+= Dalele1.gy*LaikoTarpas
			
