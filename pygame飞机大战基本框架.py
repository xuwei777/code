#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import pygame,sys,time,random

pygame.init()

kuan = 512
chang = 768
ck = pygame.display.set_mode([kuan,chang])
#背景图
num = str(random.randint(1,5))

bjtp1 = pygame.image.load("PlaneWar/res/img_bg_level_" + num + ".jpg")
bjtp2 = pygame.image.load("PlaneWar/res/img_bg_level_" + num + ".jpg")
# 英雄飞机
fj1 = pygame.image.load("PlaneWar/res/hero2.png")
plane_rect = fj1.get_rect()

# 敌人飞机
i = 0

#djlb = [pygame.image.load("PlaneWar/res/img-plane_" + djnum + ".png")for _ in range(5)]


bj1_rect = bjtp1.get_rect(centerx = 0 + kuan / 2,centery = 0 + chang / 2)
bj2_rect = bjtp2.get_rect(centerx = 0 + kuan / 2,centery = 0 + -chang / 2)

bj1_y = bj1_rect[1]
bj2_y = bj2_rect[1]
speed = 3
plane_rect.move_ip(kuan / 2 - plane_rect[2] / 2, chang - plane_rect[3] - 20)



def tc():
    sys.exit()
    pygame.quit()


while True:

    # dj = pygame.image.load("PlaneWar/res/img-plane_1.png")
    # dj_rect = dj.get_rect()
    # dj_rect.move_ip(30,50)
    # ck.blit()
    #


    """
        背景图滚动效果
    """
    ck.blit(bjtp1,(0,bj1_y))
    ck.blit(bjtp2,(0,bj2_y))

    if bj1_y >= chang:
        bj1_y = 0
    if bj2_y >= 0:
        bj2_y = -chang
    bj1_y += speed
    bj2_y += speed
    """
        敌人飞机
    """
    djlb = []
    i = 0
    while i < 3:
        djnum = str(random.randint(1, 7))
        djlb.append(pygame.image.load("PlaneWar/res/img-plane_" + djnum + ".png"))
        i += 1

    if len(djlb) <= 3:
        for djwz in djlb:
            dj_rect = djwz.get_rect()
            dj_rect.move_ip(random.randint(50,480),40)
            ck.blit(djwz,(dj_rect[0],dj_rect[1]))
            while dj_rect[1] >= chang:
                djlb.remove(djwz)
    """
        处理飞机移动效果
    """
    # plane_rect.move_ip(kuan / 2 - plane_rect[2] / 2, chang - plane_rect[3] - 20)
    ck.blit(fj1,(plane_rect[0],plane_rect[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tc()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                tc()
            if event.key == pygame.K_SPACE or event.key == pygame.K_j:
                print("发射子弹")

    cxaj = pygame.key.get_pressed()
    if cxaj[pygame.K_UP]:
        if plane_rect[1] > 0:
            plane_rect.move_ip(0,-speed)
    if cxaj[pygame.K_DOWN]:
        if plane_rect[1] < chang - plane_rect[3]:
            plane_rect.move_ip(0,speed)
    if cxaj[pygame.K_LEFT]:
        if plane_rect[0] > 0:
            plane_rect.move_ip(-speed,0)
    if cxaj[pygame.K_RIGHT]:
        if plane_rect[0] < kuan - plane_rect[2]:
            plane_rect.move_ip(speed,0)
    pygame.display.update()