import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf




def run_game():
    ai_settings = Settings()
    # Initlaize game and create object
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # Set background colour


    #Make a ship

    ship = Ship(ai_settings,screen)
    #Make a group to store bullets in
    bullets = Group()




    #Start main loop of game
    while True:


          gf.check_events(ai_settings,screen, ship, bullets)
          ship.update()
          bullets.update()
          for bullet in bullets.copy():
              if bullet.rect.bottom <= 0:
                  bullets.remove(bullet)
          print(len(bullets))
          gf.update_screens(ai_settings,screen,ship,bullets)














run_game()



