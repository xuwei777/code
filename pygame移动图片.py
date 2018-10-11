#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import pygame
kuan = 512
chang = 768

pygame.init()

ck = pygame.display.set_mode([kuan,chang])

bjtp1 = pygame.image.load("img_bg_level_2.jpg")
bjtp2 = pygame.image.load("img_bg_level_2.jpg")

bj1_rect = bjtp1.get_rect(centerx = 0 + kuan / 2,centery = 0 + chang / 2)
bj2_rect = bjtp2.get_rect(centerx = 0 + kuan / 2,centery = 0 + -chang / 2)
# bj1_rect[1] = 0
# bj2_rect[1] = -chang

bj1_y = bj1_rect[1]
bj2_y = bj2_rect[1]

speed = 3
while True:
    ck.blit(bjtp1,(bj1_rect[0],bj1_y))
    ck.blit(bjtp2,(bj2_rect[0],bj2_y))

    if bj1_y >= chang:
        bj1_y = 0
    if bj2_y >= 0:
        bj2_y = -chang


    bj1_y += speed
    bj2_y += speed
    pygame.display.update()
