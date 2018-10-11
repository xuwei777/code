#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import pygame
import time
chang = 512
kuan = 768
pygame.init()
#创建界面窗口，设置界面的宽400，高600
ck = pygame.display.set_mode([chang,kuan])
#背景图片并绘制到窗口指定位置
bgtp = pygame.image.load("img_bg_level_2.jpg")
#在指定的位置加载图片对象

fj1 = pygame.image.load("PlaneWar/res/hero2.png")
fj1_rect = fj1.get_rect()
speed = 2
while True:
    ck.blit(bgtp,(0,0))
    ck.blit(fj1,(fj1_rect[0],fj1_rect[1]))
    if fj1_rect[0] <= chang - fj1_rect[2]:
        fj1_rect.move_ip(speed,0)

    pygame.display.update()



