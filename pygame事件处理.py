#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import pygame
import time
import sys

chang = 768
kuan = 512
pygame.init()

ck = pygame.display.set_mode([kuan,chang])
bjtp = pygame.image.load("img_bg_level_2.jpg")

fj1 = pygame.image.load("PlaneWar/res/hero2.png")
plane_rect = fj1.get_rect()
#(x,y.图片宽，图片高)
plane_rect.move_ip(kuan / 2 - plane_rect[2] /2,chang - plane_rect[3] - 20)
speed = 3
while True:
    ck.blit(bjtp,(0,0))
    ck.blit(fj1,(plane_rect[0],plane_rect[1]))

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    lxaj = pygame.key.get_pressed()
    if lxaj[pygame.K_UP]:
        plane_rect.move_ip(0,-speed)
    if lxaj[pygame.K_DOWN]:
        plane_rect.move_ip(0,speed)
    if lxaj[pygame.K_LEFT]:
        plane_rect.move_ip(-speed,0)
    if lxaj[pygame.K_RIGHT]:
        plane_rect.move_ip(speed,0)
    if lxaj[pygame.K_SPACE]:
        print("发射子弹......")

    pygame.display.update()
    #time.sleep(1)


    #
