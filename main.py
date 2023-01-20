import pygame as pg
from time import perf_counter
from random import random


Vec = pg.Vector2
W,H = 720, 720
FPS = 120

pg.init()


class Ball:
	def __init__(self):
		self.color = "#ff0020"
		self.rad = 25
		self.pos = Vec(W//2, H//2)
		
		self.max_vel = 700

		self.vel = Vec(2*(random()-.5), 2*(random()-.5))
		self.acc = Vec(0, 0)

	def show(self, surf):
		pg.draw.circle(surf, self.color, self.pos, self.rad)
	
	def edges(self):
		if self.pos.x < self.rad:
			self.vel.x *= -1
			self.pos.x = self.rad

		elif self.pos.x > (W - self.rad):
			self.vel.x *= -1
			self.pos.x = (W - self.rad)
		
		if self.pos.y < self.rad:
			self.vel.y *= -1
			self.pos.y = self.rad

		elif self.pos.y > (H - self.rad):
			self.vel.y *= -1
			self.pos.y = (H - self.rad)


	def update(self, dt, edge=True):
		if edge: self.edges()

		self.pos += (self.vel * self.max_vel * dt)
		self.acc = Vec()


class Game:
	def __init__(self):
		self.screen = pg.display.set_mode((W,H))
		self.clock = pg.time.Clock()

		self.running = True


	def Run(self):
		B1 = Ball()
		delta_t = perf_counter()

		while self.running:
			delta_t = perf_counter() - delta_t
			delta_time = delta_t
			delta_t = perf_counter()
			self.clock.tick(FPS)

			self.screen.fill("#181818")
			
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					self.running = False
			
			B1.update(delta_time)
			B1.show(self.screen)

			pg.display.update()




def main():
	Bounce_Ball = Game()
	Bounce_Ball.Run()


if __name__ == "__main__":
	main()