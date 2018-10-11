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
ck.blit(bgtp,(0,0))
fj1 = pygame.image.load("PlaneWar/res/hero2.png")
ck.blit(fj1,(chang / 2 - 120 / 2,kuan / 2 - 78 / 2))

#创建矩形对象，然后图片根据矩形对象找位置，就只用移动矩形对象不用重新绘图了
fj1_rect = fj1.get_rect(centerx = chang / 2 - 120 / 2,centery = kuan / 2 - 78 / 2)
print(fj1_rect)

fj1_rect.move_ip(30,0)
print(fj1_rect[0],fj1_rect[1])
ck.blit(fj1,(fj1_rect[0],fj1_rect[1]))


#刷新屏幕
pygame.display.update()
time.sleep(2)
# while True:
#     ck.blit(bgtp,(0,0))
#     ck.blit(fj1,(chang / 2 - 120 / 2,kuan / 2 - 78 / 2 - 10))
#
#     pygame.display.update()

input()
