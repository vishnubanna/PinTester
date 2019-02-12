import pygame

events = pygame.events.get()

for event in events:
    if event == pygame.K_1:
        print("1 is pressed")
    else:
        print(event.char
