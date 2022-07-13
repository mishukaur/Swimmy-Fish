import pygame
from src import controller

def main():
	pygame.init()
	team = {"lead": "Manjot Kaur", "backend": "Brianna Nunez", "frontend": "Najah Julien"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:" , team["frontend"])
	main_window = controller.controller()
	main_window.mainLoop()

main()
