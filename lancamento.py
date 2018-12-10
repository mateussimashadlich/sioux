import math

class Lancamento():


	def __init__(self, angulo, vel_0):

		self.an = angulo
		self.vel_0 = vel_0
		self.grav = -0.33
		self.tx = 0
		self.ty = 0
		self.t = 3
		self.vox = self.vel_0*math.cos(self.an*math.pi/180)
		self.voy = self.vel_0*math.sin(self.an*math.pi/180)
		self.yo = 510
		self.xo = 0

	def calcular(self):

		self.xo += self.vox
		self.yo -= self.voy
		self.voy += self.grav

	def calcular_tempo(self,vel,grav):
		
		tempo = vel/grav
		return tempo
		
	def lancar(self):
		while self.ty < 50:
			self.calcular()

if __name__ == "__main__":
	lancamento = Lancamento(30,50)
	lancamento.lancar()



